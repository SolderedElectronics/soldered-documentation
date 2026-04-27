---
slug: /iis2dulpx/overview
title: Overview
id: iis2dulpx-overview 
hide_title: False
pagination_prev: null
---

## IIS2DULPX Accelerometer breakout

The **IIS2DULPX Accelerometer Breakout** is a compact board built around the **IIS2DULPX** — an ultra-low-power 3-axis MEMS accelerometer from **STMicroelectronics**. It is capable of measuring acceleration across four selectable full-scale ranges (±2g, ±4g, ±8g, ±16g) and supports output data rates from **1.6 Hz up to 800 Hz**, with three distinct power modes: Ultra Low Power, Low Power, and High Performance.

Beyond standard motion sensing, the IIS2DULPX also integrates a **QVAR (charge variation)** sensing channel, enabling applications such as capacitive touch detection, liquid level sensing, or electric field detection. On-chip features include **wake-up detection**, **free-fall detection**, **single/double tap recognition**, **6D/4D orientation detection**, **step counting**, **tilt detection**, and **configurable FIFO buffering** for efficient data management.

The board includes **2 Qwiic (formerly easyC) connectors**, making it easy to daisy-chain with other I2C peripherals and eliminating the need for soldering.

<CenteredImage src="/img/iis2dulpx/DSC01008.png" alt="IIS2DULPX Accelerometer breakout" caption="IIS2DULPX Accelerometer breakout" />

---

## Which products is this documentation for?

<QuickLink
  title="IIS2DULPX Accelerometer breakout"
  description="333363"
  url="https://soldered.com/products/iis2dulpx-accelerometer-breakout"
  image="/img/iis2dulpx/DSC01008.png"
/>

---

## Key Features

- **Measurement range:** ±2g / ±4g / ±8g / ±16g (selectable)
- **Output data rate:**
  - Ultra Low Power mode: 1.6 Hz, 3 Hz, 25 Hz
  - Low Power mode: 6 Hz to 800 Hz
  - High Performance mode: 6 Hz to 800 Hz
- **Sensitivity:** 0.061 mg/LSB (±2g) to 0.488 mg/LSB (±16g)
- **QVAR sensing:** On-chip charge variation sensing for touch and electric field detection
- **On-chip features:** Wake-up, free-fall, tap/double-tap, 6D/4D orientation, step counter, tilt, sleep detection
- **FIFO buffer:** Configurable FIFO for efficient data batching
- **Communication:** I2C (address **0x18**)
- **IC supply voltage:** 1.62V to 3.6V (onboard regulator provides 5V compatibility)
- **Power consumption:** 3 µA (ULP) / 6.5 µA (LP) / 9.3 µA (HP) / 12 nA (deep power-down)
- **Connector:** 2 × **Qwiic (formerly easyC) ports** (plug-and-play, no soldering needed)
- **Mounting:** Two mounting holes for secure attachment

---

## You may also need

<QuickLink
  title="Qwiic cable"
  description="Qwiic (formerly easyC) compatible cables with connectors on both ends, available in various lengths."
  url="https://soldered.com/product/easyc-cable/"
  image="/img/333311.webp"
/>
