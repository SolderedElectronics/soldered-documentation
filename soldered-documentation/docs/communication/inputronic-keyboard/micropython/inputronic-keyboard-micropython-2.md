---
slug: /inputronic-keyboard/micropython/reading-keys
title: Inputronic Keyboard - Reading key events
sidebar_label: Reading key events
id: inputronic-keyboard-micropython-2
hide_title: False
---

## Connections for this example

<!-- TODO: Add connection image -->

Connect the Inputronic Keyboard to your microcontroller via Qwiic/easyC cable or I²C pins as shown in the Getting Started guide.

---

## Initialization

To use the Inputronic Keyboard, first import the required module, create the keyboard object, and initialize it:

```python
from inputronic_keyboard import InputronicKeyboard

kbd = InputronicKeyboard()

if not kbd.begin():
    print("Keyboard not found! Check connection.")
else:
    print("Keyboard initialized successfully!")
```

<FunctionDocumentation
    functionName="kbd.begin()"
    description="Initializes the TCA8418 keypad controller, configuring the 8×10 matrix and I²C communication"
    returnDescription="Boolean value. True if the keyboard was successfully initialized, False otherwise."
    parameters={[]}
/>

---

## Reading Key Events

The keyboard uses a **10-event FIFO** to store key presses and releases. To read events, first check if any are available, then read and decode them.

```python
while kbd.eventsAvailable() > 0:
    isRelease, row, col, label = kbd.readMappedEvent()

    if not isRelease and label:  # Only process key presses
        print("Key pressed: {} (Row: {}, Col: {})".format(label, row, col))
```

<FunctionDocumentation
    functionName="kbd.eventsAvailable()"
    description="Returns the number of pending events in the FIFO"
    returnDescription="Integer value representing the number of events (0-15)"
    parameters={[]}
/>

<FunctionDocumentation
    functionName="kbd.readMappedEvent()"
    description="Reads one event from the FIFO and decodes it into row, column, and label"
    returnDescription="Tuple: (isRelease, row, col, label) where isRelease is bool, row/col are integers (0-7, 0-9), and label is a string"
    parameters={[]}
/>

---

## Converting Labels to Characters

For printable keys, you can convert the label to a character. The module automatically handles **SHIFT** and **CAPS** behavior.

```python
isRelease, row, col, label = kbd.readMappedEvent()

if not isRelease and label:
    char = kbd.labelToChar(label, applyShift=True)
    if char:
        print("Character: {}".format(char))
```

<FunctionDocumentation
    functionName="kbd.labelToChar(label, applyShift)"
    description="Converts a single-character label to a printable character. Automatically applies SHIFT and CAPS logic."
    returnDescription="String containing a single character, or None if the label is not a printable character"
    parameters={[
        { type: 'str', name:'label', description: "Key label from the keymap" },
        { type: 'bool', name:'applyShift', description: "Whether to apply SHIFT transformations (default: True)" }
    ]}
/>

---

## Checking Key State

You can check if a specific key is currently pressed:

```python
if kbd.isKeyPressed("SHIFT"):
    print("SHIFT is held down")

if kbd.isKeyPressed("A"):
    print("A key is pressed")
```

<FunctionDocumentation
    functionName="kbd.isKeyPressed(label)"
    description="Checks if a specific key is currently being held down"
    returnDescription="Boolean value: True if the key is pressed, False otherwise"
    parameters={[
        { type: 'str', name:'label', description: "Key label to check (e.g., 'SHIFT', 'A', 'ENTER')" }
    ]}
/>

<!-- TODO: Add screenshot of serial output -->
<!-- <CenteredImage src="/img/inputronic-keyboard/keyboardpoll.png" alt="Serial output for keyboard polling" caption="Serial output showing key events" width="800px"/> -->

## Full Example

<QuickLink
    title="keyboard_poll.py"
    description="Polls the keyboard for key events and prints each key press with its label, row, and column to the console."
    url="https://github.com/SolderedElectronics/Soldered-MicroPython-Modules/tree/main/Communication/Inputronic-KEYBOARD/Inputronic-KEYBOARD/Examples/keyboard_poll.py"
/>
