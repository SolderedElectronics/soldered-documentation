# Soldered PCB Photo Editor

A desktop tool for processing PCB product photos. It guides you through six steps:

1. **Load** — import RAW (`.dng`, `.nef`, `.cr2`, etc.) or JPEG/PNG files
2. **Preview** — focus-stack multiple shots into a single sharp image
3. **Auto Edit** — white balance, colour normalisation, exposure correction
4. **Crop Board** — polygon crop with lasso, arc, and cut-zone tools
5. **Dust Removal** — AI inpainting to remove scratches, dust, and lines
6. **Export** — composite onto a 2400×2400 template and export as PNG

## Requirements

- Windows 10/11
- Python 3.9–3.13

## Installation

```bat
install.bat
```

This installs: `rawpy`, `numpy`, `opencv-python`, `Pillow`, `tifffile`.

For AI-powered dust removal (optional, downloads ~200 MB LaMa model on first use):

```bat
install_iopaint.bat
```

## Running

```bat
run.bat
```

Or directly:

```bat
python main.py
```

## Manual dependency install

```
pip install -r requirements.txt
```
