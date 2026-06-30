# Inkplate 13SPECTRA — Documentation TODO

Hand-off list for finishing the Inkplate 13SPECTRA docs.

The **first draft is already live**: all image placeholders were removed so the
published pages read cleanly. This file lists everything still missing so the
docs can be completed to full quality. Every item below is real work that was
stubbed/placeholdered in the first draft.

All paths are relative to `soldered-documentation/docs/inkplate/13spectra/`.

---

## How to work through this

1. **For every code example: run it on a real Inkplate 13SPECTRA, photograph the
   output, add the photo to the page.** A doc page that shows a code block but no
   result photo is not finished. Take the photo straight-on, well lit, board
   filling most of the frame.
2. Save images under `soldered-documentation/static/img/13spectra/`. Reference
   them in markdown with `<CenteredImage src="/img/13spectra/<file>" alt="..."
   caption="..." width="..." />` (copy the pattern already used in
   `hardware/13spectra_hardware_design.md`). Note the path in markdown is
   `/img/...` (no `/documentation` prefix — site baseUrl is `/`).
3. After writing, run `npm run build` from `soldered-documentation/`. Build must
   pass with **zero broken links**. Fix anything it reports before pushing.
4. Re-enable the two pages removed from the sidebar (FAQ, Free GPIO) only once
   their content is done — see those sections below.

---

## 1. Image / photo tasks (per page)

These pages had an image placeholder removed. Add the described photo/screenshot.

### Getting started — `13spectra_getting_started.md`
- Photo: onboard **USB-C connector** highlighted on the board.
- Photo: onboard **power switch** highlighted on the board.
- Place them in "Step 1. Connect Inkplate via USB and power it on".

### Overview — `13spectra_overview.md`
- Hero photo of the **13SPECTRA display board** (colour content on screen looks
  best). Add near the top, after the intro paragraphs.

### Basics → Drawing graphics — `basics/drawing_graphics.md`
- **Run the shapes example, photograph the output**, add it after the code block
  (right before "Below are the detailed references to these functions").

### Hardware → Hardware design — `hardware/13spectra_hardware_design.md`
- Photo: **front side of board with components marked/labelled** (in the
  "Components" section). A back-side overview image already exists; add the
  marked front side.

### Hardware → Hardware files — `hardware/13spectra_hardware_files.md`
- Screenshot: **KiCad project** open (CAD files section).
- Screenshot: **schematic** PDF (Schematic section).
- Screenshot: **interactive BOM / BOM table** (BOM section).

### Hardware → Bypass power switch — `hardware/13spectra_bypass_power_switch.md`
- Photo: **location of the power-switch bypass pads highlighted** on the PCB.
- Also fill the real **pad name/designator** — the draft removed a
  `[PADS PLACEHOLDER]` and now just says "the bypass pads". Name them.

### Hardware → Battery — `hardware/13spectra_hardware_battery.md`
- Photo: **battery polarity / JST connector** on the board, matching the
  polarity text (notch up → + left, − right).

### MicroSD basics (Arduino) — `microsd/sd_basic.md`
- Photo: **microSD card slot highlighted** on the board.

### MicroSD formatting (MicroPython) — `micropython/microsd/formatting_the_microsd_card.md`
- Photo: **microSD card slot highlighted** (can reuse the same shot as above).

### Battery voltage (MicroPython) — `micropython/battery_voltage.md`
- Photo: **battery connection** to the board.
- Draft note: the line "Battery should be connected like this:" + its image were
  removed. Re-add a short sentence + the photo.

---

## 2. Pages removed from the sidebar — finish, then re-add

These two pages were unpublishable (essentially empty) so they were removed from
`sidebars.js`. The `.md` files still exist. Finish the content, then re-add the
sidebar entry and rebuild.

### FAQ and troubleshooting — `13spectra_faq.md`  ⚠️ EMPTY PAGE
- The file is **frontmatter only — no body at all.**
- Write the FAQ. Use the FAQ pages of other Inkplate models as a template
  (e.g. `docs/inkplate/6motion/6motion_faq*.md`,
  `docs/inkplate/10/10_faq.md`). Cover at minimum:
  - Board not detected / wrong COM port / CH340 driver install.
  - Upload fails / how to enter bootloader.
  - Display not refreshing, ghosting, full-refresh-only (no partial update on
    SPECTRA), colour looks wrong.
  - Battery not charging / polarity warning.
  - microSD not detected / supported formats (FAT16/32, exFAT).
  - Where to get help (forum / support link).
- **Re-add to sidebar:** in `sidebars.js`, inside the 13SPECTRA category `items`,
  add `"inkplate/13spectra/13spectra-faq-troubleshooting"` as the **last** entry
  (after the MicroPython sub-category), matching how other models place FAQ last.

### Hardware → Free GPIO pins — `hardware/13spectra_hardware_free_gpio.md`  ⚠️ SHELL PAGE
- Page is a shell: intro text only, everything else is placeholders.
- Still contains one `[IMAGE PLACEHOLDER ...]` and `[TEXT PLACEHOLDER ...]` and
  `[TABLE PLACEHOLDER ...]` — do NOT publish until filled.
