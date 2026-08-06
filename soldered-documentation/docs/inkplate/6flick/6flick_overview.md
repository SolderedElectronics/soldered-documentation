---  
slug: /inkplate/6flick/overview  
title: Inkplate 6FLICK - Overview  
sidebar_label: Overview  
id: 6flick-overview
hide_title: True  
pagination_prev: null  
tags:
  - 333317
  - 333319
  - 333318
  - 333320
  - Inkplate 6FLICK
  - Inkplate6FLICK
---

<SectionTitle title="Overview" />

**Inkplate 6FLICK** is a 6-inch e-paper display with a capacitive touchscreen and a frontlight, driven by an ESP32. The panel is a recycled ED060XC3 pulled from e-readers, so it holds its image with the power off and stays readable in sunlight. Unlike the other Inkplates, this one you can touch and read in the dark.

Touch is two-point capacitive, and the frontlight runs across 64 brightness steps. Partial updates land in about 225 ms, which is quick enough for menus and drawing rather than just static pages.

Wi-Fi and Bluetooth are built in. You can program it in Arduino or MicroPython, and expand it over GPIO, I²C, SPI and the easyC/Qwiic header.

Because the panels are reclaimed rather than newly made, expect the occasional cosmetic mark on the glass. It does not affect how the display works.



<CenteredImage src="/img/inkplate_6_flick/333317.png" alt="Inkplate 6FLICK" caption="Inkplate 6FLICK e-paper display board"/>

## Which product is this documentation for?

<QuickLink 
  title="Inkplate 6FLICK" 
  description="333317"
  url="https://soldered.com/product/inkplate-6flick/"
  image="/img/inkplate_6_flick/333317.png" 
/>

<QuickLink 
  title="Inkplate 6FLICK without e-paper Display" 
  description="333319"
  url="https://soldered.com/product/inkplate-6flick/"
  image="/img/inkplate_6_flick/boardonly.png" 
/>

<QuickLink 
  title="Inkplate 6FLICK with e-paper & enclosure" 
  description="333318"
  url="https://soldered.com/product/inkplate-6flick/"
  image="/img/inkplate_6_flick/enclosure.png" 
/>

<QuickLink 
  title="Inkplate 6FLICK with e-paper, Enclosure & Battery" 
  description="333320"
  url="https://soldered.com/product/inkplate-6flick/"
  image="/img/inkplate_6_flick/ennbat.png" 
/>

## Key features

- **Display Size:** 6.0" e-paper (ED060XC3, touchscreen with frontlight)
- **Resolution:** 1024 × 758 pixels
- **Refresh Time:** 225 ms (1-bit), 1.26s (3-bit greyscale)
- **Color Support:** 3-bit greyscale (8 shades)
- **Touchscreen:** 2-point capacitive multi-touch
- **Lighting:** Adjustable in 64 brightness steps
- **Microcontroller:** ESP32-WROVER (Wi-Fi + Bluetooth 4.2 BR/EDR and BLE)
- **Power Supply:** USB-C or Li-Ion battery (charger included)
- **Power Consumption:** 23 µA in deep sleep mode
- **Programming Support:** Arduino (Adafruit GFX compatible), MicroPython
- **Storage:** microSD card slot for media/data
- **Clock:** Real-Time Clock (RTC) with battery backup
- **Expansion:** GPIO, I²C, SPI, EasyC/Qwiic-compatible
- **Sustainability:** Recycled e-paper display (minor cosmetic flaws possible)
- **Open Source:** Hardware and software
- **Made in EU:** Designed and manufactured in the European Union
- **Dimensions (without case):** 150.4 × 107.8 × 11.5 mm / 6.06 × 4.24 × 0.45 inch
- **Dimensions (with case):** 173.3 × 116.8 × 14.5 mm / 6.80 × 4.45 × 0.57 inch