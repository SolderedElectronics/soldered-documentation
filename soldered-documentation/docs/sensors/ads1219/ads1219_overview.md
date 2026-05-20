---
slug: /ads1219/overview
title: ADS1219 - Overview
sidebar_label: Overview
id: ads1219-overview 
hide_title: False
pagination_prev: null
---

## ADS1219 24-bit ADC

The **ADS1219** is a precision **24-bit delta-sigma analog-to-digital converter (ADC)** with a built-in **programmable gain amplifier (PGA)**, an internal voltage reference, and an **I2C interface**. It features **four input channels** that can be configured as differential or single-ended inputs, making it suitable for measuring small signals such as those from load cells, thermocouples, and bridge sensors.

The onboard PGA supports gains of **1, 2, 4, and 8**, and the data rate is configurable between **20, 90, 330, and 1000 SPS**. The device includes a **2.048 V internal reference** but can also use an external reference for greater flexibility. Multiple ADS1219 boards can be connected to the same I2C bus by configuring the address via onboard jumpers.

<CenteredImage src="/img/ads1219/ads1219.JPG" alt="ADS1219 24-bit ADC" caption="ADS1219 24-bit ADC" />

---

## Which product is this documentation for?

<WarningBox>The product link for this board is not available yet! We're working on it. In the meantime, please [**contact us**](https://soldered.com/contact/) for more information.</WarningBox>

---

## Key Features

- **Resolution:** 24-bit delta-sigma ADC  
- **Input channels:** 4 (configurable as differential or single-ended)  
- **Programmable gain:** 1, 2, 4, 8  
- **Data rates:** 20, 90, 330, 1000 SPS  
- **Internal voltage reference:** 2.048 V (external reference also supported)  
- **Communication:** I2C (address selectable via jumpers: 0x40, 0x41, 0x42, 0x43)  
- **Operating voltage:** 3.3V (onboard regulator for 5V compatibility)  
- **Connector:** 2 × **Qwiic (formerly easyC) ports** (plug-and-play, no soldering needed)  
- **Mounting:** **Two mounting holes** for secure attachment  
- **Dimensions:** **38 × 22 mm** (1.5 × 0.9 inch)  

---

## You may also need

<QuickLink 
  title="Qwiic cable" 
  description="Qwiic (formerly easyC) compatible cables with connectors on both ends, available in various lengths."
  url="https://soldered.com/product/easyc-cable/"
  image="/img/333311.webp" 
/>
