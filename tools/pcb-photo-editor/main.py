import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import threading, io, datetime
from pathlib import Path

MISSING_DEPS = []
try:    import rawpy
except ImportError: MISSING_DEPS.append("rawpy")
try:    import numpy as np
except ImportError: MISSING_DEPS.append("numpy")
try:    import cv2
except ImportError: MISSING_DEPS.append("opencv-python")
try:    from PIL import Image, ImageTk
except ImportError: MISSING_DEPS.append("Pillow")
try:    import tifffile
except ImportError: MISSING_DEPS.append("tifffile")

THUMB_W, THUMB_H = 150, 180
SLOT_W,  SLOT_H  = 175, 265
SLOTS_PER_ROW    = 6
OUTPUT_DIR      = Path(r"C:\Users\borna\Documents\photo editor\photos\output")
END_PRODUCT_DIR = Path(r"C:\Users\borna\Documents\photo editor\photos\cropped image")
ACCENT, DARK, BG = "#500B76", "#3a0a52", "#f0f0f0"


# ──────────────────────────────────────────── Step bar ────────────────────────

class StepBar(tk.Frame):
    LABELS = ["1  Load Images", "2  Preview", "3  Auto Edit", "4  Crop Board", "5  Dust Removal", "6  Export"]

    def __init__(self, parent, on_click=None, **kw):
        super().__init__(parent, bg=BG, pady=6, **kw)
        self._btns = []
        self._on_click = on_click
        for i, txt in enumerate(self.LABELS):
            lbl = tk.Label(self, text=txt, font=("Helvetica", 10, "bold"),
                           bg=BG, fg="#bbbbbb", padx=18, pady=5, relief=tk.FLAT,
                           cursor="hand2")
            lbl.grid(row=0, column=i * 2)
            self._btns.append(lbl)
            if on_click is not None:
                lbl.bind("<Button-1>", lambda e, n=i: on_click(n))
            lbl.bind("<Enter>", lambda e, l=lbl, idx=i: self._hover(l, idx, True))
            lbl.bind("<Leave>", lambda e, l=lbl, idx=i: self._hover(l, idx, False))
            if i < len(self.LABELS) - 1:
                tk.Label(self, text="›", bg=BG, fg="#cccccc",
                         font=("Helvetica", 14)).grid(row=0, column=i * 2 + 1)
        self._current = 0
        self.set_step(0)

    def _hover(self, lbl, idx, entering):
        if idx == self._current:
            return
        lbl.configure(bg="#ddd" if entering else BG)

    def set_step(self, n):
        self._current = n
        for i, lbl in enumerate(self._btns):
            if i == n:
                lbl.configure(bg=ACCENT, fg="white")
            elif i < n:
                lbl.configure(bg=BG, fg=ACCENT)
            else:
                lbl.configure(bg=BG, fg="#bbbbbb")


# ──────────────────────────────────────────── Image slot ─────────────────────

class ImageSlot(tk.Frame):
    def __init__(self, parent, index, path, thumb_tk, focus_dist, on_remove):
        super().__init__(parent, relief=tk.RIDGE, borderwidth=2,
                         width=SLOT_W, height=SLOT_H, bg="#f5f5f5")
        self.grid_propagate(False)
        self.pack_propagate(False)
        self.index      = index
        self.path       = path
        self.focus_dist = focus_dist  # metres from Exif, or None

        tk.Label(self, text=f"Image {index + 1}",
                 font=("Helvetica", 9, "bold"), bg="#f5f5f5").pack(pady=(6, 3))

        pf = tk.Frame(self, width=THUMB_W, height=THUMB_H,
                      bg="#d0d0d0", relief=tk.SUNKEN, bd=1)
        pf.pack(padx=6)
        pf.pack_propagate(False)
        lbl = tk.Label(pf, image=thumb_tk, bg="#d0d0d0")
        lbl.image = thumb_tk
        lbl.place(relx=.5, rely=.5, anchor=tk.CENTER)

        tk.Label(self, text=Path(path).name, bg="#f5f5f5",
                 wraplength=160, font=("Helvetica", 7), fg="#555").pack(pady=(3, 2))
        dist_txt = f"{focus_dist:.2f} m" if focus_dist is not None else "focus: n/a"
        tk.Label(self, text=dist_txt, bg="#f5f5f5",
                 font=("Helvetica", 7), fg="#888").pack()
        ttk.Button(self, text="✕ Remove",
                   command=lambda: on_remove(self.index)).pack(pady=3)


# ──────────────────────────────────────────── Main app ───────────────────────

class PhotoEditorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Board Photo Editor")
        self.root.geometry("1440x900")
        self.root.minsize(1440, 860)
        self.root.resizable(True, True)
        self.root.configure(bg=BG)

        self.slots               = []
        self._last_result        = None
        self._sharpness_mask     = None
        self._show_sharpness_overlay = True
        # Edit step
        self._edit_source   = None   # original stacked image (never modified)
        self._edit_result   = None   # current edited image passed to crop step
        self._edit_pil      = None   # downscaled display copy
        self._edit_orig_wh  = (0, 0)
        self._edit_base_tk  = None
        self._edit_last_nw  = 0
        self._edit_last_nh  = 0
        self._edit_last_off = (-1, -1)
        self._edit_zoom     = 1.0
        self._edit_fit      = True
        self._edit_offset   = (0, 0)
        self._edit_wb_point      = None   # (x0, y0, x1, y1) sampled rectangle in full-res coords
        self._edit_picking       = False
        self._edit_wb_drag_start = None   # (canvas_x, canvas_y, img_x, img_y) on press
        self._edit_wb_drag_end   = None   # (canvas_x, canvas_y) current drag position
        self._edit_do_levels     = tk.BooleanVar(value=False)
        self._edit_do_pcb        = tk.BooleanVar(value=True)
        self._edit_do_sharpen    = tk.BooleanVar(value=False)
        # Crop step
        self._crop_image     = None
        self._crop_full      = None
        self._crop_source_id = None   # id() of image used to init crop; skip reinit if same
        self._crop_pil      = None   # downscaled display copy (max 1200px)
        self._crop_orig_wh  = (0, 0) # original full-res (w, h)
        self._crop_tk       = None
        self._crop_rect     = None
        self._crop_zoom     = 1.0
        self._crop_fit      = True
        self._crop_pan      = [0, 0]   # image top-left in canvas coords (replaces offset+scroll)
        self._crop_mid_drag = None     # (start_ex, start_ey, pan_x0, pan_y0) during middle-drag
        self._crop_offset   = (0, 0)   # kept for _hit_crop_handle compatibility
        self._crop_drag     = None
        self._crop_spins    = {}
        self._crop_updating = False
        self._crop_auto_var = tk.BooleanVar(value=False)
        self._crop_base_tk  = None
        self._crop_last_view_key = None   # (vx0,vy0,vx1,vy1,dw,dh,src_id) viewport cache key
        self._crop_last_off      = (-1, -1)
        self._crop_pending  = False
        self._crop_history    = []   # undo stack — list of {'rect':..,'holes':[..]} dicts
        self._crop_redo_stack = []   # redo stack

        # Lasso draw + edge refinement
        self._crop_lasso_mode    = False
        self._crop_lasso_closed  = False    # lasso drawn but not yet applied
        self._crop_lasso_pts     = []       # [(ix, iy), …] in full-res coords
        self._crop_lasso_cursor  = None     # live cursor pos for rubber-band line
        self._crop_lasso_btn     = None
        self._crop_holes         = []       # list of np.float32 arrays — each punches a hole in the mask
        # Cut-zones tool
        self._crop_cut_mode      = False
        self._crop_cut_active    = []       # in-progress polygon points (np.float32 [x,y])
        self._crop_cut_btn       = None
        self._crop_delete_mode   = False
        self._crop_delete_btn    = None
        self._crop_arc_mode     = False
        self._crop_arc_pts      = []       # vertex indices (0, 1, or 2 placed)
        self._crop_arc_btn      = None
        self._crop_preview_bg   = "white"  # "white" | "green" | "red"
        self._crop_preview_btn  = None
        self._crop_preview_pil  = None
        self._crop_refine_var   = tk.IntVar(value=10)
        self._crop_smooth_var   = tk.IntVar(value=2)
        self._crop_feather_var  = tk.IntVar(value=2)
        self._crop_result_rgba  = None   # PIL RGBA produced by _apply_crop

        # Dust Removal step
        self._dust_enabled      = tk.BooleanVar(value=True)
        self._dust_method       = tk.StringVar(value="lama")
        self._lama_model        = None   # cached ModelManager, loaded on first use
        self._dust_dl_bar       = None   # ttk.Progressbar shown during model download
        self._dust_dl_frame     = None
        self._dust_dl_pct_var   = None
        self._dust_exclude_rects  = []   # [(x0,y0,x1,y1)] image-space exclusion zones
        self._dust_freedraw_polys = []   # completed free-draw exclusion polygons (np.int32)
        self._dust_mark_polys     = []   # completed free-draw REMOVAL polygons (np.int32)
        self._dust_freedraw_pts   = []   # active free-draw stroke points [(ix,iy),…]
        self._dust_excl_drag      = None # rect drag: (ix0, iy0, cx0, cy0, cx1, cy1)
        self._dust_draw_mode      = tk.StringVar(value="excl_rect")
        self._dust_paint_radius   = tk.IntVar(value=20)
        self._dust_paint_active   = False
        self._dust_api_key      = tk.StringVar(value="")
        self._dust_sensitivity  = tk.IntVar(value=50)
        self._dust_min_px       = tk.IntVar(value=5)
        self._dust_max_px       = tk.IntVar(value=200)
        self._dust_show_mask    = tk.BooleanVar(value=False)
        self._dust_source_rgba  = None
        self._dust_result_rgba  = None
        self._dust_mask_pil     = None
        self._dust_display_tk   = None
        self._dust_zoom         = 1.0
        self._dust_pan          = [0, 0]
        self._dust_pan_start    = None
        self._dust_canvas       = None
        self._dust_run_btn      = None
        self._dust_detect_btn   = None
        self._dust_api_frame    = None
        self._dust_local_controls = None
        self._dust_status_var   = None

        # Export step
        self._export_source_rgba    = None   # PIL RGBA from dust/crop step
        self._export_scale          = None   # tk.DoubleVar — set in _build_export_page
        self._export_margin         = None   # tk.IntVar — set in _build_export_page
        self._export_offset         = [1200, 1200]  # product center in 2400×2400
        self._export_view_zoom      = 1.0
        self._export_view_pan       = [0, 0]
        self._export_view_pan_start = None
        self._export_img_drag_start = None  # (ex, ey, off_x, off_y)
        self._export_canvas         = None
        self._export_display_tk     = None
        self._export_status_var     = None
        self._export_preview_bg     = None  # tk.StringVar "white"|"checker"
        self._export_scale_before   = 95.0  # tracks scale before spinbox click

        # Undo / redo stacks (dust step and export step)
        self._dust_undo_stack   = []
        self._dust_redo_stack   = []
        self._export_undo_stack = []
        self._export_redo_stack = []

        self._build_ui()
        self.root.bind("<Control-z>", self._handle_undo)
        self.root.bind("<Control-y>", self._handle_redo)
        if MISSING_DEPS:
            self.set_status(f"Missing: {', '.join(MISSING_DEPS)} — run install.bat", True)

    # ═══════════════════════════════════════════ UI shell ════════════════════

    def _build_ui(self):
        # Header
        hdr = tk.Frame(self.root, bg=ACCENT, pady=10)
        hdr.pack(fill=tk.X)
        tk.Label(hdr, text="Board Photo Editor",
                 font=("Helvetica", 16, "bold"), bg=ACCENT, fg="white").pack()

        # Step bar
        self._step_bar = StepBar(self.root, on_click=self._show_step)
        self._step_bar.pack(fill=tk.X, padx=16, pady=(6, 0))
        ttk.Separator(self.root).pack(fill=tk.X, padx=16)

        # Content area
        self._content = tk.Frame(self.root, bg=BG)
        self._content.pack(fill=tk.BOTH, expand=True, padx=0, pady=0)

        self._pages = [
            self._build_load_page(),
            self._build_preview_page(),
            self._build_edit_page(),
            self._build_crop_page(),
            self._build_dust_page(),
            self._build_export_page(),
        ]

        # Nav bar
        nav = tk.Frame(self.root, bg="#e8e8e8", pady=6)
        nav.pack(fill=tk.X, side=tk.BOTTOM)

        self._back_btn = ttk.Button(nav, text="← Back",  command=self._prev_step)
        self._back_btn.pack(side=tk.LEFT, padx=10)
        self._next_btn = ttk.Button(nav, text="Next →",  command=self._next_step)
        self._next_btn.pack(side=tk.RIGHT, padx=10)
        self._skip_export_btn = ttk.Button(nav, text="Skip to Export →",
                                            command=lambda: self._show_step(5))
        # Not packed initially — shown only on step 3 via _show_step

        self._progress = ttk.Progressbar(nav, mode="determinate", length=200)
        self._progress.pack(side=tk.RIGHT, padx=6)

        self._status_var = tk.StringVar(value="Load your ARW images to begin.")
        self._status_lbl = tk.Label(nav, textvariable=self._status_var,
                                    bg="#e8e8e8", font=("Helvetica", 9), anchor=tk.W)
        self._status_lbl.pack(side=tk.LEFT, padx=6, fill=tk.X, expand=True)

        self._step = -1
        self._show_step(0)

    # ═══════════════════════════════════════════ Step pages ══════════════════

    def _build_load_page(self):
        page = tk.Frame(self._content, bg=BG)

        top = tk.Frame(page, bg=BG)
        top.pack(fill=tk.X, padx=14, pady=8)
        ttk.Button(top, text="Load Images", command=self._load_multiple).pack(side=tk.LEFT)
        ttk.Button(top, text="Clear All",   command=self._clear_all).pack(side=tk.LEFT, padx=6)

        outer = ttk.LabelFrame(page, text=" Source Images ", padding=6)
        outer.pack(fill=tk.BOTH, expand=True, padx=14, pady=(0, 8))

        canvas = tk.Canvas(outer, bg=BG, highlightthickness=0)
        vs = ttk.Scrollbar(outer, orient=tk.VERTICAL, command=canvas.yview)
        canvas.configure(yscrollcommand=vs.set)
        vs.pack(side=tk.RIGHT, fill=tk.Y)
        canvas.pack(fill=tk.BOTH, expand=True)

        self._slots_inner = tk.Frame(canvas, bg=BG)
        canvas.create_window((0, 0), window=self._slots_inner, anchor=tk.NW)
        self._slots_inner.bind("<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        self._empty_lbl = tk.Label(self._slots_inner,
                                   text="Click 'Load Images' to get started",
                                   bg=BG, fg="#aaaaaa", font=("Helvetica", 11))
        self._empty_lbl.grid(row=0, column=0, padx=20, pady=40)
        return page

    def _build_preview_page(self):
        page = tk.Frame(self._content, bg=BG)

        top = tk.Frame(page, bg=BG)
        top.pack(fill=tk.X, padx=14, pady=6)
        ttk.Button(top, text="Re-combine",
                   command=self._start_combine).pack(side=tk.LEFT)
        ttk.Button(top, text="Fit to Window",
                   command=self._preview_fit).pack(side=tk.LEFT, padx=6)
        ttk.Button(top, text="100%",
                   command=self._preview_100).pack(side=tk.LEFT)
        self._overlay_btn = ttk.Button(top, text="Hide Overlay",
                                       command=self._toggle_sharpness_overlay)
        self._overlay_btn.pack(side=tk.LEFT, padx=6)
        ttk.Button(top, text="Save Image",
                   command=self._save_stacked).pack(side=tk.LEFT, padx=6)
        ttk.Button(top, text="How it works",
                   command=self._show_stack_info).pack(side=tk.LEFT, padx=6)
        self._preview_fix_btn = ttk.Button(top, text="Fix Artifact",
                                           command=self._preview_toggle_fix)
        self._preview_fix_btn.pack(side=tk.LEFT, padx=6)
        self._preview_zoom_lbl = tk.Label(top, text="", bg=BG,
                                          font=("Helvetica", 9), fg="#555")
        self._preview_zoom_lbl.pack(side=tk.LEFT, padx=12)
        self._preview_dim_lbl  = tk.Label(top, text="", bg=BG,
                                          font=("Helvetica", 9), fg="#888")
        self._preview_dim_lbl.pack(side=tk.RIGHT, padx=6)

        # Warning banner — always packed but invisible when text is empty
        self._warn_frame = tk.Frame(page, bg=BG)
        self._warn_frame.pack(fill=tk.X, padx=14)
        self._warn_lbl = tk.Label(self._warn_frame, text="", bg=BG,
                                  font=("Helvetica", 10, "bold"), fg=BG, pady=4,
                                  justify=tk.LEFT)
        self._warn_lbl.pack(anchor=tk.W)

        cv_frame = tk.Frame(page, bg="#1a1a1a")
        cv_frame.pack(fill=tk.BOTH, expand=True, padx=14, pady=(0, 8))

        self._preview_canvas = tk.Canvas(cv_frame, bg="#1a1a1a",
                                          highlightthickness=0, cursor="fleur")
        hs = ttk.Scrollbar(cv_frame, orient=tk.HORIZONTAL,
                           command=self._preview_canvas.xview)
        vs = ttk.Scrollbar(cv_frame, orient=tk.VERTICAL,
                           command=self._preview_canvas.yview)
        self._preview_canvas.configure(xscrollcommand=hs.set,
                                       yscrollcommand=vs.set)
        vs.pack(side=tk.RIGHT,   fill=tk.Y)
        hs.pack(side=tk.BOTTOM,  fill=tk.X)
        self._preview_canvas.pack(fill=tk.BOTH, expand=True)

        self._preview_canvas.bind("<MouseWheel>", self._preview_wheel)
        self._preview_canvas.bind("<ButtonPress-1>",
            lambda e: self._preview_canvas.scan_mark(e.x, e.y))
        self._preview_canvas.bind("<B1-Motion>",
            lambda e: self._preview_canvas.scan_dragto(e.x, e.y, gain=1))
        self._preview_canvas.bind("<ButtonPress-2>",
            lambda e: self._preview_canvas.scan_mark(e.x, e.y))
        self._preview_canvas.bind("<B2-Motion>",
            lambda e: self._preview_canvas.scan_dragto(e.x, e.y, gain=1))

        self._preview_pil   = None
        self._preview_tk_img = None
        self._preview_zoom  = 1.0
        self._preview_fit_mode = True
        self._preview_fix_mode = False
        return page

    def _build_edit_page(self):
        page = tk.Frame(self._content, bg=BG)

        top = tk.Frame(page, bg=BG)
        top.pack(fill=tk.X, padx=14, pady=6)

        self._edit_wb_btn = ttk.Button(top, text="Pick White Point",
                                        command=self._edit_toggle_pick)
        self._edit_wb_btn.pack(side=tk.LEFT)
        ttk.Button(top, text="Reset",
                   command=self._edit_reset).pack(side=tk.LEFT, padx=6)

        ttk.Separator(top, orient=tk.VERTICAL).pack(side=tk.LEFT, fill=tk.Y, padx=10)

        ttk.Button(top, text="Apply Auto Edit",
                   command=self._edit_apply_auto).pack(side=tk.LEFT)
        ttk.Checkbutton(top, text="Auto Levels",
                        variable=self._edit_do_levels).pack(side=tk.LEFT, padx=(6, 2))
        ttk.Checkbutton(top, text="PCB Color",
                        variable=self._edit_do_pcb).pack(side=tk.LEFT, padx=2)
        ttk.Checkbutton(top, text="Sharpen",
                        variable=self._edit_do_sharpen).pack(side=tk.LEFT, padx=2)

        ttk.Separator(top, orient=tk.VERTICAL).pack(side=tk.LEFT, fill=tk.Y, padx=10)
        ttk.Button(top, text="Fit to Window",
                   command=self._edit_fit_view).pack(side=tk.LEFT)
        ttk.Button(top, text="100%",
                   command=lambda: self._edit_set_zoom(1.0)).pack(side=tk.LEFT, padx=6)

        self._edit_info_lbl = tk.Label(top, text="", bg=BG,
                                        font=("Helvetica", 9), fg="#555")
        self._edit_info_lbl.pack(side=tk.LEFT, padx=12)

        cv_frame = tk.Frame(page, bg="#1a1a1a")
        cv_frame.pack(fill=tk.BOTH, expand=True, padx=14, pady=(0, 8))

        self._edit_canvas = tk.Canvas(cv_frame, bg="#1a1a1a",
                                       highlightthickness=0, cursor="crosshair")
        self._edit_canvas.pack(fill=tk.BOTH, expand=True)

        self._edit_canvas.bind("<ButtonPress-1>",   self._edit_canvas_press)
        self._edit_canvas.bind("<B1-Motion>",        self._edit_canvas_drag_wb)
        self._edit_canvas.bind("<ButtonRelease-1>",  self._edit_canvas_release_wb)
        self._edit_canvas.bind("<MouseWheel>",       self._edit_wheel)
        self._edit_canvas.bind("<ButtonPress-2>",
            lambda e: self._edit_canvas.scan_mark(e.x, e.y))
        self._edit_canvas.bind("<B2-Motion>",
            lambda e: self._edit_canvas.scan_dragto(e.x, e.y, gain=1))
        self._edit_canvas.bind("<Configure>",
            lambda e: self._edit_refresh_canvas())

        tk.Label(page,
                 text="Click 'Pick White Point' then drag a rectangle over a neutral/grey area  ·  Middle-drag to pan  ·  Scroll to zoom",
                 bg=BG, fg="#888", font=("Helvetica", 8)).pack()
        return page

    def _build_crop_page(self):
        page = tk.Frame(self._content, bg=BG)

        top = tk.Frame(page, bg=BG)
        top.pack(fill=tk.X, padx=14, pady=6)

        ttk.Button(top, text="Auto Detect Board",
                   command=self._crop_auto_detect).pack(side=tk.LEFT)
        ttk.Button(top, text="Fit to Window",
                   command=self._crop_fit_view).pack(side=tk.LEFT, padx=6)
        ttk.Button(top, text="100%",
                   command=self._crop_100).pack(side=tk.LEFT)

        ttk.Separator(top, orient=tk.VERTICAL).pack(side=tk.LEFT, fill=tk.Y, padx=10)

        tk.Label(top, text="Padding:", bg=BG,
                 font=("Helvetica", 9)).pack(side=tk.LEFT)
        var_pad = tk.IntVar(value=20)
        var_pad.trace_add("write", lambda *a: self._crop_spin_changed('padding'))
        self._crop_spins['padding'] = var_pad
        ttk.Spinbox(top, textvariable=var_pad, from_=0, to=400,
                    width=6).pack(side=tk.LEFT, padx=(0, 4))
        tk.Label(top, text="px", bg=BG, font=("Helvetica", 9)).pack(side=tk.LEFT, padx=(0, 10))

        ttk.Checkbutton(top, text="Auto-crop (skip review)",
                        variable=self._crop_auto_var).pack(side=tk.LEFT, padx=6)

        self._crop_dim_lbl = tk.Label(top, text="", bg=BG,
                                       font=("Helvetica", 9), fg="#888")
        self._crop_dim_lbl.pack(side=tk.RIGHT, padx=6)
        ttk.Button(top, text="Crop & Save",
                   command=self._apply_crop).pack(side=tk.RIGHT, padx=(0, 6))

        # ── Second row — lasso / refine / sliders / preview ─────────────────
        row2 = tk.Frame(page, bg=BG)
        row2.pack(fill=tk.X, padx=14, pady=(0, 4))

        self._crop_lasso_btn = ttk.Button(row2, text="Draw Lasso",
                                           command=self._crop_toggle_lasso)
        self._crop_lasso_btn.pack(side=tk.LEFT)

        self._crop_cut_btn = ttk.Button(row2, text="Draw Lines",
                                         command=self._crop_cut_toggle)
        self._crop_cut_btn.pack(side=tk.LEFT, padx=(6, 0))

        ttk.Button(row2, text="Refine Edge",
                   command=self._crop_do_refine).pack(side=tk.LEFT, padx=(6, 0))
        ttk.Button(row2, text="Smooth",
                   command=self._crop_do_smooth).pack(side=tk.LEFT, padx=6)
        self._crop_delete_btn = ttk.Button(row2, text="Delete Vertex",
                                            command=self._crop_toggle_delete)
        self._crop_delete_btn.pack(side=tk.LEFT)
        self._crop_arc_btn = ttk.Button(row2, text="3-pt Arc",
                                         command=self._crop_toggle_arc)
        self._crop_arc_btn.pack(side=tk.LEFT, padx=(6, 0))

        ttk.Separator(row2, orient=tk.VERTICAL).pack(side=tk.LEFT, fill=tk.Y, padx=8)

        tk.Label(row2, text="Radius:", bg=BG, font=("Helvetica", 9)).pack(side=tk.LEFT)
        ttk.Scale(row2, from_=2, to=40, orient=tk.HORIZONTAL,
                  variable=self._crop_refine_var, length=90).pack(side=tk.LEFT, padx=(2, 0))
        self._crop_refine_lbl = tk.Label(row2, text="10 px", bg=BG,
                                          font=("Helvetica", 9), width=5)
        self._crop_refine_lbl.pack(side=tk.LEFT, padx=(2, 8))
        self._crop_refine_var.trace_add("write", lambda *_:
            self._crop_refine_lbl.configure(
                text=f"{int(self._crop_refine_var.get())} px"))

        tk.Label(row2, text="Smooth:", bg=BG, font=("Helvetica", 9)).pack(side=tk.LEFT)
        ttk.Scale(row2, from_=0, to=8, orient=tk.HORIZONTAL,
                  variable=self._crop_smooth_var, length=70).pack(side=tk.LEFT, padx=(2, 0))
        self._crop_smooth_lbl = tk.Label(row2, text="2", bg=BG,
                                          font=("Helvetica", 9), width=3)
        self._crop_smooth_lbl.pack(side=tk.LEFT, padx=(2, 8))
        self._crop_smooth_var.trace_add("write", lambda *_:
            self._crop_smooth_lbl.configure(
                text=str(int(self._crop_smooth_var.get()))))

        tk.Label(row2, text="Feather:", bg=BG, font=("Helvetica", 9)).pack(side=tk.LEFT)
        ttk.Scale(row2, from_=0, to=20, orient=tk.HORIZONTAL,
                  variable=self._crop_feather_var, length=80).pack(side=tk.LEFT, padx=(2, 0))
        self._crop_feather_lbl = tk.Label(row2, text="2 px", bg=BG,
                                           font=("Helvetica", 9), width=5)
        self._crop_feather_lbl.pack(side=tk.LEFT, padx=(2, 8))
        self._crop_feather_var.trace_add("write", lambda *_:
            self._crop_feather_lbl.configure(
                text=f"{int(self._crop_feather_var.get())} px"))

        ttk.Separator(row2, orient=tk.VERTICAL).pack(side=tk.LEFT, fill=tk.Y, padx=8)

        self._crop_preview_btn = ttk.Button(row2, text="BG: White",
                                             command=self._crop_cycle_preview)
        self._crop_preview_btn.pack(side=tk.LEFT)

        cv_frame = tk.Frame(page, bg="#1a1a1a")
        cv_frame.pack(fill=tk.BOTH, expand=True, padx=14, pady=(0, 8))

        self._crop_canvas = tk.Canvas(cv_frame, bg="#1a1a1a",
                                       highlightthickness=0, cursor="crosshair")
        self._crop_canvas.pack(fill=tk.BOTH, expand=True)

        self._crop_canvas.bind("<ButtonPress-1>",   self._crop_mouse_down)
        self._crop_canvas.bind("<B1-Motion>",        self._crop_mouse_drag)
        self._crop_canvas.bind("<ButtonRelease-1>",  self._crop_mouse_up)
        self._crop_canvas.bind("<Double-Button-1>",  self._crop_double_click)
        self._crop_canvas.bind("<MouseWheel>",       self._crop_wheel)
        self._crop_canvas.bind("<Motion>",           self._crop_mouse_motion)
        self._crop_canvas.bind("<ButtonPress-3>",    self._crop_right_click)
        self._crop_canvas.bind("<ButtonPress-2>",   self._crop_mid_press)
        self._crop_canvas.bind("<B2-Motion>",        self._crop_mid_drag_move)
        self._crop_canvas.bind("<ButtonRelease-2>",  lambda e: setattr(self, '_crop_mid_drag', None))
        self._crop_canvas.bind("<Configure>",
            lambda e: self._refresh_crop_canvas())
        self._crop_canvas.bind("<Escape>", lambda e: self._crop_esc())

        tk.Label(page,
                 text="Draw Lasso: click vertices, double-click to close  ·  Drag handles  ·  Middle-drag to pan  ·  Scroll to zoom",
                 bg=BG, fg="#888", font=("Helvetica", 8)).pack()
        return page

    # ═══════════════════════════════════════════ Navigation ══════════════════

    def _show_step(self, n):
        # Auto-save crop when navigating away from step 3 without an explicit save
        if self._step == 3 and n != 3 and self._crop_rect is not None \
                and self._crop_result_rgba is None:
            self._crop_silent_save()

        if self._step >= 0:
            self._pages[self._step].pack_forget()
        self._pages[n].pack(fill=tk.BOTH, expand=True)
        self._step = n
        self._step_bar.set_step(n)
        self._back_btn.state(["!disabled"] if n > 0 else ["disabled"])
        self._next_btn.state(["!disabled"] if n < 5 else ["disabled"])
        if n == 3:
            self._skip_export_btn.pack(side=tk.RIGHT, padx=(0, 4),
                                       after=self._next_btn)
        else:
            self._skip_export_btn.pack_forget()
        if n == 2:
            self._load_edit_image()
        elif n == 3:
            self._load_crop_image()
        elif n == 4:
            self._load_dust_step()
        elif n == 5:
            self._load_export_step()

    def _prev_step(self):
        if self._step > 0:
            self._show_step(self._step - 1)

    def _next_step(self):
        if self._step == 0:
            if not self.slots:
                messagebox.showwarning("No images", "Load at least 2 ARW images first.")
                return
            self._show_step(1)
            self._start_combine()   # auto-trigger on entering preview step
        elif self._step == 1:
            self._show_step(2)
        elif self._step == 2:
            self._show_step(3)
        elif self._step == 3:
            self._show_step(4)
        elif self._step == 4:
            self._show_step(5)

    def _handle_undo(self, event=None):
        if self._step == 3:
            self._crop_undo()
        elif self._step == 4:
            self._dust_undo()
        elif self._step == 5:
            self._export_undo()

    def _handle_redo(self, event=None):
        if self._step == 3:
            self._crop_redo()
        elif self._step == 4:
            self._dust_redo()
        elif self._step == 5:
            self._export_redo()

    # ═══════════════════════════════════════════ Step 0 — Load ═══════════════

    def _load_multiple(self):
        if MISSING_DEPS:
            messagebox.showerror("Missing deps", f"Run install.bat\n\n{', '.join(MISSING_DEPS)}")
            return
        paths = filedialog.askopenfilenames(
            title="Select ARW images",
            filetypes=[("Sony RAW", "*.arw *.ARW"),
                       ("All RAW",  "*.raw *.dng *.DNG"),
                       ("All files", "*.*")])
        if not paths:
            return
        self.set_status(f"Loading {len(paths)} image(s)…")
        for p in paths:
            threading.Thread(target=self._load_thumb_thread, args=(p,),
                             daemon=True).start()

    def _load_thumb_thread(self, path):
        try:
            focus_dist = None
            with rawpy.imread(path) as raw:
                try:
                    th = raw.extract_thumb()
                    img = (Image.open(io.BytesIO(th.data))
                           if th.format == rawpy.ThumbFormat.JPEG
                           else Image.fromarray(th.data))
                    # Exif tag 37382 = SubjectDistance (metres, IFRational)
                    try:
                        exif = img.getexif()
                        sd = exif.get(37382)
                        if sd is not None:
                            focus_dist = (float(sd[0]) / float(sd[1])
                                          if isinstance(sd, tuple) and sd[1]
                                          else float(sd))
                            if focus_dist <= 0 or focus_dist > 9999:
                                focus_dist = None
                    except Exception:
                        pass
                except rawpy.LibRawNoThumbnailError:
                    img = Image.fromarray(
                        raw.postprocess(half_size=True, use_auto_wb=True, output_bps=8))
            img.thumbnail((THUMB_W, THUMB_H), Image.LANCZOS)
            tk_img = ImageTk.PhotoImage(img)
            self.root.after(0, self._add_slot, path, tk_img, focus_dist)
        except Exception as e:
            self.root.after(0, self.set_status, f"Error: {e}", True)

    def _add_slot(self, path, tk_img, focus_dist=None):
        if self._empty_lbl.winfo_ismapped():
            self._empty_lbl.grid_remove()
        idx  = len(self.slots)
        slot = ImageSlot(self._slots_inner, idx, path, tk_img, focus_dist, self._remove_image)
        slot.grid(row=idx // SLOTS_PER_ROW, column=idx % SLOTS_PER_ROW, padx=5, pady=5)
        self.slots.append(slot)
        self.set_status(f"{len(self.slots)} image(s) loaded.")

    def _remove_image(self, index):
        self.slots[index].destroy()
        self.slots.pop(index)
        for i, s in enumerate(self.slots):
            s.index = i
            s.grid(row=i // SLOTS_PER_ROW, column=i % SLOTS_PER_ROW, padx=5, pady=5)
        if not self.slots:
            self._empty_lbl.grid(row=0, column=0, padx=20, pady=40)
        self.set_status(f"{len(self.slots)} image(s) loaded.")

    def _clear_all(self):
        for s in self.slots:
            s.destroy()
        self.slots.clear()
        self._empty_lbl.grid(row=0, column=0, padx=20, pady=40)
        self._last_result = None
        self.set_status("Cleared.")

    # ═══════════════════════════════════════════ Step 1 — Preview ════════════

    def _start_combine(self):
        if not self.slots:
            messagebox.showwarning("No images", "Load images first.")
            return
        self._next_btn.state(["disabled"])
        self._progress["value"] = 0
        self._sharpness_mask = None
        self._update_sharpness_warning(0)
        threading.Thread(target=self._combine_thread,
                         args=(list(self.slots), True), daemon=True).start()

    def _combine_thread(self, slots, preview_only):
        try:
            # Sort frames in focus order before stacking
            has_exif = all(s.focus_dist is not None for s in slots)
            if has_exif:
                slots = sorted(slots, key=lambda s: s.focus_dist)
                self.root.after(0, self.set_status, "Frames sorted by Exif focus distance…")
            else:
                slots = sorted(slots, key=lambda s: Path(s.path).name)
                self.root.after(0, self.set_status, "Frames sorted by filename (no Exif focus data)…")

            paths = [s.path for s in slots]
            n     = len(paths)
            images = []
            for i, p in enumerate(paths):
                self.root.after(0, self.set_status, f"Decoding {i+1}/{n}…")
                self.root.after(0, self._set_progress, int(i/n*50))
                with rawpy.imread(p) as raw:
                    rgb = raw.postprocess(
                        half_size=preview_only,
                        use_auto_wb=True,
                        no_auto_bright=False,
                        output_bps=8 if preview_only else 16)
                images.append(rgb)

            self.root.after(0, self.set_status, "Stitching…")
            self.root.after(0, self._set_progress, 55)
            result, max_sharp = self._auto_stitch(images)

            self._last_result = result
            self.root.after(0, self._set_progress, 85)

            gap_count = 0
            self._sharpness_mask = None
            try:
                self.root.after(0, self.set_status, "Checking focus coverage…")
                mask, gap_count = self._compute_gap_mask(result, max_sharp)
                self._sharpness_mask = mask
            except Exception:
                pass

            self.root.after(0, self._set_progress, 100)
            status = f"Done — {result.shape[1]}×{result.shape[0]} px"
            if gap_count > 0:
                status += f"  |  ⚠ {gap_count} focus gap(s) detected"
            else:
                status += "  |  Full focus coverage"
            self.root.after(0, self.set_status, status)
            self.root.after(0, self._show_preview_result, result)
            self.root.after(0, self._update_sharpness_warning, gap_count)
            self.root.after(0, self._next_btn.state, ["!disabled"])
        except Exception as e:
            self.root.after(0, self.set_status, f"Error: {e}", True)
            self.root.after(0, self._next_btn.state, ["!disabled"])

    def _show_preview_result(self, result):
        img = result
        if img.dtype == np.uint16:
            img = (img >> 8).astype(np.uint8)
        self._preview_pil = Image.fromarray(img)
        h, w = img.shape[:2]
        self._preview_dim_lbl.configure(text=f"{w} × {h} px")
        self.root.after(50, self._preview_fit)

    def _preview_fit(self):
        if self._preview_pil is None:
            return
        self._preview_fit_mode = True
        cw = self._preview_canvas.winfo_width()  or 1000
        ch = self._preview_canvas.winfo_height() or 650
        ow, oh = self._preview_pil.size
        self._preview_zoom = min(cw/ow, ch/oh)
        self._preview_render()

    def _preview_100(self):
        self._preview_fit_mode = False
        self._preview_zoom = 1.0
        self._preview_render()

    def _preview_wheel(self, e):
        if self._preview_pil is None:
            return
        self._preview_fit_mode = False
        old_zoom = self._preview_zoom
        new_zoom = max(0.05, min(30.0, old_zoom * (1.20 if e.delta > 0 else (1.0 / 1.20))))
        self._preview_zoom = new_zoom

        ow, oh = self._preview_pil.size
        cw = self._preview_canvas.winfo_width()  or 1000
        ch = self._preview_canvas.winfo_height() or 650
        nw_old = max(1, int(ow * old_zoom));  nh_old = max(1, int(oh * old_zoom))
        nw_new = max(1, int(ow * new_zoom));  nh_new = max(1, int(oh * new_zoom))
        x_old = max(0, (cw - nw_old) // 2);  y_old = max(0, (ch - nh_old) // 2)
        x_new = max(0, (cw - nw_new) // 2);  y_new = max(0, (ch - nh_new) // 2)
        s_x = self._preview_canvas.canvasx(0)
        s_y = self._preview_canvas.canvasy(0)
        img_x = (s_x + e.x - x_old) / old_zoom
        img_y = (s_y + e.y - y_old) / old_zoom
        s_x_new = x_new + img_x * new_zoom - e.x
        s_y_new = y_new + img_y * new_zoom - e.y
        sr_w = max(cw, nw_new);  sr_h = max(ch, nh_new)
        self._preview_pending_scroll = (
            max(0.0, min(1.0, s_x_new / sr_w)) if sr_w > 0 else 0.0,
            max(0.0, min(1.0, s_y_new / sr_h)) if sr_h > 0 else 0.0)

        if getattr(self, "_preview_render_job", None):
            self.root.after_cancel(self._preview_render_job)
        self._preview_render_job = self.root.after(20, self._preview_render)

    def _preview_render(self):
        if self._preview_pil is None:
            return
        ow, oh = self._preview_pil.size
        nw = max(1, int(ow * self._preview_zoom))
        nh = max(1, int(oh * self._preview_zoom))
        resized = self._preview_pil.resize((nw, nh),
            Image.BILINEAR if self._preview_zoom > 1.0 else Image.LANCZOS)

        # Orange overlay on blurry regions
        if (self._show_sharpness_overlay and
                self._sharpness_mask is not None and
                self._sharpness_mask.any()):
            mask_pil = Image.fromarray(
                (self._sharpness_mask.astype(np.uint8) * 255), mode='L')
            mask_resized = mask_pil.resize((nw, nh), Image.NEAREST)
            mask_arr = np.array(mask_resized) > 128
            overlay = np.zeros((nh, nw, 4), dtype=np.uint8)
            overlay[mask_arr] = [255, 110, 0, 150]   # orange, semi-transparent
            overlay_pil = Image.fromarray(overlay, 'RGBA')
            resized = Image.alpha_composite(
                resized.convert('RGBA'), overlay_pil).convert('RGB')
        self._preview_tk_img = ImageTk.PhotoImage(resized)

        cw = self._preview_canvas.winfo_width()  or 1000
        ch = self._preview_canvas.winfo_height() or 650
        x  = max(0, (cw - nw) // 2)
        y  = max(0, (ch - nh) // 2)

        self._preview_canvas.delete("all")
        self._preview_canvas.create_image(x, y, anchor=tk.NW,
                                           image=self._preview_tk_img)
        self._preview_canvas.configure(
            scrollregion=(0, 0, max(cw, nw), max(ch, nh)))
        ps = getattr(self, "_preview_pending_scroll", None)
        if ps is not None:
            self._preview_pending_scroll = None
            self._preview_canvas.xview_moveto(ps[0])
            self._preview_canvas.yview_moveto(ps[1])
        self._preview_zoom_lbl.configure(
            text=f"Zoom: {int(self._preview_zoom*100)}%")

    def _preview_toggle_fix(self):
        self._preview_fix_mode = not self._preview_fix_mode
        if self._preview_fix_mode:
            self._preview_fix_btn.configure(text="Cancel Fix")
            self._preview_canvas.configure(cursor="crosshair")
            self._preview_canvas.bind("<ButtonPress-1>", self._preview_fix_click)
            self._preview_canvas.bind("<B1-Motion>", lambda e: None)
            self.set_status("Fix Artifact: click directly on the white blob to fill it")
        else:
            self._preview_fix_btn.configure(text="Fix Artifact")
            self._preview_canvas.configure(cursor="fleur")
            self._preview_canvas.bind("<ButtonPress-1>",
                lambda e: self._preview_canvas.scan_mark(e.x, e.y))
            self._preview_canvas.bind("<B1-Motion>",
                lambda e: self._preview_canvas.scan_dragto(e.x, e.y, gain=1))
            self.set_status("")

    def _preview_fix_click(self, e):
        if self._preview_pil is None:
            return
        zoom = self._preview_zoom
        ow, oh = self._preview_pil.size
        nw = max(1, int(ow * zoom))
        nh = max(1, int(oh * zoom))
        cw = self._preview_canvas.winfo_width()  or 1000
        ch = self._preview_canvas.winfo_height() or 650
        x_off = max(0, (cw - nw) // 2)
        y_off = max(0, (ch - nh) // 2)

        img_x = int((self._preview_canvas.canvasx(e.x) - x_off) / zoom)
        img_y = int((self._preview_canvas.canvasy(e.y) - y_off) / zoom)
        img_x = max(0, min(ow - 1, img_x))
        img_y = max(0, min(oh - 1, img_y))

        arr  = np.array(self._preview_pil)          # (H,W,3) uint8
        grey = cv2.cvtColor(arr, cv2.COLOR_RGB2GRAY)

        if int(grey[img_y, img_x]) < 100:
            self.set_status("Fix Artifact: clicked pixel is too dark — click on the white/bright blob")
            return

        # Flood-fill from the seed point to find the connected bright region.
        # loDiff/upDiff=50 captures smooth gradients at blob edges.
        h_img, w_img = grey.shape
        flood_mask = np.zeros((h_img + 2, w_img + 2), dtype=np.uint8)
        fill_flags = cv2.FLOODFILL_MASK_ONLY | (255 << 8) | cv2.FLOODFILL_FIXED_RANGE
        cv2.floodFill(grey.copy(), flood_mask, (img_x, img_y),
                      newVal=0, loDiff=50, upDiff=50, flags=fill_flags)
        region = flood_mask[1:-1, 1:-1]             # strip the 1-px border padding

        if not region.any():
            self.set_status("Fix Artifact: flood fill found nothing — try clicking the centre of the blob")
            return

        # Dilate slightly so inpainting has a border to sample from
        inpaint_mask = cv2.dilate(region, np.ones((7, 7), np.uint8))
        fixed = cv2.inpaint(arr, inpaint_mask, inpaintRadius=12, flags=cv2.INPAINT_TELEA)

        self._preview_pil = Image.fromarray(fixed)

        # Patch _last_result so the fix carries into downstream steps
        if self._last_result is not None:
            if self._last_result.dtype == np.uint8:
                np.copyto(self._last_result, fixed,
                          where=(inpaint_mask[:, :, np.newaxis] > 0))
            else:
                fixed16 = fixed.astype(np.uint16) << 8
                mask3   = inpaint_mask[:, :, np.newaxis] > 0
                self._last_result = np.where(mask3, fixed16, self._last_result)

        px = int(region.sum())
        self.set_status(f"Fix Artifact: filled {px:,} px — click another artifact or 'Cancel Fix' when done")
        self._preview_render()

    # ═══════════════════════════════════════════ Step 2 — Auto Edit ═══════════

    def _load_edit_image(self):
        if self._last_result is None:
            self.set_status("No image — complete the Preview step first.", True)
            return
        self._edit_source        = self._last_result.copy()
        self._edit_result        = self._edit_source
        self._edit_wb_point      = None
        self._edit_picking       = False
        self._edit_wb_drag_start = None
        self._edit_wb_drag_end   = None
        self._edit_wb_btn.configure(text="Pick White Point")
        self._edit_info_lbl.configure(text="No edits applied yet")
        self._load_edit_display(self._edit_source)

    def _load_edit_display(self, img):
        img8 = (img >> 8).astype(np.uint8) if img.dtype == np.uint16 else img.astype(np.uint8)
        h, w = img8.shape[:2]
        self._edit_pil     = Image.fromarray(img8)   # full resolution — no pre-downscale
        self._edit_orig_wh = (w, h)
        self._edit_last_nw = 0
        self._edit_last_nh = 0
        self._edit_fit     = True
        self.root.after(50, self._edit_refresh_canvas)

    def _edit_refresh_canvas(self):
        if self._edit_pil is None:
            return
        ow, oh = self._edit_orig_wh if self._edit_orig_wh != (0, 0) else self._edit_pil.size
        cw = self._edit_canvas.winfo_width()  or 1000
        ch = self._edit_canvas.winfo_height() or 650
        if self._edit_fit:
            self._edit_zoom = min(cw / ow, ch / oh)
        nw = max(1, int(ow * self._edit_zoom))
        nh = max(1, int(oh * self._edit_zoom))
        x_off = max(0, (cw - nw) // 2)
        y_off = max(0, (ch - nh) // 2)
        self._edit_offset = (x_off, y_off)

        if nw != self._edit_last_nw or nh != self._edit_last_nh:
            base = self._edit_pil.resize((nw, nh),
                Image.BILINEAR if self._edit_zoom > 1.0 else Image.LANCZOS)
            self._edit_base_tk = ImageTk.PhotoImage(base)
            self._edit_last_nw, self._edit_last_nh = nw, nh
            self._edit_canvas.delete("all")
            self._edit_canvas.create_image(x_off, y_off, anchor=tk.NW,
                                            image=self._edit_base_tk, tags="edit_bg")
        elif (x_off, y_off) != self._edit_last_off:
            self._edit_canvas.coords("edit_bg", x_off, y_off)
        self._edit_last_off = (x_off, y_off)

        self._edit_canvas.delete("edit_ov")
        if self._edit_wb_point is not None:
            wx0, wy0, wx1, wy1 = self._edit_wb_point
            rx0 = int(wx0 * self._edit_zoom) + x_off
            ry0 = int(wy0 * self._edit_zoom) + y_off
            rx1 = int(wx1 * self._edit_zoom) + x_off
            ry1 = int(wy1 * self._edit_zoom) + y_off
            self._edit_canvas.create_rectangle(rx0, ry0, rx1, ry1,
                                                outline="#00ff00", width=2, tags="edit_ov")

        if self._edit_picking and self._edit_wb_drag_start is not None:
            sx_c, sy_c = self._edit_wb_drag_start[0], self._edit_wb_drag_start[1]
            ex_c, ey_c = self._edit_wb_drag_end if self._edit_wb_drag_end else (sx_c, sy_c)
            self._edit_canvas.create_rectangle(sx_c, sy_c, ex_c, ey_c,
                                                outline="#00ff00", width=1,
                                                dash=(4, 4), tags="edit_ov")

        self._edit_canvas.configure(
            scrollregion=(0, 0, max(cw, nw + x_off), max(ch, nh + y_off)))
        ps = getattr(self, "_edit_pending_scroll", None)
        if ps is not None:
            self._edit_pending_scroll = None
            self._edit_canvas.xview_moveto(ps[0])
            self._edit_canvas.yview_moveto(ps[1])

    def _edit_canvas_to_image(self, ex, ey):
        cx = self._edit_canvas.canvasx(ex)
        cy = self._edit_canvas.canvasy(ey)
        ox, oy = self._edit_offset
        return (cx - ox) / self._edit_zoom, (cy - oy) / self._edit_zoom

    def _edit_toggle_pick(self):
        self._edit_picking = not self._edit_picking
        if self._edit_picking:
            self._edit_wb_drag_start = None
            self._edit_wb_drag_end   = None
            self._edit_wb_btn.configure(text="Cancel Pick")
            self._edit_canvas.configure(cursor="tcross")
            self.set_status("Drag a rectangle over a neutral grey area to set the white balance.")
        else:
            self._edit_wb_drag_start = None
            self._edit_wb_drag_end   = None
            self._edit_wb_btn.configure(text="Pick White Point")
            self._edit_canvas.configure(cursor="crosshair")

    def _edit_canvas_press(self, e):
        if not self._edit_picking:
            return
        ix, iy = self._edit_canvas_to_image(e.x, e.y)
        self._edit_wb_drag_start = (e.x, e.y, float(ix), float(iy))
        self._edit_wb_drag_end   = (e.x, e.y)

    def _edit_canvas_drag_wb(self, e):
        if not self._edit_picking or self._edit_wb_drag_start is None:
            return
        self._edit_wb_drag_end = (e.x, e.y)
        self._edit_refresh_canvas()

    def _edit_canvas_release_wb(self, e):
        if not self._edit_picking or self._edit_wb_drag_start is None:
            return
        if self._edit_source is None:
            return
        _, _, isx, isy = self._edit_wb_drag_start
        ix, iy = self._edit_canvas_to_image(e.x, e.y)
        h, w = self._edit_source.shape[:2]
        x0 = max(0, min(w - 1, int(min(isx, ix))))
        x1 = max(0, min(w - 1, int(max(isx, ix))))
        y0 = max(0, min(h - 1, int(min(isy, iy))))
        y1 = max(0, min(h - 1, int(max(isy, iy))))
        # If barely moved treat it as a point click — use a 10px patch
        if x1 - x0 < 3 and y1 - y0 < 3:
            r = 10
            cx, cy = int(isx), int(isy)
            x0, y0 = max(0, cx - r), max(0, cy - r)
            x1, y1 = min(w - 1, cx + r), min(h - 1, cy + r)
        self._edit_wb_drag_start = None
        self._edit_wb_drag_end   = None
        self._edit_wb_point = (x0, y0, x1, y1)
        self._edit_picking  = False
        self._edit_wb_btn.configure(text="Pick White Point")
        self._edit_canvas.configure(cursor="crosshair")
        patch = self._edit_source[y0:y1 + 1, x0:x1 + 1].astype(np.float32)
        avg   = patch.mean(axis=(0, 1))
        if self._edit_source.dtype == np.uint16:
            avg = avg / 257.0
        area = (x1 - x0 + 1) * (y1 - y0 + 1)
        self.set_status(
            f"Grey point set  ({x0},{y0})→({x1},{y1})  {area} px  —  "
            f"RGB: ({avg[0]:.0f}, {avg[1]:.0f}, {avg[2]:.0f})")
        self._edit_apply()

    def _edit_wheel(self, e):
        self._edit_fit = False
        old_zoom = self._edit_zoom
        new_zoom = max(0.05, min(30.0, old_zoom * (1.20 if e.delta > 0 else (1.0 / 1.20))))
        self._edit_zoom  = new_zoom
        self._edit_last_nw = 0

        ow, oh = self._edit_orig_wh if self._edit_orig_wh != (0, 0) else (
            self._edit_pil.size if self._edit_pil else (1, 1))
        cw = self._edit_canvas.winfo_width()  or 1000
        ch = self._edit_canvas.winfo_height() or 650
        nw_old = max(1, int(ow * old_zoom));  nh_old = max(1, int(oh * old_zoom))
        nw_new = max(1, int(ow * new_zoom));  nh_new = max(1, int(oh * new_zoom))
        x_old = max(0, (cw - nw_old) // 2);  y_old = max(0, (ch - nh_old) // 2)
        x_new = max(0, (cw - nw_new) // 2);  y_new = max(0, (ch - nh_new) // 2)
        s_x = self._edit_canvas.canvasx(0)
        s_y = self._edit_canvas.canvasy(0)
        img_x = (s_x + e.x - x_old) / old_zoom
        img_y = (s_y + e.y - y_old) / old_zoom
        s_x_new = x_new + img_x * new_zoom - e.x
        s_y_new = y_new + img_y * new_zoom - e.y
        sr_w = max(cw, nw_new + x_new);  sr_h = max(ch, nh_new + y_new)
        self._edit_pending_scroll = (
            max(0.0, min(1.0, s_x_new / sr_w)) if sr_w > 0 else 0.0,
            max(0.0, min(1.0, s_y_new / sr_h)) if sr_h > 0 else 0.0)

        if getattr(self, "_edit_render_job", None):
            self.root.after_cancel(self._edit_render_job)
        self._edit_render_job = self.root.after(20, self._edit_refresh_canvas)

    def _edit_fit_view(self):
        self._edit_fit = True
        self._edit_last_nw = 0
        self._edit_refresh_canvas()

    def _edit_set_zoom(self, z):
        self._edit_fit  = False
        self._edit_zoom = z
        self._edit_last_nw = 0
        self._edit_refresh_canvas()

    def _edit_apply(self):
        if self._edit_source is None:
            return
        if self._edit_wb_point is not None:
            img = self._apply_white_balance(self._edit_source, *self._edit_wb_point)
            x0, y0, x1, y1 = self._edit_wb_point
            area = (x1 - x0 + 1) * (y1 - y0 + 1)
            self._edit_info_lbl.configure(
                text=f"White balance applied — {area} px sample")
            self.set_status("White balance applied.")
        else:
            img = self._edit_source
            self._edit_info_lbl.configure(text="")
        self._edit_result = img
        self._load_edit_display(img)

    def _edit_apply_auto(self):
        if self._edit_source is None:
            return
        img = self._edit_source
        steps = []

        # White balance + brightness normalisation — use manual point if set,
        # otherwise detect background from image corners.
        # Both paths normalise to _WB_TARGET so every board ends up the same brightness.
        if self._edit_wb_point is not None:
            img = self._apply_white_balance(img, *self._edit_wb_point)
            x0, y0, x1, y1 = self._edit_wb_point
            steps.append(f"WB+brightness ({(x1-x0+1)*(y1-y0+1)} px sample)")
        else:
            img = self._auto_white_balance(img)
            steps.append("auto WB+brightness (corners)")

        if self._edit_do_levels.get():
            img = self._apply_auto_levels(img)
            steps.append("levels")

        if self._edit_do_pcb.get():
            img, count = self._apply_pcb_color(img)
            steps.append(f"PCB color ({count} px)")

        if self._edit_do_sharpen.get():
            img = self._unsharp_mask(img)
            steps.append("sharpen")

        self._edit_result = img
        self._edit_info_lbl.configure(text="Auto edit: " + ", ".join(steps))
        self.set_status("Auto edit applied — " + ", ".join(steps) + ".")
        self._load_edit_display(img)

    def _edit_reset(self):
        if self._edit_source is None:
            return
        self._edit_result        = self._edit_source
        self._edit_wb_point      = None
        self._edit_wb_drag_start = None
        self._edit_wb_drag_end   = None
        self._edit_info_lbl.configure(text="Reset to original")
        self._load_edit_display(self._edit_source)
        self.set_status("Reset to original stacked image.")

    # ═══════════════════════════════════════════ Step 3 — Crop Board ════════

    # _crop_rect: np.array shape (N,2) float32 — N polygon vertices following
    # the board outline (from cv2.approxPolyDP).  Every vertex is a draggable
    # handle.  On save the polygon is applied as a mask and the bounding box
    # is cropped out.

    def _load_crop_image(self):
        if self._edit_result is not None:
            img = self._edit_result
        elif self._last_result is not None:
            img = self._last_result
        else:
            self.set_status("No image — complete the Preview step first.", True)
            return

        # If returning to this step with the same source image, just redisplay
        if id(img) == self._crop_source_id and self._crop_rect is not None:
            self.root.after(100, self._refresh_crop_canvas)
            return

        self._crop_source_id  = id(img)
        self._crop_history    = []
        self._crop_redo_stack = []
        self._crop_holes      = []
        self._crop_cut_active = []
        self._crop_result_rgba = None   # new source → old save is stale

        img8 = (img >> 8).astype(np.uint8) if img.dtype == np.uint16 else img.astype(np.uint8)
        polygon, detection_ok = self._detect_and_mask_board(img8)

        orig_h, orig_w = img8.shape[:2]
        self._crop_orig_wh = (orig_w, orig_h)
        # Keep full resolution — viewport rendering crops only the visible slice
        self._crop_pil = Image.fromarray(img8)

        self._crop_full     = img      # original, unmasked — masking only applied on save
        self._crop_image    = img8
        self._crop_rect     = polygon  # np.array (N,2)
        self._crop_last_view_key = None   # invalidate cached background

        if self._crop_auto_var.get() and detection_ok:
            self.set_status(f"Auto-cropping ({len(polygon)} pts)…")
            self.root.after(0, self._apply_crop)
            return

        if not detection_ok:
            self.set_status("Board not detected — drag handles to refine the outline, then Crop & Save.")
        else:
            self.set_status(f"Board outline detected ({len(polygon)} pts) — drag handles to refine, then Crop & Save.")
        self.root.after(100, self._refresh_crop_canvas)

    def _board_contour_from_gray(self, gray, dilation_px=60, close_px=50):
        """Detect board contour using border-connected background flooding."""
        h, w = gray.shape
        _, light = cv2.threshold(gray, 210, 255, cv2.THRESH_BINARY)

        n_lbl, labels = cv2.connectedComponents(light, connectivity=8)
        bm = np.zeros((h, w), dtype=bool)
        bm[0, :] = bm[-1, :] = bm[:, 0] = bm[:, -1] = True
        border_labels = set(int(v) for v in np.unique(labels[bm]) if v > 0)

        bg_connected = np.isin(labels, list(border_labels)).astype(np.uint8) * 255
        k_dil = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (dilation_px, dilation_px))
        bg_final = cv2.dilate(bg_connected, k_dil)

        board_rough = (bg_final == 0).astype(np.uint8) * 255
        k_cl = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (close_px, close_px))
        board_filled = cv2.morphologyEx(board_rough, cv2.MORPH_CLOSE, k_cl)

        contours, _ = cv2.findContours(board_filled, cv2.RETR_EXTERNAL,
                                        cv2.CHAIN_APPROX_SIMPLE)
        if not contours:
            return None
        return max(contours, key=cv2.contourArea)

    def _contour_to_polygon(self, contour):
        """Simplify a contour to a manageable polygon (approxPolyDP)."""
        peri = cv2.arcLength(contour, True)
        # Start coarse; if too few points refine
        for eps_frac in (0.008, 0.004, 0.002):
            poly = cv2.approxPolyDP(contour, eps_frac * peri, True)
            if len(poly) >= 6:
                break
        return poly.reshape(-1, 2).astype(np.float32)

    def _detect_and_mask_board(self, img8):
        """Detect board outline. Returns (polygon np.float32 (N,2), detection_ok bool).
        detection_ok is False when detection failed and the hardcoded fallback is used."""
        h, w = img8.shape[:2]
        gray = cv2.cvtColor(img8, cv2.COLOR_RGB2GRAY)

        fallback = np.float32([
            [w*.1, h*.9], [w*.1, h*.6], [w*.1, h*.1],
            [w*.6, h*.1], [w*.9, h*.1], [w*.9, h*.4],
            [w*.9, h*.9], [w*.4, h*.9]])

        contour = self._board_contour_from_gray(gray)
        if contour is None:
            return fallback, False

        return self._contour_to_polygon(contour), True

    def _auto_detect_board_polygon(self):
        """Re-detect board polygon from the preview image."""
        if self._crop_image is None:
            return None
        gray = cv2.cvtColor(self._crop_image, cv2.COLOR_RGB2GRAY)
        contour = self._board_contour_from_gray(gray, dilation_px=20, close_px=20)
        if contour is None:
            return None
        return self._contour_to_polygon(contour)

    def _crop_auto_detect(self):
        p = self._auto_detect_board_polygon()
        if p is not None:
            self._crop_rect = p
            self.set_status(f"Re-detected: {len(p)} pts")
            self._refresh_crop_canvas()

    def _crop_fit_view(self):
        self._crop_fit = True
        self._refresh_crop_canvas()

    def _crop_100(self):
        self._crop_fit  = False
        self._crop_zoom = 1.0
        ow, oh = self._crop_orig_wh if self._crop_orig_wh != (0, 0) else (1, 1)
        cw = self._crop_canvas.winfo_width()  or 1000
        ch = self._crop_canvas.winfo_height() or 650
        nw, nh = int(ow * 1.0), int(oh * 1.0)
        self._crop_pan = [max(0, (cw - nw) // 2), max(0, (ch - nh) // 2)]
        self._refresh_crop_canvas()

    def _crop_wheel(self, e):
        self._crop_fit = False
        old_zoom = self._crop_zoom
        factor = 1.20 if e.delta > 0 else (1.0 / 1.20)
        self._crop_zoom = max(0.05, min(old_zoom * factor, 30.0))
        # Zoom toward cursor: keep the image point under the cursor fixed
        ow, oh = self._crop_orig_wh if self._crop_orig_wh != (0, 0) else self._crop_pil.size
        nw = max(1, int(ow * self._crop_zoom))
        nh = max(1, int(oh * self._crop_zoom))
        cw = self._crop_canvas.winfo_width()  or 1000
        ch = self._crop_canvas.winfo_height() or 650
        img_x = (e.x - self._crop_pan[0]) / old_zoom
        img_y = (e.y - self._crop_pan[1]) / old_zoom
        self._crop_pan[0] = e.x - img_x * self._crop_zoom
        self._crop_pan[1] = e.y - img_y * self._crop_zoom
        self._crop_clamp_pan(nw, nh, cw, ch)
        if getattr(self, "_crop_render_job", None):
            self.root.after_cancel(self._crop_render_job)
        self._crop_render_job = self.root.after(20, self._refresh_crop_canvas)
        return "break"  # prevent Tkinter default canvas scroll

    def _crop_clamp_pan(self, nw, nh, cw, ch):
        if nw <= cw:
            self._crop_pan[0] = (cw - nw) // 2
        else:
            self._crop_pan[0] = max(cw - nw, min(0, self._crop_pan[0]))
        if nh <= ch:
            self._crop_pan[1] = (ch - nh) // 2
        else:
            self._crop_pan[1] = max(ch - nh, min(0, self._crop_pan[1]))

    def _crop_mid_press(self, e):
        self._crop_mid_drag = (e.x, e.y, self._crop_pan[0], self._crop_pan[1])

    def _crop_mid_drag_move(self, e):
        if not self._crop_mid_drag:
            return
        sx, sy, spx, spy = self._crop_mid_drag
        if self._crop_pil is None:
            return
        ow, oh = self._crop_orig_wh if self._crop_orig_wh != (0, 0) else self._crop_pil.size
        nw = max(1, int(ow * self._crop_zoom))
        nh = max(1, int(oh * self._crop_zoom))
        cw = self._crop_canvas.winfo_width()  or 1000
        ch = self._crop_canvas.winfo_height() or 650
        self._crop_pan[0] = spx + (e.x - sx)
        self._crop_pan[1] = spy + (e.y - sy)
        self._crop_clamp_pan(nw, nh, cw, ch)
        if not self._crop_pending:
            self._crop_pending = True
            self.root.after_idle(self._refresh_crop_canvas)

    def _refresh_crop_canvas(self):
        if self._crop_pil is None:
            return
        self._crop_pending = False

        ow, oh = self._crop_orig_wh if self._crop_orig_wh != (0, 0) else self._crop_pil.size
        cw = self._crop_canvas.winfo_width()  or 1000
        ch = self._crop_canvas.winfo_height() or 650

        nw = max(1, int(ow * self._crop_zoom))
        nh = max(1, int(oh * self._crop_zoom))

        if self._crop_fit:
            self._crop_zoom = min(cw / ow, ch / oh)
            nw = max(1, int(ow * self._crop_zoom))
            nh = max(1, int(oh * self._crop_zoom))
            self._crop_pan[0] = (cw - nw) // 2
            self._crop_pan[1] = (ch - nh) // 2
        else:
            self._crop_clamp_pan(nw, nh, cw, ch)

        x_off = int(self._crop_pan[0])
        y_off = int(self._crop_pan[1])
        self._crop_offset = (x_off, y_off)

        # ── Background image — viewport rendering ────────────────────────────
        # Zoom (_crop_zoom) is defined relative to full-res (_crop_orig_wh).
        # src_pil may be downscaled (max 1200 px), so we convert visible-region
        # coords from full-res space into src_pil space before cropping.
        src_pil = (self._crop_preview_pil
                   if (self._crop_preview_pil is not None
                       and self._crop_preview_bg != "white")
                   else self._crop_pil)

        sw, sh = src_pil.size                  # actual PIL dimensions
        sx = sw / ow                           # src_pil / full-res scale factors
        sy = sh / oh

        # Visible src_pil region (in src_pil pixel coords)
        spx0 = max(0,  (-x_off)      * sx / self._crop_zoom)
        spy0 = max(0,  (-y_off)      * sy / self._crop_zoom)
        spx1 = min(sw, (cw - x_off)  * sx / self._crop_zoom)
        spy1 = min(sh, (ch - y_off)  * sy / self._crop_zoom)
        spx0i, spy0i = int(spx0), int(spy0)
        spx1i, spy1i = max(spx0i + 1, int(spx1) + 1), max(spy0i + 1, int(spy1) + 1)
        spx1i, spy1i = min(spx1i, sw), min(spy1i, sh)

        # Canvas display dimensions for this crop
        disp_w = max(1, min(cw, round((spx1i - spx0i) * self._crop_zoom / sx)))
        disp_h = max(1, min(ch, round((spy1i - spy0i) * self._crop_zoom / sy)))
        img_x  = max(0, x_off)
        img_y  = max(0, y_off)

        view_key = (spx0i, spy0i, spx1i, spy1i, disp_w, disp_h, id(src_pil))
        if view_key != self._crop_last_view_key:
            region = src_pil.crop((spx0i, spy0i, spx1i, spy1i))
            base   = region.resize((disp_w, disp_h), Image.BILINEAR)
            self._crop_base_tk       = ImageTk.PhotoImage(base)
            self._crop_last_view_key = view_key
            self._crop_canvas.delete("all")
            self._crop_canvas.create_image(img_x, img_y, anchor=tk.NW,
                                            image=self._crop_base_tk, tags="crop_bg")
        elif (img_x, img_y) != self._crop_last_off:
            self._crop_canvas.coords("crop_bg", img_x, img_y)
        self._crop_last_off = (img_x, img_y)

        # ── Overlays ─────────────────────────────────────────────────────────
        self._crop_canvas.delete("crop_ov")

        # Existing polygon — hidden when colored bg is active (product edge is already visible)
        if self._crop_rect is not None and self._crop_preview_bg == "white":
            pts_s = (self._crop_rect * self._crop_zoom).astype(np.int32)
            N = len(pts_s)
            for i in range(N):
                x1 = int(pts_s[i][0]) + x_off
                y1 = int(pts_s[i][1]) + y_off
                x2 = int(pts_s[(i + 1) % N][0]) + x_off
                y2 = int(pts_s[(i + 1) % N][1]) + y_off
                self._crop_canvas.create_line(x1, y1, x2, y2,
                                               fill="#ff5050", width=2, tags="crop_ov")
            # Handles: orange in delete mode (click to remove), white in normal mode
            # Hidden only during active lasso drawing (would be confusing)
            if not self._crop_lasso_mode:
                HS = 6
                h_fill    = "#ff9900" if self._crop_delete_mode else "white"
                h_outline = "#cc6600" if self._crop_delete_mode else "#dc3232"
                for px, py in pts_s:
                    cx, cy = int(px) + x_off, int(py) + y_off
                    self._crop_canvas.create_oval(cx - HS, cy - HS, cx + HS, cy + HS,
                                                   fill=h_fill, outline=h_outline,
                                                   width=2, tags="crop_ov")

        # Holes (finalized cutouts) — always red + editable handles like main polygon
        if self._crop_holes and self._crop_preview_bg == "white":
            HS = 6
            for hole in self._crop_holes:
                nh = len(hole)
                for i in range(nh):
                    x1 = int(hole[i][0]          * self._crop_zoom) + x_off
                    y1 = int(hole[i][1]          * self._crop_zoom) + y_off
                    x2 = int(hole[(i+1) % nh][0] * self._crop_zoom) + x_off
                    y2 = int(hole[(i+1) % nh][1] * self._crop_zoom) + y_off
                    self._crop_canvas.create_line(x1, y1, x2, y2,
                                                   fill="#ff5050", width=2, tags="crop_ov")
                for pt in hole:
                    chx = int(pt[0] * self._crop_zoom) + x_off
                    chy = int(pt[1] * self._crop_zoom) + y_off
                    self._crop_canvas.create_oval(chx-HS, chy-HS, chx+HS, chy+HS,
                                                   fill="white", outline="#dc3232",
                                                   width=2, tags="crop_ov")

        # In-progress cut polygon (drawing mode)
        if self._crop_cut_mode and self._crop_cut_active and self._crop_preview_bg == "white":
            ap = self._crop_cut_active
            n  = len(ap)
            # Edges between placed points
            for i in range(n - 1):
                x1 = int(ap[i][0]   * self._crop_zoom) + x_off
                y1 = int(ap[i][1]   * self._crop_zoom) + y_off
                x2 = int(ap[i+1][0] * self._crop_zoom) + x_off
                y2 = int(ap[i+1][1] * self._crop_zoom) + y_off
                self._crop_canvas.create_line(x1, y1, x2, y2,
                                               fill="#ff9900", width=2,
                                               dash=(8, 4), tags="crop_ov")
            # Close-preview dashes when ≥3 points
            if n >= 3:
                x1 = int(ap[-1][0] * self._crop_zoom) + x_off
                y1 = int(ap[-1][1] * self._crop_zoom) + y_off
                x2 = int(ap[0][0]  * self._crop_zoom) + x_off
                y2 = int(ap[0][1]  * self._crop_zoom) + y_off
                self._crop_canvas.create_line(x1, y1, x2, y2,
                                               fill="#ff9900", width=1,
                                               dash=(5, 3), tags="crop_ov")
            # Rubber-band from last point to cursor
            if self._crop_lasso_cursor is not None:
                lx = int(ap[-1][0] * self._crop_zoom) + x_off
                ly = int(ap[-1][1] * self._crop_zoom) + y_off
                mx = int(self._crop_lasso_cursor[0] * self._crop_zoom) + x_off
                my = int(self._crop_lasso_cursor[1] * self._crop_zoom) + y_off
                self._crop_canvas.create_line(lx, ly, mx, my,
                                               fill="#ff9900", width=1,
                                               dash=(4, 4), tags="crop_ov")
            # Handles — same style as main crop handles
            HS = 6
            for k, apt in enumerate(ap):
                cx_c = int(apt[0] * self._crop_zoom) + x_off
                cy_c = int(apt[1] * self._crop_zoom) + y_off
                if k == 0 and n >= 3:
                    self._crop_canvas.create_oval(cx_c - HS - 5, cy_c - HS - 5,
                                                   cx_c + HS + 5, cy_c + HS + 5,
                                                   outline="#00ff44", width=2, tags="crop_ov")
                self._crop_canvas.create_oval(cx_c - HS, cy_c - HS, cx_c + HS, cy_c + HS,
                                               fill="white", outline="#dc3232",
                                               width=2, tags="crop_ov")

        # Pending (closed) lasso — solid green, old polygon still visible in red
        if self._crop_lasso_closed and len(self._crop_lasso_pts) >= 3 and self._crop_preview_bg == "white":
            lp  = self._crop_lasso_pts
            nlp = len(lp)
            for i in range(nlp):
                x1 = int(lp[i][0]          * self._crop_zoom) + x_off
                y1 = int(lp[i][1]          * self._crop_zoom) + y_off
                x2 = int(lp[(i+1) % nlp][0] * self._crop_zoom) + x_off
                y2 = int(lp[(i+1) % nlp][1] * self._crop_zoom) + y_off
                self._crop_canvas.create_line(x1, y1, x2, y2,
                                               fill="#00ff44", width=2, tags="crop_ov")
            for (ix_l, iy_l) in lp:
                cx_l = int(ix_l * self._crop_zoom) + x_off
                cy_l = int(iy_l * self._crop_zoom) + y_off
                self._crop_canvas.create_oval(cx_l-4, cy_l-4, cx_l+4, cy_l+4,
                                               fill="#00ff44", outline="white",
                                               width=1, tags="crop_ov")

        # In-progress lasso polygon (only shown on white bg)
        if self._crop_lasso_mode and self._crop_preview_bg == "white":
            lp = self._crop_lasso_pts
            for i in range(len(lp) - 1):
                x1 = int(lp[i][0]   * self._crop_zoom) + x_off
                y1 = int(lp[i][1]   * self._crop_zoom) + y_off
                x2 = int(lp[i+1][0] * self._crop_zoom) + x_off
                y2 = int(lp[i+1][1] * self._crop_zoom) + y_off
                self._crop_canvas.create_line(x1, y1, x2, y2,
                                               fill="#00ff44", width=2,
                                               dash=(8, 4), tags="crop_ov")
            for (ix, iy) in lp:
                cx = int(ix * self._crop_zoom) + x_off
                cy = int(iy * self._crop_zoom) + y_off
                self._crop_canvas.create_oval(cx-5, cy-5, cx+5, cy+5,
                                               fill="#00ff44", outline="white",
                                               width=1, tags="crop_ov")
            # Close-target ring on first vertex when ≥3 points placed
            if len(lp) >= 3:
                fx = int(lp[0][0] * self._crop_zoom) + x_off
                fy = int(lp[0][1] * self._crop_zoom) + y_off
                self._crop_canvas.create_oval(fx-10, fy-10, fx+10, fy+10,
                                               outline="#00ff44", width=2, tags="crop_ov")
            # Rubber-band line from last vertex to cursor
            if lp and self._crop_lasso_cursor is not None:
                lx = int(lp[-1][0] * self._crop_zoom) + x_off
                ly = int(lp[-1][1] * self._crop_zoom) + y_off
                mx = int(self._crop_lasso_cursor[0] * self._crop_zoom) + x_off
                my = int(self._crop_lasso_cursor[1] * self._crop_zoom) + y_off
                self._crop_canvas.create_line(lx, ly, mx, my,
                                               fill="#00ff44", width=1,
                                               dash=(4, 4), tags="crop_ov")

        # 3-pt Arc overlay
        if self._crop_arc_mode:
            def _arc_poly(pid):
                if pid == -1:
                    return self._crop_rect
                return self._crop_holes[pid] if pid < len(self._crop_holes) else None

            for pid, vidx in self._crop_arc_pts:
                poly = _arc_poly(pid)
                if poly is None or vidx >= len(poly):
                    continue
                px, py = poly[vidx]
                cx_a = int(px * self._crop_zoom) + x_off
                cy_a = int(py * self._crop_zoom) + y_off
                self._crop_canvas.create_oval(cx_a-9, cy_a-9, cx_a+9, cy_a+9,
                                               fill="#ff9900", outline="white",
                                               width=2, tags="crop_ov")

            cur = self._crop_lasso_cursor
            if len(self._crop_arc_pts) == 1 and cur:
                pid0, vi0 = self._crop_arc_pts[0]
                poly = _arc_poly(pid0)
                if poly is not None and vi0 < len(poly):
                    p1 = poly[vi0]
                    self._crop_canvas.create_line(
                        int(p1[0]*self._crop_zoom)+x_off,
                        int(p1[1]*self._crop_zoom)+y_off,
                        int(cur[0]*self._crop_zoom)+x_off,
                        int(cur[1]*self._crop_zoom)+y_off,
                        fill="#ff9900", width=1, dash=(4, 4), tags="crop_ov")

            elif len(self._crop_arc_pts) == 2 and cur:
                pid0, vi0 = self._crop_arc_pts[0]
                pid1, vi1 = self._crop_arc_pts[1]
                poly = _arc_poly(pid0)
                if poly is not None and vi0 < len(poly) and vi1 < len(poly):
                    p1 = tuple(map(float, poly[vi0]))
                    p2 = tuple(map(float, poly[vi1]))
                    try:
                        preview = self._sample_arc(p1, p2, cur, n=35)
                        for k in range(len(preview) - 1):
                            self._crop_canvas.create_line(
                                int(preview[k][0]  *self._crop_zoom)+x_off,
                                int(preview[k][1]  *self._crop_zoom)+y_off,
                                int(preview[k+1][0]*self._crop_zoom)+x_off,
                                int(preview[k+1][1]*self._crop_zoom)+y_off,
                                fill="#ff9900", width=2, dash=(4, 2), tags="crop_ov")
                    except Exception:
                        pass

        self._crop_canvas.configure(scrollregion=(0, 0, cw, ch))

        pts = self._crop_rect
        try:
            PAD = self._crop_spins['padding'].get()
        except (tk.TclError, KeyError):
            PAD = 20
        x_vals, y_vals = pts[:, 0], pts[:, 1]
        ow_est = int(x_vals.max() - x_vals.min() + 2 * PAD)
        oh_est = int(y_vals.max() - y_vals.min() + 2 * PAD)
        self._crop_dim_lbl.configure(
            text=f"Output ≈ {ow_est} × {oh_est} px  |  {N} pts")

    def _hit_crop_handle(self, canvas_x, canvas_y):
        """Return 'v{i}' for the nearest vertex handle within hit radius, or None."""
        if self._crop_rect is None:
            return None
        ox, oy = self._crop_offset
        R = 10
        for i, pt in enumerate(self._crop_rect):
            hx = pt[0] * self._crop_zoom + ox
            hy = pt[1] * self._crop_zoom + oy
            if abs(canvas_x - hx) < R and abs(canvas_y - hy) < R:
                return f'v{i}'
        return None

    def _crop_canvas_to_image(self, ex, ey):
        return ((ex - self._crop_pan[0]) / self._crop_zoom,
                (ey - self._crop_pan[1]) / self._crop_zoom)

    def _crop_mouse_down(self, e):
        ix, iy = self._crop_canvas_to_image(e.x, e.y)

        if self._crop_cut_mode:
            thresh = 14.0 / max(self._crop_zoom, 0.01)
            if not self._crop_cut_active:
                # Editing mode: check hole handles for drag
                for hi, hole in enumerate(self._crop_holes):
                    for pi in range(len(hole)):
                        if float(np.linalg.norm(np.array([ix, iy]) - hole[pi])) < thresh:
                            self._crop_drag = {
                                'type':        'cut_hole',
                                'hole':        hi,
                                'idx':         pi,
                                'start_img':   (ix, iy),
                                'orig_pt':     hole[pi].copy(),
                                'start_holes': [h.copy() for h in self._crop_holes],
                                'moved':       False,
                            }
                            return
                # Empty space → start new polygon
                self._crop_cut_active = [np.array([float(ix), float(iy)], dtype=np.float32)]
            else:
                # Drawing in progress: close if near first point, else add
                if len(self._crop_cut_active) >= 3:
                    fp = self._crop_cut_active[0]
                    if float(np.linalg.norm(np.array([ix, iy]) - fp)) < thresh:
                        self._close_cut_polygon()
                        return
                self._crop_cut_active.append(np.array([float(ix), float(iy)], dtype=np.float32))
            self._refresh_crop_canvas()
            return

        if self._crop_arc_mode:
            if len(self._crop_arc_pts) < 2:
                pid, idx = self._nearest_vertex_idx_all(ix, iy)
                key = (pid, idx)
                if not self._crop_arc_pts or self._crop_arc_pts[0] != key:
                    self._crop_arc_pts.append(key)
                msgs = ["3-pt Arc: click vertex 1 (arc start) …",
                        "3-pt Arc: click vertex 2 (arc end) …",
                        "3-pt Arc: click the through-point to define the curve …"]
                self.set_status(msgs[len(self._crop_arc_pts)])
            else:
                pid0, vi0 = self._crop_arc_pts[0]
                pid1, vi1 = self._crop_arc_pts[1]
                if pid0 != pid1:
                    self.set_status("3-pt Arc: both vertices must be on the same polygon — try again.")
                    self._crop_arc_pts = []
                    self._refresh_crop_canvas()
                    return
                poly = self._crop_rect if pid0 == -1 else self._crop_holes[pid0]
                p1   = tuple(map(float, poly[vi0]))
                p2   = tuple(map(float, poly[vi1]))
                arc_pts_arr = self._sample_arc(p1, p2, (float(ix), float(iy)), n=50)
                self._crop_push_history()
                new_poly = self._arc_replace_poly(poly, vi0, vi1, arc_pts_arr)
                if pid0 == -1:
                    self._crop_rect = new_poly
                else:
                    self._crop_holes[pid0] = new_poly
                self._crop_arc_pts = []
                self.set_status("Arc applied — click vertex 1 for another arc, or exit arc mode.")
                self._rebuild_preview_pil()
            self._refresh_crop_canvas()
            return

        if self._crop_delete_mode:
            p         = np.array([ix, iy], dtype=np.float32)
            threshold = 20.0 / self._crop_zoom

            # Try main polygon first
            if self._crop_rect is not None and len(self._crop_rect) > 3:
                pts = self._crop_rect
                N   = len(pts)
                best_dist   = float('inf')
                best_vertex = -1
                for i in range(N):
                    a      = pts[i].astype(np.float32)
                    b      = pts[(i + 1) % N].astype(np.float32)
                    ab     = b - a
                    len_sq = float(np.dot(ab, ab))
                    if len_sq < 1e-6:
                        continue
                    t        = max(0.0, min(1.0, float(np.dot(p - a, ab)) / len_sq))
                    closest  = a + t * ab
                    seg_dist = float(np.linalg.norm(p - closest))
                    if seg_dist < best_dist:
                        best_dist   = seg_dist
                        best_vertex = i if np.linalg.norm(p - a) < np.linalg.norm(p - b) \
                                      else (i + 1) % N
                if best_dist < threshold and best_vertex >= 0:
                    self._crop_push_history()
                    self._crop_rect = np.delete(pts, best_vertex, axis=0).astype(np.float32)
                    self.set_status(f"Vertex deleted — {len(self._crop_rect)} pts remaining")
                    self._rebuild_preview_pil()
                    self._refresh_crop_canvas()
                    return
            elif not self._crop_holes:
                self.set_status("Cannot delete — polygon needs at least 3 vertices.")
                return

            # Try holes
            for hi, hole in enumerate(self._crop_holes):
                if len(hole) <= 3:
                    continue
                N_h         = len(hole)
                best_dist   = float('inf')
                best_vertex = -1
                for i in range(N_h):
                    a      = hole[i].astype(np.float32)
                    b      = hole[(i + 1) % N_h].astype(np.float32)
                    ab     = b - a
                    len_sq = float(np.dot(ab, ab))
                    if len_sq < 1e-6:
                        continue
                    t        = max(0.0, min(1.0, float(np.dot(p - a, ab)) / len_sq))
                    closest  = a + t * ab
                    seg_dist = float(np.linalg.norm(p - closest))
                    if seg_dist < best_dist:
                        best_dist   = seg_dist
                        best_vertex = i if np.linalg.norm(p - a) < np.linalg.norm(p - b) \
                                      else (i + 1) % N_h
                if best_dist < threshold and best_vertex >= 0:
                    self._crop_push_history()
                    self._crop_holes[hi] = np.delete(hole, best_vertex, axis=0).astype(np.float32)
                    self.set_status(f"Line vertex deleted — {len(self._crop_holes[hi])} pts remaining")
                    self._rebuild_preview_pil()
                    self._refresh_crop_canvas()
                    return
            return

        if self._crop_lasso_mode:
            # Click near first vertex (≥3 pts already) → close polygon
            if len(self._crop_lasso_pts) >= 3:
                fx, fy = self._crop_lasso_pts[0]
                if ((ix - fx)**2 + (iy - fy)**2)**0.5 < 20 / self._crop_zoom:
                    self._crop_finish_lasso()
                    return
            self._crop_lasso_pts.append((float(ix), float(iy)))
            self._refresh_crop_canvas()
            return

        handle = self._hit_crop_handle(e.x, e.y)
        if handle:
            self._crop_push_history()
            self._crop_drag = {'type': 'vertex', 'handle': handle,
                                'start_rect': self._crop_rect.copy(),
                                'start_img': (ix, iy)}
        else:
            # Check hole handles
            thresh = 14.0 / max(self._crop_zoom, 0.01)
            self._crop_drag = None
            for hi, hole in enumerate(self._crop_holes):
                for pi in range(len(hole)):
                    if float(np.linalg.norm(np.array([ix, iy]) - hole[pi])) < thresh:
                        self._crop_drag = {
                            'type':        'cut_hole',
                            'hole':        hi,
                            'idx':         pi,
                            'start_img':   (ix, iy),
                            'orig_pt':     hole[pi].copy(),
                            'start_holes': [h.copy() for h in self._crop_holes],
                            'moved':       False,
                        }
                        break
                if self._crop_drag:
                    break

    def _crop_mouse_drag(self, e):
        if not self._crop_drag:
            return
        ix, iy = self._crop_canvas_to_image(e.x, e.y)
        sx, sy = self._crop_drag['start_img']
        dx, dy = float(ix - sx), float(iy - sy)

        if self._crop_drag['type'] == 'cut_hole':
            hi = self._crop_drag['hole']
            pi = self._crop_drag['idx']
            self._crop_holes[hi][pi] = (
                self._crop_drag['orig_pt'] + np.array([dx, dy], dtype=np.float32))
            thresh_img = 1.0 / max(self._crop_zoom, 0.01)
            if abs(dx) > thresh_img or abs(dy) > thresh_img:
                self._crop_drag['moved'] = True
            if not self._crop_pending:
                self._crop_pending = True
                self.root.after_idle(self._refresh_crop_canvas)
            return

        pts = self._crop_drag['start_rect'].copy()
        if self._crop_drag['type'] == 'vertex':
            idx      = int(self._crop_drag['handle'][1:])
            pts[idx] = pts[idx] + np.array([dx, dy], dtype=np.float32)

        self._crop_rect = pts
        if not self._crop_pending:
            self._crop_pending = True
            self.root.after_idle(self._refresh_crop_canvas)

    def _crop_mouse_up(self, e):
        if self._crop_drag and self._crop_drag.get('type') == 'cut_hole':
            if self._crop_drag.get('moved', False):
                # Push the pre-drag state as the undo snapshot
                self._crop_history.append({
                    'rect':  self._crop_rect.copy() if self._crop_rect is not None else None,
                    'holes': self._crop_drag['start_holes'],
                })
                self._crop_redo_stack.clear()
                if len(self._crop_history) > 50:
                    self._crop_history.pop(0)
            self._crop_drag = None
            if self._crop_preview_bg != "white":
                self._rebuild_preview_pil()
                self._refresh_crop_canvas()
            return
        self._crop_drag = None
        if self._crop_preview_bg != "white":
            self._rebuild_preview_pil()
            self._refresh_crop_canvas()

    def _crop_double_click(self, e):
        if self._crop_cut_mode:
            if self._crop_cut_active:
                # The second ButtonPress-1 already added a duplicate point — remove it
                if len(self._crop_cut_active) > 1:
                    self._crop_cut_active.pop()
                if len(self._crop_cut_active) >= 3:
                    self._close_cut_polygon()
                else:
                    self._refresh_crop_canvas()
            else:
                # Not drawing: insert vertex into nearest hole edge
                if not self._crop_holes:
                    return
                ix, iy = self._crop_canvas_to_image(e.x, e.y)
                p = np.array([ix, iy], dtype=np.float32)
                vtx_thresh = 14.0 / max(self._crop_zoom, 0.01)
                # Don't insert if click is on an existing vertex
                on_vertex = any(
                    float(np.linalg.norm(hole - p, axis=1).min()) < vtx_thresh
                    for hole in self._crop_holes if len(hole)
                )
                if on_vertex:
                    self._refresh_crop_canvas()
                    return
                threshold = 15.0 / self._crop_zoom
                best_hole, best_dist, best_idx, best_pt = -1, float('inf'), -1, None
                for hi, hole in enumerate(self._crop_holes):
                    N = len(hole)
                    for i in range(N):
                        a = hole[i].astype(np.float32)
                        b = hole[(i + 1) % N].astype(np.float32)
                        ab = b - a
                        len_sq = float(np.dot(ab, ab))
                        if len_sq < 1e-6:
                            continue
                        t = max(0.0, min(1.0, float(np.dot(p - a, ab)) / len_sq))
                        closest = a + t * ab
                        dist = float(np.linalg.norm(p - closest))
                        if dist < best_dist:
                            best_dist, best_hole, best_idx, best_pt = dist, hi, i, closest
                if best_hole >= 0 and best_dist < threshold:
                    self._crop_push_history()
                    hole = self._crop_holes[best_hole]
                    self._crop_holes[best_hole] = np.insert(
                        hole, best_idx + 1, best_pt, axis=0).astype(np.float32)
                    self.set_status(f"Line vertex added — {len(self._crop_holes[best_hole])} pts")
                    self._rebuild_preview_pil()
                    self._refresh_crop_canvas()
            return

        if self._crop_lasso_mode:
            # The two single-click events already added duplicate pts — remove one
            if len(self._crop_lasso_pts) > 1:
                self._crop_lasso_pts.pop()
            self._crop_finish_lasso()
            return

        # Debounce: rapid clicks (triple-click) can fire Double-Button-1 twice.
        # Ignore if we already handled a double-click within the last 350 ms.
        if getattr(self, '_crop_dbl_locked', False):
            return
        self._crop_dbl_locked = True
        self.root.after(350, lambda: setattr(self, '_crop_dbl_locked', False))

        if self._crop_rect is None:
            return
        # The second ButtonPress-1 of the double-click fires _crop_mouse_down just
        # before this handler and may have started a drag on an existing vertex.
        # If it did, the user double-clicked ON a vertex (not an edge) — cancel and
        # do not insert a new point.
        if self._crop_drag is not None:
            dtype = self._crop_drag.get('type')
            if dtype == 'vertex':
                self._crop_rect = self._crop_drag['start_rect'].copy()
                if self._crop_history:
                    self._crop_history.pop()
                self._crop_drag = None
                self._refresh_crop_canvas()
                return
            elif dtype == 'cut_hole':
                hi = self._crop_drag['hole']
                pi = self._crop_drag['idx']
                self._crop_holes[hi][pi] = self._crop_drag['orig_pt'].copy()
                self._crop_drag = None
                self._refresh_crop_canvas()
                return
            self._crop_drag = None

        ix, iy = self._crop_canvas_to_image(e.x, e.y)
        p = np.array([ix, iy], dtype=np.float32)

        # Never insert a vertex when the click is already on top of an existing one.
        # This catches the case where the drag was already cleared by mouse-up before
        # Double-Button-1 fires, as well as any rapid re-click on the new vertex.
        vtx_thresh = 14.0 / max(self._crop_zoom, 0.01)
        if self._crop_rect is not None:
            if float(np.linalg.norm(self._crop_rect - p, axis=1).min()) < vtx_thresh:
                self._refresh_crop_canvas()
                return
        for hole in self._crop_holes:
            if float(np.linalg.norm(hole - p, axis=1).min()) < vtx_thresh:
                self._refresh_crop_canvas()
                return

        pts = self._crop_rect
        N   = len(pts)

        best_dist, best_idx, best_pt = float('inf'), -1, None
        for i in range(N):
            a  = pts[i].astype(np.float32)
            b  = pts[(i + 1) % N].astype(np.float32)
            ab = b - a
            len_sq = float(np.dot(ab, ab))
            if len_sq < 1e-6:
                continue
            t       = max(0.0, min(1.0, float(np.dot(p - a, ab)) / len_sq))
            closest = a + t * ab
            dist    = float(np.linalg.norm(p - closest))
            if dist < best_dist:
                best_dist, best_idx, best_pt = dist, i, closest

        # Accept if within ~15 canvas pixels of an edge
        threshold = 15.0 / self._crop_zoom
        if best_idx >= 0 and best_dist < threshold:
            self._crop_push_history()
            new_pts = np.insert(pts, best_idx + 1, best_pt, axis=0)
            self._crop_rect = new_pts.astype(np.float32)
            self.set_status(f"Vertex added — {len(self._crop_rect)} pts total")
            self._refresh_crop_canvas()
            return

        # Check hole edges if main polygon edge wasn't close enough
        if self._crop_holes:
            best_hole, best_hdist, best_hidx, best_hpt = -1, float('inf'), -1, None
            for hi, hole in enumerate(self._crop_holes):
                N_h = len(hole)
                for i in range(N_h):
                    a  = hole[i].astype(np.float32)
                    b  = hole[(i + 1) % N_h].astype(np.float32)
                    ab = b - a
                    len_sq = float(np.dot(ab, ab))
                    if len_sq < 1e-6:
                        continue
                    t       = max(0.0, min(1.0, float(np.dot(p - a, ab)) / len_sq))
                    closest = a + t * ab
                    dist    = float(np.linalg.norm(p - closest))
                    if dist < best_hdist:
                        best_hdist, best_hole, best_hidx, best_hpt = dist, hi, i, closest
            if best_hole >= 0 and best_hdist < threshold:
                self._crop_push_history()
                hole = self._crop_holes[best_hole]
                self._crop_holes[best_hole] = np.insert(
                    hole, best_hidx + 1, best_hpt, axis=0).astype(np.float32)
                self.set_status(f"Line vertex added — {len(self._crop_holes[best_hole])} pts")
                self._rebuild_preview_pil()
                self._refresh_crop_canvas()

    # ── Undo / Redo ───────────────────────────────────────────────────────────

    def _crop_push_history(self):
        if self._crop_rect is None:
            return
        self._crop_history.append({
            'rect':  self._crop_rect.copy(),
            'holes': [h.copy() for h in self._crop_holes],
        })
        self._crop_redo_stack.clear()
        if len(self._crop_history) > 50:
            self._crop_history.pop(0)

    def _crop_undo(self, event=None):
        if self._step != 3 or not self._crop_history:
            return
        self._crop_redo_stack.append({
            'rect':  self._crop_rect.copy() if self._crop_rect is not None else None,
            'holes': [h.copy() for h in self._crop_holes],
        })
        state = self._crop_history.pop()
        self._crop_rect  = state['rect']
        self._crop_holes = state['holes']
        self._rebuild_preview_pil()
        self._refresh_crop_canvas()
        self.set_status(f"Undo  ({len(self._crop_history)} left)")

    def _crop_redo(self, event=None):
        if self._step != 3 or not self._crop_redo_stack:
            return
        self._crop_history.append({
            'rect':  self._crop_rect.copy() if self._crop_rect is not None else None,
            'holes': [h.copy() for h in self._crop_holes],
        })
        state = self._crop_redo_stack.pop()
        self._crop_rect  = state['rect']
        self._crop_holes = state['holes']
        self._rebuild_preview_pil()
        self._refresh_crop_canvas()
        self.set_status(f"Redo  ({len(self._crop_redo_stack)} left)")

    def _crop_spin_changed(self, which):
        if self._crop_image is not None and self._crop_rect is not None:
            self._refresh_crop_canvas()

    def _update_crop_spinboxes(self):
        pass

    # ── Lasso tool ────────────────────────────────────────────────────────────

    def _crop_toggle_arc(self):
        self._crop_arc_mode = not self._crop_arc_mode
        if self._crop_arc_mode:
            # Cancel other special modes
            if self._crop_lasso_mode or self._crop_lasso_closed:
                self._crop_lasso_cancel()
            if self._crop_delete_mode:
                self._crop_delete_mode = False
                self._crop_delete_btn.configure(text="Delete Vertex")
            if self._crop_cut_mode:
                self._crop_cut_mode   = False
                self._crop_cut_active = []
                self._crop_cut_btn.configure(text="Draw Lines")
            self._crop_arc_pts = []
            self._crop_arc_btn.configure(text="Cancel Arc")
            self._crop_canvas.configure(cursor="crosshair")
            self.set_status("3-pt Arc: click vertex 1 (arc start) …")
        else:
            self._crop_arc_pts = []
            self._crop_arc_btn.configure(text="3-pt Arc")
            self._crop_canvas.configure(cursor="crosshair")
            self.set_status("")
        self._refresh_crop_canvas()

    def _nearest_vertex_idx(self, ix, iy):
        p = np.array([ix, iy], dtype=np.float32)
        return int(np.argmin(np.linalg.norm(self._crop_rect - p, axis=1)))

    def _nearest_vertex_idx_all(self, ix, iy):
        """Return (poly_id, idx): poly_id=-1 = main polygon, >=0 = hole index."""
        p         = np.array([ix, iy], dtype=np.float32)
        best_dist = float('inf')
        best_pid  = -1
        best_idx  = 0
        if self._crop_rect is not None:
            dists = np.linalg.norm(self._crop_rect - p, axis=1)
            i = int(np.argmin(dists))
            d = float(dists[i])
            if d < best_dist:
                best_dist, best_pid, best_idx = d, -1, i
        for hi, hole in enumerate(self._crop_holes):
            dists = np.linalg.norm(hole - p, axis=1)
            i = int(np.argmin(dists))
            d = float(dists[i])
            if d < best_dist:
                best_dist, best_pid, best_idx = d, hi, i
        return best_pid, best_idx

    def _arc_replace_poly(self, pts, p1_idx, p2_idx, arc_pts):
        """Replace shorter segment between two vertices with arc_pts. Returns new array."""
        pts = pts.copy()
        n   = len(pts)
        i, j = p1_idx, p2_idx
        if i > j:
            i, j = j, i
            arc_pts = arc_pts[::-1]
        fwd = j - i
        bwd = n - fwd
        if fwd <= bwd:
            before = pts[:i]   if i   > 0 else np.empty((0, 2), np.float32)
            after  = pts[j+1:] if j+1 < n else np.empty((0, 2), np.float32)
            parts  = [x for x in [before, arc_pts, after] if len(x)]
        else:
            kept    = pts[i+1:j] if j > i+1 else np.empty((0, 2), np.float32)
            arc_rev = arc_pts[::-1]
            parts   = [x for x in [kept, arc_rev] if len(x)]
        if not parts:
            return pts
        new_pts = np.vstack(parts).astype(np.float32)
        return new_pts if len(new_pts) >= 3 else pts

    def _sample_arc(self, p1, p2, p3, n=50):
        """Circular arc from p1 to p2 passing through p3, sampled at n points."""
        p1 = np.asarray(p1, dtype=np.float64)
        p2 = np.asarray(p2, dtype=np.float64)
        p3 = np.asarray(p3, dtype=np.float64)
        ax, ay = p1;  bx, by = p2;  cx, cy = p3
        D = 2.0 * (ax*(by - cy) + bx*(cy - ay) + cx*(ay - by))
        if abs(D) < 1e-6:                              # collinear → straight line
            return np.linspace(p1, p2, n).astype(np.float32)
        ux = ((ax**2+ay**2)*(by-cy) + (bx**2+by**2)*(cy-ay) + (cx**2+cy**2)*(ay-by)) / D
        uy = ((ax**2+ay**2)*(cx-bx) + (bx**2+by**2)*(ax-cx) + (cx**2+cy**2)*(bx-ax)) / D
        r  = float(np.hypot(ax - ux, ay - uy))
        a1 = np.arctan2(p1[1]-uy, p1[0]-ux)
        a2 = np.arctan2(p2[1]-uy, p2[0]-ux)
        a3 = np.arctan2(p3[1]-uy, p3[0]-ux)

        def ccw(start, end):          # CCW angular span from start to end, in [0, 2π)
            return (end - start) % (2*np.pi)

        span_to_p2 = ccw(a1, a2)
        span_to_p3 = ccw(a1, a3)
        if span_to_p3 < span_to_p2:  # p3 lies on the CCW arc → go CCW
            angles = np.linspace(a1, a1 + span_to_p2, n)
        else:                          # p3 outside CCW arc → go CW
            angles = np.linspace(a1, a1 - (2*np.pi - span_to_p2), n)

        return np.column_stack([ux + r*np.cos(angles),
                                 uy + r*np.sin(angles)]).astype(np.float32)

    def _replace_polygon_segment_with_arc(self, p1_idx, p2_idx, arc_pts):
        """Replace the shorter polygon path between two vertices with arc_pts."""
        pts = self._crop_rect.copy()
        n   = len(pts)
        i, j = p1_idx, p2_idx

        # Normalise so i ≤ j; if swapped, reverse the arc so it still runs i → j
        if i > j:
            i, j = j, i
            arc_pts = arc_pts[::-1]

        fwd = j - i       # forward path length (i → i+1 → … → j)
        bwd = n - fwd     # backward path (wrapping through 0)

        if fwd <= bwd:
            # Replace the forward segment, keep everything outside [i..j]
            before = pts[:i]   if i   > 0     else np.empty((0, 2), np.float32)
            after  = pts[j+1:] if j+1 < n     else np.empty((0, 2), np.float32)
            parts  = [x for x in [before, arc_pts, after] if len(x)]
        else:
            # Replace the backward (wrap-around) segment, keep pts[i+1 .. j-1]
            kept     = pts[i+1:j] if j > i+1  else np.empty((0, 2), np.float32)
            arc_rev  = arc_pts[::-1]           # goes from pts[j] back to pts[i]
            parts    = [x for x in [kept, arc_rev] if len(x)]

        new_pts = np.vstack(parts).astype(np.float32)
        if len(new_pts) >= 3:
            self._crop_rect = new_pts

    def _crop_toggle_delete(self):
        self._crop_delete_mode = not self._crop_delete_mode
        if self._crop_delete_mode:
            # Exit all other special modes
            if self._crop_lasso_mode or self._crop_lasso_closed:
                self._crop_lasso_cancel()
            if self._crop_arc_mode:
                self._crop_arc_mode = False
                self._crop_arc_pts  = []
                self._crop_arc_btn.configure(text="3-pt Arc")
            if self._crop_cut_mode:
                self._crop_cut_mode   = False
                self._crop_cut_active = []
                self._crop_cut_btn.configure(text="Draw Lines")
            self._crop_delete_btn.configure(text="Cancel Delete")
            self._crop_canvas.configure(cursor="X_cursor")
            self.set_status("Click on a line segment to delete its nearest vertex  ·  Esc to cancel")
        else:
            self._crop_delete_btn.configure(text="Delete Vertex")
            self._crop_canvas.configure(cursor="crosshair")
            self.set_status("")
        self._refresh_crop_canvas()

    def _crop_toggle_lasso(self):
        if self._crop_lasso_closed:
            self._crop_apply_lasso()
            return
        self._crop_lasso_mode = not self._crop_lasso_mode
        if self._crop_lasso_mode:
            # Exit all other special modes
            if self._crop_arc_mode:
                self._crop_arc_mode = False
                self._crop_arc_pts  = []
                self._crop_arc_btn.configure(text="3-pt Arc")
            if self._crop_delete_mode:
                self._crop_delete_mode = False
                self._crop_delete_btn.configure(text="Delete Vertex")
            if self._crop_cut_mode:
                self._crop_cut_mode   = False
                self._crop_cut_active = []
                self._crop_cut_btn.configure(text="Draw Lines")
            self._crop_lasso_pts = []
            self._crop_lasso_btn.configure(text="Cancel Lasso")
            self._crop_canvas.configure(cursor="pencil")
            self.set_status(
                "Click to place vertices  ·  Click near start or double-click to close  ·  Esc to cancel")
        else:
            self._crop_lasso_pts = []
            self._crop_lasso_btn.configure(text="Draw Lasso")
            self._crop_canvas.configure(cursor="crosshair")
        self._refresh_crop_canvas()

    def _crop_esc(self):
        """Cancel whichever special mode is active."""
        if self._crop_cut_mode:
            if self._crop_cut_active:
                self._crop_cut_active = []
                self.set_status("Drawing cancelled — click anywhere to start a new line")
                self._refresh_crop_canvas()
            else:
                self._crop_cut_toggle()
            return
        if self._crop_lasso_mode or self._crop_lasso_closed:
            self._crop_lasso_cancel()
        elif self._crop_delete_mode:
            self._crop_delete_mode = False
            self._crop_delete_btn.configure(text="Delete Vertex")
            self._crop_canvas.configure(cursor="crosshair")
            self.set_status("")
            self._refresh_crop_canvas()
        elif self._crop_arc_mode:
            if self._crop_arc_pts:
                self._crop_arc_pts = []
                self.set_status("3-pt Arc: click vertex 1 (arc start) …")
                self._refresh_crop_canvas()
            else:
                self._crop_arc_mode = False
                self._crop_arc_btn.configure(text="3-pt Arc")
                self._crop_canvas.configure(cursor="crosshair")
                self.set_status("")
                self._refresh_crop_canvas()

    def _crop_lasso_cancel(self):
        if not (self._crop_lasso_mode or self._crop_lasso_closed):
            return
        self._crop_lasso_mode   = False
        self._crop_lasso_closed = False
        self._crop_lasso_pts    = []
        self._crop_lasso_btn.configure(text="Draw Lasso")
        self._crop_canvas.configure(cursor="crosshair")
        self.set_status("Lasso discarded — original selection unchanged.")
        self._refresh_crop_canvas()

    def _crop_finish_lasso(self):
        """Close the in-progress lasso into a pending state; _crop_rect is untouched."""
        if len(self._crop_lasso_pts) < 3:
            return
        self._crop_lasso_mode   = False
        self._crop_lasso_closed = True
        self._crop_lasso_btn.configure(text="Apply Lasso")
        self._crop_canvas.configure(cursor="crosshair")
        self.set_status(
            f"Lasso ready ({len(self._crop_lasso_pts)} pts) — "
            "click 'Apply Lasso' to use it, or Esc to discard")
        self._refresh_crop_canvas()

    def _crop_apply_lasso(self):
        """Replace _crop_rect with the pending lasso polygon."""
        if not self._crop_lasso_closed or len(self._crop_lasso_pts) < 3:
            return
        self._crop_push_history()
        self._crop_rect         = np.array(self._crop_lasso_pts, dtype=np.float32)
        self._crop_lasso_closed = False
        self._crop_lasso_pts    = []
        self._crop_lasso_btn.configure(text="Draw Lasso")
        self.set_status(f"Lasso applied — {len(self._crop_rect)} vertices")
        self._rebuild_preview_pil()
        self._refresh_crop_canvas()

    # ── Cut-zones tool ────────────────────────────────────────────────────────

    def _crop_cut_toggle(self):
        self._crop_cut_mode = not self._crop_cut_mode
        if self._crop_cut_mode:
            if self._crop_lasso_mode or self._crop_lasso_closed:
                self._crop_lasso_cancel()
            if self._crop_delete_mode:
                self._crop_delete_mode = False
                self._crop_delete_btn.configure(text="Delete Vertex")
            if self._crop_arc_mode:
                self._crop_arc_mode = False
                self._crop_arc_btn.configure(text="3-pt Arc")
            self._crop_cut_active = []
            self._crop_cut_btn.configure(text="Exit Lines")
            self._crop_canvas.configure(cursor="crosshair")
            self.set_status(
                "Draw Lines: click to place points  ·  "
                "click first point to close shape  ·  "
                "drag handles to move  ·  "
                "double-click line edge to add point  ·  "
                "right-click to delete  ·  Esc to cancel")
        else:
            # Convert any in-progress polygon to a hole so it stays visible and fully editable
            if len(self._crop_cut_active) >= 2:
                self._crop_push_history()
                self._crop_holes.append(
                    np.array(self._crop_cut_active, dtype=np.float32))
                self._rebuild_preview_pil()
            self._crop_cut_active = []
            self._crop_cut_btn.configure(text="Draw Lines")
            self._crop_canvas.configure(cursor="crosshair")
            self.set_status("")
        self._refresh_crop_canvas()

    def _close_cut_polygon(self):
        """Finalize the in-progress line polygon into a hole."""
        if len(self._crop_cut_active) < 3:
            return
        poly = np.array(self._crop_cut_active, dtype=np.float32)
        self._crop_push_history()
        self._crop_holes.append(poly)
        self._crop_cut_active = []
        self.set_status(
            f"Line zone created — {len(self._crop_holes)} zone(s)  ·  "
            "drag handles or double-click edge to edit  ·  right-click to delete")
        self._rebuild_preview_pil()
        self._refresh_crop_canvas()

    def _crop_mouse_motion(self, e):
        needs_update = (self._crop_lasso_mode or
                        (self._crop_arc_mode and len(self._crop_arc_pts) >= 1) or
                        (self._crop_cut_mode and bool(self._crop_cut_active)))
        if not needs_update:
            return
        ix, iy = self._crop_canvas_to_image(e.x, e.y)
        self._crop_lasso_cursor = (float(ix), float(iy))
        if not self._crop_pending:
            self._crop_pending = True
            self.root.after_idle(self._refresh_crop_canvas)

    def _crop_right_click(self, e):
        """Right-click: cancel in-progress drawing, or delete a finished hole."""
        ix, iy = self._crop_canvas_to_image(e.x, e.y)

        # In draw-lines mode while drawing → cancel the current in-progress polygon
        if self._crop_cut_mode and self._crop_cut_active:
            self._crop_cut_active = []
            self.set_status("Drawing cancelled — click to start a new line")
            self._refresh_crop_canvas()
            return

        if not self._crop_holes:
            return
        p = np.array([ix, iy], dtype=np.float32)
        for i, hole in enumerate(self._crop_holes):
            hit = False
            if len(hole) >= 3:
                hit = cv2.pointPolygonTest(
                    hole.astype(np.float32), (float(ix), float(iy)), False) >= 0
            else:
                # For open/degenerate holes (< 3 pts) test proximity to any handle
                thresh = 15.0 / max(self._crop_zoom, 0.01)
                hit = any(float(np.linalg.norm(p - pt)) < thresh for pt in hole)
            if hit:
                self._crop_push_history()
                self._crop_holes.pop(i)
                self.set_status(f"Line deleted — {len(self._crop_holes)} line(s) remaining")
                self._rebuild_preview_pil()
                self._refresh_crop_canvas()
                return

    # ── Edge refinement helpers ───────────────────────────────────────────────

    def _densify_polygon(self, pts, step=4):
        """Insert interpolated points so no segment is longer than `step` px."""
        dense = []
        n = len(pts)
        for i in range(n):
            a = pts[i].astype(np.float32)
            b = pts[(i + 1) % n].astype(np.float32)
            seg = float(np.linalg.norm(b - a))
            num = max(1, int(seg / step))
            for t in range(num):
                dense.append(a + (b - a) * (t / num))
        return np.array(dense, dtype=np.float32)

    def _thin_polygon(self, pts, target):
        """Uniformly subsample `pts` down to `target` vertices."""
        n = len(pts)
        if n <= target:
            return pts.astype(np.float32)
        idx = [int(round(i * n / target)) % n for i in range(target)]
        return pts[idx].astype(np.float32)

    def _smooth_polygon_chaikin(self, pts, iterations=1):
        """Chaikin corner-cutting — each pass doubles vertices and rounds corners."""
        for _ in range(iterations):
            n = len(pts)
            out = []
            for i in range(n):
                p0 = pts[i].astype(np.float32)
                p1 = pts[(i + 1) % n].astype(np.float32)
                out.append(0.75 * p0 + 0.25 * p1)
                out.append(0.25 * p0 + 0.75 * p1)
            pts = np.array(out, dtype=np.float32)
        return pts

    def _crop_do_smooth(self):
        if self._crop_rect is None and not self._crop_holes:
            return
        n = int(self._crop_smooth_var.get())
        if n < 1:
            return
        self._crop_push_history()
        if self._crop_rect is not None:
            smoothed        = self._smooth_polygon_chaikin(self._crop_rect, iterations=n)
            self._crop_rect = self._thin_polygon(smoothed, target=max(8, len(self._crop_rect)))
        for i, hole in enumerate(self._crop_holes):
            smoothed            = self._smooth_polygon_chaikin(hole, iterations=n)
            self._crop_holes[i] = self._thin_polygon(smoothed, target=max(4, len(hole)))
        self._rebuild_preview_pil()
        self._refresh_crop_canvas()

    def _crop_do_refine(self):
        """Snap polygon boundary to nearest image edges within Radius pixels."""
        if self._crop_image is None:
            return
        if self._crop_rect is None and not self._crop_holes:
            return
        self._crop_push_history()
        radius = int(self._crop_refine_var.get())
        img8   = self._crop_image
        gray   = cv2.cvtColor(img8, cv2.COLOR_RGB2GRAY)

        # Two-threshold Canny: fine detail + coarse structure
        e1 = cv2.Canny(gray, 30,  90)
        e2 = cv2.Canny(gray, 80, 200)
        edges = cv2.bitwise_or(e1, e2)
        edges = cv2.dilate(edges,
                           cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3)))
        h, w = img8.shape[:2]

        def _refine_one(poly):
            dense   = self._densify_polygon(poly, step=4)
            refined = dense.copy()
            n_pts   = len(dense)
            for i in range(n_pts):
                pt      = dense[i]
                tangent = dense[(i + 1) % n_pts] - dense[(i - 1) % n_pts]
                tlen    = float(np.linalg.norm(tangent))
                if tlen < 1e-6:
                    continue
                normal     = np.array([-tangent[1], tangent[0]]) / tlen
                best_pt    = pt.copy()
                best_score = -1.0
                for r in range(-radius, radius + 1):
                    s  = pt + normal * r
                    sx = int(round(float(s[0])))
                    sy = int(round(float(s[1])))
                    if 0 <= sx < w and 0 <= sy < h:
                        score = float(edges[sy, sx])
                        if score > best_score:
                            best_score = score
                            best_pt    = np.array([float(sx), float(sy)])
                refined[i] = best_pt
            return self._thin_polygon(refined, target=len(poly))

        if self._crop_rect is not None:
            self._crop_rect = _refine_one(self._crop_rect)
        for i, hole in enumerate(self._crop_holes):
            self._crop_holes[i] = _refine_one(hole)

        self._rebuild_preview_pil()
        self._refresh_crop_canvas()
        n_main = len(self._crop_rect) if self._crop_rect is not None else 0
        self.set_status(
            f"Refine Edge done — {n_main} main pts"
            + (f", {len(self._crop_holes)} hole(s)" if self._crop_holes else ""))

    # ── Preview background ────────────────────────────────────────────────────

    def _crop_cycle_preview(self):
        modes = ["white", "green", "red"]
        self._crop_preview_bg = modes[(modes.index(self._crop_preview_bg) + 1) % 3]
        labels = {"white": "BG: White", "green": "BG: Green", "red": "BG: Red"}
        self._crop_preview_btn.configure(text=labels[self._crop_preview_bg])
        self._rebuild_preview_pil()
        self._refresh_crop_canvas()

    def _rebuild_preview_pil(self):
        """Build a colored-background composite for green/red preview modes."""
        if self._crop_preview_bg == "white" or self._crop_image is None or self._crop_rect is None:
            self._crop_preview_pil = None
            self._crop_last_view_key = None
            return
        img8 = self._crop_image
        h, w = img8.shape[:2]
        poly = self._crop_rect.astype(np.int32)
        mask = np.zeros((h, w), dtype=np.uint8)
        cv2.fillPoly(mask, [poly], 255)
        for hole in self._crop_holes:
            if len(hole) >= 3:
                cv2.fillPoly(mask, [hole.astype(np.int32)], 0)
        bg = [0, 210, 60] if self._crop_preview_bg == "green" else [210, 30, 30]
        composite = img8.copy()
        composite[mask == 0] = bg
        MAX_PX = 1200
        factor = min(1.0, MAX_PX / max(w, h))
        pil = Image.fromarray(composite)
        self._crop_preview_pil = (pil.resize((int(w * factor), int(h * factor)),
                                              Image.LANCZOS)
                                   if factor < 1.0 else pil)
        self._crop_last_view_key = None  # force PhotoImage rebuild on next render

    def _crop_silent_save(self):
        """Render and save the crop to END_PRODUCT_DIR without any dialog."""
        if self._crop_full is None or self._crop_rect is None:
            return
        try:
            PAD = self._crop_spins['padding'].get()
        except (tk.TclError, KeyError):
            PAD = 20

        hf, wf = self._crop_full.shape[:2]
        poly    = self._crop_rect.astype(np.int32)

        feather = max(0, int(self._crop_feather_var.get()))
        mask = np.zeros((hf, wf), dtype=np.uint8)
        cv2.fillPoly(mask, [poly], 255)
        for hole in self._crop_holes:
            if len(hole) >= 3:
                cv2.fillPoly(mask, [hole.astype(np.int32)], 0)
        if feather > 0:
            ksize = feather * 4 + 1
            if ksize % 2 == 0:
                ksize += 1
            alpha_f = cv2.GaussianBlur(mask.astype(np.float32),
                                        (ksize, ksize), feather * 0.7) / 255.0
        else:
            alpha_f = mask.astype(np.float32) / 255.0
        alpha_u8 = (alpha_f * 255).astype(np.uint8)

        if self._crop_full.dtype == np.uint16:
            rgb8 = (self._crop_full >> 8).astype(np.uint8)
        else:
            rgb8 = self._crop_full.astype(np.uint8)

        x0 = max(0,  int(poly[:, 0].min()) - PAD)
        y0 = max(0,  int(poly[:, 1].min()) - PAD)
        x1 = min(wf, int(poly[:, 0].max()) + PAD)
        y1 = min(hf, int(poly[:, 1].max()) + PAD)

        rgb_crop   = rgb8[y0:y1, x0:x1]
        alpha_crop = alpha_u8[y0:y1, x0:x1]
        rgba       = np.dstack([rgb_crop, alpha_crop])
        out_img    = Image.fromarray(rgba, 'RGBA')
        self._crop_result_rgba = out_img

        END_PRODUCT_DIR.mkdir(parents=True, exist_ok=True)
        ts   = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        path = END_PRODUCT_DIR / f"board_crop_{ts}.png"
        out_img.save(str(path), format='PNG')
        self.set_status(f"Auto-saved crop → {path.name}")

    def _apply_crop(self):
        if self._crop_full is None or self._crop_rect is None:
            messagebox.showwarning("Nothing to crop", "Complete the Preview step first.")
            return
        try:
            PAD = self._crop_spins['padding'].get()
        except (tk.TclError, KeyError):
            PAD = 20

        hf, wf = self._crop_full.shape[:2]
        poly   = self._crop_rect.astype(np.int32)

        # Build alpha mask — feather width from slider
        feather = max(0, int(self._crop_feather_var.get()))
        mask = np.zeros((hf, wf), dtype=np.uint8)
        cv2.fillPoly(mask, [poly], 255)
        for hole in self._crop_holes:
            if len(hole) >= 3:
                cv2.fillPoly(mask, [hole.astype(np.int32)], 0)
        if feather > 0:
            ksize = feather * 4 + 1
            if ksize % 2 == 0:
                ksize += 1
            alpha_f = cv2.GaussianBlur(mask.astype(np.float32),
                                        (ksize, ksize), feather * 0.7) / 255.0
        else:
            alpha_f = mask.astype(np.float32) / 255.0
        alpha_u8 = (alpha_f * 255).astype(np.uint8)

        # RGB as 8-bit for the PNG (downscale 16-bit source if needed)
        if self._crop_full.dtype == np.uint16:
            rgb8 = (self._crop_full >> 8).astype(np.uint8)
        else:
            rgb8 = self._crop_full.astype(np.uint8)

        # Crop to polygon bounding box + padding
        x0 = max(0,  int(poly[:, 0].min()) - PAD)
        y0 = max(0,  int(poly[:, 1].min()) - PAD)
        x1 = min(wf, int(poly[:, 0].max()) + PAD)
        y1 = min(hf, int(poly[:, 1].max()) + PAD)

        rgb_crop   = rgb8[y0:y1, x0:x1]
        alpha_crop = alpha_u8[y0:y1, x0:x1]

        # Combine into RGBA — transparent outside the board polygon
        rgba = np.dstack([rgb_crop, alpha_crop])
        out_img = Image.fromarray(rgba, 'RGBA')
        self._crop_result_rgba = out_img

        END_PRODUCT_DIR.mkdir(parents=True, exist_ok=True)
        ts   = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        path = END_PRODUCT_DIR / f"board_crop_{ts}.png"
        out_img.save(str(path), format='PNG')
        self.set_status(f"Saved → {path.name}")
        messagebox.showinfo("Saved", f"Cropped image saved:\n{path}")

    # ═══════════════════════════════════════════ Sharpness analysis ══════════

    def _compute_gap_mask(self, image_rgb, max_sharp):
        """Return (gap_mask, count) — board regions where no stacked frame was sharp."""
        if image_rgb.dtype == np.uint16:
            img8 = (image_rgb >> 8).astype(np.uint8)
        else:
            img8 = image_rgb.astype(np.uint8)

        gray_u8 = cv2.cvtColor(img8, cv2.COLOR_RGB2GRAY)
        h, w    = gray_u8.shape

        # Board mask — only pixels inside the detected board contour are eligible
        contour = self._board_contour_from_gray(gray_u8)
        board_mask = np.zeros((h, w), dtype=np.uint8)
        if contour is not None:
            cv2.drawContours(board_mask, [contour], -1, 255, cv2.FILLED)
        else:
            # Fallback: flood-fill background from corners and invert
            bg_bin   = (gray_u8 > 245).astype(np.uint8) * 255
            ff_mask  = np.zeros((h + 2, w + 2), dtype=np.uint8)
            bg_flood = bg_bin.copy()
            for seed in [(0, 0), (0, w - 1), (h - 1, 0), (h - 1, w - 1)]:
                if bg_flood[seed] > 0:
                    cv2.floodFill(bg_flood, ff_mask, (seed[1], seed[0]), 128)
            board_mask = (~cv2.dilate(
                (bg_flood == 128).astype(np.uint8),
                cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (12, 12))
            ).astype(bool)).astype(np.uint8) * 255

        # Board detail pixels: edges that fall inside the board contour
        edges    = cv2.Canny(gray_u8, 15, 45)
        has_edge = cv2.dilate(edges,
                              cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (25, 25)))
        board_detail = (board_mask > 0) & (has_edge > 0)

        detail_vals = max_sharp[board_detail]
        if detail_vals.size < 500 or detail_vals.max() < 1.0:
            return np.zeros((h, w), dtype=bool), 0

        # Pixels where the best frame barely reached 20 % of the board's typical
        # sharpness peak — these were never in focus across the whole stack.
        p85       = float(np.percentile(detail_vals, 85))
        threshold = p85 * 0.20

        gap_u8 = (board_detail & (max_sharp < threshold)).astype(np.uint8)

        k_open   = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (30, 30))
        k_dilate = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (35, 35))
        gap_u8 = cv2.morphologyEx(gap_u8, cv2.MORPH_OPEN,  k_open)
        gap_u8 = cv2.dilate(gap_u8, k_dilate)

        n_labels, _ = cv2.connectedComponents(gap_u8)
        count = max(0, n_labels - 1)
        return gap_u8.astype(bool), count

    def _save_stacked(self):
        if self._last_result is None:
            messagebox.showwarning("No image", "Run focus stacking first.")
            return
        path = filedialog.asksaveasfilename(
            title="Save stacked image",
            defaultextension=".tiff",
            filetypes=[("16-bit TIFF", "*.tiff *.tif"),
                       ("PNG",         "*.png")])
        if not path:
            return
        path = Path(path)
        try:
            if path.suffix.lower() in (".tif", ".tiff"):
                tifffile.imwrite(str(path), self._last_result, photometric="rgb")
            else:
                img8 = (self._last_result >> 8).astype(np.uint8) \
                       if self._last_result.dtype == np.uint16 \
                       else self._last_result.astype(np.uint8)
                Image.fromarray(img8).save(str(path))
            self.set_status(f"Saved → {path.name}")
        except Exception as e:
            messagebox.showerror("Save error", str(e))

    def _show_stack_info(self):
        win = tk.Toplevel(self.root)
        win.title("How focus stacking works")
        win.geometry("560x480")
        win.resizable(False, False)
        win.configure(bg=BG)

        tk.Label(win, text="Focus Stacking — Process Documentation",
                 font=("Helvetica", 12, "bold"), bg=BG, fg=ACCENT).pack(pady=(16, 4))

        txt = tk.Text(win, wrap=tk.WORD, bg=BG, relief=tk.FLAT,
                      font=("Helvetica", 9), padx=18, pady=8, state=tk.NORMAL)
        txt.pack(fill=tk.BOTH, expand=True, padx=12)

        INFO = """\
1. FRAME SORTING
   If all loaded ARW files contain a SubjectDistance value in their Exif \
metadata (tag 0x9206), frames are sorted nearest→farthest before stacking. \
This matches the physical shooting order (focus pulled from near to far across \
the board). If any file is missing this tag, frames are sorted by filename \
instead — Sony cameras name files sequentially (DSC00001, DSC00002 …) so \
filename order equals shoot order.

2. ALIGNMENT
   Each frame is decoded from ARW via rawpy/LibRaw at full 16-bit resolution. \
ORB feature detection finds ~8 000 keypoints per frame. A brute-force Hamming \
matcher finds corresponding points between each frame and the reference (first \
frame after sorting). RANSAC homography is computed from the best 300 matches; \
frames are warped to the reference perspective with Lanczos interpolation. This \
corrects any small camera movement between shots.

3. SHARPNESS WEIGHTING
   The Laplacian (second derivative) of each aligned frame is computed — high \
values mean a sharp edge is present. A 51 px Gaussian blur smooths the result \
into a regional sharpness map. Weights are raised to the 4th power so the \
sharpest frame at each pixel strongly dominates, minimising blending artefacts \
at focus transitions.

4. BLENDING
   Frames are combined as a weighted average using the per-pixel sharpness \
weights. In flat/uniform regions where all frames score near zero, equal \
weights are used as a fallback.

5. ARTEFACT REMOVAL
   Female pin-header holes reflect light at specific angles, producing bright \
dots in one frame that the sharpness weighting picks up. A 21 px median \
neighbourhood test detects bright pixels inside dark surroundings; TELEA \
inpainting fills them from surrounding context.

6. POST-PROCESSING
   Unsharp mask (σ = 0.8, amount = 2.5) for crispness. Image scaled to \
2400 × 2400 px with Lanczos interpolation.

7. FOCUS GAP DETECTION
   During stacking the maximum sharpness any single frame achieved at each \
pixel is recorded. After the stack is built, board-detail pixels (edges, \
excluding background) where this maximum is below 20 % of the board's \
85th-percentile peak are flagged as a focus gap — meaning no frame in the \
stack had the lens focused there. Flagged regions are highlighted in orange \
and counted in the warning banner. A gap means a focus distance was skipped \
during shooting; re-photograph with the missing focal plane covered.

8. OUTPUT FORMAT
   The in-memory result is uint16 (16-bit per channel RGB). It can be saved \
as a 16-bit TIFF, passed to the Auto Edit step for colour correction, or sent \
directly to the crop step — all without any quality loss."""

        txt.insert(tk.END, INFO)
        txt.configure(state=tk.DISABLED)

        ttk.Button(win, text="Close", command=win.destroy).pack(pady=10)

    def _toggle_sharpness_overlay(self):
        self._show_sharpness_overlay = not self._show_sharpness_overlay
        self._overlay_btn.configure(
            text="Hide Overlay" if self._show_sharpness_overlay else "Show Overlay")
        self._preview_render()

    def _update_sharpness_warning(self, count):
        if count > 0:
            msg = (f"⚠  {count} focus gap(s) detected — "
                   "orange region(s) were not covered by any frame, please re-photograph with focus in those areas")
            self._warn_frame.configure(bg="#fff3cd")
            self._warn_lbl.configure(bg="#fff3cd", fg="#7a4f00", text=msg)
        else:
            self._warn_frame.configure(bg=BG)
            self._warn_lbl.configure(bg=BG, fg=BG, text="")

    # ═══════════════════════════════════════════ Auto-edit corrections ══════════

    # Target brightness for WB normalization: background → 94% of max scale.
    # This gives a natural off-white rather than clipped pure white, and is
    # the same target whether the user picks manually or uses auto-detect.
    _WB_TARGET = 0.94

    def _apply_white_balance(self, img, x0, y0, x1, y1):
        """Manual WB: normalise picked patch to neutral at _WB_TARGET brightness."""
        scale = 65535.0 if img.dtype == np.uint16 else 255.0
        target = scale * self._WB_TARGET
        h, w = img.shape[:2]
        patch = img[max(0, y0):min(h, y1 + 1),
                    max(0, x0):min(w, x1 + 1)].astype(np.float64)
        white = patch.mean(axis=(0, 1))
        if white.min() < 1.0:
            return img
        factors = target / white          # per-channel scale so patch → neutral white
        result = np.clip(img.astype(np.float64) * factors[None, None, :], 0, scale)
        return result.astype(img.dtype)

    def _auto_white_balance(self, img):
        """Auto WB: sample image corners (where background is visible in product shots),
        then scale each channel so that background → neutral at _WB_TARGET brightness."""
        scale = 65535.0 if img.dtype == np.uint16 else 255.0
        target = scale * self._WB_TARGET
        img_f  = img.astype(np.float64)
        h, w   = img_f.shape[:2]

        # Corners are almost always background in centred product photography
        bsz = max(30, min(h, w) // 8)
        corners = np.concatenate([
            img_f[:bsz,    :bsz   ].reshape(-1, 3),
            img_f[:bsz,    w-bsz: ].reshape(-1, 3),
            img_f[h-bsz:,  :bsz   ].reshape(-1, 3),
            img_f[h-bsz:,  w-bsz: ].reshape(-1, 3),
        ], axis=0)

        # Within corners, keep only the brighter half (avoid shadow/edge pixels)
        lum = 0.299 * corners[:, 0] + 0.587 * corners[:, 1] + 0.114 * corners[:, 2]
        thresh = np.percentile(lum, 50)
        bright = corners[lum >= thresh]

        if len(bright) < 20:
            return img
        bg = bright.mean(axis=0)
        if bg.min() < 1.0:
            return img

        factors = target / bg             # per-channel scale so background → neutral white
        result = np.clip(img_f * factors[None, None, :], 0, scale)
        return result.astype(img.dtype)

    def _apply_auto_levels(self, img):
        scale = 65535.0 if img.dtype == np.uint16 else 255.0
        result = img.astype(np.float64)
        for c in range(3):
            lo = float(np.percentile(result[:, :, c], 1))
            hi = float(np.percentile(result[:, :, c], 99))
            if hi > lo:
                result[:, :, c] = np.clip(
                    (result[:, :, c] - lo) / (hi - lo) * scale, 0, scale)
        return result.astype(img.dtype)

    def _apply_pcb_color(self, img):
        """Shift PCB substrate pixels toward Soldered brand colour #5b2379.
        Works entirely in float32 — no uint8 round-trip, no precision loss."""
        scale = 65535.0 if img.dtype == np.uint16 else 255.0
        img_f = img.astype(np.float32) / scale          # [0, 1]

        # float32 HSV: H [0, 360°], S [0, 1], V [0, 1]
        hsv = cv2.cvtColor(img_f, cv2.COLOR_RGB2HSV)
        h_ch, s_ch, v_ch = hsv[:, :, 0], hsv[:, :, 1], hsv[:, :, 2]

        # #5b2379 = H 279°, S 0.711, V 0.475 (brand swatch).
        # Target V for product photography is slightly higher than the flat swatch
        # because the board has highlights; 0.52 reads as the right purple on screen.
        _PCB_H, _PCB_S, _PCB_V = 279.0, 0.711, 0.52

        pcb = (h_ch >= 240.0) & (h_ch <= 320.0) & (s_ch > 0.20) & (v_ch > 0.06)
        count = int(pcb.sum())
        if count < 1000:
            return img, 0

        avg_h = float(np.mean(h_ch[pcb]))
        avg_s = float(np.mean(s_ch[pcb]))
        avg_v = float(np.mean(v_ch[pcb]))

        dh = _PCB_H - avg_h                         # hue rotation to target
        ds = _PCB_S / max(avg_s, 1e-4)             # saturation scale
        dv = _PCB_V / max(avg_v, 1e-4)             # value scale

        hsv_out = hsv.copy()
        hsv_out[:, :, 0][pcb] = np.clip(hsv_out[:, :, 0][pcb] + dh, 0.0, 360.0)
        hsv_out[:, :, 1][pcb] = np.clip(hsv_out[:, :, 1][pcb] * ds, 0.0,   1.0)
        hsv_out[:, :, 2][pcb] = np.clip(hsv_out[:, :, 2][pcb] * dv, 0.0,   1.0)

        rgb_out = cv2.cvtColor(hsv_out, cv2.COLOR_HSV2RGB)

        result_f = img_f.copy()
        result_f[pcb] = rgb_out[pcb]                # only PCB pixels replaced
        return np.clip(result_f * scale, 0, scale).astype(img.dtype), count

    # ═══════════════════════════════════════════ Image processing ═════════════

    def _auto_stitch(self, images):
        dtype = images[0].dtype
        scale = 65535.0 if dtype == np.uint16 else 255.0
        imgs_f = [(i.astype(np.float32) / scale) for i in images]
        ref_f  = imgs_f[0]
        h, w   = ref_f.shape[:2]

        ref_8    = np.clip(ref_f * 255, 0, 255).astype(np.uint8)
        ref_gray = cv2.cvtColor(ref_8, cv2.COLOR_RGB2GRAY)
        det      = cv2.ORB_create(8000)
        kp_r, des_r = det.detectAndCompute(ref_gray, None)

        aligned = [ref_f]
        valids  = [np.ones((h, w), dtype=np.float32)]

        for img_f in imgs_f[1:]:
            img_8    = np.clip(img_f * 255, 0, 255).astype(np.uint8)
            img_gray = cv2.cvtColor(img_8, cv2.COLOR_RGB2GRAY)
            kp, des  = det.detectAndCompute(img_gray, None)
            warped, valid = img_f, np.ones((h, w), dtype=np.float32)
            if des is not None and des_r is not None and len(kp) >= 4:
                m = sorted(cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
                           .match(des_r, des), key=lambda x: x.distance)[:300]
                if len(m) >= 8:
                    p1 = np.float32([kp_r[x.queryIdx].pt for x in m])
                    p2 = np.float32([kp[x.trainIdx].pt   for x in m])
                    H, _ = cv2.findHomography(p2, p1, cv2.RANSAC, 5.0)
                    if H is not None:
                        warped = cv2.warpPerspective(
                            img_f, H, (w, h), flags=cv2.INTER_LANCZOS4,
                            borderMode=cv2.BORDER_CONSTANT, borderValue=0)
                        valid = cv2.warpPerspective(
                            np.ones((h, w), dtype=np.float32), H, (w, h),
                            flags=cv2.INTER_NEAREST,
                            borderMode=cv2.BORDER_CONSTANT, borderValue=0)
            aligned.append(warped)
            valids.append(valid)

        BLUR = 51
        sharpness = []
        for img_f, v in zip(aligned, valids):
            g   = cv2.cvtColor(np.clip(img_f*255,0,255).astype(np.uint8),
                               cv2.COLOR_RGB2GRAY)
            lap = cv2.Laplacian(g.astype(np.float32), cv2.CV_32F)
            sh  = cv2.GaussianBlur(np.abs(lap), (BLUR, BLUR), 0) * v
            # Near-saturated (blown-out) pixels have no real sharpness info.
            # Penalise them so overexposed frames are never preferred over
            # correctly-exposed darker frames at the same location.
            # Ramp: 0 penalty below 220, full penalty at 255.  Blur spreads
            # the suppression zone so the Laplacian halo around the blown area
            # is also suppressed.
            sat = np.clip((g.astype(np.float32) - 220.0) / 35.0, 0.0, 1.0)
            sat_penalty = cv2.GaussianBlur(sat, (BLUR, BLUR), 0)
            sh = sh * (1.0 - sat_penalty)
            sharpness.append(sh)

        # Best sharpness any frame achieved at each pixel — used for gap detection
        max_sharp = np.max(np.stack(sharpness, axis=0), axis=0)

        # Soft weighted blend: raises weights to power 4 so sharpest pixels
        # dominate without hard cut-offs that create seam/dot artifacts.
        sharp_stack = np.stack(sharpness, axis=0).astype(np.float64)  # (N,H,W)
        sharp_stack = sharp_stack ** 4
        total_sharp = np.sum(sharp_stack, axis=0)
        # Fall back to equal weights where all sharpness is zero (uniform areas)
        flat = total_sharp < 1e-12
        sharp_stack[:, flat] = 1.0
        total_sharp[flat] = len(aligned)
        weights = sharp_stack / total_sharp[None, :, :]          # (N,H,W)

        imgs_stack = np.stack(aligned, axis=0)                   # (N,H,W,3)
        result_f = np.einsum('nhw,nhwc->hwc', weights, imgs_stack).astype(np.float32)

        # ── White artifact removal ────────────────────────────────────────────
        tmp      = (np.clip(result_f, 0, 1) * 255).astype(np.uint8)
        grey_tmp = cv2.cvtColor(tmp, cv2.COLOR_RGB2GRAY)

        # Pass 1 — small dot removal (pin-header contact reflections, 3-5 px)
        # Bright pixel whose 21-px neighbourhood median is still dark → inpaint.
        dark_nbr = cv2.medianBlur(grey_tmp, 21) < 55
        dot_mask = np.zeros(grey_tmp.shape, dtype=np.uint8)
        for c in range(3):
            ch  = tmp[:, :, c]
            bg9 = cv2.medianBlur(ch, 9)
            dot_mask |= (dark_nbr & ((ch.astype(np.int16) - bg9.astype(np.int16)) > 12)).astype(np.uint8)
        if dot_mask.any():
            dot_mask = cv2.dilate(dot_mask, np.ones((3, 3), np.uint8))
            tmp = cv2.inpaint(tmp, dot_mask, inpaintRadius=5, flags=cv2.INPAINT_TELEA)
            grey_tmp = cv2.cvtColor(tmp, cv2.COLOR_RGB2GRAY)

        # Pass 2 — large blown-out blob removal (overexposed port/connector
        # interiors such as Ethernet and USB sockets).  The 21-px median used
        # in pass 1 fails for blobs wider than ~20 px because the kernel stays
        # inside the bright region.  Instead use connected-component analysis:
        # any large bright cluster whose border ring is predominantly dark is
        # a connector interior artifact — fill it with the median border colour.
        _, bright = cv2.threshold(grey_tmp, 235, 255, cv2.THRESH_BINARY)
        n_lbl, lbl_map, stats, _ = cv2.connectedComponentsWithStats(
            bright, connectivity=8)
        h_img, w_img = grey_tmp.shape
        RING_K = np.ones((51, 51), np.uint8)   # ring wide enough to reach port walls
        for lbl in range(1, n_lbl):
            area = stats[lbl, cv2.CC_STAT_AREA]
            # Skip: too small (normal highlight) or too large (bright background)
            if area < 150 or area > h_img * w_img * 0.015:
                continue
            blob = (lbl_map == lbl).astype(np.uint8)
            border_ring = cv2.dilate(blob, RING_K) - blob
            if not border_ring.any():
                continue
            border_grey = grey_tmp[border_ring > 0]
            if border_grey.mean() < 75:   # border is dark → port interior
                fill = np.median(tmp[border_ring > 0].reshape(-1, 3),
                                 axis=0).astype(np.uint8)
                tmp[blob > 0] = fill

        result_f = tmp.astype(np.float32) / 255.0

        result = np.clip(result_f * scale, 0, scale).astype(dtype)
        return self._post_process(result, aux=max_sharp)

    def _post_process(self, image_rgb, aux=None):
        dtype = image_rgb.dtype
        fv    = 65535 if dtype == np.uint16 else 255
        bk    = 1000  if dtype == np.uint16 else 10

        valid = np.any(image_rgb > bk, axis=2)
        rows  = np.where(np.any(valid, axis=1))[0]
        cols  = np.where(np.any(valid, axis=0))[0]
        if rows.size and cols.size:
            image_rgb = image_rgb[rows[0]:rows[-1]+1, cols[0]:cols[-1]+1]
            valid     = valid    [rows[0]:rows[-1]+1, cols[0]:cols[-1]+1]
            if aux is not None:
                aux = aux[rows[0]:rows[-1]+1, cols[0]:cols[-1]+1]

        bk_mask = cv2.dilate((~valid).astype(np.uint8),
                              np.ones((3,3), np.uint8)).astype(bool)
        image_rgb = image_rgb.copy()
        image_rgb[bk_mask] = fv

        h, w  = image_rgb.shape[:2]
        scale = max(2400/w, 2400/h)
        nw, nh = int(w*scale), int(h*scale)
        scaled = cv2.resize(image_rgb, (nw, nh), interpolation=cv2.INTER_LANCZOS4)
        y0, x0 = (nh-2400)//2, (nw-2400)//2
        result = scaled[y0:y0+2400, x0:x0+2400]
        result = self._unsharp_mask(result, sigma=0.8, amount=2.5)

        if aux is not None:
            aux_scaled = cv2.resize(aux.astype(np.float32), (nw, nh),
                                     interpolation=cv2.INTER_LINEAR)
            aux_out = aux_scaled[y0:y0+2400, x0:x0+2400]
            return result, aux_out
        return result

    def _unsharp_mask(self, img, sigma=0.8, amount=2.5):
        dtype = img.dtype
        scale = 65535.0 if dtype == np.uint16 else 255.0
        f = img.astype(np.float32) / scale
        blur = cv2.GaussianBlur(f, (0,0), sigmaX=sigma)
        return np.clip((f + amount*(f - blur)) * scale, 0, scale).astype(dtype)

    # ═══════════════════════════════════════════ Step 4 — Dust Removal ═══════

    def _build_dust_page(self):
        page = tk.Frame(self._content, bg=BG)

        # Row 1 controls
        ctrl = tk.Frame(page, bg=BG, pady=4)
        ctrl.pack(fill=tk.X, padx=8)

        ttk.Checkbutton(ctrl, text="Enable Dust Removal",
                        variable=self._dust_enabled,
                        command=self._dust_toggle_enable).pack(side=tk.LEFT, padx=(0, 16))

        tk.Label(ctrl, text="Method:", bg=BG).pack(side=tk.LEFT)
        ttk.Radiobutton(ctrl, text="LaMa AI (recommended)", variable=self._dust_method,
                        value="lama",     command=self._dust_method_changed).pack(side=tk.LEFT, padx=4)
        ttk.Radiobutton(ctrl, text="Local (OpenCV)",        variable=self._dust_method,
                        value="local",    command=self._dust_method_changed).pack(side=tk.LEFT, padx=4)
        ttk.Radiobutton(ctrl, text="ClipDrop API",          variable=self._dust_method,
                        value="clipdrop", command=self._dust_method_changed).pack(side=tk.LEFT, padx=4)

        self._dust_api_frame = tk.Frame(ctrl, bg=BG)
        tk.Label(self._dust_api_frame, text="API Key:", bg=BG).pack(side=tk.LEFT)
        ttk.Entry(self._dust_api_frame, textvariable=self._dust_api_key,
                  width=28, show="*").pack(side=tk.LEFT, padx=4)
        # hidden by default; shown when ClipDrop selected

        # Row 2 controls
        ctrl2 = tk.Frame(page, bg=BG, pady=2)
        ctrl2.pack(fill=tk.X, padx=8)

        # Draw-mode selector
        tk.Label(ctrl2, text="Draw:", bg=BG).pack(side=tk.LEFT)
        ttk.Radiobutton(ctrl2, text="Excl. Rect",  variable=self._dust_draw_mode,
                        value="excl_rect",  command=self._dust_mode_changed).pack(side=tk.LEFT, padx=2)
        ttk.Radiobutton(ctrl2, text="Excl. Free",  variable=self._dust_draw_mode,
                        value="excl_free",  command=self._dust_mode_changed).pack(side=tk.LEFT, padx=2)
        ttk.Radiobutton(ctrl2, text="Paint Dust",  variable=self._dust_draw_mode,
                        value="paint_dust", command=self._dust_mode_changed).pack(side=tk.LEFT, padx=2)
        ttk.Radiobutton(ctrl2, text="Mark Lines",  variable=self._dust_draw_mode,
                        value="mark_lines", command=self._dust_mode_changed).pack(side=tk.LEFT, padx=2)
        # Brush size controls — shown only when Paint Dust mode is active
        self._dust_brush_frame = tk.Frame(ctrl2, bg=BG)
        tk.Label(self._dust_brush_frame, text="Brush size:", bg=BG).pack(side=tk.LEFT, padx=(0, 4))
        self._dust_brush_lbl = tk.Label(self._dust_brush_frame, text="20 px",
                                         bg=BG, width=5, anchor="w")
        self._dust_brush_lbl.pack(side=tk.LEFT)
        self._dust_brush_scale = tk.Scale(
            self._dust_brush_frame, from_=2, to=300, orient=tk.HORIZONTAL,
            variable=self._dust_paint_radius, length=140, showvalue=False,
            bg=BG, highlightthickness=0, troughcolor="#ccc",
            command=lambda v: self._dust_brush_lbl.configure(text=f"{int(float(v))} px"))
        self._dust_brush_scale.pack(side=tk.LEFT)
        # Not packed initially — appears only in paint_dust mode

        self._dust_local_controls = tk.Frame(ctrl2, bg=BG)
        # only packed when "local" method is selected; hidden for lama (default)
        tk.Label(self._dust_local_controls, text="Sensitivity:", bg=BG).pack(side=tk.LEFT)
        ttk.Scale(self._dust_local_controls, from_=1, to=100,
                  variable=self._dust_sensitivity, orient=tk.HORIZONTAL,
                  length=120).pack(side=tk.LEFT, padx=4)
        tk.Label(self._dust_local_controls, text="Min px:", bg=BG).pack(side=tk.LEFT, padx=(8, 0))
        ttk.Spinbox(self._dust_local_controls, from_=1, to=500,
                    textvariable=self._dust_min_px, width=5).pack(side=tk.LEFT, padx=2)
        tk.Label(self._dust_local_controls, text="Max px:", bg=BG).pack(side=tk.LEFT, padx=(4, 0))
        ttk.Spinbox(self._dust_local_controls, from_=1, to=5000,
                    textvariable=self._dust_max_px, width=5).pack(side=tk.LEFT, padx=2)

        self._dust_detect_btn = ttk.Button(ctrl2, text="Detect Dust",
                                           command=self._dust_detect)
        self._dust_detect_btn.pack(side=tk.LEFT, padx=(12, 4))

        self._dust_run_btn = ttk.Button(ctrl2, text="Remove Detected Dust",
                                        command=self._dust_run)
        self._dust_run_btn.pack(side=tk.LEFT, padx=4)

        ttk.Button(ctrl2, text="Remove Marked Lines",
                   command=self._dust_remove_lines).pack(side=tk.LEFT, padx=4)

        ttk.Checkbutton(ctrl2, text="Show mask",
                        variable=self._dust_show_mask,
                        command=self._dust_refresh_canvas).pack(side=tk.LEFT, padx=4)

        ttk.Button(ctrl2, text="Fit",  command=self._dust_fit_view, width=5).pack(side=tk.LEFT, padx=4)
        ttk.Button(ctrl2, text="100%", command=self._dust_100,       width=5).pack(side=tk.LEFT)
        ttk.Button(ctrl2, text="Clear Exclusions", command=self._dust_clear_exclusions).pack(side=tk.LEFT, padx=(10, 4))
        ttk.Button(ctrl2, text="Revert Changes",   command=self._dust_revert).pack(side=tk.LEFT)
        ttk.Button(ctrl2, text="Save result",  command=self._dust_save).pack(side=tk.RIGHT, padx=8)
        ttk.Button(ctrl2, text="Load Image…",  command=self._dust_load_image).pack(side=tk.RIGHT, padx=4)

        self._dust_status_var = tk.StringVar(value="")
        tk.Label(page, textvariable=self._dust_status_var,
                 bg=BG, fg="#333", anchor="w").pack(fill=tk.X, padx=10)

        # Download progress bar — hidden until LaMa model needs to be downloaded
        self._dust_dl_frame   = tk.Frame(page, bg=BG)
        self._dust_dl_pct_var = tk.StringVar(value="0%")
        tk.Label(self._dust_dl_frame, text="Downloading LaMa model:",
                 bg=BG, font=("Helvetica", 9, "bold")).pack(side=tk.LEFT, padx=(10, 6))
        self._dust_dl_bar = ttk.Progressbar(self._dust_dl_frame, length=320,
                                             mode="determinate", maximum=100)
        self._dust_dl_bar.pack(side=tk.LEFT)
        tk.Label(self._dust_dl_frame, textvariable=self._dust_dl_pct_var,
                 bg=BG, width=5).pack(side=tk.LEFT, padx=6)
        # not packed here — shown only when needed

        canvas_frame = tk.Frame(page, bg="black")
        canvas_frame.pack(fill=tk.BOTH, expand=True)
        self._dust_canvas = tk.Canvas(canvas_frame, bg="black", highlightthickness=0)
        self._dust_canvas.pack(fill=tk.BOTH, expand=True)
        self._dust_canvas.bind("<MouseWheel>",      self._dust_wheel)
        self._dust_canvas.bind("<ButtonPress-1>",  self._dust_excl_press)
        self._dust_canvas.bind("<B1-Motion>",      self._dust_excl_motion)
        self._dust_canvas.bind("<ButtonRelease-1>",self._dust_excl_release)
        self._dust_canvas.bind("<ButtonPress-2>",  self._dust_mid_press)
        self._dust_canvas.bind("<B2-Motion>",      self._dust_mid_drag)

        return page

    def _load_dust_step(self):
        # If we have a crop result and haven't loaded it yet (or source changed), pull it in
        if self._crop_result_rgba is not None and \
                self._dust_source_rgba is not self._crop_result_rgba:
            self._dust_source_rgba = self._crop_result_rgba.copy()
            self._dust_result_rgba = None
            self._dust_mask_pil    = None
        if self._dust_source_rgba is None:
            self._dust_status_var.set(
                "No image loaded — use 'Load Image…' to open a cropped PNG, "
                "or complete the Crop Board step first.")
            return
        self._dust_status_var.set("Click 'Run Dust Removal' to process the image automatically.")
        self.root.after(100, self._dust_fit_view)

    def _dust_load_image(self):
        path = filedialog.askopenfilename(
            title="Load image for dust removal",
            filetypes=[("PNG / TIFF / JPEG", "*.png *.tif *.tiff *.jpg *.jpeg"),
                       ("All files", "*.*")])
        if not path:
            return
        try:
            img = Image.open(path).convert("RGBA")
        except Exception as exc:
            messagebox.showerror("Load error", str(exc))
            return
        self._dust_source_rgba   = img
        self._dust_result_rgba   = None
        self._dust_mask_pil      = None
        self._dust_exclude_rects  = []
        self._dust_freedraw_polys = []
        self._dust_mark_polys     = []
        self._dust_freedraw_pts   = []
        self._dust_undo_stack     = []
        self._dust_redo_stack     = []
        self._dust_status_var.set(
            f"Loaded: {Path(path).name}  ({img.width}×{img.height})  — "
            "click 'Run Dust Removal' to process.")
        self.root.after(50, self._dust_fit_view)

    def _dust_toggle_enable(self):
        if self._dust_run_btn:
            self._dust_run_btn.state(
                ["!disabled"] if self._dust_enabled.get() else ["disabled"])

    def _dust_method_changed(self):
        method = self._dust_method.get()
        if self._dust_local_controls:
            self._dust_local_controls.pack_forget()
        if self._dust_api_frame:
            self._dust_api_frame.pack_forget()
        if method == "local":
            if self._dust_local_controls:
                self._dust_local_controls.pack(side=tk.LEFT)
        elif method == "clipdrop":
            if self._dust_api_frame:
                self._dust_api_frame.pack(side=tk.LEFT, padx=8)

    def _dust_detect(self):
        """Run only the detection pass and show a red overlay preview."""
        if self._dust_source_rgba is None:
            self._dust_status_var.set("No image loaded.")
            return
        if self._dust_method.get() == "clipdrop":
            self._dust_status_var.set(
                "Detection preview is not available for ClipDrop — "
                "click 'Remove Detected Dust' to process directly.")
            return
        self._dust_status_var.set("Detecting dust…")
        if self._dust_detect_btn:
            self._dust_detect_btn.state(["disabled"])
        threading.Thread(target=self._dust_detect_thread, daemon=True).start()

    def _dust_detect_thread(self):
        try:
            _, mask_pil = self._dust_run_local(self._dust_source_rgba)
            self.root.after(0, self._dust_detect_done, mask_pil)
        except Exception as e:
            self.root.after(0, self._dust_detect_done, None, str(e))

    def _dust_detect_done(self, mask_pil, error=None):
        if self._dust_detect_btn:
            self._dust_detect_btn.state(["!disabled"])
        if error:
            self._dust_status_var.set(f"Detection error: {error}")
            return
        self._dust_mask_pil = mask_pil
        arr = np.array(mask_pil)
        n_dust = int(np.count_nonzero(arr))
        self._dust_status_var.set(
            f"Detected {n_dust} dust pixels across "
            f"{int((arr > 0).sum() > 0)} region(s) — "
            "adjust parameters and re-detect, or click 'Remove Detected Dust'.")
        # Count blobs for a more useful message
        n_labels, _ = cv2.connectedComponents((arr > 0).astype(np.uint8))
        self._dust_status_var.set(
            f"Detected {max(0, n_labels - 1)} dust spot(s) ({n_dust} px total) — "
            "review the overlay, then click 'Remove Detected Dust'.")
        self._dust_show_mask.set(False)  # show overlay, not raw mask
        self._dust_refresh_canvas()

    def _dust_run(self):
        if not self._dust_enabled.get():
            self._dust_status_var.set("Dust removal is disabled.")
            return
        if self._dust_source_rgba is None:
            self._dust_status_var.set("No image loaded. Complete the Crop Board step first.")
            return
        self._dust_status_var.set("Running…")
        self._dust_run_btn.state(["disabled"])
        method = self._dust_method.get()
        if method == "clipdrop":
            threading.Thread(target=self._dust_api_thread, daemon=True).start()
        elif method == "lama":
            threading.Thread(target=self._dust_run_lama_thread, daemon=True).start()
        else:
            threading.Thread(target=self._dust_run_local_thread, daemon=True).start()

    def _dust_run_local_thread(self):
        try:
            result_pil, mask_pil = self._dust_run_local(self._dust_source_rgba)
            self.root.after(0, self._dust_done, result_pil, mask_pil, None)
        except Exception as e:
            self.root.after(0, self._dust_done, None, None, str(e))

    def _dust_dl_bar_show(self):
        if self._dust_dl_frame:
            self._dust_dl_frame.pack(fill=tk.X, pady=(0, 2))

    def _dust_dl_bar_hide(self):
        if self._dust_dl_frame:
            self._dust_dl_frame.pack_forget()

    def _dust_dl_bar_set(self, pct):
        if self._dust_dl_bar:
            self._dust_dl_bar["value"] = pct
        if self._dust_dl_pct_var:
            self._dust_dl_pct_var.set(f"{int(pct)}%")

    def _dust_run_lama_thread(self):
        try:
            try:
                from iopaint.model_manager import ModelManager
                from iopaint.schema import InpaintRequest
            except ImportError:
                self.root.after(0, self._dust_done, None, None,
                    "IOPaint not installed. Run install_iopaint.bat first.")
                return

            # Use existing mask from Detect Dust, or run detection now
            if self._dust_mask_pil is not None:
                mask_pil = self._dust_mask_pil
            else:
                self.root.after(0, lambda: self._dust_status_var.set("Detecting dust…"))
                _, mask_pil = self._dust_run_local(self._dust_source_rgba)

            mask_arr = np.array(mask_pil)
            if mask_arr.max() == 0:
                self.root.after(0, self._dust_done,
                                self._dust_source_rgba.copy(), mask_pil, None)
                return

            rgba  = np.array(self._dust_source_rgba)
            rgb   = rgba[:, :, :3].copy()
            alpha = rgba[:, :, 3]

            k = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 7))
            inpaint_mask = cv2.dilate(mask_arr, k)
            inpaint_mask = self._dust_apply_exclusions(inpaint_mask)

            # ── Load model (with download progress bar on first run) ────────
            if self._lama_model is None:
                self.root.after(0, lambda: self._dust_status_var.set(
                    "Loading LaMa model — first run downloads ~200 MB…"))

                # Patch tqdm so any large file download updates the Tk bar
                _dl_started = [False]
                _root = self.root

                try:
                    import tqdm as _tqdm_mod
                    _orig_cls = _tqdm_mod.tqdm

                    show  = self._dust_dl_bar_show
                    upd   = self._dust_dl_bar_set
                    hide  = self._dust_dl_bar_hide

                    class _DlTqdm(_orig_cls):
                        def __init__(self_, *a, **kw):
                            super().__init__(*a, **kw)
                            # Only track large downloads (model weights, not tiny metadata)
                            if self_.total and self_.total > 5_000_000:
                                _dl_started[0] = True
                                _root.after(0, show)
                                _root.after(0, lambda: upd(0))

                        def update(self_, n=1):
                            super().update(n)
                            if _dl_started[0] and self_.total:
                                pct = min(100.0, self_.n / self_.total * 100.0)
                                _root.after(0, lambda p=pct: upd(p))

                        def close(self_):
                            super().close()
                            if _dl_started[0]:
                                _root.after(0, lambda: upd(100))

                    _tqdm_mod.tqdm = _DlTqdm
                    # Also patch huggingface_hub's own tqdm reference
                    _orig_hf = None
                    try:
                        import huggingface_hub.file_download as _hf
                        _orig_hf = _hf.tqdm
                        _hf.tqdm = _DlTqdm
                    except Exception:
                        pass

                    self._lama_model = ModelManager(name="lama", device="cpu")

                finally:
                    _tqdm_mod.tqdm = _orig_cls
                    try:
                        if _orig_hf is not None:
                            import huggingface_hub.file_download as _hf
                            _hf.tqdm = _orig_hf
                    except Exception:
                        pass
                    if _dl_started[0]:
                        _root.after(600, hide)
            # ────────────────────────────────────────────────────────────────

            # Downscale to max 1024 px before LaMa — full-res on CPU is
            # prohibitively slow; dust spots are small so quality is unaffected.
            MAX_PX = 1024
            h_src, w_src = rgb.shape[:2]
            scale = min(1.0, MAX_PX / max(h_src, w_src))
            if scale < 1.0:
                lama_rgb  = cv2.resize(rgb,          (int(w_src * scale), int(h_src * scale)),
                                       interpolation=cv2.INTER_LANCZOS4)
                lama_mask = cv2.resize(inpaint_mask, (int(w_src * scale), int(h_src * scale)),
                                       interpolation=cv2.INTER_NEAREST)
            else:
                lama_rgb, lama_mask = rgb, inpaint_mask

            # Start elapsed-time counter so the user can see it's running
            import time as _time
            _t0 = _time.time()
            _running = [True]

            def _tick():
                if _running[0]:
                    elapsed = int(_time.time() - _t0)
                    self._dust_status_var.set(
                        f"Running LaMa inpainting… {elapsed}s elapsed")
                    self.root.after(1000, _tick)

            self.root.after(0, _tick)

            result_lama = self._lama_model(lama_rgb, lama_mask, InpaintRequest())
            _running[0] = False

            # Upscale result and blend with feathered mask to avoid hard colour edges
            if scale < 1.0:
                result_up = cv2.resize(result_lama.astype(np.uint8),
                                       (w_src, h_src), interpolation=cv2.INTER_LANCZOS4)
            else:
                result_up = result_lama.astype(np.uint8)

            # Colour-match: shift inpainted pixels to match the surrounding context
            # (uses undilated mask_arr so the ring samples the actual neighbour pixels)
            result_up = self._dust_color_match(result_up, rgb, mask_arr)

            # Gaussian feather of the mask: core pixels fully replaced, boundary fades
            blend_f = cv2.GaussianBlur(inpaint_mask.astype(np.float32),
                                       (0, 0), sigmaX=5).clip(0, 255) / 255.0
            blend_f3 = np.stack([blend_f] * 3, axis=2)
            result_rgb_out = (result_up.astype(np.float32) * blend_f3
                              + rgb.astype(np.float32) * (1.0 - blend_f3)).astype(np.uint8)

            rgba_out   = np.dstack([result_rgb_out, alpha])
            result_pil = Image.fromarray(rgba_out, 'RGBA')
            self.root.after(0, self._dust_done, result_pil, mask_pil, None)
        except Exception as e:
            self.root.after(0, self._dust_dl_bar_hide)
            self.root.after(0, self._dust_done, None, None, str(e))

    def _dust_run_local(self, source_pil):
        """Morphological background estimation → diff → blob filter → TELEA inpaint."""
        rgba  = np.array(source_pil)
        rgb   = rgba[:, :, :3]
        alpha = rgba[:, :, 3]
        board_mask = alpha > 0

        gray = cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY)

        sensitivity = self._dust_sensitivity.get()
        min_px = max(1, self._dust_min_px.get())
        max_px = max(min_px + 1, self._dust_max_px.get())

        close_r = max(15, min(80, int(min_px * 3 + sensitivity * 0.3)))
        k_close = cv2.getStructuringElement(
            cv2.MORPH_ELLIPSE, (close_r * 2 + 1, close_r * 2 + 1))
        bg = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, k_close)

        diff = cv2.subtract(bg, gray).astype(np.float32)
        dmax = diff.max()
        if dmax > 0:
            diff_norm = (diff / dmax * 255).astype(np.uint8)
        else:
            diff_norm = diff.astype(np.uint8)

        thresh_val = max(5, int(200 - sensitivity * 1.9))
        _, dust_bin = cv2.threshold(diff_norm, thresh_val, 255, cv2.THRESH_BINARY)
        dust_bin[~board_mask] = 0

        n_labels, labels, stats, _ = cv2.connectedComponentsWithStats(
            dust_bin, connectivity=8)
        dust_filtered = np.zeros_like(dust_bin)
        for lbl in range(1, n_labels):
            area = stats[lbl, cv2.CC_STAT_AREA]
            if min_px <= area <= max_px:
                dust_filtered[labels == lbl] = 255

        mask_pil = Image.fromarray(dust_filtered, 'L')
        if dust_filtered.max() == 0:
            return source_pil.copy(), mask_pil

        k_dilate = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
        inpaint_mask = cv2.dilate(dust_filtered, k_dilate)
        inpaint_mask = self._dust_apply_exclusions(inpaint_mask)

        rgb_inpainted = cv2.inpaint(rgb, inpaint_mask, inpaintRadius=5,
                                    flags=cv2.INPAINT_TELEA)
        rgb_inpainted = self._dust_color_match(rgb_inpainted, rgb, dust_filtered)
        blend_f  = cv2.GaussianBlur(inpaint_mask.astype(np.float32),
                                    (0, 0), sigmaX=3).clip(0, 255) / 255.0
        blend_f3 = np.stack([blend_f] * 3, axis=2)
        rgb_out  = (rgb_inpainted.astype(np.float32) * blend_f3
                    + rgb.astype(np.float32) * (1.0 - blend_f3)).astype(np.uint8)
        rgba_out   = np.dstack([rgb_out, alpha])
        result_pil = Image.fromarray(rgba_out, 'RGBA')
        return result_pil, mask_pil

    def _dust_api_thread(self):
        try:
            import urllib.request
            api_key = self._dust_api_key.get().strip()
            if not api_key:
                self.root.after(0, self._dust_done, None, None,
                                "ClipDrop API key is empty. Enter your key.")
                return

            buf = io.BytesIO()
            self._dust_source_rgba.save(buf, format='PNG')
            png_bytes = buf.getvalue()

            boundary = b"----DustRemovalBoundary"
            body  = b"--" + boundary + b"\r\n"
            body += b'Content-Disposition: form-data; name="image_file"; filename="image.png"\r\n'
            body += b"Content-Type: image/png\r\n\r\n"
            body += png_bytes + b"\r\n"
            body += b"--" + boundary + b"--\r\n"

            req = urllib.request.Request(
                "https://clipdrop-api.co/cleanup/v1",
                data=body,
                headers={
                    "x-api-key": api_key,
                    "Content-Type": "multipart/form-data; boundary=----DustRemovalBoundary"
                },
                method="POST"
            )
            with urllib.request.urlopen(req, timeout=60) as resp:
                result_bytes = resp.read()

            result_pil = Image.open(io.BytesIO(result_bytes)).convert("RGBA")
            orig_alpha = self._dust_source_rgba.split()[3]
            result_pil.putalpha(orig_alpha)
            self.root.after(0, self._dust_done, result_pil, None, None)
        except Exception as e:
            self.root.after(0, self._dust_done, None, None, str(e))

    def _dust_done(self, result_pil, mask_pil, error):
        if self._dust_run_btn:
            self._dust_run_btn.state(["!disabled"])
        if error:
            self._dust_status_var.set(f"Error: {error}")
            return
        self._dust_push_undo()
        self._dust_result_rgba = result_pil
        self._dust_mask_pil    = mask_pil
        n_dust = 0
        if mask_pil is not None:
            arr = np.array(mask_pil)
            n_dust = int(np.count_nonzero(arr))
        self._dust_status_var.set(
            f"Done. Dust pixels detected: {n_dust}. "
            + ("Use Save to export." if n_dust else "No dust found — image unchanged."))
        self._dust_refresh_canvas()

    def _dust_make_overlay(self):
        """Composite source image with a red highlight over detected dust areas."""
        src = self._dust_source_rgba
        mask = self._dust_mask_pil
        if src is None or mask is None:
            return src
        base = src.convert("RGBA")
        red  = Image.new("RGBA", base.size, (220, 40, 40, 180))
        # Dilate mask slightly so it's easier to see
        mask_arr = np.array(mask)
        k = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
        mask_arr = cv2.dilate(mask_arr, k)
        mask_rgba = Image.fromarray(mask_arr, "L")
        overlay = Image.composite(red, Image.new("RGBA", base.size, (0, 0, 0, 0)), mask_rgba)
        result  = Image.alpha_composite(base, overlay)
        return result

    def _dust_refresh_canvas(self):
        if self._dust_canvas is None:
            return
        if self._dust_show_mask.get() and self._dust_mask_pil is not None:
            pil_img = self._dust_mask_pil.convert("RGB")
        elif self._dust_result_rgba is not None:
            pil_img = self._dust_result_rgba
        elif self._dust_mask_pil is not None and self._dust_source_rgba is not None:
            # Detection done but removal not yet run — show red overlay
            pil_img = self._dust_make_overlay()
        elif self._dust_source_rgba is not None:
            pil_img = self._dust_source_rgba
        else:
            return

        cw = self._dust_canvas.winfo_width()
        ch = self._dust_canvas.winfo_height()
        if cw < 2 or ch < 2:
            self._dust_canvas.after(50, self._dust_refresh_canvas)
            return

        iw, ih = pil_img.size
        zoom   = self._dust_zoom
        disp_w = int(iw * zoom)
        disp_h = int(ih * zoom)
        ox = self._dust_pan[0] + (cw - disp_w) // 2
        oy = self._dust_pan[1] + (ch - disp_h) // 2

        sx = max(0, int(-ox / zoom))
        sy = max(0, int(-oy / zoom))
        ex = min(iw, int((cw - ox) / zoom) + 1)
        ey = min(ih, int((ch - oy) / zoom) + 1)
        if ex <= sx or ey <= sy:
            return

        crop = pil_img.crop((sx, sy, ex, ey))
        tw = max(1, int((ex - sx) * zoom))
        th = max(1, int((ey - sy) * zoom))
        crop = crop.resize((tw, th),
            Image.BILINEAR if zoom > 1.0 else Image.LANCZOS)

        self._dust_display_tk = ImageTk.PhotoImage(crop)
        self._dust_canvas.delete("all")
        dx = ox + int(sx * zoom)
        dy = oy + int(sy * zoom)
        self._dust_canvas.create_image(dx, dy, anchor="nw",
                                        image=self._dust_display_tk)

        # Line width scales with zoom so overlays stay visible at any zoom level
        lw = max(1, min(8, round(zoom * 0.8 + 0.5)))

        # Draw committed exclusion zones (dashed green rectangles)
        for (rx0, ry0, rx1, ry1) in self._dust_exclude_rects:
            cx0 = ox + rx0 * zoom; cy0 = oy + ry0 * zoom
            cx1 = ox + rx1 * zoom; cy1 = oy + ry1 * zoom
            self._dust_canvas.create_rectangle(cx0, cy0, cx1, cy1,
                outline="#00dd00", width=lw, dash=(6, 3))
        # Draw committed free-draw exclusion polygons (green)
        for poly in self._dust_freedraw_polys:
            coords = []
            for (px, py) in poly:
                coords.extend([ox + px * zoom, oy + py * zoom])
            if len(coords) >= 4:
                self._dust_canvas.create_polygon(coords, outline="#00dd00",
                    fill="", width=lw, dash=(6, 3))
        # Draw committed mark-line strokes (orange open polylines — will be removed)
        stroke_lw = max(2, round(zoom))  # 2 px minimum so strokes remain visible
        for stroke in self._dust_mark_polys:
            coords = []
            for (px, py) in stroke:
                coords.extend([ox + px * zoom, oy + py * zoom])
            if len(coords) >= 4:
                self._dust_canvas.create_line(coords, fill="#ff6600",
                    width=stroke_lw, capstyle=tk.ROUND, joinstyle=tk.ROUND)
        # Draw in-progress rect rubber-band
        if self._dust_excl_drag is not None:
            _cx0, _cy0, _cx1, _cy1 = self._dust_excl_drag[2:]
            self._dust_canvas.create_rectangle(_cx0, _cy0, _cx1, _cy1,
                outline="#00ff00", width=lw, dash=(4, 4))
        # Draw in-progress free-draw stroke (green = exclusion, orange = mark lines)
        if self._dust_freedraw_pts:
            mode = self._dust_draw_mode.get()
            coords = []
            for (px, py) in self._dust_freedraw_pts:
                coords.extend([ox + px * zoom, oy + py * zoom])
            if len(coords) >= 4:
                if mode == "mark_lines":
                    self._dust_canvas.create_line(coords, fill="#ff8800",
                        width=stroke_lw, capstyle=tk.ROUND, joinstyle=tk.ROUND)
                else:
                    self._dust_canvas.create_line(coords, fill="#00ff44",
                        width=lw, dash=(4, 3))

    def _dust_canvas_to_image(self, cx, cy):
        if self._dust_source_rgba is None:
            return 0.0, 0.0
        iw, ih = self._dust_source_rgba.size
        zoom   = self._dust_zoom
        cw = self._dust_canvas.winfo_width()
        ch = self._dust_canvas.winfo_height()
        ox = self._dust_pan[0] + (cw - int(iw * zoom)) // 2
        oy = self._dust_pan[1] + (ch - int(ih * zoom)) // 2
        return (cx - ox) / zoom, (cy - oy) / zoom

    def _dust_mode_changed(self):
        mode = self._dust_draw_mode.get()
        if mode == "paint_dust":
            self._dust_brush_frame.pack(side=tk.LEFT, padx=(8, 0))
        else:
            self._dust_brush_frame.pack_forget()
        self._dust_canvas.configure(cursor="crosshair")

    def _dust_image_to_canvas(self, ix, iy):
        if self._dust_source_rgba is None:
            return 0.0, 0.0
        iw, ih = self._dust_source_rgba.size
        zoom   = self._dust_zoom
        cw = self._dust_canvas.winfo_width()
        ch = self._dust_canvas.winfo_height()
        ox = self._dust_pan[0] + (cw - int(iw * zoom)) // 2
        oy = self._dust_pan[1] + (ch - int(ih * zoom)) // 2
        return ox + ix * zoom, oy + iy * zoom

    # ── unified mouse handlers routed by draw mode ─────────────────────────

    def _dust_excl_press(self, e):
        mode = self._dust_draw_mode.get()
        ix, iy = self._dust_canvas_to_image(e.x, e.y)
        if mode == "excl_rect":
            self._dust_excl_drag = (ix, iy, e.x, e.y, e.x, e.y)
        elif mode in ("excl_free", "mark_lines"):
            self._dust_freedraw_pts = [(ix, iy)]
            self._dust_excl_drag = None
        elif mode == "paint_dust":
            self._dust_paint_active = True
            self._dust_paint_at(ix, iy)

    def _dust_excl_motion(self, e):
        mode = self._dust_draw_mode.get()
        ix, iy = self._dust_canvas_to_image(e.x, e.y)
        if mode == "excl_rect":
            if self._dust_excl_drag is None:
                return
            ix0, iy0, cx0, cy0, _, _ = self._dust_excl_drag
            self._dust_excl_drag = (ix0, iy0, cx0, cy0, e.x, e.y)
            self._dust_refresh_canvas()
        elif mode in ("excl_free", "mark_lines"):
            self._dust_freedraw_pts.append((ix, iy))
            self._dust_refresh_canvas()
        elif mode == "paint_dust":
            if self._dust_paint_active:
                self._dust_paint_at(ix, iy)

    def _dust_excl_release(self, e):
        mode = self._dust_draw_mode.get()
        ix, iy = self._dust_canvas_to_image(e.x, e.y)
        if mode == "excl_rect":
            if self._dust_excl_drag is None:
                return
            ix0, iy0, cx0, cy0, _, _ = self._dust_excl_drag
            self._dust_excl_drag = None
            if abs(e.x - cx0) < 5 and abs(e.y - cy0) < 5:
                self._dust_refresh_canvas()
                return
            x0 = int(min(ix0, ix)); x1 = int(max(ix0, ix))
            y0 = int(min(iy0, iy)); y1 = int(max(iy0, iy))
            self._dust_exclude_rects.append((x0, y0, x1, y1))
            n_zones = len(self._dust_exclude_rects) + len(self._dust_freedraw_polys)
            self._dust_status_var.set(
                f"{n_zones} exclusion zone(s) — dust inside green areas will not be removed.")
            self._dust_refresh_canvas()
        elif mode == "excl_free":
            pts = self._dust_freedraw_pts
            if len(pts) >= 3:
                poly = np.array(pts, dtype=np.int32)
                self._dust_freedraw_polys.append(poly)
                n_zones = len(self._dust_exclude_rects) + len(self._dust_freedraw_polys)
                self._dust_status_var.set(
                    f"{n_zones} exclusion zone(s) — dust inside green areas will not be removed.")
            self._dust_freedraw_pts = []
            self._dust_refresh_canvas()
        elif mode == "mark_lines":
            pts = self._dust_freedraw_pts
            if len(pts) >= 2:
                stroke = np.array(pts, dtype=np.int32)
                self._dust_mark_polys.append(stroke)
                self._dust_status_var.set(
                    f"{len(self._dust_mark_polys)} scratch stroke(s) marked — "
                    "click 'Remove Marked Lines' to fill them.")
            self._dust_freedraw_pts = []
            self._dust_refresh_canvas()
        elif mode == "paint_dust":
            self._dust_paint_active = False
            self._dust_refresh_canvas()

    # ── paint-dust helpers ─────────────────────────────────────────────────

    def _dust_paint_at(self, ix, iy):
        """Paint a circle of radius _dust_paint_radius into the dust mask."""
        if self._dust_source_rgba is None:
            return
        iw, ih = self._dust_source_rgba.size
        # Create mask if not present
        if self._dust_mask_pil is None:
            self._dust_mask_pil = Image.fromarray(
                np.zeros((ih, iw), dtype=np.uint8), 'L')
        mask_arr = np.array(self._dust_mask_pil)
        r = max(1, self._dust_paint_radius.get())
        cx, cy = int(ix), int(iy)
        cv2.circle(mask_arr, (cx, cy), r, 255, -1)
        self._dust_mask_pil = Image.fromarray(mask_arr, 'L')
        self._dust_refresh_canvas()

    # ── exclusion management ───────────────────────────────────────────────

    def _dust_clear_exclusions(self):
        self._dust_exclude_rects  = []
        self._dust_freedraw_polys = []
        self._dust_mark_polys     = []
        self._dust_freedraw_pts   = []
        self._dust_excl_drag      = None
        self._dust_refresh_canvas()
        self._dust_status_var.set("Exclusion zones cleared.")

    def _dust_revert(self):
        if self._dust_source_rgba is None:
            return
        self._dust_push_undo()
        self._dust_result_rgba = None
        self._dust_status_var.set("Reverted to original — run Detect Dust or Remove Detected Dust again.")
        self._dust_refresh_canvas()

    def _dust_remove_lines(self):
        """Fill marked scratch strokes using TELEA inpainting + per-component colour match."""
        if not self._dust_mark_polys:
            self._dust_status_var.set(
                "No scratches marked — switch to Mark Lines mode and draw over them first.")
            return

        source = self._dust_result_rgba or self._dust_source_rgba
        if source is None:
            self._dust_status_var.set("No image loaded.")
            return

        try:
            rgba = np.array(source.convert("RGBA"))
            h, w = rgba.shape[:2]
            rgb  = rgba[:, :, :3].copy()

            # Rasterise each stroke segment-by-segment using cv2.line.
            # Thickness scales with image width so it covers the scratch
            # regardless of resolution.
            stroke_thickness = max(8, w // 400)
            line_mask = np.zeros((h, w), dtype=np.uint8)
            for stroke in self._dust_mark_polys:
                arr = stroke
                if len(arr) < 2:
                    # Single point — draw a filled circle
                    cv2.circle(line_mask,
                                (int(arr[0, 0]), int(arr[0, 1])),
                                stroke_thickness // 2, 255, -1)
                    continue
                for i in range(len(arr) - 1):
                    p1 = (int(arr[i,   0]), int(arr[i,   1]))
                    p2 = (int(arr[i+1, 0]), int(arr[i+1, 1]))
                    cv2.line(line_mask, p1, p2, 255, stroke_thickness)

            if line_mask.max() == 0:
                self._dust_status_var.set("Mask is empty — strokes may be outside the image.")
                return

            core_mask = line_mask.copy()

            # Dilate for better fill coverage around the stroke edges
            k_dilate = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
            inpaint_mask = cv2.dilate(line_mask, k_dilate)
            inpaint_mask = self._dust_apply_exclusions(inpaint_mask)

            # TELEA handles thin scratches/lines well
            rgb_inpainted = cv2.inpaint(rgb, inpaint_mask, inpaintRadius=7,
                                        flags=cv2.INPAINT_TELEA)
            rgb_inpainted = self._dust_color_match(rgb_inpainted, rgb, core_mask)

            # Feathered blend to avoid hard edges
            blend_f = cv2.GaussianBlur(
                inpaint_mask.astype(np.float32), (0, 0), sigmaX=3
            ).clip(0, 255) / 255.0
            blend_f3 = np.stack([blend_f] * 3, axis=2)
            rgb_out = (rgb_inpainted.astype(np.float32) * blend_f3
                       + rgb.astype(np.float32) * (1.0 - blend_f3)).astype(np.uint8)

            self._dust_push_undo()
            result_arr = rgba.copy()
            result_arr[:, :, :3] = rgb_out
            self._dust_result_rgba = Image.fromarray(result_arr, "RGBA")

            self._dust_mark_polys = []
            self._dust_status_var.set(
                "Lines removed — check result, then export or continue editing.")
            self._dust_refresh_canvas()

        except Exception as exc:
            self._dust_status_var.set(f"Remove lines error: {exc}")
            import traceback; traceback.print_exc()

    # ── dust undo / redo ───────────────────────────────────────────────────────

    def _dust_push_undo(self):
        state = self._dust_result_rgba.copy() if self._dust_result_rgba is not None else None
        self._dust_undo_stack.append(state)
        if len(self._dust_undo_stack) > 20:
            self._dust_undo_stack.pop(0)
        self._dust_redo_stack.clear()

    def _dust_undo(self):
        if not self._dust_undo_stack:
            self._dust_status_var.set("Nothing to undo.")
            return
        redo_state = self._dust_result_rgba.copy() if self._dust_result_rgba is not None else None
        self._dust_redo_stack.append(redo_state)
        self._dust_result_rgba = self._dust_undo_stack.pop()
        self._dust_refresh_canvas()
        self._dust_status_var.set(f"Undo  ({len(self._dust_undo_stack)} step(s) remaining)")

    def _dust_redo(self):
        if not self._dust_redo_stack:
            self._dust_status_var.set("Nothing to redo.")
            return
        undo_state = self._dust_result_rgba.copy() if self._dust_result_rgba is not None else None
        self._dust_undo_stack.append(undo_state)
        self._dust_result_rgba = self._dust_redo_stack.pop()
        self._dust_refresh_canvas()
        self._dust_status_var.set(f"Redo  ({len(self._dust_redo_stack)} step(s) remaining)")

    # ── export undo / redo ─────────────────────────────────────────────────────

    def _export_push_undo(self):
        if self._export_scale is None:
            return
        self._export_undo_stack.append((list(self._export_offset), self._export_scale.get()))
        if len(self._export_undo_stack) > 20:
            self._export_undo_stack.pop(0)
        self._export_redo_stack.clear()

    def _export_undo(self):
        if not self._export_undo_stack:
            self._export_status_var.set("Nothing to undo.")
            return
        self._export_redo_stack.append((list(self._export_offset), self._export_scale.get()))
        offset, scale = self._export_undo_stack.pop()
        self._export_offset[:] = offset
        self._export_scale.set(scale)
        self._export_scale_before = scale
        self._export_refresh_canvas()
        self._export_status_var.set(f"Undo  ({len(self._export_undo_stack)} step(s) remaining)")

    def _export_redo(self):
        if not self._export_redo_stack:
            self._export_status_var.set("Nothing to redo.")
            return
        self._export_undo_stack.append((list(self._export_offset), self._export_scale.get()))
        offset, scale = self._export_redo_stack.pop()
        self._export_offset[:] = offset
        self._export_scale.set(scale)
        self._export_scale_before = scale
        self._export_refresh_canvas()
        self._export_status_var.set(f"Redo  ({len(self._export_redo_stack)} step(s) remaining)")

    def _dust_apply_exclusions(self, mask_arr):
        """Zero out mask pixels inside all exclusion zones (rects + free polygons)."""
        if not self._dust_exclude_rects and not self._dust_freedraw_polys:
            return mask_arr
        result = mask_arr.copy()
        h, w = result.shape[:2]
        for (rx0, ry0, rx1, ry1) in self._dust_exclude_rects:
            px0 = max(0, min(rx0, rx1))
            py0 = max(0, min(ry0, ry1))
            px1 = min(w, max(rx0, rx1) + 1)
            py1 = min(h, max(ry0, ry1) + 1)
            result[py0:py1, px0:px1] = 0
        for poly in self._dust_freedraw_polys:
            cv2.fillPoly(result, [poly], 0)
        return result

    def _dust_color_match(self, result_rgb, original_rgb, core_mask):
        """Per-component Poisson seamless cloning.

        For each connected dust component, crop a tight patch, run seamlessClone
        on the patch (so src/dst are aligned correctly), then paste back.
        This forces each spot to adopt the colour of its own immediate surroundings.
        Falls back to a luminance-filtered mean-shift per component on failure.
        """
        if core_mask is None or core_mask.max() == 0:
            return result_rgb

        src = result_rgb.astype(np.uint8)
        dst = original_rgb.astype(np.uint8)
        out = dst.copy()          # start with original; only replace inpainted areas
        h, w = dst.shape[:2]

        n_labels, labels = cv2.connectedComponents(
            (core_mask > 0).astype(np.uint8), connectivity=8)

        for lbl in range(1, n_labels):
            comp = (labels == lbl).astype(np.uint8)

            ys, xs = np.where(comp > 0)
            if len(ys) == 0:
                continue

            # Bounding box with padding so seamlessClone has boundary colour context
            pad = 20
            y1 = max(0,     ys.min() - pad)
            y2 = min(h - 1, ys.max() + pad)
            x1 = max(0,     xs.min() - pad)
            x2 = min(w - 1, xs.max() + pad)

            src_crop  = src[y1:y2, x1:x2].copy()
            dst_crop  = dst[y1:y2, x1:x2].copy()
            comp_crop = comp[y1:y2, x1:x2]

            # Small dilation gives seamlessClone a colour-matched boundary ring
            k = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
            mask_crop = cv2.dilate(comp_crop * 255, k)

            ch, cw = dst_crop.shape[:2]
            cx_l, cy_l = cw // 2, ch // 2

            try:
                # seamlessClone requires mask bbox to be fully inside the crop
                my, mx = np.where(mask_crop > 0)
                if (my.min() < 2 or my.max() > ch - 3 or
                        mx.min() < 2 or mx.max() > cw - 3):
                    raise ValueError("mask touches crop edge")

                blended = cv2.seamlessClone(
                    src_crop, dst_crop, mask_crop,
                    (cx_l, cy_l), cv2.NORMAL_CLONE)

                # Write blended crop back (only the component pixels)
                comp_bool = comp_crop > 0
                patch = out[y1:y2, x1:x2].copy()
                patch[comp_bool] = blended[comp_bool]
                out[y1:y2, x1:x2] = patch

            except Exception:
                # Fallback: luminance-filtered mean-shift for this component
                ring_k = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (9, 9))
                outer  = cv2.dilate(comp_crop, ring_k)
                ring   = (outer > 0) & (comp_crop == 0)
                if ring.sum() < 3:
                    continue
                ring_px = dst_crop[ring].astype(np.float32)
                lum = (0.299 * ring_px[:, 0] +
                       0.587 * ring_px[:, 1] +
                       0.114 * ring_px[:, 2])
                bright = ring_px[lum >= np.percentile(lum, 40)]
                if len(bright) < 3:
                    bright = ring_px
                ctx_mean = bright.mean(axis=0)
                inp_mean = src_crop[comp_crop > 0].astype(np.float32).mean(axis=0)
                shift    = ctx_mean - inp_mean
                patch    = out[y1:y2, x1:x2].copy().astype(np.float32)
                cb       = comp_crop > 0
                patch[cb] = np.clip(src_crop[cb].astype(np.float32) + shift, 0, 255)
                out[y1:y2, x1:x2] = patch.astype(np.uint8)

        return out

    def _dust_fit_view(self):
        if self._dust_canvas is None:
            return
        pil_img = self._dust_result_rgba or self._dust_source_rgba
        if pil_img is None:
            return
        self._dust_canvas.update_idletasks()
        cw = self._dust_canvas.winfo_width()
        ch = self._dust_canvas.winfo_height()
        if cw < 2 or ch < 2:
            return
        iw, ih = pil_img.size
        self._dust_zoom = min(cw / iw, ch / ih)
        self._dust_pan  = [0, 0]
        self._dust_refresh_canvas()

    def _dust_100(self):
        self._dust_zoom = 1.0
        self._dust_pan  = [0, 0]
        self._dust_refresh_canvas()

    def _dust_wheel(self, e):
        src = self._dust_source_rgba
        if src is None:
            return
        old_zoom = self._dust_zoom
        new_zoom = max(0.05, min(30.0, old_zoom * (1.20 if e.delta > 0 else (1.0 / 1.20))))
        self._dust_zoom = new_zoom

        iw, ih = src.size
        cw = self._dust_canvas.winfo_width()  or 800
        ch = self._dust_canvas.winfo_height() or 600
        ox_old = self._dust_pan[0] + (cw - int(iw * old_zoom)) // 2
        oy_old = self._dust_pan[1] + (ch - int(ih * old_zoom)) // 2
        img_x = (e.x - ox_old) / old_zoom
        img_y = (e.y - oy_old) / old_zoom
        ox_new = e.x - img_x * new_zoom
        oy_new = e.y - img_y * new_zoom
        self._dust_pan[0] = int(round(ox_new - (cw - int(iw * new_zoom)) // 2))
        self._dust_pan[1] = int(round(oy_new - (ch - int(ih * new_zoom)) // 2))

        if getattr(self, "_dust_render_job", None):
            self.root.after_cancel(self._dust_render_job)
        self._dust_render_job = self.root.after(20, self._dust_refresh_canvas)

    def _dust_mid_press(self, e):
        self._dust_pan_start = (e.x - self._dust_pan[0], e.y - self._dust_pan[1])

    def _dust_mid_drag(self, e):
        if self._dust_pan_start:
            self._dust_pan[0] = e.x - self._dust_pan_start[0]
            self._dust_pan[1] = e.y - self._dust_pan_start[1]
            self._dust_refresh_canvas()

    def _dust_save(self):
        out_img = self._dust_result_rgba or self._dust_source_rgba
        if out_img is None:
            messagebox.showwarning("Nothing to save", "Run dust removal first.")
            return
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        ts   = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        path = OUTPUT_DIR / f"board_dust_{ts}.png"
        out_img.save(str(path), format='PNG')
        self.set_status(f"Dust removal result saved → {path.name}")
        messagebox.showinfo("Saved", f"Result saved:\n{path}")

    # ═══════════════════════════════════════════ Step 5 — Export ════════════

    def _build_export_page(self):
        self._export_scale      = tk.DoubleVar(value=95.0)
        self._export_margin     = tk.IntVar(value=0)
        self._export_preview_bg = tk.StringVar(value="white")
        self._export_status_var = tk.StringVar(value="")

        page = tk.Frame(self._content, bg=BG)

        # ── Controls row 1 ──────────────────────────────────────────────────
        ctrl = tk.Frame(page, bg=BG, pady=4)
        ctrl.pack(fill=tk.X, padx=8)

        tk.Label(ctrl, text="Scale:", bg=BG).pack(side=tk.LEFT)
        ttk.Spinbox(ctrl, from_=10.0, to=100.0, increment=1.0,
                    textvariable=self._export_scale,
                    width=6, format="%.1f",
                    command=self._export_scale_spinbox_cmd).pack(side=tk.LEFT, padx=(2, 2))
        tk.Label(ctrl, text="%  of 2400 px", bg=BG).pack(side=tk.LEFT, padx=(0, 14))

        tk.Label(ctrl, text="Margin:", bg=BG).pack(side=tk.LEFT)
        ttk.Spinbox(ctrl, from_=0, to=600, increment=10,
                    textvariable=self._export_margin,
                    width=5,
                    command=self._export_refresh_canvas).pack(side=tk.LEFT, padx=(2, 2))
        tk.Label(ctrl, text="px", bg=BG).pack(side=tk.LEFT, padx=(0, 14))

        tk.Label(ctrl, text="Preview BG:", bg=BG).pack(side=tk.LEFT)
        ttk.Radiobutton(ctrl, text="White", variable=self._export_preview_bg,
                        value="white",   command=self._export_refresh_canvas).pack(side=tk.LEFT, padx=4)
        ttk.Radiobutton(ctrl, text="Transparent", variable=self._export_preview_bg,
                        value="checker", command=self._export_refresh_canvas).pack(side=tk.LEFT, padx=4)

        ttk.Button(ctrl, text="Auto Fit & Center",
                   command=self._export_auto_fit).pack(side=tk.LEFT, padx=14)
        ttk.Button(ctrl, text="Fit view", command=self._export_fit_view, width=8).pack(side=tk.LEFT, padx=4)
        ttk.Button(ctrl, text="100%",     command=self._export_view_100,  width=6).pack(side=tk.LEFT)

        # ── Controls row 2 — export buttons ─────────────────────────────────
        ctrl2 = tk.Frame(page, bg=BG, pady=2)
        ctrl2.pack(fill=tk.X, padx=8)

        tk.Label(ctrl2, text="Drag image to reposition · Scroll to zoom preview · Middle-drag to pan",
                 bg=BG, fg="#777", font=("Helvetica", 8)).pack(side=tk.LEFT)

        ttk.Button(ctrl2, text="Export — transparent BG",
                   command=lambda: self._export_save("transparent")).pack(side=tk.RIGHT, padx=(6, 0))
        ttk.Button(ctrl2, text="Export — white BG",
                   command=lambda: self._export_save("white")).pack(side=tk.RIGHT, padx=6)

        # ── Status ───────────────────────────────────────────────────────────
        tk.Label(page, textvariable=self._export_status_var,
                 bg=BG, fg="#333", anchor="w").pack(fill=tk.X, padx=10)

        # ── Canvas ───────────────────────────────────────────────────────────
        canvas_frame = tk.Frame(page, bg="#555")
        canvas_frame.pack(fill=tk.BOTH, expand=True)
        self._export_canvas = tk.Canvas(canvas_frame, bg="#555", highlightthickness=0)
        self._export_canvas.pack(fill=tk.BOTH, expand=True)
        self._export_canvas.bind("<MouseWheel>",      self._export_wheel)
        self._export_canvas.bind("<ButtonPress-1>",   self._export_img_press)
        self._export_canvas.bind("<B1-Motion>",       self._export_img_drag)
        self._export_canvas.bind("<ButtonRelease-1>", self._export_img_release)
        self._export_canvas.bind("<ButtonPress-2>",   self._export_pan_press)
        self._export_canvas.bind("<B2-Motion>",       self._export_pan_drag)

        return page

    def _export_scale_spinbox_cmd(self):
        """Spinbox command for scale — pushes undo with the pre-click scale, then refreshes."""
        self._export_undo_stack.append((list(self._export_offset), self._export_scale_before))
        if len(self._export_undo_stack) > 20:
            self._export_undo_stack.pop(0)
        self._export_redo_stack.clear()
        self._export_scale_before = self._export_scale.get()
        self._export_refresh_canvas()

    def _load_export_step(self):
        src = self._dust_result_rgba or self._dust_source_rgba or self._crop_result_rgba
        if src is None:
            self._export_status_var.set(
                "No image available — complete the Crop Board step first.")
            return
        self._export_source_rgba = src.copy()
        self._export_offset = [1200, 1200]
        self._export_undo_stack = []
        self._export_redo_stack = []
        self._export_scale_before = self._export_scale.get() if self._export_scale else 95.0
        self._export_status_var.set(
            "Drag the image to reposition it. Use Export buttons to save the 2400×2400 PNG.")
        self.root.after(100, self._export_auto_fit)

    def _export_render_2400(self, bg="transparent"):
        """Return a 2400×2400 PIL image with the product composited at current scale/offset."""
        if bg == "white":
            canvas = Image.new("RGBA", (2400, 2400), (255, 255, 255, 255))
        else:
            canvas = Image.new("RGBA", (2400, 2400), (0, 0, 0, 0))

        src = self._export_source_rgba
        if src is None:
            return canvas

        iw, ih = src.size
        scale_f = max(0.01, self._export_scale.get() / 100.0)
        max_dim = 2400 * scale_f
        factor  = min(max_dim / iw, max_dim / ih)
        nw = max(1, int(round(iw * factor)))
        nh = max(1, int(round(ih * factor)))

        resized = src.resize((nw, nh), Image.LANCZOS)

        cx, cy = self._export_offset
        x0 = cx - nw // 2
        y0 = cy - nh // 2

        canvas.paste(resized, (x0, y0), resized.split()[3])
        return canvas

    def _export_make_checker(self, size=2400, tile=30):
        """2400×2400 checkerboard as RGBA for transparent-BG preview."""
        img = np.zeros((size, size, 3), dtype=np.uint8)
        light, dark = 200, 155
        for r in range(0, size, tile):
            for c in range(0, size, tile):
                col = light if ((r // tile) + (c // tile)) % 2 == 0 else dark
                img[r:r+tile, c:c+tile] = col
        return Image.fromarray(img, "RGB")

    def _export_refresh_canvas(self, *_):
        if self._export_canvas is None or self._export_source_rgba is None:
            return

        cw = self._export_canvas.winfo_width()
        ch = self._export_canvas.winfo_height()
        if cw < 2 or ch < 2:
            self._export_canvas.after(50, self._export_refresh_canvas)
            return

        # Build the 2400×2400 composite
        composite = self._export_render_2400(bg="transparent")

        if self._export_preview_bg.get() == "white":
            bg_img = Image.new("RGB", (2400, 2400), (255, 255, 255))
        else:
            bg_img = self._export_make_checker()

        preview = bg_img.copy()
        preview.paste(composite, (0, 0), composite.split()[3])

        zoom   = self._export_view_zoom
        disp   = int(2400 * zoom)
        ox = self._export_view_pan[0] + (cw - disp) // 2
        oy = self._export_view_pan[1] + (ch - disp) // 2

        sx = max(0, int(-ox / zoom))
        sy = max(0, int(-oy / zoom))
        ex = min(2400, int((cw - ox) / zoom) + 1)
        ey = min(2400, int((ch - oy) / zoom) + 1)
        if ex <= sx or ey <= sy:
            return

        crop = preview.crop((sx, sy, ex, ey))
        tw = max(1, int((ex - sx) * zoom))
        th = max(1, int((ey - sy) * zoom))
        crop = crop.resize((tw, th),
            Image.BILINEAR if zoom > 1.0 else Image.LANCZOS)

        self._export_display_tk = ImageTk.PhotoImage(crop)
        self._export_canvas.delete("all")
        # Border outline for the 2400×2400 frame
        bx0 = ox; by0 = oy; bx1 = ox + disp; by1 = oy + disp
        self._export_canvas.create_rectangle(bx0 - 1, by0 - 1, bx1, by1,
                                              outline="#aaa", width=1)
        dx = ox + int(sx * zoom)
        dy = oy + int(sy * zoom)
        self._export_canvas.create_image(dx, dy, anchor="nw",
                                          image=self._export_display_tk)
        # Margin guide — dashed blue rectangle showing safe area
        margin = self._export_margin.get() if self._export_margin else 0
        if margin > 0:
            mx0 = ox + margin * zoom
            my0 = oy + margin * zoom
            mx1 = ox + (2400 - margin) * zoom
            my1 = oy + (2400 - margin) * zoom
            self._export_canvas.create_rectangle(mx0, my0, mx1, my1,
                outline="#4499ff", width=1, dash=(8, 4))

    def _export_auto_fit(self):
        """Scale product to fill available area (respecting margin), center it, fit view."""
        if self._export_source_rgba is None:
            return
        self._export_push_undo()
        margin = self._export_margin.get() if self._export_margin else 0
        available = max(10, 2400 - 2 * margin)
        iw, ih = self._export_source_rgba.size
        factor = min(available / iw, available / ih)
        scale_pct = min(100.0, round(factor * 100.0, 1))
        self._export_scale.set(scale_pct)
        self._export_offset = [1200, 1200]
        self._export_fit_view()

    def _export_fit_view(self):
        if self._export_canvas is None:
            return
        self._export_canvas.update_idletasks()
        cw = self._export_canvas.winfo_width()
        ch = self._export_canvas.winfo_height()
        if cw < 2 or ch < 2:
            return
        self._export_view_zoom = min(cw / 2400, ch / 2400) * 0.97
        self._export_view_pan  = [0, 0]
        self._export_refresh_canvas()

    def _export_view_100(self):
        self._export_view_zoom = 1.0
        self._export_view_pan  = [0, 0]
        self._export_refresh_canvas()

    def _export_wheel(self, e):
        old_zoom = self._export_view_zoom
        new_zoom = max(0.03, min(30.0, old_zoom * (1.20 if e.delta > 0 else (1.0 / 1.20))))
        self._export_view_zoom = new_zoom

        cw = self._export_canvas.winfo_width()  or 800
        ch = self._export_canvas.winfo_height() or 600
        ox_old = self._export_view_pan[0] + (cw - int(2400 * old_zoom)) // 2
        oy_old = self._export_view_pan[1] + (ch - int(2400 * old_zoom)) // 2
        img_x = (e.x - ox_old) / old_zoom
        img_y = (e.y - oy_old) / old_zoom
        ox_new = e.x - img_x * new_zoom
        oy_new = e.y - img_y * new_zoom
        self._export_view_pan[0] = int(round(ox_new - (cw - int(2400 * new_zoom)) // 2))
        self._export_view_pan[1] = int(round(oy_new - (ch - int(2400 * new_zoom)) // 2))

        if getattr(self, "_export_render_job", None):
            self.root.after_cancel(self._export_render_job)
        self._export_render_job = self.root.after(20, self._export_refresh_canvas)

    def _export_pan_press(self, e):
        self._export_view_pan_start = (e.x - self._export_view_pan[0],
                                       e.y - self._export_view_pan[1])

    def _export_pan_drag(self, e):
        if self._export_view_pan_start:
            self._export_view_pan[0] = e.x - self._export_view_pan_start[0]
            self._export_view_pan[1] = e.y - self._export_view_pan_start[1]
            self._export_refresh_canvas()

    def _export_img_press(self, e):
        self._export_push_undo()
        self._export_img_drag_start = (e.x, e.y,
                                        self._export_offset[0],
                                        self._export_offset[1])

    def _export_img_drag(self, e):
        if self._export_img_drag_start is None:
            return
        ex0, ey0, ox0, oy0 = self._export_img_drag_start
        dcanvas_x = e.x - ex0
        dcanvas_y = e.y - ey0
        zoom = max(0.001, self._export_view_zoom)
        self._export_offset[0] = int(ox0 + dcanvas_x / zoom)
        self._export_offset[1] = int(oy0 + dcanvas_y / zoom)
        self._export_refresh_canvas()

    def _export_img_release(self, e):
        self._export_img_drag_start = None

    def _export_save(self, bg_mode):
        """Save a 2400×2400 PNG with bg_mode='white' or 'transparent'."""
        if self._export_source_rgba is None:
            messagebox.showwarning("Nothing to export",
                                   "Complete the previous steps first.")
            return

        self._export_status_var.set("Rendering…")
        self._export_canvas.update_idletasks()

        composite = self._export_render_2400(bg=bg_mode)
        if bg_mode == "white":
            out_img = composite.convert("RGB")
        else:
            out_img = composite  # keep RGBA

        suffix = "white" if bg_mode == "white" else "transparent"
        ts   = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        path = OUTPUT_DIR / f"product_{suffix}_{ts}.png"

        try:
            out_img.save(str(path), format="PNG")
            self._export_status_var.set(f"Saved → {path.name}")
            messagebox.showinfo("Exported", f"2400×2400 PNG saved:\n{path}")
        except Exception as exc:
            self._export_status_var.set(f"Save error: {exc}")
            messagebox.showerror("Save error", str(exc))

    # ═══════════════════════════════════════════ Helpers ══════════════════════

    def _set_progress(self, v):
        self._progress["value"] = v

    def set_status(self, msg, error=False):
        self._status_var.set(msg)
        self._status_lbl.configure(fg="red" if error else "#333")


# ─────────────────────────────────────────────────────────────────────────────

def main():
    root = tk.Tk()
    PhotoEditorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
