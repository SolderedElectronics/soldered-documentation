---  
slug: /inkplate/6motion/overview  
title:  Inkplate 6MOTION - Overview  
sidebar_label: Overview  
id: 6motion-overview
hide_title: True  
pagination_prev: null  
tags:
  - 333321
  - 333322
  - 333324
  - Inkplate 6MOTION
  - Inkplate6MOTION
---

<SectionTitle title="Overview" />

**Inkplate 6MOTION** is a 6-inch e-paper display built for content that moves. It runs **1024 × 758** at **4-bit grayscale (16 shades)**, and a partial refresh takes about **91 ms**, which works out to roughly **11 FPS**. That is fast enough for animation, scrolling menus and live dashboards, which is not something e-paper is usually good at.

The board runs two processors: an **STM32H743** does the work, and an **ESP32-C3** handles Wi-Fi and Bluetooth as a co-processor. Onboard you also get a gesture and proximity sensor, a temperature and humidity sensor, an accelerometer, a rotary encoder, RGB LEDs and touch buttons, plus microSD, an RTC and USB-C. It draws **22 µA** in deep sleep.

<CenteredImage src="/img/inkplate_6_motion/333321.png" alt="Inkplate 6MOTION" caption="Inkplate 6MOTION e-paper display board"/>

## Which product is this documentation for?

<QuickLink 
  title="Inkplate 6MOTION" 
  description="333321"
  url="https://soldered.com/product/inkplate-6-motion/"
  image="/img/inkplate_6_motion/333321.png" 
/>

<QuickLink 
  title="Inkplate 6MOTION with e-paper & enclosure" 
  description="333322"
  url="https://soldered.com/product/inkplate-6-motion/"
  image="/img/inkplate_6_motion/enclosure.png" 
/>

<QuickLink 
  title="Inkplate 6MOTION with e-paper, Enclosure & Battery" 
  description="333324"
  url="https://soldered.com/product/inkplate-6-motion/"
  image="/img/inkplate_6_motion/ennbat.png" 
/>

## Key features

- **Display Size:** 6.0" e-paper (grayscale, motion-optimized)
- **Resolution:** 1024 × 758 pixels (212 PPI)
- **Refresh Rate:** 91 ms (partial), 500 ms (full B&W), 800 ms (full grayscale)
- **Grayscale Support:** 4-bit (16 shades)
- **Main Processor:** STM32H743ZIT6 (2MB Flash, 1MB SRAM, 32MB DRAM)
- **Co-Processor:** ESP32-C3 (Wi-Fi + Bluetooth 5 LE)
- **Power Consumption:** 22 µA in low-power mode
- **Power Supply:** USB-C or Li-Ion battery (MCP73831 charger onboard)
- **Storage:** microSD card slot for image/media loading
- **Sensors:**
  - LSM6DSO32 accelerometer + gyroscope
  - SHTC3 temperature & humidity sensor
  - APDS-9960 gesture & proximity sensor
- **Input & Feedback:**
  - 3x side push buttons
  - Rotary encoder with backlit indicator
  - 2x WS2812B RGB LEDs (programmable)
- **Expansion:** 30+ GPIO pins supporting I²C, SPI, UART, Ethernet & more
- **Connectivity:** Wi-Fi and BLE via ESP32-C3
- **Ecosystem:** Fully compatible with EasyC
- **Programming Support:** Arduino (examples available)
- **Open Source:** hardware and software
- **Enclosure Options:**
  - With 3D-printed enclosure
  - With enclosure and 1200mAh battery
  - Without e-paper display
- **Dimensions (with enclosure):** 161 × 116 × 15 mm / 6.34 × 4.56 × 0.59 inch