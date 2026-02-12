---
slug: /inputronic-keyboard/overview
title: Inputronic Keyboard - Overview
sidebar_label: Overview
id: inputronic-keyboard-overview 
hide_title: False
pagination_prev: null
---

## Inputronic Keyboard

The **Inputronic Keyboard** is a versatile keypad scanning breakout board featuring the TCA8418 I²C controller chip. It can scan up to **80 buttons** using an 8×10 or 10×8 keypad matrix, with a **10-event FIFO** for storing key presses and releases. The board supports both keypad matrix scanning and general-purpose I/O operation, with hardware debouncing and programmable keypad lock/unlock sequences. This board uses the **I²C communication protocol** with a fixed address of **0x34**. It has 2 onboard **Qwiic ports** for easy integration.

<CenteredImage src="/img/inputronic-keyboard/333360.jpg" alt="Inputronic Keyboard" caption="Inputronic Keyboard" width="1000px" />

---

## Which products is this documentation for?

<QuickLink
  title="Inputronic Keyboard"
  description="333360"
  url="https://soldered.com/product/inputronic-keyboard/"
  image="/img/inputronic-keyboard/333360f.jpg"
/>

---

## Key Features

- **80-Key Support:** Configure up to 18 GPIOs in an 8×10 or 10×8 matrix
- **Flexible Configuration:** Each pin can be keypad row/column or GPIO
- **10-Event FIFO:** Stores key press and release events with overflow protection
- **Hardware Debouncing:** Integrated 50 µs debounce timing
- **Keypad Lock/Unlock:** Programmable two-key unlock sequence
- **I²C Interface:** Up to 1 MHz Fast Mode Plus communication
- **Dual Qwiic Connectors:** Solderless, plug-and-play connectivity
- **Wide Voltage Range:** 1.65V to 3.6V operation
- **Ultra-Low Power:** 3 µA standby current
- **ESD Protection:** 2000V HBM, 1000V CDM on all pins
- **Arduino & MicroPython Libraries:** Easy integration and quick prototyping

---

## You may also need

<QuickLink 
  title="Qwiic cable" 
  description="Qwiic (formerly easyC) compatible cables with connectors on both ends, available in various lengths."
  url="https://soldered.com/product/easyc-cable/"
  image="/img/333311.webp" 
/>
