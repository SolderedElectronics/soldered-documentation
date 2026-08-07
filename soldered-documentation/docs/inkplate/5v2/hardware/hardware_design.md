---  
slug: /inkplate/5v2/hardware/design  
title: Inkplate 5V2 – Hardware design
sidebar_label: Hardware design
id: hardware-design  
hide_title: true  
---  

<SectionTitle title="Hardware design" backgroundImage="/img/inkplate_6_motion/6_motion_hw.png" />

Inkplate 5V2 is an open-source product, so its full hardware design is out in the open. On the following pages you'll find schematics, KiCad design files, and other technical details about the hardware, whether you want to modify the board, troubleshoot it, or just see how it works inside.

<InfoBox>All hardware designs and resources are provided under an [**open-source license**](https://github.com/SolderedElectronics/Soldered-Inkplate-5-Gen2-hardware-design/blob/main/LICENSE.md), so you're free to explore, modify, and build on them.</InfoBox>

---

## Basic overview

Inkplate 5V2 has a 5.17-inch e-paper display, USB-C for both power and programming, and plenty of GPIO pins with I2C, SPI, and a Qwiic header. The onboard ESP32 handles Wi-Fi and Bluetooth, the CH340C bridges USB to UART, and there's a microSD slot for storage. Power management runs on a mix of TI ICs for the e-paper supply and regulation (which also handles temperature sensing through a built-in NTC input) and a Microchip charger IC for the battery.

<CenteredImage src="/img/5v2/Inkplate5_v2_back.webp" alt="Inkplate 5V2 back side" caption="Inkplate 5V2, back side" width="1000px" />

---

## E-paper panel

The **ED052TC4** is a 5.17-inch e-paper display panel from E Ink Holdings Inc. This model comes without a frontlight or touchscreen, which suits low-power, high-contrast uses such as e-book readers.

It has a 720 × 1280 resolution and a reflective matte treatment, and supports 3-bit grayscale. The display operates in a 0°C to 50°C temperature range and can be stored in temperatures as low as -25°C.

<InfoBox>The 720 × 1280 figure is the panel's native portrait orientation. The Inkplate library uses the display in landscape by default, so in your sketches the canvas is 1280 pixels wide and 720 pixels tall. Use `setRotation()` if you want portrait.</InfoBox>

See the table below for detailed specifications:

| **Specification**         | **Details**                                               |
|---------------------------|-----------------------------------------------------------|
| **Brand**                 | E Ink                                                     |
| **Model Number**          | ED052TC4                                                  |
| **Diagonal Size**         | 5.17 inches                                               |
| **Resolution**            | 720 x 1280 pixels                                           |
| **Pixel Format**          | Rectangle                                                 |
| **Active Area**           | 64.44 (H)×114.56 (V)mm                                     |
| **Outline Dimensions**    | 69.14 (W) × 124.59 (H) × 0.68 (D)                           |
| **Touchscreen**           | No (this version has no touchscreen)                      |
| **Backlight**             | No backlight, no driver                                   |
| **Interface**             | Parallel                                                  |
| **Voltage Supply**        | 3.3V (Typ.)                                               |
| **Operating Temperature** | 0°C to 50°C                                               |
| **Storage Temperature**   | -25°C to 70°C                                             |

<InfoBox>All specifications listed above come from available datasheets and may contain minor inaccuracies. Check with the manufacturer for the latest details.</InfoBox>