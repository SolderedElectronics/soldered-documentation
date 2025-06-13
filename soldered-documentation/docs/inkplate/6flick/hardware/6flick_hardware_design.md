---  
slug: /inkplate/6flick/hardware/design  
title: Inkplate 6FLICK – Hardware Design
id: 6flick-hardware-design  
hide_title: true  
---

<SectionTitle title="Hardware Design" backgroundImage="/img/inkplate_6_motion/6_motion_hw.png" />

Inkplate 6Flick is an **open-source** product, and we’re happy to share its complete hardware design with the community. In this section, you’ll find KiCad design files, schematics, component lists, and technical notes that help you better understand or build upon the hardware. Whether you're modifying, repairing, or just exploring, this page gives you a solid foundation.

<InfoBox>All design files and assets are licensed under an [**open-source license**](https://github.com/SolderedElectronics/Soldered-Inkplate-6-FLICK-hardware-design/blob/0552552410c75d7dd4bcbb29ad8a3da2e37524c3/LICENSE.md), so feel free to explore, improve, or repurpose them.</InfoBox>

---

## Basic Overview

Inkplate 6Flick features a **6.0″ E Ink display** powered by an **ESP32 microcontroller**, offering built-in Wi-Fi and Bluetooth connectivity. The board also includes:

- A **capacitive touchscreen** with multitouch support (up to two fingers)
- A **64-level frontlight/backlight system** for low-light use
- **MicroSD card support** for external storage
- **USB-C** interface for programming and power
- **TI-based power management**, including Li-ion charging and temperature sensing

The form factor and component layout are optimized for integration into enclosures or custom applications.

<InfoBox>Fun fact: Inkplate 6Flick reuses displays from **Kindle e-readers**, extending the life of high-quality e-paper panels that would otherwise be discarded.</InfoBox>

---

## Components Overview

The following labeled images show the front and back of the Inkplate 6Flick board, highlighting key components:

<CenteredImage src="/img/inkplate_6_flick/Inkplate6flick_front.png" alt="Inkplate 6Flick front" caption="Inkplate 6Flick – front view" />
<CenteredImage src="/img/inkplate_6_flick/Inkplate6flick_back.png" alt="Inkplate 6Flick back" caption="Inkplate 6Flick – back view" />

---

## E-Paper Panel: ED060XC3

The Inkplate 6Flick uses the **ED060XC3** e-paper panel — a 6.0″ display originally manufactured by E Ink and commonly found in Kindle devices. This panel is known for its high contrast, fast refresh capabilities in 1-bit mode, and support for partial updates, making it well-suited for dynamic, interactive projects.

| **Specification**         | **Details**                            |
| ------------------------- | -------------------------------------- |
| **Panel Model**           | ED060XC3                               |
| **Diagonal Size**         | 6.0 inches                             |
| **Resolution**            | 1024 × 758 pixels (212 PPI)            |
| **Grayscale Levels**      | 8 (3-bit mode)                         |
| **Touchscreen**           | Yes, multitouch (2 points)             |
| **Frontlight**            | Yes, adjustable in 64 brightness steps |
| **Partial Updates**       | Supported                              |
| **Full Refresh Time**     | ~1.26 seconds                          |
| **Fast Refresh Time**     | ~225 ms (1-bit mode)                   |
| **Interface**             | Parallel (1-channel, 8-bit), 34-pin FPC  |
| **Voltage Supply**        | 3.3V (typical)                         |
| **Operating Temperature** | 0°C to 50°C                            |
| **Storage Temperature**   | -25°C to 70°C                          |

<InfoBox>The ED060XC3 is a commonly reused panel in the maker community due to its performance and availability. The exact variant used may vary slightly, but all are fully supported by the Inkplate firmware stack.</InfoBox>