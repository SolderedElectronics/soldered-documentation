---
slug: /bhi385/arduino/geting-started
title: BHI385 – Getting started
sidebar_label: Getting started
id: bhi385-arduino-1
hide_title: False
---

## Arduino library

To install the Arduino library, you can use the **Arduino Library Manager** (search for **Soldered BHI385 IMU**) or download it directly from the GitHub repository:

<QuickLink
  title="Soldered BHI385 IMU Arduino library"
  description="Soldered-BHI385-Arduino-Library"
  url="https://github.com/SolderedElectronics/Soldered-BHI385-Arduino-Library"
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

## Firmware binary

<WarningBox>

**The BHI385 requires a firmware binary to be uploaded on every power-on.** The Soldered library does not bundle the firmware due to licensing — you need to obtain it from Bosch Sensortec:

1. Download the BHI385 SensorAPI from the [Bosch Sensortec GitHub](https://github.com/boschsensortec/BHI3_SensorAPI).
2. Locate the firmware header file (e.g. `BHI385_firmware.h`) in the firmware folder.
3. Copy that file into your Arduino sketch folder (same directory as your `.ino` file).
4. Include it at the top of your sketch: `#include "BHI385_firmware.h"`

Without this file the examples will not compile.

</WarningBox>

---

## Connections

Below is an example connection diagram for **Dasduino CONNECTPLUS**. These pins will be used in the examples throughout this documentation.

| **Dasduino CONNECTPLUS** | **BHI385 Breakout Board** |
| ------------------------ | ------------------------- |
| Qwiic                    | Qwiic                     |

<InfoBox>

If you prefer, you can use I2C pins to manually connect:

| **Dasduino CONNECTPLUS** | **BHI385 Breakout Board** |
| ------------------------ | ------------------------- |
| IO21 (Default SDA pin)   | SDA                       |
| IO22 (Default SCL pin)   | SCL                       |
| 3V3                      | 3V3                       |
| GND                      | GND                       |

</InfoBox>

<WarningBox>The **IO21** and **IO22** pins can differ for your personally used board, so **make sure to validate** the information before you start working!</WarningBox>
