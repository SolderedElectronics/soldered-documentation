---
slug: /bhi-385-smart-imu-breakout/how-it-works
title: BHI385 Smart IMU – How it works
sidebar_label: How it works
id: bhi-385-smart-imu-breakout-how-it-works
hide_title: false
---

The BHI385 is a **Smart IMU** from [**Bosch Sensortec**](https://www.bosch-sensortec.com/products/smart-sensors/bhi385/) that goes well beyond a conventional MEMS sensor. While talking to a typical accelerometer or gyroscope means reading a pair of registers, communicating with the BHI385 means uploading a firmware binary into the chip's program RAM, enabling virtual sensors by name, and reading processed motion data from a pair of hardware FIFOs. Every meaningful motion output — rotation quaternion, step count, tap event, wrist gesture — is a product of algorithms running on the chip's **internal Fuser2 processor**, not your host microcontroller.

<!-- <CenteredImage src="/img/bhi-385-smart-imu-breakout/bhi-385-smart-imu-breakout_onboard.webp" alt="BHI385 on board" caption="BHI385 Smart IMU on the breakout board" width="400px" /> -->

---

## Datasheet

For full electrical specifications, register maps, and firmware protocol details, refer to the official BHI385 datasheet:

<QuickLink
  title="BHI385 Datasheet"
  description="Complete technical reference for the Bosch BHI385 Smart IMU, including register maps, electrical characteristics, and firmware protocol."
  url="https://www.bosch-sensortec.com/media/boschsensortec/downloads/datasheets/bst-bhi385-ds000.pdf"
/>

---

## How the Smart IMU works

The BHI385 integrates a **6-DOF MEMS inertial unit** — a 3-axis capacitive accelerometer and a 3-axis MEMS gyroscope — alongside a **Fuser2 processor (Synopsys ARC EM4)** inside a single 2.5 × 3.0 mm LGA package. The accelerometer converts physical acceleration into a differential capacitance signal: a proof mass suspended by spring structures shifts position when the chip accelerates, and the capacitance between that mass and fixed electrodes changes in proportion. The gyroscope uses the Coriolis effect — a vibrating structure deflects perpendicular to its oscillation axis when the chip rotates, and that deflection is sensed capacitively. Both signals are digitised by internal ADCs and passed to the Fuser2 core for processing.

What makes the BHI385 a "Smart" IMU is what the firmware does with those raw values. Instead of exposing raw ADC counts, the BHI385 runs a suite of **virtual sensor algorithms** that translate inertial data into application-ready outputs. The **corrected accelerometer and gyroscope** virtual sensors apply calibration coefficients and bias removal. The **Game Rotation Vector** fuses accelerometer and gyroscope data through a sensor-fusion algorithm to produce a normalized quaternion (x, y, z, w) that represents the device's 3D orientation — pitch and roll are gravity-referenced; yaw is relative to power-on orientation since there is no magnetometer. The **step counter** uses an adaptive pedometer algorithm to increment a cumulative count as the sensor detects the characteristic acceleration signature of a footstep. The **multi-tap** and **wrist gesture** detectors classify short impulse patterns or continuous motion trajectories into named events (single tap, double tap, wrist shake, arm flick).

Because the BHI385 has no on-chip flash, none of this firmware persists through a power cycle. The host must transfer the firmware binary — obtained from Bosch Sensortec's SensorAPI — into the chip's program RAM on every power-on before enabling any sensors. The chip's ROM bootloader handles the upload; once it verifies the CRC of the received binary, it boots the Fuser2 core and the firmware brings up all virtual sensor pipelines.

---

## I2C communication and FIFO architecture

The BHI385 uses **I2C** at a default address of **0x29** (HSDO tied high) or **0x28** (HSDO tied low). The board's NMOS-dual level-shifter bridges the chip's 1.8V I2C bus to the 3.3V host interface, so you connect normally to the Qwiic connector or pin header without any additional circuitry.

Unlike most I2C sensors, the BHI385 does not use a simple register map for data. It exposes four **DMA channel registers**:

- **Channel 0 (CMD):** write-only — host sends commands (firmware upload, sensor enable/configure)
- **Channel 1 (FIFO WU):** read-only — wake-up sensor events (tap, gesture, wrist wear)
- **Channel 2 (FIFO NW):** read-only — non-wake-up sensor events (accel, gyro, quaternion, steps)
- **Channel 3 (STATUS):** read-only — firmware status messages and parameter responses

Each FIFO read begins with a 2-byte length header indicating how many bytes of event data follow. The firmware packs multiple sensor events back-to-back in the buffer, each identified by a 1-byte virtual sensor ID. The library's `update()` call drains both FIFOs and dispatches each event to the appropriate internal data field.

<InfoBox>The BHI385 also has an interrupt output (**HIRQ**) that asserts when FIFO data is available. This board exposes the HIRQ signal on the **INT** pin of the 2-pin header, making it straightforward to wire a hardware interrupt to your Dasduino and avoid polling entirely.</InfoBox>
