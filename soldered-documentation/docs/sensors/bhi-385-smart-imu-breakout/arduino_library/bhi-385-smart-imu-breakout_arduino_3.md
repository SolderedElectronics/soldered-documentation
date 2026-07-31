---
slug: /bhi-385-smart-imu-breakout/arduino/firmware-types
title: Firmware variants
sidebar_label: Firmware variants
id: bhi-385-smart-imu-breakout-arduino-3
hide_title: false
pagination_next: null
---

The BHI385 IMU chip can handle processing directly on-board, which is why Bosch Sensortec offers several firmware variants tailored for different projects. You can find the full list of firmware versions in their [**GitHub repository**](https://github.com/boschsensortec/BHI385_SensorAPI/tree/master/firmware/bhi385).

---

## Understanding the Firmware Names

Here is how to read a firmware file name, using `Bosch_Shuttle3_BHI385_BMM350C_bsxsam_ndof.fw.h` as an example:

- `Bosch_Shuttle3_BHI385`: Designed for the Bosch Shuttle Board 3.0 with the BHI385 as the primary sensor.
- `_BMM350C` (or BMP58X, BME688): Supports external slave sensors connected directly to the BHI385.
- `_bsxsam` (or `*_lite`, `*_turbo`, `*_lite_Klio`): Includes the full Bosch BSX Sensor Fusion library. It does all the math to turn raw sensor data into clean, usable physical orientation tracking.
  <InfoBox>`*_Klio` offers the Klio machine learning engine to learn repetitive motions and recognize activities, like gym exercises.</InfoBox>
- `_ndof`: N-degrees of Freedom. This usually means 9-DoF absolute orientation fusion if you connect the BMM350 magnetometer.
- `.fw.h` (.fw): A C/C++ header version of the binary file, wrapped in a `const unsigned char` array so you can include it directly in your Arduino or embedded projects.

---

## Choosing the Right Firmware

You can change the BHI385's firmware depending on what your project needs.

| Firmware variant | Use when...                                                                               |
| ---------------- | :---------------------------------------------------------------------------------------- |
| bsxsam_lite      | You only need accelerometer and gyroscope. It saves the most memory (smallest footprint). |
| bsxsam           | You want accelerometer and gyroscope data combined with full BSX sensor fusion.           |
| bsxsam_turbo     | You need a high output data rate (up to 800 Hz) with BSX fusion.                          |
| bsxsam_lite_Klio | You need accelerometer, gyroscope, and Klio motion pattern recognition.                   |

---

## Writing Your Own Firmware

Why write custom firmware? You might want to create your own firmware if you need to:

- **Create a virtual sensor**: Calculate specific metrics directly on the chip, like golf swing angles or precise vibration patterns.
- **Connect unsupported hardware**: Write custom drivers for new external sensors connected to the BHI385's master I2C or SPI pins.
- **Free up your main microcontroller**: Move heavy math and filtering from your ESP32 or STM32 to run entirely inside the low-power BHI385.

To build your own firmware, you will need Bosch's official development tools:

1. **Bosch BHI3xx SDK (Software Development Kit)**: A C-based development kit with the framework, RTOS headers, and drivers.
2. **ARC GNU Toolchain**: Required because the BHI385 runs on a Synopsys ARC EM4 architecture. You can download it [**here**](https://github.com/foss-for-synopsys-dwc-arc-processors/toolchain/releases).
3. **Bosch Motion AI Studio**: Use this to design, train, and run custom machine learning models (like gesture recognition) directly on the sensor.

For a step-by-step guide, check out the [**BHI3xx SDK Quick Start Guide**](https://www.bosch-sensortec.com/media/boschsensortec/downloads/application_notes_1/bst-bhi3xx-an000.pdf).
