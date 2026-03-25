---
slug: /bhi385/how-it-works
title: BHI385 – How it works
sidebar_label: How it works
id: bhi385-how-it-works
hide_title: False
---

The **BHI385 Smart IMU Breakout** is built around the [**Bosch Sensortec BHI385**](https://www.bosch-sensortec.com/products/smart-sensor-systems/bhi385/), a fully programmable smart sensor that combines a 6-DoF MEMS IMU (accelerometer + gyroscope) with an on-chip 32-bit ARC EM4 microprocessor. The result is an IMU that performs sensor fusion and activity detection entirely on-device, delivering ready-to-use high-level outputs to the host microcontroller.

---

## Datasheet

For an in-depth look at technical specifications, refer to the official BHI385 datasheet:

<QuickLink
  title="BHI385 Datasheet"
  description="Detailed technical documentation for the Bosch Sensortec BHI385 Smart IMU"
  url="https://www.bosch-sensortec.com/media/boschsensortec/downloads/datasheets/bst-bhi385-ds001.pdf"
/>

---

## How the accelerometer works

The **accelerometer** on the BHI385 measures linear acceleration along three orthogonal axes (X, Y, Z). It works by containing a **tiny proof mass attached to a spring** inside a MEMS structure. When acceleration occurs, the proof mass moves relative to the casing due to inertia, causing the spring to compress or stretch. This displacement is **detected by capacitive sensors**, which convert the **mechanical movement into electrical signals**. These signals are processed on-chip to produce calibrated acceleration values in units of g (gravitational force). The BHI385 supports full-scale ranges from **±4 g to ±32 g**.

---

## How the gyroscope works

The **gyroscope** on the BHI385 measures angular rate (rotational velocity) along the same three axes. It operates by containing tiny vibrating MEMS structures that experience the **Coriolis force** when the sensor is rotated. This force deflects the vibrating mass, and the deflection is **detected by capacitive sensors** and converted into an **electrical signal** proportional to the rotation rate. The processed output is given in degrees per second (dps), with full-scale ranges from **±125 dps to ±2000 dps**.

---

## The Fuser2 processor and virtual sensors

What makes the BHI385 unique is its integrated **Fuser2 processor** — a 32-bit ARC EM4 CPU running inside the sensor package. This processor executes the **Bosch BSX sensor fusion library firmware**, which combines accelerometer and gyroscope readings to produce higher-level outputs called **virtual sensors**.

Virtual sensors are software-defined outputs that the firmware calculates from the raw IMU data. Instead of reading raw acceleration and rotation values and doing the math yourself on the host, you simply enable a virtual sensor and the BHI385 delivers the result directly. Examples of virtual sensors supported by the Soldered Arduino library:

| Virtual Sensor | Description |
|----------------|-------------|
| **Accelerometer** | Calibrated linear acceleration (g), X/Y/Z |
| **Gyroscope** | Calibrated angular rate (dps), X/Y/Z |
| **Game Rotation Vector** | Normalized orientation quaternion (accel + gyro fusion, no magnetometer) |
| **Step Counter** | Cumulative step count |
| **Single / Double Tap** | Tap detection with configurable sensitivity |
| **Wrist Gesture Detect** | Wrist shake, arm flick in / arm flick out |

---

## Firmware upload

The BHI385 requires a **firmware binary** to be uploaded to its RAM on every power-on — without it, the virtual sensors cannot be activated. The firmware is provided by Bosch Sensortec as part of the [BHI385 SensorAPI](https://github.com/boschsensortec/BHI3_SensorAPI).

<InfoBox>

When using the **Soldered Arduino library**, firmware upload is handled automatically by calling `imu.loadFirmware()` in your `setup()` function. You just need to obtain the firmware header file (`BHI385_firmware.h`) from Bosch Sensortec and place it in your Arduino sketch folder. The library uploads it over I2C every time the board powers on — the process takes approximately **1.3 seconds** at 400 kHz or **~5 seconds** at the default 100 kHz.

</InfoBox>

---

## I2C communication

The BHI385 communicates with the host microcontroller over **I2C**. On the Soldered breakout, an onboard **NMOS dual level shifter** translates between the BHI385's 1.8V I2C signals and the standard **3.3V** host logic level.

The BHI385 uses a **channel-based FIFO protocol** rather than simple register reads. The host writes commands to channel 0 and reads sensor data from channels 1–3 (FIFO buffers). The Soldered Arduino library handles all FIFO management internally.

**I2C address:**
- **0x29** — default (JP5 bridged to 0x29 pad, default from factory)
- **0x28** — alternate (move JP5 solder bridge to the 0x28 pad)

**I2C speed:**
- Standard: 100 kHz
- Fast mode: **400 kHz** (recommended — significantly reduces firmware upload time)

---

## Measurement process

1. **Power-up**
   The BHI385 bootloader initializes. The host interface becomes ready within ~5 ms.

2. **Firmware upload**
   The host uploads the BSX firmware binary over I2C (channel 0). The BHI385 CRC-verifies the binary and boots into firmware mode (~500 ms after upload).

3. **Enable virtual sensors**
   The host sends commands to activate individual virtual sensors at the desired output data rate and range.

4. **Data retrieval**
   The BHI385 continuously fills its internal FIFO buffers with sensor events. The host calls `update()` (polling or interrupt-driven) to drain the FIFO and parse the latest values. Updated flags indicate which sensors produced new data.