- Needed content:
  - **Free-pin text list:** the GPIO pins on the ESP32-S3-WROOM-2 **not**
    connected to any onboard component (quick reference for someone who just
    wants the numbers).
  - **Image:** board photo/pinout with the free GPIO pins highlighted.
  - **Table:** every pin → function → what it connects to. Use the free-GPIO
    page of another model as the table template
    (e.g. `docs/inkplate/6motion/hardware/6motion_hardware_free_gpio.md`,
    `docs/inkplate/10/hardware/10_hardware_free_gpio.md`).
  - Source of truth = the 13SPECTRA schematic / KiCad project.
- **Re-add to sidebar:** in `sidebars.js`, in the 13SPECTRA Hardware sub-category
  `items`, re-insert
  `"inkplate/13spectra/hardware/13spectra-hardware-free-gpio"` between
  `...-hardware-jumpers` and `...-hardware-power-switch`.

---

## 3. Pages kept live but with sections still to write

### Hardware → Hardware design — `hardware/13spectra_hardware_design.md`
Page is published, but the **E-paper panel section is unfinished**:
- `[MODEL NAME PLACEHOLDER]` — fill in the **exact E Ink panel model/part
  number** for 13SPECTRA.
- `[TEXT PLACEHOLDER - display information]` — write the display description
  (technology, colours, refresh behaviour, recommended use).
- `[TABLE PLACEHOLDER - display specification table]` — build the **display spec
  table** (resolution 1600×1200, size 13.3", colours, refresh time, operating
  conditions, etc.) from the panel datasheet.
- Also fix the **section header background image**: line uses
  `backgroundImage="/img/inkplate_6_motion/6_motion_hw.png"` (6MOTION's image) —
  replace with a 13SPECTRA image.
- Typos to fix in the "Basic overview" paragraph: "chac" → "such", "charing" →
  "charging".

### Any other `[TABLE PLACEHOLDER ...]`
Same rule everywhere: a `[TABLE PLACEHOLDER ...]` marks a table that must be
built from the relevant datasheet/schematic. Search before publishing:
`grep -rn "TABLE PLACEHOLDER" docs/inkplate/13spectra`.

---

## 4. Remaining `[LINK PLACEHOLDER ...]` — fill in real URLs

Throughout the docs there are `[LINK PLACEHOLDER ...]` markers that must be
replaced with real links. Find them all with:

```
grep -rn "LINK PLACEHOLDER" docs/inkplate/13spectra
```

Known ones and what they should point to:
- `13spectra_overview.md` — **product page** (soldered.com 13SPECTRA product).
- `13spectra_getting_started.md` — **troubleshooting page** link.
- `hardware/13spectra_hardware_design.md` — **open-source license** link.
- `hardware/13spectra_hardware_open_source.md` — **license files** in repo.
- `hardware/13spectra_hardware_files.md` — **GitHub hardware repo** link.
- `wifi/wifi_https_certificate.md`, `wifi/wifi_basics.md` — **GitHub example**
  links.
- `basics/printing_text.md` — **examples on GitHub** link.
- `deepsleep/sleep_simple.md` — **wake-up button example** on GitHub.
- `micropython/battery_voltage.md` — **13SPECTRA batteries** doc/product link.
- `micropython/rtc/basic_rtc_usage.md`, `rtc/rtc_alarm.md` — **RTC example**
  GitHub links.
- `microsd/sd_basic.md` — **txt read** and **txt write** example links.
- `microsd/sd_image.md` — **example images download** + **example GitHub** links.

Also: `wifi/wifi_https_certificate.md` has `const char* certificate ="";` — leave
the empty string (user supplies their own cert), but make sure the surrounding
text explains that.

---

## 5. Final QA — test the docs properly before sign-off

Do not consider the docs done until all of this passes:

1. **Follow the Getting Started guide end to end on real hardware** — install the
   board/library, create the sketch, upload it, confirm "Hello World" appears.
   The written steps must match what actually happens.
2. **Run every code example** on a 13SPECTRA and confirm it behaves as the page
   says (and that the result photo you added matches).
3. **Click every link** — internal cross-links and external GitHub/product links.
   No 404s. Internal doc links use `/inkplate/13spectra/...` form (NO
   `/documentation/` prefix).
4. **`npm run build` passes with zero broken links / broken anchors** for all
   13SPECTRA pages.
5. **Proofread** — fix typos (several exist, e.g. overview page: "informatin",
   "trully", "extremenly", "integratino", "long-temr", "low.maintenance";
   hardware design: "chac", "charing"). Check every page still reads as
   13SPECTRA (earlier drafts were copy-pasted from Inkplate 10 / 6COLOR — verify
   no other board names slipped through).
6. Confirm **FAQ** and **Free GPIO** pages are finished AND re-added to the
   sidebar.
