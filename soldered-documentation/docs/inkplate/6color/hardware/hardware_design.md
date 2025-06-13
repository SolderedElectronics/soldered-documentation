---
slug: /inkplate/6color/hardware/design
title: Inkplate 6COLOR – Hardware design
id: hardware-design
hide_title: true
---

<SectionTitle title="Hardware design" backgroundImage="/img/inkplate_6_motion/6_motion_hw.png" />

Inkplate 6COLOR is an **open-source** product, and we are happy to share an overview of its hardware design. On the following pages, you'll find schematics, KiCad design files, and other technical details related to the hardware. Whether you're looking to modify, troubleshoot, or simply understand the inner workings of Inkplate, this section has everything you need.  

<InfoBox>All hardware designs and resources are provided under an [**open-source license**](https://github.com/SolderedElectronics/Soldered-Inkplate-6-COLOR-hardware-design/blob/main/LICENSE.md), meaning you're free to explore, modify, and improve upon them as needed.</InfoBox>  

---

## Basic overview

The Inkplate 6COLOR features a 5.8″ e-paper display, USB-C connectivity for both power and programming, abundant GPIO pins with I2C, SPI, and Qwiic header, on‑board ESP32–driven Wi‑Fi/Bluetooth, CH340C USB‑to‑UART bridging, microSD expansion, and TI-based power management (battery charging and temperature sensing) — all in a form factor primed for custom enclosures.

---

## Components

Here is an overview of on‑board components with their locations:
<CenteredImage src="/img/6color/placeholder.jpg" alt="Inkplate 6COLOR front" caption="Inkplate 6COLOR front" width="400px" />
<CenteredImage src="/img/6color/placeholder.jpg" alt="Inkplate 6COLOR back" caption="Inkplate 6COLOR back" width="400px" />

---

## E-paper panel

The **AC057TC1** is a **5.65-inch** e-paper display panel from **E Ink Holdings Inc.** This model is **without a frontlight or touchscreen**, making it ideal for **low-power, high-contrast applications** such as **e-book readers**.  

It features **a 600 × 488 resolution (132 DPI)**, **reflective matte treatment**, and can display **7 colors:** Black, White, Red, Yellow, Blue, Green, and Orange. The display operates in a **15°C to 35°C** temperature range and can be stored in temperatures as low as **-25°C**.  

The inclusion of colors comes at the cost of the **screen refresh time**, which takes **12 seconds**

See the table below for detailed specifications:  

| **Specification**     | **Details**                                               |
|-----------------------|-----------------------------------------------------------|
| **Brand**             | E Ink                                                     |
| **Model Number**      | AC057TC1                                                  |
| **Diagonal Size**     | 5.65 inches                                               |
| **Resolution**        | 600 x 488 pixels (132 DPI)                                  |
| **Pixel Format**      | Square                                                    |
| **Active Area**       | 191.5 x 191.5 um                                          |
| **Outline Dimensions**| 125.4(H) x 99.5(V) x 0.91(D) mm                             |
| **Touchscreen**       | No (this version has no touchscreen)                      |
| **Backlight**         | No backlight, no driver                                   |
| **Interface**         | Serial Peripheral Interface (SPI)                         |
| **Voltage Supply**    | 3.3V (Typ.)                                               |
| **Operating Temperature** | 15°C to 35°C                                          |
| **Storage Temperature**   | -25°C to 60°C                                          |

<InfoBox>**Note:** All specifications listed above are based on available datasheets and may contain minor inaccuracies. Always verify with the manufacturer for the latest details.</InfoBox>