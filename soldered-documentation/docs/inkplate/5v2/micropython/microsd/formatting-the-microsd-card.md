---
slug: /inkplate/5v2/micropython/microsd/formatting-the-microsd-card
title: Inkplate 5v2 MicroPython - Formatting the microSD card
sidebar_label: Formatting the microSD card
id: formatting-the-microsd-card
---

The bulit-in microSD card slot on the back of Inkplate 5v2 can be a great asset for your projects, either for storing a very large number of high-quality images which can be displayed or reading and writing data between deep sleep cycles.

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
from inkplate5v2 import Inkplate
import time
from os import listdir

inkplate=Inkplate(Inkplate.INKPLATE_1BIT)
inkplate.begin()

# Note:
# - This function must be called before accessing files on the SD card.
# - The fastboot option has no effect if the device is already running.
inkplate.initSDCard(fastBoot=True)

inkplate.SDCardSleep()

```

<FunctionDocumentation
  functionName="inkplate.initSDCard()"
  description="Initialize the onboard microSD card interface, allowing images, fonts, and data files to be loaded from the SD card."
  returnDescription="Boolean — True if the SD card was successfully initialized, otherwise False."
  parameters={[
    { type: 'Boolean', name: 'fastBoot', description: 'Optional. If True (default), use faster initialization to reduce startup time.' }
  ]}
/>

<FunctionDocumentation 
functionName="inkplate.SDCardSleep()" 
description="Puts the microSD card circuitry into low-power sleep mode to save energy when the card is not in use." 
/>