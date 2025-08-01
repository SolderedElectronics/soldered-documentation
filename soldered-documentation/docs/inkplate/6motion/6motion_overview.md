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
  - Inkplate 6 MOTION
  - Inkplate6MOTION
---

<SectionTitle title="Overview" backgroundImage="/img/arduino_bg.jpg" />

**Inkplate 6MOTION** is a high-performance **6-inch e-paper display** designed for real-time applications like animations, interactive menus, dashboards, and dynamic signage. With a stunning **1024×758 resolution**, **4-bit grayscale support (16 shades)**, and **91 ms partial refresh rate**, it enables motion-capable content at up to **11 FPS**, a major breakthrough in DIY e-paper displays.

The board is powered by a dual-core architecture: a **STM32H743 main processor** paired with an **ESP32-C3 co-processor** for wireless connectivity. It’s packed with features such as **gesture and proximity sensors**, **rotary encoder**, **RGB indicator LEDs**, and **touch input buttons**, making it ideal for interactive environments. Add ultra-low power consumption (22 µA), **microSD**, **RTC**, and **USB-C**, and you've got a fully open-source powerhouse ready for any advanced e-paper project.

<CenteredImage src="/img/inkplate_6_motion/333321.png" alt=" Inkplate 6MOTION" caption=" Inkplate 6MOTION e-paper display board"/>

## Which product is this documentation for?

<QuickLink 
  title=" Inkplate 6MOTION" 
  description="333321"
  url="https://soldered.com/product/inkplate-6-motion/"
  image="/img/inkplate_6_motion/333321.png" 
/>

<QuickLink 
  title=" Inkplate 6MOTION with e-paper & enclosure" 
  description="333322"
  url="https://soldered.com/product/inkplate-6-motion/"
  image="/img/inkplate_6_motion/enclosure.png" 
/>

<QuickLink 
  title=" Inkplate 6MOTION with e-paper, Enclosure & Battery" 
  description="333324"
  url="https://soldered.com/product/inkplate-6-motion/"
  image="/img/inkplate_6_motion/ennbat.png" 
/>

## Key Features

- **Display Size:** 6.0" e-paper (greyscale, motion-optimized)
- **Resolution:** 1024 × 758 pixels (212 PPI)
- **Refresh Rate:** 91 ms (partial), 500 ms (full B&W), 800 ms (full grayscale)
- **Grayscale Support:** 4-bit (16 shades)
- **Main Processor:** STM32H743ZIT6 (2MB Flash, 1MB SRAM, 32MB DRAM)
- **Co-Processor:** ESP32-C3 (Wi-Fi + Bluetooth 4.0 BLE)
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