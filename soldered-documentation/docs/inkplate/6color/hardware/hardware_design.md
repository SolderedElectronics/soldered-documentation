---
slug: /inkplate/6color/hardware/design
title: Inkplate 6COLOR – Hardware design
sidebar_label: Hardware design
id: hardware-design
hide_title: true
---

<SectionTitle title="Hardware design" backgroundImage="/img/inkplate_6_motion/6_motion_hw.png" />

Inkplate 6COLOR is an **open-source** product, and we are happy to share an overview of its hardware design. On the following pages, you'll find schematics, KiCad design files, and other technical details related to the hardware. Whether you're looking to modify, troubleshoot, or simply understand the inner workings of Inkplate, this section has everything you need.  

<InfoBox>All hardware designs and resources are provided under an [**open-source license**](https://github.com/SolderedElectronics/Soldered-Inkplate-6-COLOR-hardware-design/blob/main/LICENSE.md), meaning you're free to explore, modify, and improve upon them as needed.</InfoBox>  

---

## Basic overview

Inkplate 6COLOR is built around a 7-color e-paper panel and an ESP32-WROVER, which handles Wi-Fi and Bluetooth. A single USB-C port covers power and programming, with a CH340C doing the USB-to-UART conversion.

Unlike the monochrome Inkplates, this panel needs no external power supply chip: the AC057TC1 has its own gate and source drivers, timing controller and DC-DC boost circuit built in, and the ESP32 talks to it over SPI. Battery charging is handled by a Microchip MCP73831, and the 3.3 V rail comes from a TI TPS7A2633. For expansion there are free GPIO pins, a 16-pin I/O expander, I2C, SPI, an easyC/Qwiic header and a microSD slot.

---

## Components

Here is an overview of on‑board components with their locations:
<CenteredImage src="/img/6color/placeholder.jpg" alt="Inkplate 6COLOR front" caption="Inkplate 6COLOR front" width="400px" />
<CenteredImage src="/img/6color/placeholder.jpg" alt="Inkplate 6COLOR back" caption="Inkplate 6COLOR back" width="400px" />

---

## E-paper panel

The **AC057TC1** is a **5.65-inch** e-paper panel from **E Ink Holdings Inc.**, built on their ACeP (Advanced Color ePaper) technology. There is no frontlight and no touchscreen. Each pixel mixes its own color, so the panel needs no color filter array.

It has a **600 × 448 resolution (132 DPI)**, a reflective matte finish, and displays **7 colors:** black, white, red, yellow, blue, green and orange. Note the narrow operating range of **15°C to 35°C**, which is tighter than the monochrome Inkplates.

Color costs you refresh time. A full refresh takes about **12 seconds**, and the panel cannot do partial updates at all, so plan your project around occasional redraws rather than anything animated.

See the table below for detailed specifications:  

| **Specification**     | **Details**                                               |
|-----------------------|-----------------------------------------------------------|
| **Brand**             | E Ink                                                     |
| **Model Number**      | AC057TC1                                                  |
| **Diagonal Size**     | 5.65 inches (active area)                                 |
| **Resolution**        | 600 x 448 pixels (132 DPI)                                |
| **Pixel Format**      | Square                                                    |
| **Pixel Pitch**       | 191.5 x 191.5 um                                          |
| **Active Area**       | 114.9 (H) x 85.8 (V) mm                                   |
| **Outline Dimensions**| 125.4(H) x 99.5(V) x 0.91(D) mm                             |
| **Touchscreen**       | No (this version has no touchscreen)                      |
| **Backlight**         | No backlight, no driver                                   |
| **Interface**         | Serial Peripheral Interface (SPI)                         |
| **Voltage Supply**    | 3.3V (Typ.)                                               |
| **Operating Temperature** | 15°C to 35°C                                          |
| **Storage Temperature**   | -25°C to 60°C                                          |

<InfoBox>**Note:** All specifications listed above are based on available datasheets and may contain minor inaccuracies. Always verify with the manufacturer for the latest details.</InfoBox>