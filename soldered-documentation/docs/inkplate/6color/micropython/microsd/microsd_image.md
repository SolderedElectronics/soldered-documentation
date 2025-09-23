---  
slug: /inkplate/6color/micropython/microsd/image-display
title: Inkplate 6COLOR – MicroSD Display Image
sidebar_label: MicroSD Display Image
id: image-display
hide_title: true
---

<SectionTitle title="MicroSD Display Image" backgroundImage="img/arduino_bg.jpg" />

Built in microSD card slot on the back of Inkplate 6COLOR can be a great asset for your projects, either for storing a very large number of high-quality images which can be displayed or reading and writing data between deep sleep cycles. This page walks through microSD initialization and image display.

<InfoBox>Inkplate 6COLOR uses the [**SdFat library**](https://github.com/greiman/SdFat)</InfoBox>

<WarningBox>All supported card formats are: **FAT16, FAT32, exFAT**</WarningBox>

<WarningBox>All supported card types are: **SD, SDHC and SDXC**</WarningBox>

---

## Display Image from SD card

<InfoBox>Supported image formats: JPG, BMP, and PNG.</InfoBox>

Before the microSD card can be used, it must first be initialized. This powers on the microSD card circuitry and performs all the necessary memory allocations.

```python
from inkplate6COLOR import Inkplate

from os import listdir

# Create Inkplate object
inkplate = Inkplate()

# Initialize the display, needs to be called only once
inkplate.begin()

# Initialize the SD card.
# This function must be called before accessing files on the SD card.
# The fastboot option has no effect if the device is already running.
inkplate.initSDCard(fastBoot=True)

# This prints all the files on card
print(listdir("/sd"))
inkplate.drawImage("sd/coastal.jpg", 0, 0, invert=False, dither=True, kernel_type=Inkplate.KERNEL_FLOYD_STEINBERG)

# Show the image from the buffer
inkplate.display()

inkplate.SDCardSleep()
# To turn it back on, use:
# inkplate.SDCardWake()
```

<CenteredImage src="/img/6color/6color-sd-mp.jpg" alt="Expected output on Inkplate display" caption="Example image from sd card" />

<FunctionDocumentation
    functionName="inkplate.initSDCard()"
    description="Significantly improves SD card read speeds"
    parameters={[
        { type: "bool", name: "fastBoot", description: "If True, performs a soft reboot immediately after SD card initialization (only on cold start or hard reset)." }
    ]}
/>