---  
slug: /inkplate/6/overview  
title: Inkplate 6 - Overview  
sidebar_label: Overview  
id: 6-overview
hide_title: True  
pagination_prev: null  
tags:
  - 333232
  - 333234
  - 333233
  - 333229
  - Inkplate 6
  - Inkplate6
---

<SectionTitle title="Overview" />

**Inkplate 6** is a 6-inch e-paper display with an ESP32 behind it. The panel is a recycled 800 × 600 E-Ink screen pulled from e-readers, so it stays readable in direct sunlight and holds its image with the power off. Wi-Fi and Bluetooth are built in, and the board is Arduino compatible out of the box.

You can program it in Arduino (the library is Adafruit GFX compatible) or MicroPython. It draws in black and white or in eight levels of grayscale, and supports partial updates when you only need to change part of the screen. For anything you want to add, there are free GPIO pins plus I²C, SPI and an easyC/Qwiic header.

Because the panels are reclaimed rather than newly made, expect the occasional cosmetic scratch on the glass. It does not affect how the display works.

<CenteredImage src="/img/6/333232.png" alt="Inkplate 6" caption="Inkplate 6 e-paper display board"/>

## Which product is this documentation for?

<QuickLink 
  title="Inkplate 6" 
  description="333232"
  url="https://soldered.com/product/inkplate-6-6-e-paper-board/"
  image="/img/6/333232.png" 
/>

<QuickLink 
  title="Inkplate 6 without e-paper Display" 
  description="333234"
  url="https://soldered.com/product/inkplate-6-6-e-paper-board/"
  image="/img/6/boardonly.png" 
/>

<QuickLink 
  title="Inkplate 6 with e-paper & enclosure" 
  description="333233"
  url="https://soldered.com/product/inkplate-6-6-e-paper-board/"
  image="/img/6/enclosure.png" 
/>

<QuickLink 
  title="Inkplate 6 with e-paper, Enclosure & Battery" 
  description="333229"
  url="https://soldered.com/product/inkplate-6-6-e-paper-board/"
  image="/img/6/ennbat.png" 
/>

## Key features

- **Display Size:** 6" e-paper (black, white + grayscale)
- **Resolution:** 800 × 600 pixels
- **Refresh Rate:** 1.26s (full), 0.26s (partial)
- **Microcontroller:** ESP32-WROVER (Wi-Fi + Bluetooth 4.2 BR/EDR and BLE)
- **Power Supply:** USB or Li-Ion battery (charger included)
- **Power Consumption:** 25 µA in deep sleep mode
- **Programming Support:** Arduino (Adafruit GFX), MicroPython
- **Storage:** microSD card slot for image loading and data logging
- **Clock:** Real-Time Clock (PCF85063A) with battery holder
- **Expansion:** GPIO, I²C, SPI, EasyC/Qwiic-compatible
- **Sustainability:** Recycled E-Ink display (minor cosmetic scratches possible)
- **Enclosure Options:**
  - With 3D-printed enclosure
  - With enclosure and integrated 1200mAh battery
  - Without e-paper display (custom display integration)
- **Dimensions (without EPD):** 144.5 × 107.8 × 10 mm / 5.7 × 4.2 × 0.4 inch
- **Dimensions (with enclosure):** 160.7 × 116.8 × 13.7 mm / 6.3 × 4.6 × 0.5 inch