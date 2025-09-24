---  
slug: /inkplate/6color/micropython/microsd/formatting
title: Inkplate 6COLOR – Formatting MicroSD
sidebar_label: Formatting
id: microsd-formatting
hide_title: true
---

<SectionTitle title="Formatting MicroSD" backgroundImage="img/arduino_bg.jpg" />

Built in microSD card slot on the back of Inkplate 6COLOR can be a great asset for your projects, either for storing a very large number of high-quality images which can be displayed or reading and writing data between deep sleep cycles. This page walks through microSD initialization and image display.

<WarningBox>All supported card formats are: **FAT16, FAT32, exFAT**</WarningBox>

<WarningBox>All supported card types are: **SD, SDHC and SDXC**</WarningBox>

---

## Preparing the microSD card before usage

For best results, use the [**official SD card formatter**](https://www.sdcard.org/downloads/formatter/) to format the card to **FAT32** before usage.

<CenteredImage src="/img/inkplate10/sdcard_formatter.png" alt="Official SD card formatter" caption="The official SD Card formatter" width="400px" />

---

## Initialization

Before the microSD card can be used, it must first be initialized. This powers on the microSD card circuitry and performs all the necessary memory allocations:

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
```

<FunctionDocumentation
    functionName="inkplate.initSDCard()"
    description="Initializes SD card through SPI"
    parameters={[
        { type: "bool", name: "fastBoot", description: "If True, performs a soft reboot immediately after SD card initialization (only on cold start or hard reset) which significantly improves SD card read speeds." }
    ]}
/>