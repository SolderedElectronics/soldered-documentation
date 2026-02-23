---
slug: /inkplate/13spectra/micropython/microsd/draw-image-from-microsd-card
title: Inkplate 13SPECTRA MicroPython - Draw Image from microSD card
sidebar_label: Draw Image from microSD card
id: 13spectra-draw-image-from-microsd-card
---

Inkplate 13SPECTRA can load and render images directly from the onboard microSD card. This example shows how to initialize the SD card, list its contents and display a JPEG, PNG or BMP image on screen.

---

## Displaying an image from the SD card

Before running this example, make sure your SD card is formatted as **FAT16, FAT32 or exFAT** and inserted into Inkplate 10.
To learn how to format the microSD card click [**here**](/documentation/inkplate/10/micropython/microsd/formatting-the-microsd-card/#preparing-the-microsd-card-before-usage)

The picture used in the example can be downloaded directly from the [Inkplate MicroPython Library](https://github.com/SolderedElectronics/Inkplate-micropython/blob/master/Examples/Inkplate10/displayImageSd/mountain.jpg).

```python
from inkplate13SPECTRA import Inkplate

from os import listdir

# Create Inkplate object
inkplate = Inkplate()

# Initialize the display, needs to be called only once
inkplate.begin()

# Initializes the SD card.
#
# Parameters:
# - fastboot (bool, default=False): 
#     If True, performs a soft reboot immediately after SD card initialization 
#     (only on cold start or hard reset). This significantly improves SD card 
#     read speeds—typically doubling performance.
#
# Note:
# - This function must be called before accessing files on the SD card.
# - The fastboot option has no effect if the device is already running.
inkplate.initSDCard(fastBoot=True)

# This prints all the files on card
print(listdir("/sd"))


# Draw an image on the screen.
#
# Parameters:
# - path: File path to the image. Supports local paths (e.g., from SD card) or URLs.
#         Supported formats: JPG, PNG, BMP.
#
# - x0: X-coordinate of the top-left corner where the image will be displayed.
#
# - y0: Y-coordinate of the top-left corner where the image will be displayed.
#
# - invert (bool, default=False): If True, inverts the image colors.
#
# - dither (bool, default=False): If True, applies a dithering algorithm to the image for better grayscale rendering.
#
# - kernel_type (int): Specifies the dithering algorithm to use.
#     Available options:
#       Inkplate.KERNEL_FLOYD_STEINBERG = 0
#       Inkplate.KERNEL_JJN             = 1
#       Inkplate.KERNEL_STUCKI          = 2
#       Inkplate.KERNEL_BURKES          = 3
#
# Performance Notes:
# - JPG: ~52 seconds (or ~90s with dithering)
#
# Example usage:
inkplate.drawImage("sd/coast.jpg", 0, 0, invert=False, dither=True, kernel_type=Inkplate.KERNEL_FLOYD_STEINBERG )

# Show the image from the buffer
inkplate.display()

inkplate.SDCardSleep()
# To turn it back on, use:
# inkplate.SDCardWake()
```

<CenteredImage src="/img/13spectra/DSC00715.jpg" alt="Example output displayed on e-paper display" caption="Example output displayed on e-paper display" width="1200px" />

<FunctionDocumentation
functionName="inkplate.drawImage()"
description="Draw an image from a file path or URL into the display buffer."
parameters={[
{ type: 'String', name: 'path', description: 'Path to image (e.g. "sd/mountain.jpg") or URL.' },
{ type: 'Number', name: 'x0', description: 'X coordinate of the top-left corner.' },
{ type: 'Number', name: 'y0', description: 'Y coordinate of the top-left corner.' },
{ type: 'Boolean', name: 'invert', description: 'If True, invert image colors.' },
{ type: 'Boolean', name: 'dither', description: 'If True, apply dithering for better grayscale rendering.' },
{ type: 'Constant', name: 'kernel_type', description: 'Dithering algorithm. Options: Inkplate.KERNEL_FLOYD_STEINBERG, Inkplate.KERNEL_JJN, Inkplate.KERNEL_STUCKI, Inkplate.KERNEL_BURKES.' }
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