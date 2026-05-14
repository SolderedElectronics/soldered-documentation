---
slug: /inputronic-bridge/overview
title: Overview
id: inputronic-bridge-overview 
hide_title: False
pagination_prev: null
---
The **Inputronic BRIDGE** is a highly versatile interface board powered by the **ESP32-S3** microcontroller. It is designed to act as a bridge for various communication protocols, making it an ideal tool for debugging, testing, and connecting different hardware ecosystems.

The board features a comprehensive pinout, easy-to-use **Qwiic connectors** for plug-and-play I2C communication, and a protected **Female USB-A** port. With built-in selectable protocols via onboard jumpers, it ensures seamless integration for makers and engineers.

<CenteredImage src="/img/under_construction.png"  alt="Inputronic BRIDGE" caption="Inputronic BRIDGE" width="500px"/>

---

## Which product is this documentation for?

<QuickLink 
  title="Inputronic BRIDGE" 
  description="333359"
  url="https://soldered.com/product/inputronic-bridge/"
  image="/img/under_construction.png" 
/>

---

## Key Features

- **Microcontroller:** ESP32-S3 for reliable and fast processing.
- **USB Host Capabilities:** Automatically translates standard USB HID devices (Keyboards, Mice, MIDI) into easily parsable data.
- **Multi-Protocol Output:** Selectable communication interfaces including I2C (default), UART, and SPI.
- **Software Support:** Fully supported by a dedicated open-source Arduino library with built-in event structures.
- **Advanced Data Modes:** Access raw HID reports and USB descriptors, or use ready-made parsed events.
- **Efficiency:** Supports standard polling or an interrupt-driven mode (via the INT pin) to save host MCU CPU cycles.
- **USB Interface:** Female USB-A connector with overcurrent protection (Max 260mA).
- **Power Supply:** 3.3V logic, equipped with an onboard 3.3V to 5V boost converter.
- **Qwiic Ecosystem:** Qwiic connectors (SMD) for fast I2C device integration.