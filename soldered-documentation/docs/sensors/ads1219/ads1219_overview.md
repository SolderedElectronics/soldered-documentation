---
slug: /ads1219/overview
title: ADS1219 24-bit ADC - Overview
sidebar_label: Overview
id: ads1219-overview 
hide_title: False
pagination_prev: null
---

## ADS1219 24-bit ADC

The **ADS1219** is a precision **24-bit delta-sigma analog-to-digital converter (ADC)** with a built-in **programmable gain amplifier (PGA)**, an internal voltage reference, and an **I2C interface**. It features **four input channels** that can be configured as differential or single-ended inputs.

The onboard PGA supports gains of **1 and 4**, and the data rate is configurable between **20, 90, 330, and 1000 SPS**. The device includes a **2.048 V internal reference** but can also accept an external reference via the REFP and REFN pins. Multiple ADS1219 boards can be connected to the same I2C bus by configuring the address via onboard jumpers.

<CenteredImage src="/img/ads1219/ads1219.JPG" alt="ADS1219 24-bit ADC" caption="ADS1219 24-bit ADC" />

---

## Which product is this documentation for?

{/* <QuickLink 
  title="ADS1219 24-bit ADC 4-channel with PGA"
  description="333380"
  url="https://solde.red/333380"
  image="/img/ads1219/ads1219.JPG" 
/> */}

<WarningBox>The product page for this board is not available yet! We're working on it. In the meantime, please [**contact us**](https://soldered.com/contact/) for more information.</WarningBox>

---

## Key Features

- **Resolution:** 24-bit delta-sigma ADC  
- **Input channels:** 4 (configurable as differential or single-ended)  
- **Programmable gain:** 1, 4  
- **Data rates:** 20, 90, 330, 1000 SPS  
- **Internal voltage reference:** 2.048 V (external reference also supported)  
- **Communication:** I2C (16 selectable addresses via jumpers: 0x40-0x4F, default 0x40)  
- **Operating voltage:** 2.3V to 5.5V, works directly at either 3.3V or 5V  
- **Connector:** 2 × **Qwiic (formerly easyC) ports** (plug-and-play, no soldering needed)  
- **Mounting:** Two mounting holes  
- **Dimensions:** **22 × 22 mm** (0.9 × 0.9 inch)  

---

## You may also need

<QuickLink 
  title="Qwiic cable" 
  description="Qwiic (formerly easyC) compatible cables with connectors on both ends, available in various lengths."
  url="https://soldered.com/product/easyc-cable/"
  image="/img/333311.webp" 
/>

{/*
TODO - outstanding items for this module:
- Connections/wiring photo needed for the Single-Shot Reading example (arduino_2)
- Connections/wiring photo needed for the Multiplexer/Channel Selection example (arduino_3)
- Dedicated example still needed showing a distinct external reference voltage (voltage generator/precision reference at a value other than VCC) - deferred, not yet started
- Product page link still commented out above, pending the real product page going live
*/}


