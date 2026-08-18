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

SPI is disabled by default. The module ships in **I2C + UART** mode, and the SDA/SCL/TX/RX pins only switch to SPI functions once you re-bridge the selectable **JP4** jumper on the board to its other position (see [Hardware details](/neo-m9n-00b/hardware) for more on this jumper). With JP4 re-bridged:

| **NULA Deepsleep**      | **NEO-M9N-00B** |
| ------------------------- | ---------------- |
| IO10 (Default CS pin)     | SDA / SPI CS      |
| IO11 (Default MOSI pin)   | RX / SPI MOSI     |
| IO13 (Default MISO pin)   | TX / SPI MISO     |
| IO12 (Default SCK pin)    | SCL / SPI SCK     |
| 3V3                       | 3V3               |
| GND                       | GND               |

<InfoBox>

SPI communication won't work until **JP4** is re-bridged to its SPI position. Left at its default position, the module stays in I2C + UART mode and ignores anything sent over these pins as SPI.

</InfoBox>

<InfoBox>

Re-bridging JP4 is not enough by itself. You must also open the module in **u-center** and set the SPI port's input/output protocol to **UBX only**, otherwise it will not respond to commands over SPI, even with the jumper and wiring correct. See [Configuring the module with u-center](#configuring-the-module-with-u-center) below.

</InfoBox>

---

## Configuring the module with u-center

<QuickLink
  title="u-center"
  description="u-blox's free desktop application for configuring, monitoring, and debugging u-blox GNSS receivers"
  url="https://www.u-blox.com/en/product/u-center"
/>

u-center connects to the module over UART or a USB-to-serial adapter and shows you live satellite data, message traffic, and every configuration option the module supports. You don't need it for normal I2C or UART use since the library configures everything from your sketch, but it's required to get SPI working, and useful for a few other things too:

- **Getting SPI working (required)** - the SPI port's protocol must be set explicitly to UBX, or the module will not respond over SPI. In u-center, open **View → Messages View**, go to **UBX → CFG → PRT**, select the **SPI** target port, and set both **In Protocol** and **Out Protocol** to **UBX** only, then click **Send**. Use **CFG → CFG** to save the setting to the module's flash so it persists after a power cycle.
- **Watching raw satellite data** - the **Messages View** shows UBX and NMEA messages as they arrive, which is useful for confirming the module is actually receiving data before you start debugging your own code.
- **Changing constellation or update-rate settings** - anything you'd otherwise set with library calls like `myGNSS.setNavigationFrequency()` can be tested interactively first.

<InfoBox>u-center only runs on Windows and needs a serial connection (UART or USB-to-serial), so connect over one of those interfaces for configuration even if you plan to use SPI or I2C in your actual project.</InfoBox>