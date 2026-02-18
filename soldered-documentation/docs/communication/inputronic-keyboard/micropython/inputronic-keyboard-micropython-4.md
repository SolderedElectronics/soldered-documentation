---
slug: /inputronic-keyboard/micropython/oled-type
title: Inputronic Keyboard - Live typing to OLED
sidebar_label: Typing to OLED
id: inputronic-keyboard-micropython-4
hide_title: False
---

## Overview

This example demonstrates live typing using the Inputronic Keyboard with output to an **OLED display** (SSD1306-compatible). Text is rendered in real-time on the screen as you type.

---

## Hardware Requirements

- **Inputronic Keyboard** (I²C address: 0x34)
- **SSD1306 OLED Display** (I²C address: 0x3C)
- Both devices connected via Qwiic/easyC or I²C

<InfoBox>This example uses the **Soldered OLED Display MicroPython module**. You can download it from the Soldered MicroPython Modules repository.</InfoBox>

---

## Initialization

Both the OLED display and the keyboard are initialized over I²C. A string buffer holds the typed text.

```python
from inputronic_keyboard import InputronicKeyboard
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
from time import sleep

# I2C and OLED setup
i2c = I2C(0, scl=Pin(22), sda=Pin(21))
display = SSD1306_I2C(128, 64, i2c)

# Keyboard setup
kbd = InputronicKeyboard()

# Text buffer
typed_text = ""

if not kbd.begin():
    print("Keyboard not found!")
else:
    print("Keyboard and OLED ready!")
    redrawOled()
```

---

## Redrawing the Display

A helper function clears the OLED and reprints the entire text buffer. This is called whenever the buffer changes.

```python
def redrawOled():
    display.fill(0)

    # Simple text rendering with line wrapping
    lines = typed_text.split('\n')
    y = 0
    for line in lines[:8]:  # Max 8 lines on 64px display with 8px font
        display.text(line[:16], 0, y, 1)  # Max 16 chars per line
        y += 8

    display.show()
```

---

## Handling Key Events

The main loop reads key events and appends characters to the `typed_text` buffer. Special keys (SPACE, BACK, ENTER) are handled individually, and the display is only redrawn when the buffer actually changes.

```python
while True:
    changed = False

    while kbd.eventsAvailable() > 0:
        isRelease, row, col, label = kbd.readMappedEvent()

        if isRelease or not label:
            continue

        if label == "SPACE":
            typed_text += " "
            changed = True
            continue

        if label == "BACK":
            if len(typed_text) > 0:
                typed_text = typed_text[:-1]
                changed = True
            continue

        if label == "ENTER":
            typed_text += "\n"
            changed = True
            continue

        if label in ["CAPS", "SHIFT"]:
            continue

        char = kbd.labelToChar(label, applyShift=True)
        if char:
            typed_text += char
            changed = True

    if changed:
        redrawOled()

    sleep(0.001)
```

<InfoBox>
The display is only redrawn when `changed` is true. This avoids unnecessary I²C traffic and display flicker.
</InfoBox>

<!-- TODO: Add photo of OLED display with typed text -->
<!-- <CenteredImage src="/img/inputronic-keyboard/oledtype.png" alt="OLED live typing" caption="Live typing displayed on SSD1306 OLED" width="800px"/> -->

## Full Example

<QuickLink
    title="oled_type.py"
    description="Demonstrates live typing on an SSD1306 OLED display using the Inputronic Keyboard, with real-time rendering, backspace, and newline support."
    url="https://github.com/SolderedElectronics/Soldered-MicroPython-Modules/tree/main/Communication/Inputronic-KEYBOARD/Inputronic-KEYBOARD/Examples/oled_type.py"
/>
