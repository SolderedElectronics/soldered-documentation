---
slug: /inputronic-keyboard/how-it-works
title: Inputronic Keyboard - How it works
sidebar_label: How it works
id: inputronic-keyboard-how-it-works
hide_title: false
---

The Inputronic Keyboard is built around the [**TCA8418**](https://www.ti.com/product/TCA8418) by Texas Instruments. All communication with the board goes through the TCA8418 over **I²C**.

<CenteredImage src="/img/inputronic_keyboard/333360_highlighted.png" alt="TCA8418" caption="TCA8418" width="500px"/>

---

## Datasheet

The official TCA8418 datasheet:

<QuickLink
    title="TCA8418 Datasheet"
    description="Detailed technical documentation for the TCA8418 keypad scanner"
    url="https://www.ti.com/lit/ds/symlink/tca8418.pdf"
/>

---

## How the scanner works

The TCA8418 is a keypad scanning controller that continuously monitors a matrix of buttons arranged in rows and columns. The chip configures column pins as outputs (driven low) and row pins as inputs with internal pull-up resistors. When a key is pressed, it creates an electrical connection between a row and column, pulling the row input low and alerting the chip to scan the matrix. The scanner then systematically drives one column at a time while reading all row inputs to determine exactly which key was pressed. Each key press and release is debounced by a 50 µs hardware filter and stored in a **10-event FIFO** buffer with a press/release flag. The chip pulls its interrupt line low to signal the microcontroller that events are ready, so the host can read them via I²C without polling.

<InfoBox>The TCA8418 supports up to **80 keys** in an 8×10 matrix configuration and can detect multiple simultaneous key presses accurately!</InfoBox>

---

## I²C communication

The Inputronic Keyboard uses the I²C protocol to communicate with the microcontroller. It operates with a fixed I²C address of **0x34**. Upon request, the chip responds with key event data from its FIFO buffer, including which key was pressed or released. The board supports I²C speeds up to **1 MHz** (Fast Mode Plus), but you can use our library to interface with it more easily.

---

## Key features explained

### Event FIFO

The 10-byte FIFO stores key press and release events. Each event contains:
- **Key value** (7 bits): Which key was pressed (1-80 for matrix keys, 97-114 for GPIO)
- **Press/Release flag** (1 bit): Indicates whether the key was pressed (1) or released (0)

The FIFO shifts as you read, so multiple events can be processed one at a time.

### Hardware debouncing

Mechanical switches naturally "bounce" when pressed, creating multiple electrical signals for a single press. The TCA8418 has a built-in 50 µs filter that eliminates bounce signals so each key press registers only once.

### Keypad lock/unlock

The chip includes a programmable security feature that requires a two-key sequence to unlock:
- Program two specific unlock keys
- Set the time window between key presses (0-7 seconds)
- Optionally configure an interrupt mask timer for LCD backlight control

### Power consumption

- **Idle mode**: 10 µA
- **Active scan**: 50-90 µA
- **Sleep mode**: 3 µA

The internal oscillator shuts off when no keys are pressed. Operating temperature: -40°C to 85°C.
