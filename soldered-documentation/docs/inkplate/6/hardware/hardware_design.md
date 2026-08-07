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

Inkplate 6 is built around a 6″ e-paper panel and an ESP32-WROVER, which handles both Wi-Fi and Bluetooth. A single USB-C port covers power and programming, with a CH340C doing the USB-to-UART conversion.

The e-paper rails come from a TI TPS65186, which also reads the panel's NTC thermistor so you can get a temperature reading. Battery charging is handled by a Microchip MCP73831. For expansion there are free GPIO pins, I2C, SPI, an easyC/Qwiic header and a microSD slot.

<CenteredImage src="/img/6/back.webp" alt="Inkplate 6 back side" caption="Inkplate 6, back side" width="1000px" />

---

## E-paper panel

The **ED060SC7** is a **6-inch** e-paper display panel from **E Ink Holdings Inc.** This model is **without a frontlight or touchscreen**, making it ideal for **low-power, high-contrast applications** such as **e-book readers**.

It has **480,000 pixels**, a **reflective matte treatment**, and supports 3-bit grayscale. The display operates in a **0°C to 50°C** temperature range and can be stored between **-25°C and 70°C**.

Inkplate mounts the panel in landscape, so the frame buffer you draw into is **800 px wide by 600 px tall**. The datasheet below quotes the panel's own portrait orientation, where the 600-pixel axis is H and the 800-pixel axis is V, the same panel, described along the other axis.

See the table below for detailed specifications:

| **Specification**         | **Details**                                               |
|---------------------------|-----------------------------------------------------------|
| **Brand**                 | E Ink                                                     |
| **Model Number**          | ED060SC7                                                 |
| **Diagonal Size**         | 6 inches                                               |
| **Resolution**            | 600 (H) x 800 (V) pixels                                   |
| **Pixel Format**          | Rectangle                                                 |
| **Pixel Pitch**           | 0.151 (H) 0.153 (V) mm                                    |
| **Active Area**           | 90.6 (H) 122.4 (V) mm                                     |
| **Outline Dimensions**    | 101.8 (W) 138.4 (H) 1.18 (D) mm                           |
| **Module Weight**         | 34 g                                                      |
| **Touchscreen**           | No (this version has no touchscreen)                      |
| **Backlight**             | No backlight, no driver                                   |
| **Interface**             | Parallel                                                  |
| **Voltage Supply**        | 3.3V (Typ.)                                               |
| **Operating Temperature** | 0°C to 50°C                                               |
| **Storage Temperature**   | -25°C to 70°C                                             |

<InfoBox>**Note:** All specifications listed above are based on available datasheets and may contain minor inaccuracies. Always verify with the manufacturer for the latest details.</InfoBox>