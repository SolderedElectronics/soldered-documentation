---
slug: /bhi385/overview
title: BHI385 – Overview
sidebar_label: Overview
id: bhi385-overview
hide_title: False
pagination_prev: null
---

## BHI385 Smart IMU Breakout

**BHI385 Smart IMU Breakout** is a compact board built around Bosch Sensortec's **BHI385**, an ultra-low-power, fully programmable smart sensor that integrates a **6-DoF IMU** (3-axis accelerometer + 3-axis gyroscope) with an on-chip **32-bit ARC EM4 processor (Fuser2)**. Unlike a conventional IMU, the BHI385 runs a complete sensor fusion firmware on-device — the **BSX sensor fusion library** — producing high-level **virtual sensor outputs** such as orientation quaternions, step counts, tap detection, and wrist gestures directly, without loading the host processor.

The board includes an **onboard 1.8V LDO** so it runs from a standard 3.3V supply, a built-in **I2C level shifter** for 3.3V host compatibility, and **two Qwiic (formerly easyC) connectors** for solderless plug-and-play integration.

<CenteredImage src="/img/bhi385/333375.jpg" alt="BHI385 Smart IMU Breakout" caption="BHI385 Smart IMU Breakout" />

---

## Which products is this documentation for?

<QuickLink
  title="BHI385 Smart IMU Breakout"
  description="333375"
  url="https://solde.red/333375"
  image="/img/bhi385/333375.jpg"
/>

---

## Key Features

- **Measurement range:**
  - **Accelerometer:** ±4 / ±8 / ±16 / ±32 g
  - **Gyroscope:** ±125 / ±250 / ±500 / ±1000 / ±2000 dps
- **Virtual sensor outputs (firmware-generated):** orientation quaternion, step counter, tap detection (single/double/triple), wrist gesture detection, and more
- **On-chip processor:** 32-bit ARC EM4 (Fuser2) running Bosch BSX sensor fusion library
- **Ultra-low power consumption:**
  - Sleep mode: ~5 µA
  - Accelerometer only (low-power): ~200 µA
  - Accelerometer + Gyroscope (normal mode): ~1.4 mA
- **Operating voltage:** 3.3V (onboard LDO generates 1.8V for the BHI385 chip)
- **Communication:** I2C (up to 400 kHz), with onboard level shifter for 3.3V compatibility
- **I2C addresses:** 0x29 (default) / 0x28 (selectable via JP5 jumper)
- **Connector:** 2 × **Qwiic (formerly easyC) ports** (plug-and-play, no soldering needed)
- **Mounting:** Two mounting holes for secure attachment (M3, 3.2 mm diameter)
- **Dimensions:** 23 × 23 mm (0.9 × 0.9 inch)

---

## You may also need

<QuickLink
  title="Qwiic cable"
  description="Qwiic (formerly easyC) compatible cables with connectors on both ends, available in various lengths."
  url="https://soldered.com/product/easyc-cable/"
  image="/img/333311.webp"
/>
