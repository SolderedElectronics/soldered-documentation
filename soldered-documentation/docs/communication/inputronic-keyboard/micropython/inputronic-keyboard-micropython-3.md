---
slug: /inputronic-keyboard/micropython/live-typing 
title: Inputronic Keyboard - Live typing to Serial
sidebar_label: Typing to Serial
id: inputronic-keyboard-micropython-3 
hide_title: False
---

This example demonstrates live typing using the Inputronic Keyboard with output to the serial console.

## Key Behavior

| Key | Action |
|-----|--------|
| **Printable keys** | Printed to console |
| **SPACE** | Prints space character |
| **BACK** | Removes last character (backspace) |
| **ENTER** | Prints newline |
| **CAPS** | Toggles upper/lower keymap (internal) |
| **SHIFT** | Modifier (handled automatically) |

<InfoBox>
**SHIFT and CAPS** logic is handled internally by the module. When SHIFT is held:
- Letters have their case inverted (CAPS XOR SHIFT)
- Numbers and symbols use the shift map (e.g., '1' becomes '!')
</InfoBox>

---

## String Input Helper

The module provides a convenient `stringInput()` function for collecting text:

```python
# Collect up to 64 characters, end on ENTER, backspace on BACK
text = kbd.stringInput(maxLen=64, endLabel="ENTER", backspaceLabel="BACK")
print("You typed: {}".format(text))
```

<FunctionDocumentation
    functionName="kbd.stringInput(maxLen, timeout, endLabel, backspaceLabel)"
    description="Blocking function that collects keyboard input until endLabel is pressed or timeout expires"
    returnDescription="String containing all typed characters"
    parameters={[
        { type: 'int', name:'maxLen', description: "Maximum string length (default: 64)" },
        { type: 'int', name:'timeout', description: "Timeout in milliseconds, 0=no timeout (default: 0)" },
        { type: 'str', name:'endLabel', description: "Key that ends input (default: 'ENTER')" },
        { type: 'str', name:'backspaceLabel', description: "Key used for backspace (default: 'BACK')" }
    ]}
/>

---

## Full Live Typing Example

This example demonstrates real-time character-by-character typing to the console:

```python
# FILE: live-typing.py
# AUTHOR: Soldered
# BRIEF: Live typing example that prints characters to console in real-time
# WORKS WITH: Inputronic Keyboard: www.solde.red/333360

from inputronic_keyboard import InputronicKeyboard
from time import sleep

# Create keyboard instance
kbd = InputronicKeyboard()

# Initialize keyboard
if not kbd.begin():
    print("Keyboard not found! Check connection.")
else:
    print("Keyboard ready! Start typing...\n")
    
    # Main typing loop
    while True:
        # Process all pending events
        while kbd.eventsAvailable() > 0:
            isRelease, row, col, label = kbd.readMappedEvent()
            
            # Only process key presses
            if isRelease or not label:
                continue
            
            # Handle special keys
            if label == "SPACE":
                print(" ", end="")
                continue
            
            if label == "BACK":
                print("\b \b", end="")  # Terminal backspace
                continue
            
            if label == "ENTER":
                print()  # New line
                continue
            
            # CAPS and SHIFT are modifiers only
            if label in ["CAPS", "SHIFT"]:
                continue
            
            # Print printable characters (SHIFT applied automatically)
            char = kbd.labelToChar(label, applyShift=True)
            if char:
                print(char, end="")
        
        sleep(0.001)
```

---

## String Input Example

This example uses the blocking `stringInput()` helper for easier text collection:

```python
# FILE: string-input.py
# AUTHOR: Soldered
# BRIEF: Example using the stringInput() helper function
# WORKS WITH: Inputronic Keyboard: www.solde.red/333360

from inputronic_keyboard import InputronicKeyboard

# Create and initialize keyboard
kbd = InputronicKeyboard()

if not kbd.begin():
    print("Keyboard not found!")
else:
    print("Type your name and press ENTER:")
    
    # Collect string (blocking until ENTER is pressed)
    name = kbd.stringInput(maxLen=32, endLabel="ENTER", backspaceLabel="BACK")
    
    print("\nHello, {}!".format(name))
    
    print("\nType a message (64 chars max):")
    message = kbd.stringInput(maxLen=64)
    
    print("\nYou wrote:")
    print(message)
```

<!-- TODO: Add screenshot of console output -->
<!-- <CenteredImage src="/img/tca8418/mp-live-typing.png" alt="Live typing console output" caption="Live typing in MicroPython console" width="500px"/> -->

---

## Additional Functions

### Get Last Pressed Key

```python
label = kbd.getLastKeyLabel()
if label:
    print("Last key pressed: {}".format(label))
```

<FunctionDocumentation
    functionName="kbd.getLastKeyLabel()"
    description="Returns the label of the last key that was pressed"
    returnDescription="String containing the key label, or None if no key has been pressed"
    parameters={[]}
/>

### Check Active Keymap

```python
keymap = kbd.getActiveKeymap()
# Returns 0 for UPPER, 1 for LOWER
print("Current keymap: {}".format("UPPER" if keymap == 0 else "LOWER"))
```

<FunctionDocumentation
    functionName="kbd.getActiveKeymap()"
    description="Returns the currently active keymap ID"
    returnDescription="Integer: 0 for UPPER keymap, 1 for LOWER keymap"
    parameters={[]}
/>

### Count Held Keys

```python
count = kbd.getHeldCount()
print("{} keys are currently pressed".format(count))
```

<FunctionDocumentation
    functionName="kbd.getHeldCount()"
    description="Returns the number of keys currently being held down"
    returnDescription="Integer representing the count of pressed keys"
    parameters={[]}
/>

