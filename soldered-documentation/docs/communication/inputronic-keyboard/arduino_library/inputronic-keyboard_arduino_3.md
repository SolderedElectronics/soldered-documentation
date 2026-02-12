---
slug: /inputronic-keyboard/arduino/serial-type 
title: Inputronic Keyboard - Live typing to Serial
sidebar_label: Typing to Serial
id: inputronic-keyboard-arduino-3 
hide_title: False
---

## Overview

This example demonstrates live typing using the Inputronic Keyboard with output to the **Serial Monitor**. Characters are printed in real-time as you type, making this ideal for terminal-style input and debugging.

---

## Key Behavior

| Key | Action |
|-----|--------|
| **Printable keys** | Printed to Serial |
| **SPACE** | Prints space character |
| **BACK** | Terminal-style backspace (`\b \b`) |
| **ENTER** | Prints newline |
| **CAPS** | Toggles upper/lower keymap (internal) |
| **SHIFT** | Modifier (handled automatically) |

<InfoBox>
**SHIFT and CAPS** logic is handled internally by the library. When SHIFT is held:
- Letters have their case inverted (CAPS XOR SHIFT)
- Numbers and symbols use the shift map (e.g., '1' becomes '!')
</InfoBox>

---

## Complete Example

```cpp
#include <Arduino.h>
#include "SOLDERED-Inputronic-Keyboard.h"

InputronicKeyboard kbd;

void setup(){
    Serial.begin(115200);
    
    if(!kbd.begin()){
        Serial.println("Keyboard not found!");
        while(1);
    }
    
    Serial.println("Start typing:");
}

void loop(){
    while(kbd.eventsAvailable() > 0){
        bool isRelease = false;
        uint8_t row = 0, col = 0;
        const char *label = nullptr;
        
        if(!kbd.readMappedEvent(isRelease, row, col, label))
            break;
            
        if(isRelease || !label)
            continue;
        
        // Handle special keys
        if(!strcmp(label, "SPACE")){
            Serial.print(' ');
            continue;
        }
        
        if(!strcmp(label, "BACK")){
            Serial.print("\b \b");
            continue;
        }
        
        if(!strcmp(label, "ENTER")){
            Serial.println();
            continue;
        }
        
        // CAPS and SHIFT are modifiers only
        if(!strcmp(label, "CAPS") || !strcmp(label, "SHIFT"))
            continue;
        
        // Print printable characters (SHIFT applied automatically)
        char ch;
        if(kbd.labelToChar(label, ch, true)){
            Serial.print(ch);
        }
    }
    
    delay(1);
}
```
<!-- 
<CenteredImage src="/img/tca8418/serial-type-output.png" alt="Serial Monitor live typing" caption="Live typing output in Serial Monitor" width="500px"/>
-->