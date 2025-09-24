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