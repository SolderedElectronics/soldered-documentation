---
slug: /inkplate/2/hardware/design
title: Inkplate 2 – Hardware design
sidebar_label: Hardware design
id: 2-hardware-design
hide_title: true
---

<SectionTitle title="Hardware Design" backgroundImage="/img/inkplate_2/hardware.png" />

Inkplate 2 is an open-source, low-power development board based on an **ESP32 microcontroller**, with a **2.13-inch three-color (black, white and red)** e-paper display. It has a small footprint and works with Arduino and MicroPython. This page covers the Inkplate 2’s hardware design: schematics, specs, and component layout.

<InfoBox>All hardware design files are available in the [**Inkplate 2 GitHub repository**](https://github.com/SolderedElectronics/Soldered-Inkplate-2-hardware-design) and are covered by an [**open-source license**](https://github.com/SolderedElectronics/Soldered-Inkplate-2-hardware-design/blob/main/LICENSE.md).</InfoBox>

---

## Basic overview

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
- **Qwiic-compatible connector**
- Optimized form factor for enclosure integration

<InfoBox>Inkplate 2 works well for low-power, always-on displays such as clocks, tags, signs, and small IoT dashboards. It’s beginner-friendly, yet capable enough for advanced applications.</InfoBox>

---

## Components

Here is an overview of the onboard components and their locations:
<CenteredImage src="/img/inkplate_2/front.png" alt="Inkplate 2 front" caption="Inkplate 2 front"  />
<CenteredImage src="/img/inkplate_2/back.png" alt="Inkplate 2 back" caption="Inkplate 2 back" />

---

## E-paper panel: 2.13-inch three-color

The Inkplate 2 uses a **2.13″ three-color e-paper panel** that can display black, white, and red. This kind of display stays clearly visible even in direct light and uses very little power.

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
| **Operating Temperature**   | 0°C to 40°C                             |
| **Storage Temperature**     | -25°C to 60°C                           |

<InfoBox>The Inkplate 2’s display draws almost no power, since it only uses current when the screen updates.</InfoBox>