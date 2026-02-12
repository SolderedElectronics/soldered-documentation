---
slug: /inputronic-keyboard/micropython/oled-type 
title: Inputronic Keyboard - Live typing to OLED
sidebar_label: Typing to OLED
id: inputronic-keyboard-micropython-4 
hide_title: False
---

This example demonstrates live typing using the Inputronic Keyboard with output to an **OLED display** (SSD1306-compatible). Text is rendered in real-time on the screen as you type.

## Hardware Requirements

- **Inputronic Keyboard** (I²C address: 0x34)
- **SSD1306 OLED Display** (I²C address: 0x3C)
- Both devices connected via Qwiic/easyC or I²C

<InfoBox>
This example uses the **Soldered OLED Display MicroPython module**. You can download it from the Soldered MicroPython Modules repository.
</InfoBox>

---

## Key Features

- **Real-time rendering**: Text updates immediately on the OLED
- **Newline support**: ENTER key inserts line breaks
- **Backspace**: Removes the last character from the buffer
- **SHIFT and CAPS**: Handled automatically by the module

---

## Display Helper Function

The example includes a helper function to render text with proper line wrapping:

```python
def redrawOled(display, text):
    display.fill(0)  # Clear display
    display.text(text, 0, 0, 1)  # Draw text
    display.show()  # Update screen
```

---

## Full OLED Typing Example

```python
# FILE: oled-type.py
# AUTHOR: Soldered
# BRIEF: Live typing example with OLED display output
# WORKS WITH: Inputronic Keyboard (333360) + OLED Display

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

def redrawOled():
    """Clear and redraw the OLED with current text"""
    display.fill(0)
    
    # Simple text rendering (wrap lines manually if needed)
    lines = typed_text.split('\n')
    y = 0
    for line in lines[:8]:  # Max 8 lines on 64px display with 8px font
        display.text(line[:16], 0, y, 1)  # Max 16 chars per line
        y += 8
    
    display.show()

# Initialize
if not kbd.begin():
    print("Keyboard not found!")
else:
    print("Keyboard and OLED ready!")
    redrawOled()
    
    # Main loop
    while True:
        changed = False
        
        # Process all pending events
        while kbd.eventsAvailable() > 0:
            isRelease, row, col, label = kbd.readMappedEvent()
            
            if isRelease or not label:
                continue
            
            # Handle special keys
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
            
            # Skip modifiers
            if label in ["CAPS", "SHIFT"]:
                continue
            
            # Add printable characters
            char = kbd.labelToChar(label, applyShift=True)
            if char:
                typed_text += char
                changed = True
        
        # Update display only when text changes
        if changed:
            redrawOled()
        
        sleep(0.001)
```

<!-- TODO: Add photo of OLED display with typed text -->
<!-- <CenteredImage src="/img/tca8418/mp-oled-type.jpg" alt="OLED live typing" caption="Live typing displayed on SSD1306 OLED" width="500px"/> -->

---

## Display Update Optimization

<WarningBox>
Only call `display.show()` when the text changes to reduce unnecessary screen updates and I²C traffic!
</WarningBox>

The example tracks changes with a `changed` flag:

```python
changed = False

# ... process keys ...

if label == "SPACE":
    typed_text += " "
    changed = True

# Only update display if something changed
if changed:
    redrawOled()
```

---

## Advanced: Custom Text Wrapping

For better text wrapping and scrolling, you can implement a more sophisticated rendering function:

```python
def redrawOledAdvanced(display, text, max_lines=8, max_chars=16):
    """Advanced text rendering with automatic wrapping"""
    display.fill(0)
    
    # Split into words and wrap
    words = text.split(' ')
    lines = []
    current_line = ""
    
    for word in words:
        if len(current_line + word) <= max_chars:
            current_line += word + " "
        else:
            lines.append(current_line.strip())
            current_line = word + " "
    
    if current_line:
        lines.append(current_line.strip())
    
    # Display last N lines (scrolling effect)
    display_lines = lines[-max_lines:]
    y = 0
    for line in display_lines:
        display.text(line, 0, y, 1)
        y += 8
    
    display.show()
```

---

## Related Examples

<QuickLink
    title="Serial Live Typing Example"
    description="For console output instead of OLED, see the live typing example"
    url="/documentation/inputronic-keyboard/micropython/live-typing"
/>