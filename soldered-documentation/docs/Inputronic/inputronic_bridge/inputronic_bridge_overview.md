---
slug: /inputronic_bridge/overview
title: Inputronic BRIDGE - Overview
sidebar_label: Overview
id: inputronic_bridge-overview 
hide_title: False
pagination_prev: null
---

## Inputronic BRIDGE

The **Inputronic BRIDGE** lets a microcontroller without USB host capability read input from a regular USB-A HID device, such as a keyboard, mouse, or MIDI controller. Plug the device into the onboard USB-A port, and the board's **ESP32-S3** decodes its HID reports. It then sends the parsed key presses, mouse movement, or MIDI bytes to your project over **I²C, UART, or SPI**, selected with a jumper. The default protocol is I²C at address **0x50**, which you can change in software, and the board has two onboard **Qwiic connectors** for daisy-chaining.

<ErrorBox>The product photo for this board hasn't been generated yet. We're working on it!</ErrorBox>

---

## Which products is this documentation for?

<QuickLink
  title="Inputronic BRIDGE"
  description="333390"
  url="https://soldered.com/products/soldered-inputronic-bridge"
/>

---

## Key Features

- **USB-A Host Port:** Accepts standard USB HID keyboards, mice, and MIDI devices
- **Parsed HID Events:** Keyboard, mouse, and MIDI data arrive as ready-to-use structures
- **Raw HID Fallback:** Unrecognized devices can still be read as raw HID reports
- **Selectable Protocol:** I²C (default), UART, or SPI, chosen with a jumper
- **Configurable I²C Address:** Default 0x50, changeable to any value from 0x08 to 0x77
- **Interrupt Output:** Signals your MCU when new data is ready, so you do not have to poll
- **Dual Qwiic Connectors:** Solderless daisy-chaining for I²C setups
- **14-Pin Breakout Header:** Direct access to I²C, SPI, UART, IO0, and RESET
- **USB Overcurrent Protection:** Output capped at 260 mA with a FAULT indicator
- **Built on the ESP32-S3FH4R2:** Dual-core, 4 MB flash, 2 MB PSRAM
- **Arduino Library:** Handles USB parsing and protocol framing for you

---

## You may also need

<QuickLink 
  title="Qwiic cable" 
  description="Qwiic (formerly easyC) compatible cables with connectors on both ends, available in various lengths."
  url="https://soldered.com/product/easyc-cable/"
  image="/img/333311.webp" 
/>