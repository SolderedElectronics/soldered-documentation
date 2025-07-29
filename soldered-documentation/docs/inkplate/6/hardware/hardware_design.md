---  
slug: /inkplate/6/hardware/design  
title: Inkplate 6 – Hardware design
sidebar_label: Hardware design
id: hardware-design  
hide_title: true  
---  

<SectionTitle title="Hardware design" backgroundImage="/img/inkplate_6_motion/6_motion_hw.png" />

Inkplate 6 is an **open-source** product, and we are happy to share an overview of its hardware design. On the following pages, you'll find schematics, KiCad design files, and other technical details related to the hardware. Whether you're looking to modify, troubleshoot, or simply understand the inner workings of Inkplate, this section has everything you need.

<InfoBox>All hardware designs and resources are provided under an [**open-source license**](https://github.com/SolderedElectronics/Soldered-Inkplate-6-hardware-design/blob/main/LICENSE.md), meaning you're free to explore, modify, and improve upon them as needed.</InfoBox>

---

## Basic overview

The Inkplate 6 features a 6″ e-paper display, USB-C connectivity for both power and programming, abundant GPIO pins with I2C, SPI, and Qwiic header, on‑board ESP32–driven Wi‑Fi/Bluetooth, CH340C USB‑to‑UART bridging, microSD expansion, and TI-based power management (battery charging and temperature sensing) — all in a form factor primed for custom enclosures.

---

## E-paper panel

The **ED060SC7** is a **6-inch** e-paper display panel from **E Ink Holdings Inc.** This model is **without a frontlight or touchscreen**, making it ideal for **low-power, high-contrast applications** such as **e-book readers**.

It features **a 600 × 800 resolution**, a **reflective matte treatment**, and supports 3-bit grayscale. The display operates in a **0°C to 50°C** temperature range and can be stored in temperatures as low as **-25°C**.

See the table below for detailed specifications:

| **Specification**         | **Details**                                               |
|---------------------------|-----------------------------------------------------------|
| **Brand**                 | E Ink                                                     |
| **Model Number**          | ED060SC7                                                 |
| **Diagonal Size**         | 6 inches                                               |
| **Resolution**            | 600 x 800 pixels                                           |
| **Pixel Format**          | Rectangle                                                 |
| **Active Area**           | 90.6 (H) 122.4 (V) mm                                     |
| **Outline Dimensions**    | 101.8(W) 138.4(H) 1.18(D) (panel area height)             |
| **Touchscreen**           | No (this version has no touchscreen)                      |
| **Backlight**             | No backlight, no driver                                   |
| **Interface**             | Parallel                                                  |
| **Voltage Supply**        | 3.3V (Typ.)                                               |
| **Operating Temperature** | 0°C to 50°C                                               |
| **Storage Temperature**   | -25°C to 70°C                                             |

<InfoBox>**Note:** All specifications listed above are based on available datasheets and may contain minor inaccuracies. Always verify with the manufacturer for the latest details.</InfoBox>