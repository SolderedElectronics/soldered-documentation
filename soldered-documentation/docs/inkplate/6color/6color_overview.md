---  
slug: /inkplate/6color/overview  
title: Inkplate 6COLOR - Overview  
sidebar_label: Overview  
id: 6color-overview
hide_title: True  
pagination_prev: null  
tags:
  - 333238
  - 333240
  - 333239
  - 333231
  - Inkplate 6COLOR
  - Inkplate6COLOR
---

<SectionTitle title="Overview" />

**Inkplate 6COLOR** is a 5.65-inch color e-paper display with an ESP32 behind it. The panel shows **7 colors**: black, white, red, yellow, blue, green and orange. Like every e-paper display it keeps the image with the power off, and it stays readable in direct sunlight.

The trade-off for color is speed. A full refresh takes around **12 seconds** and there is no partial update, so this board suits things you redraw now and then: a weather panel, a photo frame, a dashboard on the wall. It draws **18 µA in deep sleep**, so a battery lasts a long time between those redraws.

There is a microSD slot, a real-time clock with a coin-cell backup, and you can program it in Arduino or MicroPython. Enclosure and battery kits are available if you want it finished rather than bare.

<CenteredImage src="/img/6color/333238.png" alt="Inkplate 6COLOR" caption="Inkplate 6COLOR e-paper display board"/>

## Which product is this documentation for?

<QuickLink 
  title="Inkplate 6COLOR" 
  description="333238"
  url="https://soldered.com/product/inkplate-6color-e-paper-display/"
  image="/img/6color/333238.png" 
/>

<QuickLink 
  title="Inkplate 6COLOR without e-paper Display" 
  description="333240"
  url="https://soldered.com/product/inkplate-6color-e-paper-display/"
  image="/img/6color/boardonly.png" 
/>

<QuickLink 
  title="Inkplate 6COLOR with e-paper & enclosure" 
  description="333239"
  url="https://soldered.com/product/inkplate-6color-e-paper-display/"
  image="/img/6color/enclosure.png" 
/>

<QuickLink 
  title="Inkplate 6COLOR with e-paper, Enclosure & Battery" 
  description="333231"
  url="https://soldered.com/product/inkplate-6color-e-paper-display/"
  image="/img/6color/ennbat.png" 
/>

## Key features

- **Display Size:** 5.65" color e-paper (AC057TC1)
- **Resolution:** 600 × 448 pixels
- **Color Support:** 7 colors (Black, White, Red, Yellow, Blue, Green, Orange)
- **Refresh Time:** ~12 seconds (full refresh; no partial update)
- **Microcontroller:** ESP32-WROVER (Wi-Fi + Bluetooth 4.2 BR/EDR and BLE)
- **Power Supply:** USB or Li-Ion battery (charger onboard)
- **Power Consumption:** 18 µA in deep sleep mode
- **Programming Support:** Arduino (Adafruit GFX compatible), MicroPython
- **Storage:** microSD card slot for image display and data
- **Expansion:** GPIO, I²C, SPI, EasyC/Qwiic-compatible
- **Enclosure Options:**
  - With 3D-printed enclosure
  - With enclosure and 1200mAh battery
  - Without e-paper display (custom integrations)
- **Open Source:** Hardware and software
- **Dimensions (without EPD):** 131.5 × 105.5 × 10 mm / 5.2 × 4.2 × 0.4 inch
- **Dimensions (with enclosure):** 140 × 119.3 × 13.6 mm / 5.5 × 4.7 × 0.5 inch