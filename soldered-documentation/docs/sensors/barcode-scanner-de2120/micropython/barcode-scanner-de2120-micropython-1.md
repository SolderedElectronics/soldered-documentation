---
slug: /barcode-scanner-de2120/micropython/getting-started
title: DE2120 Barcode Scanner - Getting started (MicroPython)
sidebar_label: Getting started
id: barcode-scanner-de2120-micropython-1
hide_title: false
---

## MicroPython module

To install the MicroPython module, download it from the GitHub repository:

<QuickLink
    title="Soldered DE2120 Barcode Scanner MicroPython module"
    description="A MicroPython module for the Soldered DE2120 Barcode Scanner breakout"
    url="https://github.com/SolderedElectronics/Soldered-MicroPython-Modules/tree/main/DE2120"
/>

<InfoBox>

**First time MicroPython user?** For a detailed tutorial on how to get started with MicroPython, see this section of our docs:

<QuickLink
    title="Getting started with MicroPython"
    description="A comprehensive tutorial on how to set up and upload code for the first time on a MicroPython board from scratch!"
    url="/micropython/getting-started-with-vscode/"
/>

</InfoBox>

---

## Before you begin – set the scanner to TTL mode

<WarningBox>

The DE2120 scanner ships from the factory configured for **USB mode**. Before it will communicate over UART with your microcontroller, you must switch it to **TTL/RS232 mode** by scanning the **POR232** configuration barcode from the DYScan settings manual.

You only need to do this once — the setting is stored in the scanner's non-volatile memory.

</WarningBox>

---

## Connections

Below is an example connection diagram for **Dasduino CONNECTPLUS**. These pins will be used in the examples throughout this documentation.

| **Dasduino CONNECTPLUS** | **DE2120 Breakout Board** |
|--------------------------|---------------------------|
| IO5 (UART1 TX)           | RX                        |
| IO4 (UART1 RX)           | TX                        |
| 3V3                      | 3V3                       |
| GND                      | GND                       |

<InfoBox>

You can use any two free GPIO pins as the UART TX/RX pair. Pass them as `tx` and `rx` arguments when creating the scanner object. Remember: connect the MCU **TX** pin to the scanner **RX** pin, and the MCU **RX** pin to the scanner **TX** pin.

</InfoBox>

{/*
TODO: Add wiring photo once available
<CenteredImage src="/img/barcode-scanner-de2120/micropython_connection.jpg" alt="DE2120 wiring to Dasduino CONNECTPLUS (MicroPython)" caption="Dasduino CONNECTPLUS connected to the DE2120 barcode scanner breakout board." width="800px"/>
*/}
