---
slug: /inkplate/5v2/micropython/microsd/formatting-the-microsd-card
title: Inkplate 5v2 MicroPython - Formatting the microSD card
sidebar_label: Formatting the microSD card
id: formatting-the-microsd-card
---

The built-in microSD card slot on the back of Inkplate 5v2 is useful for storing a large number of high-quality images to display, or for reading and writing data between deep sleep cycles.

<WarningBox>All supported card formats are: **FAT16, FAT32, exFAT**</WarningBox>

<WarningBox>All supported card types are: **SD, SDHC and SDXC**</WarningBox>

---

## Preparing the microSD card before usage

For best results, use the [official SD card formatter](https://www.sdcard.org/downloads/formatter/sd-memory-card-formatter-for-windows-download/) to format the card to **FAT32** before use.

<CenteredImage src="/img/inkplate10/sdcard_formatter.png" alt="Official SD card formatter" caption="The official SD Card formatter" width="400px" />

---

## Initialization

The microSD card has to be initialized before you can use it. This powers on the microSD card circuitry and performs the necessary memory allocations:

```python
from inkplate5v2 import Inkplate

inkplate=Inkplate(Inkplate.INKPLATE_1BIT)
inkplate.begin()

# Note:
# - This function must be called before accessing files on the SD card.
# - fast_boot performs a soft reboot right after mounting the card, which speeds up
#   later reads. On a cold start the script restarts from the top when it runs, so
#   anything below this line only executes on the second pass. Leave it out if that
#   is not what you want.
inkplate.init_sd_card()

inkplate.sd_card_sleep()

```

<FunctionDocumentation
  functionName="inkplate.init_sd_card()"
  description="Initialize the onboard microSD card interface, allowing images, fonts, and data files to be loaded from the SD card."
  returnType="None"
  returnDescription="Nothing. If the card cannot be read, the error is only printed over serial."
  parameters={[
    { type: 'Boolean', name: 'fast_boot', description: 'Optional, defaults to False. If True, performs a soft reboot right after the card is mounted (only on a cold start or hard reset), which improves later SD read speeds.' }
  ]}
/>

<FunctionDocumentation 
functionName="inkplate.sd_card_sleep()"
returnType="None" 
description="Puts the microSD card circuitry into low-power sleep mode to save energy when the card is not in use." 
/>