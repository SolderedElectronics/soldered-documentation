---
slug: /bhi-385-smart-imu-breakout/arduino/getting-started
title: BHI385 Smart IMU - Getting started
sidebar_label: Getting started
id: bhi-385-smart-imu-breakout-arduino-1
hide_title: false
---

## Arduino library

To install the Arduino library, you can use the **Arduino library manager** or download it from
the GitHub repository:

<QuickLink
  title="Soldered BHI385 IMU Arduino Library"
  description="Arduino library for the Bosch BHI385 Smart IMU: firmware upload, virtual sensor enable/disable, and FIFO-based data readout."
  url="https://github.com/SolderedElectronics/Soldered-BHI385-Arduino-Library"
/>

<InfoBox>

**First time Arduino user?** For a detailed tutorial on how to get started with Arduino, see this
section of our docs:

<QuickLink
  title="Getting started with Arduino"
  description="A full, comprehensive tutorial on how to fully set up and upload code for the first time on an Arduino board, from scratch!"
  url="/arduino/quick-start-guide"
/>

</InfoBox>

---

## Getting the firmware binary

The BHI385 has no internal flash. The sensor firmware must be uploaded from your sketch on every power-on. The firmware binary is distributed by Bosch Sensortec as part of their SensorAPI package and is **not** bundled with this library due to licensing.

To get it:

1. Download the **BHI385 SensorAPI** from [Bosch Sensortec's GitHub](https://github.com/boschsensortec/BHI385_SensorAPI).
2. Inside the package, locate the firmware header file (e.g. `BHI385_firmware.h` or a `.fw.h` variant from the `firmware/` folder).
3. Copy that header file into your Arduino sketch folder alongside your `.ino` file.
4. Include it in your sketch with `#include "BHI385_firmware.h"`.

<WarningBox>Without the firmware header, `loadFirmware()` cannot be called and no virtual sensors will produce data. Make sure the file is in your sketch folder before uploading.</WarningBox>

---

## Connections

Below is an example connection diagram for **NULA DeepSleep**. These pins will be used in
the examples throughout this documentation.

| **NULA DeepSleep** | **BHI385 Breakout** |
| ------------------------ | ------------------- |
| Qwiic                    | Qwiic               |

