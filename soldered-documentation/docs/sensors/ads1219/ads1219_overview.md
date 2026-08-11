---
slug: /ads1219/overview
title: ADS1219 24-bit ADC - Overview
sidebar_label: Overview
id: ads1219-overview 
hide_title: False
pagination_prev: null
---

## ADS1219 24-bit ADC

The **ADS1219** is a precision **24-bit delta-sigma analog-to-digital converter (ADC)** with a built-in **programmable gain amplifier (PGA)**, an internal voltage reference, and an **I2C interface**. Plug in a **Qwiic cable** and it reports readings over I2C at a default address of **0x40**. It has **four input channels** that can be configured as differential or single-ended inputs.

The onboard PGA supports gains of **1 and 4**, and the data rate is configurable between **20, 90, 330, and 1000 SPS**. The device includes a **2.048 V internal reference** but can also accept an external reference via the REFP and REFN pins. Up to 16 ADS1219 boards can share one I2C bus, since the onboard jumpers move the address anywhere between **0x40** and **0x4F**.

<CenteredImage src="/img/ads1219/izo_w.webp" alt="ADS1219 24-bit ADC 4-channel breakout board" caption="ADS1219 24-bit ADC 4-channel with PGA" width="500px" />

---

## Which product is this documentation for?

{/* <QuickLink 
  title="ADS1219 24-bit ADC 4-channel with PGA"
  description="333380"
  url="https://solde.red/333380"
  image="/img/ads1219/izo_w.webp" 
/> */}

<WarningBox>The product page for this board is not available yet! We're working on it. In the meantime, please [**contact us**](https://soldered.com/contact/) for more information.</WarningBox>

---

## Key features

- **Resolution:** 24-bit delta-sigma ADC  
- **Input channels:** 4 (configurable as differential or single-ended)  
- **Programmable gain:** 1, 4  
- **Data rates:** 20, 90, 330, 1000 SPS  
- **Internal voltage reference:** 2.048 V (external reference also supported)  
- **Communication:** I2C (16 selectable addresses via jumpers: 0x40-0x4F, default 0x40)  
- **Operating voltage:** 2.3V to 5.5V, works directly at either 3.3V or 5V  
- **Connector:** 2 × **Qwiic ports** (plug-and-play, no soldering needed)  
- **Mounting:** Two mounting holes  
- **Dimensions:** **22 × 22 mm** (0.9 × 0.9 inch)  

---

## You may also need

<QuickLink 
  title="Qwiic cable" 
  description="Qwiic compatible cables with connectors on both ends, available in various lengths."
  url="https://soldered.com/product/easyc-cable/"
  image="/img/333311.webp" 
/>

{/*
TODO - outstanding items for this module:
- Connections/wiring photo needed (Arduino - Reading with Interrupt). The existing
  interrupt.JPG shows a Dasduino, not the NULA DeepSleep the pages specify - recapture.
- Connections/wiring photo needed (Arduino - Single-Shot Reading)
- Product page link above is commented out, pending the real product page going live
  (solde.red/333380 still 404s). The image path is already set to izo_w.webp.
- Hardware repository link (KiCad/Gerbers/BOM) once published - see the WarningBox
  on the Hardware details page
*/}


