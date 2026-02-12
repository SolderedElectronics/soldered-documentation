---
slug: /inputronic-keyboard/micropython/reading-keys 
title: Inputronic Keyboard - Reading key events
sidebar_label: Reading key events
id: inputronic-keyboard-micropython-2 
hide_title: False
---

This page contains simple examples with function documentation on how to read key events using the Inputronic Keyboard.

## Connections for this example

<!-- TODO: Add connection image -->
<!-- <CenteredImage src="/img/tca8418/mp-connections.jpg" alt="Connections" /> -->

Connect the Inputronic Keyboard to your microcontroller via Qwiic/easyC cable or I²C pins as shown in the Getting Started guide.

---

## Initialization

To use the Inputronic Keyboard, first import the required module and create the keyboard object:

```python
from inputronic_keyboard import InputronicKeyboard

kbd = InputronicKeyboard()
```

---

## Checking for Events

Before reading keys, check if any events are available in the FIFO buffer:

```python
if kbd.eventsAvailable() > 0:
    # Events are ready to be read
    pass
```

<FunctionDocumentation
    functionName="kbd.eventsAvailable()"
    description="Returns the number of pending key events in the FIFO buffer"
    returnDescription="Integer value representing the number of events (0-15)"
    parameters={[]}
/>

---

## Reading Key Events

To read a key event, use the `readMappedEvent()` function. It returns a tuple containing the event information:

```python
isRelease, row, col, label = kbd.readMappedEvent()

if not isRelease and label:  # Only process key presses
    print("Key pressed: {} at row {}, col {}".format(label, row, col))
```

<FunctionDocumentation
    functionName="kbd.readMappedEvent()"
    description="Reads one event from the FIFO and decodes it into row, column, and label"
    returnDescription="Tuple: (isRelease, row, col, label) where isRelease is bool, row/col are integers (0-7, 0-9), and label is a string"
    parameters={[]}
/>

---

## Converting Labels to Characters

For printable keys, convert the label to a character. The library handles **SHIFT** and **CAPS** automatically:

```python
isRelease, row, col, label = kbd.readMappedEvent()

if not isRelease and label:
    char = kbd.labelToChar(label, applyShift=True)
    if char:
        print("Character: {}".format(char))
```

<FunctionDocumentation
    functionName="kbd.labelToChar(label, applyShift)"
    description="Converts a single-character label to a printable character with SHIFT and CAPS logic applied"
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

---

## Full Example

This example continuously polls the keyboard and prints information about each key press:

```python
# FILE: keyboard-poll.py
# AUTHOR: Soldered
# BRIEF: An example showing how to read and display key events from the Inputronic Keyboard
# WORKS WITH: Inputronic Keyboard: www.solde.red/333360

from inputronic_keyboard import InputronicKeyboard
from time import sleep

# Create keyboard instance
kbd = InputronicKeyboard()

# Initialize keyboard
if not kbd.begin():
    print("Keyboard not found! Check connection.")
else:
    print("Keyboard initialized successfully!")
    print("Press any key...\n")
    
    # Main polling loop
    while True:
        # Process all pending events
        while kbd.eventsAvailable() > 0:
            isRelease, row, col, label = kbd.readMappedEvent()
            
            # Only process key presses (ignore releases)
            if not isRelease and label:
                print("PRESS\tRow: {}\tCol: {}\tLabel: {}".format(row, col, label))
                
                # Try to convert to printable character
                char = kbd.labelToChar(label, applyShift=True)
                if char:
                    print("\tChar: '{}'".format(char))
        
        sleep(0.001)  # Small delay to prevent tight polling
```

<!-- TODO: Add screenshot of serial output -->
<!-- <CenteredImage src="/img/tca8418/mp-keyboard-poll.png" alt="Serial output for keyboard polling" caption="Serial output showing key events" width="400px"/> -->

