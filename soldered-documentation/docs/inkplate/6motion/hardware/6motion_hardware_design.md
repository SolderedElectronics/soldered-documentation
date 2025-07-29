---
slug: /inkplate/6motion/hardware/design
title: 6Motion - Hardware design
sidebar_label: Hardware design
id: 6motion-hardware-design
hide_title: true
---



<SectionTitle title="Hardware design" backgroundImage="/img/inkplate_6_motion/6_motion_hw.png" />

Inkplate 6 MOTION is an **open-source** product, and we are happy to share an overview of its hardware design. On the following pages, you'll find schematics, KiCad design files, and other technical details related to the hardware. Whether you're looking to modify, troubleshoot, or simply understand the inner workings of Inkplate, this section has everything you need.  

<InfoBox>All hardware designs and resources are provided under an [**open-source license**](https://github.com/SolderedElectronics/Soldered-Inkplate-6-MOTION-hardware-design/blob/main/LICENSE.md), meaning you're free to explore, modify, and improve upon them as needed.</InfoBox>  

---

## Basic overview

Inkplate 6 MOTION’s hardware consists of two separate board designs, each serving a distinct purpose.

The main board houses key components, including the e-Paper connectors, ESP32-C3 co-processor, microSD card slot, power switch, USB connector, and various supporting components.
The STM32 board is dedicated to the **STM32H743** microcontroller and external DRAM, ensuring precise timing and efficient memory management.
This secondary board is referred to as the Inkplate 6 MOTION STM board, as its main function is to break out the STM32’s pins for connection to peripherals while maintaining stable communication with the DRAM.

<CenteredImage src="/img/inkplate_6_motion/motion_stm32.jpg" alt="STM32H743 on Inkplate 6 MOTION" caption="STM32H743 on Inkplate 6 MOTION" />

---

## Components

Here is an overview of on-board components with their locations:
<CenteredImage src="/img/inkplate_6_motion/inkplate_motion_hw_front.jpg" alt="Inkplate 6 MOTION front" caption="Inkplate 6 MOTION front"  />
<CenteredImage src="/img/inkplate_6_motion/inkplate_motion_hw_back.jpg" alt="Inkplate 6 MOTION back" caption="Inkplate 6 MOTION back" />

<InfoBox>What is referred to here as easyC is actually **qwiic** connectors</InfoBox>

---

## E-paper panel

The **ED060XC3** is a **6.0-inch** e-paper display panel from **E Ink Holdings Inc.** This model is **without a frontlight or touchscreen**, making it ideal for **low-power, high-contrast applications** such as **e-book readers**.  

It features **a 758 × 1024 resolution (212 PPI)**, **reflective matte treatment**, and a **12:1 contrast ratio**. The display operates in a **0°C to 50°C** temperature range and can be stored in temperatures as low as **-25°C**.  

See the table below for detailed specifications:  

| **Specification**  | **Details** |
|-------------------|------------|
| **Brand**        | E Ink |
| **Model Number** | ED060XC3 |
| **Diagonal Size** | 6.0 inches |
| **Resolution** | 758 × 1024 pixels (212 PPI) |
| **Pixel Format** | Rectangle |
| **Active Area** | 90.58 mm (W) × 122.368 mm (H) |
| **Outline Dimensions** | 101.8 mm (W) × 138.4 mm (H) × 1.68 mm (D) |
| **Surface Treatment** | Anti-glare |
| **Contrast Ratio** | 12:1 (Typ.) (Reflective) |
| **Viewing Angle** | Not specified |
| **Response Time** | Not specified |
| **Refresh Rate** | 85Hz |
| **Touchscreen** | No (this version has no touchscreen) |
| **Backlight** | No backlight, no driver |
| **Good Viewing Mode** | Not specified |
| **Work Mode** | Not specified |
| **Color Depth** | Grayscale |
| **Mass** | 50.0 ± 5.0 g |
| **Use Case** | E-Book Readers |
| **Interface** | Parallel Data (1ch, 8-bit), 34-pin FPC |
| **Voltage Supply** | 3.3V (Typ.) |
| **Operating Temperature** | 0°C to 50°C |
| **Storage Temperature** | -25°C to 70°C |

<InfoBox>**Note:** All specifications listed above are based on available datasheets and may contain minor inaccuracies. Always verify with the manufacturer for the latest details.</InfoBox>  

