---
slug: /inputronic_bridge/arduino/getting-started 
title: Inputronic BRIDGE - Getting started
sidebar_label: Getting started
id: inputronic_bridge-arduino-1 
hide_title: False
---

## Arduino library

To install the Arduino library, you can use the **Arduino Library Manager** or download it directly from the GitHub repository:

<QuickLink
  title="Soldered Inputronic BRIDGE Library"
  description="Parses keyboard, mouse, MIDI, descriptor, and raw HID events from the Inputronic BRIDGE over UART, I²C, or SPI"
  url="https://github.com/SolderedElectronics/Soldered-Inputronic-BRIDGE-Library"
/>

<InfoBox>

**First time Arduino user?** For a detailed tutorial on how to get started with Arduino, see this section of our docs:

<QuickLink
  title="Getting started with Arduino"
  description="A full, comprehensive tutorial on how to fully set up and upload code for the first time on an Arduino board, from scratch!"
  url="/arduino/quick-start-guide"
/>

</InfoBox>

---

## Connections

| **NULA DeepSleep ESP32-S3** | **Breakout Board** |
| ---------------------------- | ------------------- |
| Qwiic                         | Qwiic               |

---

## Using UART or SPI instead

The BRIDGE can output the same events over UART or SPI if I²C doesn't suit your project. Bridge jumper **JP3** for UART, or **JP4** for SPI, and wire up the matching pins from the 14-pin header, RX/TX for UART or MISO/MOSI/SCK/CS for SPI. See the [hardware details](/inputronic_bridge/hardware) page for the full jumper table. Whichever protocol you choose, pass the matching constant to the library's `begin()` function, covered on the next page.
