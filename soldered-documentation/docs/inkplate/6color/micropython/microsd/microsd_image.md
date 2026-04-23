---  
slug: /inkplate/6color/micropython/microsd/image-display
title: Inkplate 6COLOR – MicroSD Display Image
sidebar_label: MicroSD Display Image
id: image-display
hide_title: false
---

To display images from SD card use the `drawImage()` function, specifying the image location on SD card.

<InfoBox>Supported image formats: JPG, BMP, and PNG.</InfoBox>

```python
from inkplate6COLOR import Inkplate
from os import listdir

# Create Inkplate object
inkplate = Inkplate()

# Initialize the display, needs to be called only once
inkplate.begin()

# Initialize SD card
inkplate.initSDCard(fastBoot=True)

# This prints all the files on SD card
print(listdir("/sd"))

# Draw image found on SD card
inkplate.drawImage("sd/coastal.jpg", 0, 0, invert=False, dither=True, kernel_type=Inkplate.KERNEL_FLOYD_STEINBERG)

# Show the image from the buffer
inkplate.display()

inkplate.SDCardSleep()
# To turn it back on, use:
# inkplate.SDCardWake()
```

<CenteredImage src="/img/6color/6color-sd-mp.jpg" alt="Expected output on Inkplate display" caption="Example image from sd card" />

<FunctionDocumentation
    functionName="inkplate.drawImage()"
    description="This function draws an image from the specified char path (either web URL or local file path)"
    returnDescription="None"
    parameters={[ 
        { type: "string", name: "path", description: "Path and filename of the image. Can be a URL (for web images) or a file path (on the microSD card)." },
        { type: "int", name: "x0", description: "X-coordinate of the image's upper-left corner in the framebuffer." },
        { type: "int", name: "y0", description: "Y-coordinate of the image's upper-left corner in the framebuffer." },
        { type: "bool", name: "invert", description: "If true, inverts colors." },
        { type: "bool", name: "dither", description: "Dithering mode: 0 (disabled), 1 (enabled)." },
        { type: "int", name: "kernel_type", description: "Specifies dithering algorithm to use."}
    ]}
/>

<InfoBox>
Available options for **dithering** algorithm:

| **Algorithm**  | **Value** |
| --------------------- | ------------------------ |
| `Inkplate.KERNEL_FLOYD_STEINBERG` | 0 |
| `Inkplate.KERNEL_JJN` | 1 |
| `Inkplate.KERNEL_STUCKI` | 2 |
| `Inkplate.KERNEL_BURKES `| 3 |

**Performance Notes**
- JPG: ~3 seconds (or ~14s with dithering)
- PNG: ~9 seconds (or ~19s with dithering)
- BMP: ~20 seconds (or ~40s with dithering)
- Maximum image file size: ~800kB
</InfoBox>