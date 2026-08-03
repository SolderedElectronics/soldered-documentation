---
slug: /i2c-bus-extender-p82b715/overview
title: P82B715 I2C Bus Extender - Overview
sidebar_label: Overview
id: i2c bus extender p82b715-overview
hide_title: false
pagination_prev: null
---

## P82B715 I2C Bus Extender

The **P82B715 I2C Bus Extender** breakout board is based on the **NXP/TI P82B715** chip, a bidirectional I²C bus buffer that extends the range and capacitance limits of standard I²C communication. It gives a **10× impedance transformation**, which reduces the effective bus capacitance seen by each side. That's what lets I²C signals travel over cable runs of up to **50 metres** and drive capacitive loads of up to **3000 pF**, well beyond the standard 400 pF I²C limit.

The board connects to your microcontroller via **Qwiic (3.3V I2C)** on the local side. An onboard **boost converter** steps 3.3V up to 5V to power the P82B715 buffer, and an onboard **level shifter** handles the 3.3V ↔ 5V translation transparently. The extended (remote) side is exposed via a **screw terminal**, making it easy to connect long cables or wired I²C runs.

<WarningBox>Product images are not yet available. We're working on it!</WarningBox>

---

## Which product is this documentation for?

<WarningBox>The webstore link for this product is not available yet! We're working on it. In the meantime, please [**contact us**](https://soldered.com/contact/) for more information.</WarningBox>

---

## Key features

- **Function:** Bidirectional I²C bus buffer and extender
- **Impedance transformation:** 10× reduction in effective bus capacitance
- **Local side:** Supports up to **400 pF** bus capacitance (standard I²C)
- **Extended side:** Supports up to **3000 pF** bus capacitance
- **Max cable length:** Up to **50 m** over standard cabling
- **I²C speed:** Standard-mode (**100 kHz**) and Fast-mode (**400 kHz**)
- **Power input:** **3.3V** via Qwiic (onboard boost converter generates 5V for the buffer)
- **Level shifting:** Onboard 3.3V ↔ 5V level shifter
- **ESD protection:** Onboard ESD protection on the extended bus side
- **Local connector:** 2 × **Qwiic ports** (3.3V I2C, plug-and-play)
- **Extended connector:** **Screw terminal** for long-cable connections
- **Power LED:** Onboard purple power indicator LED

---

## You may also need

<QuickLink 
  title="Qwiic cable" 
  description="Qwiic compatible cables with connectors on both ends, available in various lengths."
  url="https://soldered.com/product/easyc-cable/"
  image="/img/333311.webp" 
/>
