---
slug: /neo-m9n-00b/arduino/geting-started 
title: NEO-M9N-00B - Getting started
sidebar_label: Getting started
id: neo-m9n-00b-arduino-1 
hide_title: False
---

## Arduino library

To install the Arduino library, use the **Arduino library manager** or download it from the GitHub repository:
<QuickLink  
  title="GPS Breakout NEO-M9N-00B Arduino library"  
  description="GPS Breakout NEO-M9N-00B Arduino library by Soldered"  
  url="https://github.com/SolderedElectronics/Soldered-u-blox-GPS-GNSS-Arduino-Library"  
/>  

<InfoBox>

**First time Arduino user?** For a detailed tutorial on getting started with Arduino, see this section of our docs:

<QuickLink  
  title="Getting started with Arduino"  
  description="A full, comprehensive tutorial on how to fully set up and upload code for the first time on an Arduino board, from scratch!"  
  url="/arduino/quick-start-guide"  
/>  

</InfoBox>

---

## Connections

The NEO-M9N-00B can be wired for **I2C, UART, or SPI**. Pick the interface that fits your project. All three share the same physical pins on the module (SDA/SCL/TX/RX double as SPI signals), so you only need to wire up the one you're actually using.

### I2C (recommended, default)

The simplest way to connect is over **Qwiic**, since I2C and UART are both active out of the box, no jumper changes needed:

| **NULA Deepsleep** | **NEO-M9N-00B** |
| ------------------- | ---------------- |
| Qwiic                | Qwiic             |

<InfoBox>

If you prefer, you can wire the I2C pins manually instead:

| **NULA Deepsleep** | **NEO-M9N-00B** |
| ------------------- | ---------------- |
| IO8 (Default SDA pin) | SDA               |
| IO9 (Default SCL pin) | SCL               |
| 3V3                   | 3V3               |
| GND                   | GND               |

</InfoBox>

### UART

UART is also enabled by default, alongside I2C, no jumper changes needed. Cross-connect the TX and RX lines:

| **NULA Deepsleep** | **NEO-M9N-00B** |
| ------------------- | ---------------- |
| IO43 (TX)             | RX                |
| IO44 (RX)             | TX                |
| 3V3                   | 3V3               |
| GND                   | GND               |

### SPI

SPI is disabled by default. The module ships in **I2C + UART** mode, and the SDA/SCL/TX/RX pins only switch to SPI functions once you close the **JP4** jumper on the board (see [Hardware details](/neo-m9n-00b/hardware) for more on this jumper). With JP4 closed:

| **NULA Deepsleep**      | **NEO-M9N-00B** |
| ------------------------- | ---------------- |
| IO10 (Default CS pin)     | SDA / SPI CS      |
| IO11 (Default MOSI pin)   | RX / SPI MOSI     |
| IO13 (Default MISO pin)   | TX / SPI MISO     |
| IO12 (Default SCK pin)    | SCL / SPI SCK     |
| 3V3                       | 3V3               |
| GND                       | GND               |

<WarningBox>

SPI communication won't work until **JP4** is closed. With JP4 left open (the default), the module stays in I2C + UART mode and ignores anything sent over these pins as SPI.

</WarningBox>