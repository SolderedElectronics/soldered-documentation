---  
slug: /inkplate/4tempera/hardware/design  
title: Hardware Design  
id: 4tempera-hardware-design  
hide_title: true  
---

<SectionTitle title="Hardware Design" backgroundImage="/img/inkplate_4_tempera/4_tempera_hw.png" />

Inkplate 4 TEMPERA is an **open-source** product, and we're excited to share its hardware design with the community. This section includes KiCad project files, schematics, board layouts, and other technical resources to help you understand, customize, or extend the device's capabilities.

<InfoBox>All hardware files are released under an [**open-source license**](https://github.com/SolderedElectronics/Soldered-Inkplate-4TEMPERA-hardware-design/blob/main/LICENSE), allowing full freedom to explore, adapt, and reuse the design.</InfoBox>

---

## Basic Overview

Inkplate 4 TEMPERA is built around a **3.8″ e-paper display** and is powered by an **ESP32 microcontroller**, which offers built-in Wi-Fi and Bluetooth support. Its compact size makes it ideal for portable or embedded projects that require high-contrast, ultra-low-power display capabilities.

Key features include:

- A **capacitive touchscreen** for direct interaction  
- A **64-step adjustable frontlight** for visibility in any lighting condition  
- **MicroSD card slot** for external storage  
- **USB-C** port for programming and power  
- **Li-ion battery support** with onboard charging (MCP73831) and power management

The board layout is optimized for enclosures and integration into compact applications.

<InfoBox>Fun fact: TEMPERA units also reuse genuine e-paper panels — giving a second life to commercial-grade displays while helping reduce waste.</InfoBox>

---

## Components Overview

The following images show the front and back of the Inkplate 4 TEMPERA board, with major components visible for easy identification:

<CenteredImage src="/img/inkplate_4_tempera/tempera.png" alt="Inkplate 4 TEMPERA front" caption="Inkplate 4 TEMPERA – front view" />
<CenteredImage src="/img/inkplate_4_tempera/tempera_front.png" alt="Inkplate 4 TEMPERA front" caption="Inkplate 4 TEMPERA – front mounted components" />
<CenteredImage src="/img/inkplate_4_tempera/tempera_rear.png" alt="Inkplate 4 TEMPERA back" caption="Inkplate 4 TEMPERA – back mounted components" />

---

## E-Paper Panel: ED038TH2

Inkplate 4 TEMPERA uses the **ED038TH2** e-paper panel — a compact 3.8″ display from E Ink. This model delivers high pixel density and fast refresh performance, making it suitable for interactive applications and rapid screen refreshes while retaining the low power consumption that e-paper is known for.

| **Specification**         | **Details**                             |
| ------------------------- | --------------------------------------- |
| **Panel Model**           | ED038TH2                                |
| **Diagonal Size**         | 3.8 inches                              |
| **Resolution**            | 600 × 448 pixels (200+ PPI)             |
| **Grayscale Levels**      | 8 (3-bit mode)                          |
| **Touchscreen**           | Yes, capacitive                         |
| **Frontlight**            | Yes, adjustable in 64 brightness steps  |
| **Partial Updates**       | Supported                               |
| **Full Refresh Time**     | ~1.0 second (typical)                   |
| **Fast Refresh Time**     | ~200 ms (1-bit mode)                    |
| **Interface**             | Parallel, 24-pin FPC                    |
| **Voltage Supply**        | 3.3V (typical)                          |
| **Operating Temperature** | 0°C to 50°C                             |
| **Storage Temperature**   | -25°C to 70°C                           |

<InfoBox>The ED038TH2 is a compact high-resolution panel with a fast refresh rate and robust grayscale support — ideal for small-format devices like Inkplate 4 TEMPERA.</InfoBox>

---

Let me know if you'd like additional documentation on jumpers, pinout diagrams, or firmware configuration pages.