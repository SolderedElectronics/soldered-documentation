---
slug: /inputronic-keyboard/micropython/live-typing
title: Inputronic Keyboard - Live typing to Serial
sidebar_label: Typing to Serial
id: inputronic-keyboard-micropython-3
hide_title: False
---

## Overview

This example demonstrates live typing using the Inputronic Keyboard with output to the **serial console**. Characters are printed in real-time as you type, making this ideal for terminal-style input and debugging.

---

## Initialization

Import the module, create the keyboard object, and initialize it. If the keyboard isn't found, the program halts.

```python
from inputronic_keyboard import InputronicKeyboard
from time import sleep

kbd = InputronicKeyboard()

if not kbd.begin():
    print("Keyboard not found!")
else:
    print("Keyboard ready! Start typing...")
```

---

## Handling Special Keys

Inside the main loop, after reading each key event with `readMappedEvent()`, special keys are handled by comparing the label string. Release events and modifier-only keys (CAPS, SHIFT) are skipped.

```python
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
```

## Key Behavior

| Key | Action |
|-----|--------|
| **Printable keys** | Printed to console |
| **SPACE** | Prints space character |
| **BACK** | Terminal-style backspace (`\b \b`) |
| **ENTER** | Prints newline |
| **CAPS** | Toggles upper/lower keymap (internal) |
| **SHIFT** | Modifier (handled automatically) |

---

## Printing Characters

For all remaining keys, `labelToChar()` converts the label to a printable character with SHIFT applied automatically, and prints it to the console.

```python
char = kbd.labelToChar(label, applyShift=True)
if char:
    print(char, end="")
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

<InfoBox>
**SHIFT and CAPS** logic is handled internally by the module. When SHIFT is held:
- Letters have their case inverted (CAPS XOR SHIFT)
- Numbers and symbols use the shift map (e.g., '1' becomes '!')
</InfoBox>

---

## String Input Helper

The module also provides a convenient blocking `stringInput()` function for collecting text in one call:

```python
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

<!-- TODO: Add screenshot of console output -->
<!-- <CenteredImage src="/img/inputronic-keyboard/serialtype.png" alt="Live typing console output" caption="Live typing in MicroPython console" width="800px"/> -->

## Full Example

<QuickLink
    title="serial_type.py"
    description="Demonstrates live typing with the Inputronic Keyboard, printing characters to the console in real-time with support for SPACE, BACK, ENTER, SHIFT, and CAPS keys."
    url="https://github.com/SolderedElectronics/Soldered-MicroPython-Modules/tree/main/Communication/Inputronic-KEYBOARD/Inputronic-KEYBOARD/Examples/serial_type.py"
/>
