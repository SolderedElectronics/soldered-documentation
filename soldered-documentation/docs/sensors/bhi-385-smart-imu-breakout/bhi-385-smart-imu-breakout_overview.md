---
slug: /bhi-385-smart-imu-breakout/overview
title: BHI385 Smart IMU - Overview
sidebar_label: Overview
id: bhi-385-smart-imu-breakout-overview
hide_title: false
pagination_prev: null
---

## BHI385 Smart IMU Breakout

The **BHI385 Smart IMU Breakout** is built around Bosch Sensortec's BHI385 — a programmable Smart IMU that combines a 6-DOF inertial measurement unit (3-axis accelerometer + 3-axis gyroscope) with an internal Fuser2 processor (Synopsys ARC EM4) that runs sensor-fusion firmware. Instead of delivering only raw sensor counts, the BHI385 runs multiple **virtual sensor algorithms** simultaneously: a Game Rotation Vector (quaternion orientation), a low-power step counter, multi-tap detection (single, double, and triple), and wrist gesture recognition — all computed on-chip, freeing up your microcontroller for other work. The board communicates over **I2C** at an address of **0x29** by default (or **0x28** via jumper), manages its own 1.8V power domain with an onboard LDO regulator, and includes a bidirectional I2C level-shifter so it is directly compatible with 3.3V systems. Two **Qwiic (formerly easyC) connectors** let you connect it to a Dasduino without soldering a wire.

<!-- <CenteredImage src="/img/bhi-385-smart-imu-breakout/333375.jpg" alt="BHI385 Smart IMU Breakout" caption="BHI385 Smart IMU Breakout" /> -->

---

## Which products is this documentation for?

<QuickLink 
  title="BHI385 Smart IMU Breakout" 
  description="333375"
  url="https://soldered.com/product/bhi385-smart-imu-breakout/"
  image="/img/bhi-385-smart-imu-breakout/333375.webp" 
/>

---

## Key Features

- **6-DOF IMU:** 3-axis accelerometer + 3-axis gyroscope  
- **Accelerometer range:** ±4g / ±8g / ±16g / ±32g (configurable)  
- **Gyroscope range:** ±125 / ±250 / ±500 / ±1000 / ±2000 deg/s (configurable)  
- **Onboard Fuser2 processor (Synopsys ARC EM4):** runs sensor-fusion firmware uploaded at every power-on  
- **Virtual sensors:** Game Rotation Vector (quaternion), step counter, multi-tap detect, wrist gesture detect  
- **Communication:** I2C (default address **0x29**, selectable to **0x28** via JP5 jumper)  
- **Supply voltage:** **3.3V** (onboard SE5218DLG-LF LDO generates 1.8V for the BHI385)  
- **Logic level:** 3.3V (onboard NMOS-dual level-shifter bridges the 1.8V I2C bus)  
- **Connectors:** 2 × **Qwiic (formerly easyC) ports** — plug-and-play, no soldering needed  
- **Interrupt output:** HIRQ pin exposed on a dedicated 2-pin header  
- **Mounting:** Two M3 screw holes  
- **Dimensions:** 22 × 22 mm  

---

## You may also need

<QuickLink 
  title="Qwiic cable" 
  description="Qwiic (formerly easyC) compatible cables with connectors on both ends, available in various lengths."
  url="https://soldered.com/product/easyc-cable/"
  image="/img/333311.webp" 
/>
