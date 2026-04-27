---
slug: /barcode-scanner-de2120/arduino/getting-started
title: DE2120 Barcode Scanner Getting Started
sidebar_label: Getting started
id: barcode-scanner-de2120-arduino-1
hide_title: true
---

# Getting started

## Arduino library

To install the Arduino library, you can use the **Arduino Library Manager** or download it directly from GitHub:

<QuickLink
  title="DE2120 2D Barcode Scanner Arduino Library"
  description="DE2120 Arduino library by Soldered"
  url="https://github.com/SolderedElectronics/Soldered-Barcode-Scanner-DE2120-Arduino-Library"
/>

<InfoBox>

**Are you a first-time Arduino user?** For a detailed tutorial on getting started with Arduino, refer to this section of our docs:

<QuickLink
  title="Getting started with Arduino"
  description="A comprehensive tutorial on how to set up and upload code to an Arduino board for the first time, from scratch!"
  url="/arduino/quick-start-guide"
/>

</InfoBox>

## Before you begin – set the scanner to TTL mode

<WarningBox>

The DE2120 scanner ships from the factory configured for **USB mode**. Before it will communicate over UART with your microcontroller, you must switch it to **TTL/RS232 mode** by scanning the **POR232** configuration barcode from the DYScan settings manual.

You only need to do this once — the setting is stored in the scanner's non-volatile memory.

</WarningBox>

## Connections

The DE2120 scanner communicates via **UART (TTL serial)**. Connect the scanner's TX to the microcontroller's RX pin, and the scanner's RX to the microcontroller's TX pin.

The examples in this library use **UART2** on the **NULA Mini** (ESP32):

| **NULA Mini** | **DE2120 Breakout Board** |
|--------------------------|---------------------------|
| IO4 (UART2 RX)           | TX                        |
| IO5 (UART2 TX)           | RX                        |
| 3V3                      | VCC                       |
| GND                      | GND                       |

<InfoBox>

You can also use **SoftwareSerial** on any two GPIO pins if UART2 is unavailable. See the `SoftwareScan` example in the library for details. Note that SoftwareSerial is less reliable at higher baud rates.

</InfoBox>
