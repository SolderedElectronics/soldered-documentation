---
slug: /inkplate/5v2/micropython/microsd/draw-image-from-microsd-card
title: Inkplate 5v2 MicroPython - Draw Image from microSD card
sidebar_label: Draw Image from microSD card
id: draw-image-from-microsd-card
---

Inkpalte 5v2 can load and render images directly from the onboard microSD card. This example shows how to initialize the SD card, list its contents and display a JPEG, PNG or BMP image on screen.

---

## Displaying an image from the SD card

Before running this example, make sure your SD card is formatted as **FAT16, FAT32 or exFAT** and inserted into Inkplate 10.
To learn how to format the microSD card click [**here**](/documentation/inkplate/10/micropython/microsd/formatting-the-microsd-card/#preparing-the-microsd-card-before-usage)

The picture used in the example can be downloaded directly from the [Inkplate MicroPython Library](https://github.com/SolderedElectronics/Inkplate-micropython/blob/master/Examples/Inkplate10/displayImageSd/mountain.jpg).

```python
from inkplate5v2 import Inkplate
import time
from os import listdir

inkplate = Inkplate(Inkplate.INKPLATE_2BIT)
inkplate.begin()
inkplate.initSDCard(fastBoot=True)
print(listdir("/sd"))

# Draw image onto the buffer
drawLength = time.ticks_ms()
inkplate.drawImage(
    "sd/mountain.jpg",
    0, 0,
    invert=False,
    dither=True,
    kernel_type=Inkplate.KERNEL_FLOYD_STEINBERG
)
drawLength = time.ticks_ms() - drawLength
print("Time it took to draw to buffer: {} ms".format(drawLength))
inkplate.display()

# Put SD card interface to sleep
inkplate.SDCardSleep()
# To wake it again, use: inkplate.SDCardWake()
```

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


<CenteredImage src="/img/inkplate5v2-micropython/imgweb.jpg" alt="Inkplate 5v2 running the example code" caption="Displaying an image from SD card." width="1000px" />