---
slug: /inkplate/6flick/hardware/design
title: Hardware design
id: 6flick-hardware-design
hide_title: true
---

<SectionTitle title="Hardware design" backgroundImage="/img/inkplate_6_motion/6_motion_hw.png" />

Inkplate 6FLICK is an **open-source** product, and we are happy to share an overview of its hardware design. On the following pages, you'll find schematics, KiCad design files, and other technical details related to the hardware. Whether you're looking to modify, troubleshoot, or simply understand the inner workings of Inkplate, this section has everything you need.  

<InfoBox>All hardware designs and resources are provided under an [**open-source license**](https://github.com/SolderedElectronics/Soldered-Inkplate-6-FLICK-hardware-design/blob/0552552410c75d7dd4bcbb29ad8a3da2e37524c3/LICENSE.md), meaning you're free to explore, modify, and improve upon them as needed.</InfoBox>  

---

## Basic overview

Inkplate 6FLICK features a 6.0″ e-paper display with a resolution of **1024×758 pixels**, offering greyscale rendering, partial updates, and a fast refresh rate. It includes a **touchscreen** supporting two simultaneous touches and a built-in backlight controllable in 64 steps, making it ideal for interactive displays. Powered by an **ESP32** microcontroller, it provides Wi-Fi and Bluetooth connectivity. The board also includes a USB-C port for power and programming, microSD expansion, and TI-based power management with battery charging and temperature sensing. Its form factor is optimized for custom enclosures.

<InfoBox>Fun fact: Inkplate 6FLICK displays come from reused Kindle E-Books </InfoBox>

---

## Components

Here is an overview of on‑board components with their locations:
<CenteredImage src="/img/inkplate_6_flick/Inkplate6flick_front.png" alt="Inkplate 6FLICK front" caption="Inkplate 6FLICK front"  />
<CenteredImage src="/img/inkplate_6_flick/Inkplate6flick_back.png" alt="Inkplate 6FLICK back" caption="Inkplate 6FLICK back" />

---

## E-paper panel

The Inkplate 6FLICK employs a 6.0-inch e-paper display with the following specifications:

| **Specification**         | **Details**                            |
| ------------------------- | -------------------------------------- |
| **Diagonal Size**         | 6.0 inches                             |
| **Resolution**            | 1024 × 758 pixels (212 PPI)            |
| **Grayscale Levels**      | 8                                      |
| **Touchscreen**           | Yes, supports two simultaneous touches |
| **Backlight**             | Yes, controllable in 64 steps          |
| **Partial Updates**       | Supported                              |
| **Full Refresh Time**     | 1.26 seconds                           |
| **Fast Refresh Time**     | 225 milliseconds (1-bit mode)          |
| **Interface**             | Parallel Data (1ch, 8-bit), 34-pin FPC |
| **Voltage Supply**        | 3.3V (Typ.)                            |
| **Operating Temperature** | 0°C to 50°C                            |
| **Storage Temperature**   | -25°C to 70°C                          |


<InfoBox>**Note:** All specifications listed above are based on available datasheets and may contain minor inaccuracies. Always verify with the manufacturer for the latest details.</InfoBox>