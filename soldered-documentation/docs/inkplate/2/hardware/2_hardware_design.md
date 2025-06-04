---
slug: /inkplate/2/hardware/design
title: Hardware design
id: 2-hardware-design
hide_title: true
---

<SectionTitle title="Hardware Design" backgroundImage="/img/inkplate_2/hardware.png" />

Inkplate 2 is an **open-source**, low-power development board based on an **ESP32 microcontroller**, featuring a **2.13-inch three-color (black, white and red)** e-paper display. Designed with simplicity and efficiency in mind, it offers a small footprint while remaining compatible with Arduino and MicroPython. This page provides a complete overview of the Inkplate 2’s hardware design, including schematics, specifications, and component layout.

<InfoBox>All hardware design files are available in the [**Inkplate 2 GitHub repository**](https://github.com/SolderedElectronics/Soldered-Inkplate-2-hardware-design) and are covered by an [**open-source license**](https://github.com/SolderedElectronics/Soldered-Inkplate-2-hardware-design/blob/main/LICENSE.md).</InfoBox>

---

## Basic Overview

Inkplate 2 is a compact, plug-and-play e-paper board with support for **Wi-Fi** and **Bluetooth** via the onboard **ESP32**. It features:

- A **2.13-inch three-color e-paper display** (black, white, and red)
- **ESP32 microcontroller** for wireless connectivity
- **USB-C** for power and programming
- **4 MB flash memory**
- Support for **Arduino**
- Ultra-low power usage: **~8µA in deep sleep mode**
- **CH340C USB to UART converter**
- **MCP73831** lithium-ion battery charger
- **GPIO, I²C, and SPI** breakouts
- **easyC/Qwiic-compatible connector**
- Optimized form factor for enclosure integration

<InfoBox>Inkplate 2 is perfect for low-power, always-on displays such as clocks, tags, signs, and small IoT dashboards. It’s beginner-friendly, yet powerful enough for advanced applications.</InfoBox>

---

## Components

Here is an overview of the onboard components and their locations:
<CenteredImage src="/img/inkplate_2/front.png" alt="Inkplate 2 front" caption="Inkplate 2 front"  />
<CenteredImage src="/img/inkplate_2/back.png" alt="Inkplate 2 back" caption="Inkplate 2 back" />

<InfoBox>The term "easyC" used here actually refers to **qwiic** connectors.</InfoBox>

---

## E-Paper Panel: 2.13-Inch Three-Color

The Inkplate 2 uses a **2.13″ three-color e-paper panel** that can display **black, white, and red**. This display type is ideal for creating eye-catching content with excellent visibility and minimal power consumption.

| **Specification**           | **Details**                             |
|-----------------------------|-----------------------------------------|
| **Panel Size**              | 2.13 inches                             |
| **Resolution**              | 212 × 104 pixels                        |
| **Color**                   | Black / White / Red                     |
| **Display Technology**      | E Ink – Active Matrix EPD               |
| **Interface**               | SPI                                     |
| **Viewing Angle**           | Ultra-wide (nearly 180°)                |
| **Refresh Time**            | Varies per color mode (~15s with red)   |
| **Touchscreen**             | No                                      |
| **Backlight**               | No                                      |
| **Power Usage**             | ~8 µA in deep sleep                     |
| **Supply Voltage**          | 3.3V                                    |
| **Operating Temperature**   | 0°C to 50°C                             |
| **Storage Temperature**     | -25°C to 70°C                           |

<InfoBox>The Inkplate 2’s display is capable of extremely low power consumption, as it only draws current when updating the screen.</InfoBox>