---
slug: /inkplate/10/hardware/design
title: Inkplate 10 – Hardware design
sidebar_label: Hardware design
id: 10-hardware-design
hide_title: true
---

<SectionTitle title="Hardware design" backgroundImage="/img/inkplate_6_motion/6_motion_hw.png" />

Inkplate 10 is an **open-source** product, and we are happy to share an overview of its hardware design. On the following pages, you'll find schematics, KiCad design files, and other technical details related to the hardware. Whether you're looking to modify, troubleshoot, or simply understand the inner workings of Inkplate, this section has everything you need.  

<InfoBox>All hardware designs and resources are provided under an [**open-source license**](https://github.com/SolderedElectronics/Soldered-Inkplate-10-hardware-design/blob/main/LICENSE.md), meaning you're free to explore, modify, and improve upon them as needed.</InfoBox>  

---

## Basic overview

The Inkplate 10 features a 9.7″ e-paper display, USB-C connectivity for both power and programming, abundant GPIO pins with I2C, SPI, and Qwiic header, on-board ESP32–driven Wi‑Fi/Bluetooth, CH340C USB‑to‑UART bridging, microSD expansion,chac and TI-based power management (battery charging and temperature sensing) — all in a form factor primed for custom enclosures.

<InfoBox>Fun fact: Inkplate 10 displays come from reused Kindle E-Books </InfoBox>

---

## Components

Here is an overview of on‑board components with their locations:
<CenteredImage src="/img/inkplate10/inkplate_10_hw_front.jpg" alt="Inkplate 10 front" caption="Inkplate 10 front"  />
<CenteredImage src="/img/inkplate10/inkplate_10_hw_back.jpg" alt="Inkplate 10 back" caption="Inkplate 10 back" />

<InfoBox>The term "easyC" used here actually refers to **qwiic** connectors.</InfoBox>

---

## E-paper panel

The **ED097OC1** is a **9.7-inch** e-paper display panel from **E Ink Holdings Inc.** This model is **without a frontlight or touchscreen**, making it ideal for **low-power, high-contrast applications** such as **e-book readers**.  

It features **an 825 × 1200 resolution (150 PPI)**, **reflective matte treatment**, and a **7:1 contrast ratio**. The display operates in a **0°C to 50°C** temperature range and can be stored in temperatures as low as **-25°C**.  

See the table below for detailed specifications:  

| **Specification**  | **Details** |
|-------------------|------------|
| **Brand**        | E Ink |
| **Model Number** | ED097OC1 / ED097OC2 / ED097OC4|
| **Diagonal Size** | 9.7 inches |
| **Resolution** | 825 × 1200 pixels (212 PPI) |
| **Pixel Format** | Rectangle |
| **Active Area** | 202.8(W)×139.425(H) mm |
| **Outline Dimensions** | 218.8(H)×156.425(V)×1.28(D) mm |
| **Surface Treatment** | Anti‑glare |
| **Contrast Ratio** | 7:1 (Typ.) (Reflective) |
| **Touchscreen** | No (this version has no touchscreen) |
| **Backlight** | No backlight, no driver |
| **Color Depth** | Grayscale |
| **Mass** | 80.0 ± 5.0 g |
| **Use Case** | E‑Book Readers |
| **Interface** | Parallel Data (1ch, 8‑bit), 34‑pin FPC |
| **Voltage Supply** | 3.3V (Typ.) |
| **Operating Temperature** | 0°C to 50°C |
| **Storage Temperature** | -25°C to 70°C |

<InfoBox>**Note:** All specifications listed above are based on available datasheets and may contain minor inaccuracies. Always verify with the manufacturer for the latest details.</InfoBox>