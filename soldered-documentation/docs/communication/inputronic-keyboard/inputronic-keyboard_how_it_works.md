---
slug: /inputronic-keyboard/how-it-works 
title: Inputronic Keyboard - How it works
sidebar_label: How it works
id: inputronic-keyboard-how-it-works 
hide_title: False
---  

The Inputronic Keyboard is built around the [**TCA8418**](https://www.ti.com/product/TCA8418) chip by Texas Instruments. When using our board, you are essentially communicating with the onboard TCA8418 directly via **I²C communication**.

<CenteredImage src="/img/inputronic-keyboard/tca8418_onboard.jpg" alt="TCA8418 chip on board" caption="TCA8418 chip on the board" width="1000px"/>

---

## Datasheet

For an in-depth look at technical specifications, refer to the official TCA8418 Datasheet

<QuickLink
    title="TCA8418 Datasheet"
    description="Detailed technical documentation for the TCA8418 keypad scanner"
    url="https://www.ti.com/lit/ds/symlink/tca8418.pdf"
/>

---

## How the scanner works

The TCA8418 is a keypad scanning controller that continuously monitors a matrix of buttons arranged in rows and columns. The chip configures column pins as outputs (driven low) and row pins as inputs with internal pull-up resistors. When a key is pressed, it creates an electrical connection between a row and column, pulling the row input low and alerting the chip to scan the matrix. The scanner then systematically drives one column at a time while reading all row inputs to determine exactly which key was pressed. Each key press and release is automatically debounced using a 50 µs hardware filter and stored in a **10-event FIFO** buffer along with whether it was a press or release. The chip generates an interrupt signal to notify your microcontroller that key events are ready to be read via I²C, allowing efficient event-driven operation without constant polling.

<InfoBox>The TCA8418 supports up to **80 keys** in an 8×10 matrix configuration and can detect multiple simultaneous key presses accurately!</InfoBox>

---

## I²C communication

The Inputronic Keyboard uses the I²C protocol to communicate with the microcontroller. It operates with a fixed I²C address of **0x34**. Upon request, the chip responds with key event data from its FIFO buffer, including which key was pressed or released. The board supports I²C speeds up to **1 MHz** (Fast Mode Plus), but you can use our library to interface with it more easily.

---

## Key Features Explained

### Event FIFO

The 10-byte FIFO stores key press and release events. Each event contains:
- **Key value** (7 bits): Which key was pressed (1–80 for matrix keys, 97–114 for GPIO)
- **Press/Release flag** (1 bit): Indicates whether the key was pressed (1) or released (0)

The FIFO automatically shifts as you read events, making it easy to process multiple key presses in sequence.

### Hardware Debouncing

Mechanical switches naturally "bounce" when pressed, creating multiple electrical signals for a single press. The TCA8418 includes integrated hardware debouncing with a 50 µs filter that eliminates these false signals, ensuring each key press is registered only once.

### Keypad Lock/Unlock

The chip includes a programmable security feature that requires a two-key sequence to unlock:
- Program two specific unlock keys
- Set the time window between key presses (0–7 seconds)
- Optionally configure an interrupt mask timer for LCD backlight control

This feature is useful for implementing device security or preventing accidental key presses.

### Power Efficiency

The TCA8418 is designed for battery-powered applications:
- **Idle mode**: 10 µA when waiting for key press
- **Active scan**: 50–90 µA during key scanning
- **Sleep mode**: 3 µA in deep sleep

The internal oscillator automatically turns off when no keys are pressed, minimizing power consumption.