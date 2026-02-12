---
slug: /inkplate/13/microsd/sd-basics
title: Inkplate 13SPECTRA – MicroSD basics
sidebar_label: MicroSD basics
id: 13spectra-microsd-basics
hide_title: true
---

<SectionTitle title="MicroSD basics" backgroundImage="/img/microsd.jpg" />

The built-in microSD card slot on Inkplate 13SPECTRA can be of great use for your project. It can store a very large number of quality image files to be displayed and read and write data between deep sleeps. This page contains basic examples which will help you quickly get started with using the built-in microSDs card slot.

[IMAGE PLACEHOLDER - sdcard slot on 13spectra highlighted]

<InfoBox>Inkplate 13SPECTRA  uses the [**SdFat library**](https://github.com/greiman/SdFat)</InfoBox>
<WarningBox>All supported card formats are: **FAT16, FAT32, exFAT**</WarningBox>
<WarningBox>All supported card types are: **SD, SDHC and SDXC**</WarningBox>

---

## Preparing the microSD card before usage

For best results, use the [**official SD card formatter**](https://www.sdcard.org/downloads/formatter/) to format the card to **FAT32** before usage.

<CenteredImage src="/img/inkplate10/sdcard_formatter.png" alt="Official SD card formatter" caption="The official SD Card formatter" width="400px" />

---

## Initializing

Before the microSD card can be used in code, it must first be initialized, this powers on the microSD card circutry and does all the necessary memory allocations. In this code snipper, the microSD card is initialized and the result of the initialization is checked:

```python
from inkplate13SPECTRA import Inkplate
import time
from os import listdir

inkplate=Inkplate()
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