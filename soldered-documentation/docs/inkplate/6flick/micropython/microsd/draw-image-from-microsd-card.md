---
slug: /inkplate/6flick/micropython/microsd/draw-image-from-microsd-card
title: Inkplate 6FLICK MicroPython - Draw Image from microSD card
sidebar_label: Draw Image from microSD card
id: draw-image-from-microsd-card
---

Inkplate 6FLICK can load and render images directly from the onboard microSD card. This example shows how to initialize the SD card, list its contents and display a JPEG, PNG or BMP image on screen.

---

## Displaying an image from the SD card

Before running this example, make sure your SD card is formatted as **FAT16, FAT32 or exFAT** and inserted into Inkplate 6FLICK.
To learn how to format the microSD card click [**here**](/inkplate/6flick/micropython/microsd/formatting-the-microsd-card/#preparing-the-microsd-card-before-usage)

The picture used in the example can be downloaded directly from the [Inkplate MicroPython Library](https://github.com/SolderedElectronics/Inkplate-micropython/blob/master/examples/inkplate6flick/displayimagesd/image.jpg).

```python
# Include needed libraries
from inkplate6_flick import Inkplate

from os import listdir, stat

# Create Inkplate object in 2-bit (real 8-level GS3) grayscale mode
inkplate = Inkplate(Inkplate.INKPLATE_2BIT)

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
inkplate.init_sd_card(fast_boot=True)

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
# - dither (bool, default=False): If True, applies a dithering algorithm to
#   the image for better grayscale rendering.
#
# - kernel_type (int): Specifies the dithering algorithm to use.
#     Available options:
#       Inkplate.KERNEL_FLOYD_STEINBERG = 0
#       Inkplate.KERNEL_JJN             = 1
#       Inkplate.KERNEL_STUCKI          = 2
#       Inkplate.KERNEL_BURKES          = 3
#
# Example usage:
IMAGE_PATH = "sd/image.jpg"
try:
    stat(IMAGE_PATH)
except OSError:
    print("Image not found on SD card: {}".format(IMAGE_PATH))
    print("Copy an image to that path on the SD card, or change IMAGE_PATH above.")
else:
    inkplate.draw_image(
        IMAGE_PATH,
        0,
        0,
        invert=False,
        dither=True,
        kernel_type=Inkplate.KERNEL_FLOYD_STEINBERG,
    )

# Show the image from the buffer
inkplate.display()

inkplate.sd_card_sleep()
# To turn it back on, use:
# inkplate.sd_card_wake()
```

<FunctionDocumentation
functionName="inkplate.draw_image()"
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


<CenteredImage src="/img/inkplate6flick-micropython/imgsd.jpg" alt="Inkplate 6FLICK running the example code" caption="Displaying an image from SD card." width="1000px" />