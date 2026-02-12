---
slug: /inputronic-keyboard/arduino/keyboard-poll 
title: Inputronic Keyboard - Reading key events
sidebar_label: Reading key events
id: inputronic-keyboard-arduino-2 
hide_title: False
---

## Connections for this example
<!-- TODO: Add connection image when available -->
Connect the Inputronic Keyboard to your microcontroller via Qwiic/easyC cable or I²C pins as shown in the Getting Started guide.

---

## Initialization

To use the Inputronic Keyboard, first include the required library, create the keyboard object, and initialize it in the `setup()` function.

```cpp
#include "SOLDERED-Inputronic-Keyboard.h"

InputronicKeyboard kbd;

void setup(){
    Serial.begin(115200);
    if(kbd.begin()){
        Serial.println("Keyboard initialized successfully!");
    }
    else{
        Serial.println("Keyboard not found. Check connection.");
        while(1);
    }
}
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

```cpp
void loop(){
    while(kbd.eventsAvailable() > 0){
        bool isRelease = false;
        uint8_t row = 0, col = 0;
        const char *label = nullptr;
        
        if(kbd.readMappedEvent(isRelease, row, col, label)){
            if(!isRelease && label){  // Only process key presses
                Serial.print("Key pressed: ");
                Serial.print(label);
                Serial.print(" (Row: ");
                Serial.print(row);
                Serial.print(", Col: ");
                Serial.print(col);
                Serial.println(")");
            }
        }
    }
    delay(1);
}
```

<FunctionDocumentation
    functionName="kbd.eventsAvailable()"
    description="Returns the number of pending events in the FIFO"
    returnDescription="Integer value representing the number of events (0-15)"
    parameters={[]}
/>

<FunctionDocumentation
    functionName="kbd.readMappedEvent(isRelease, row, col, label)"
    description="Reads one event from the FIFO and decodes it into row, column, and human-readable label"
    returnDescription="Boolean value. True if an event was successfully read and decoded."
    parameters={[
        { type: 'bool&', name:'isRelease', description: "Output: true if the event is a key release, false if press" },
        { type: 'uint8_t&', name:'row', description: "Output: matrix row (0-7)" },
        { type: 'uint8_t&', name:'col', description: "Output: matrix column (0-9)" },
        { type: 'const char*&', name:'label', description: "Output: pointer to key label string (e.g., 'A', 'ENTER', 'SHIFT')" }
    ]}
/>

---

## Converting Labels to Characters

For printable keys, you can convert the label to a character. The library automatically handles **SHIFT** and **CAPS** behavior.

```cpp
void loop(){
    while(kbd.eventsAvailable() > 0){
        bool isRelease = false;
        uint8_t row = 0, col = 0;
        const char *label = nullptr;
        
        if(kbd.readMappedEvent(isRelease, row, col, label)){
            if(!isRelease && label){
                char ch;
                if(kbd.labelToChar(label, ch, true)){  // true = apply SHIFT
                    Serial.print("Character: ");
                    Serial.println(ch);
                }
            }
        }
    }
    delay(1);
}
```

<FunctionDocumentation
    functionName="kbd.labelToChar(label, ch, applyShift)"
    description="Converts a single-character label to a printable character. Automatically applies SHIFT and CAPS logic."
    returnDescription="Boolean value. True if the label is a printable character."
    parameters={[
        { type: 'const char*', name:'label', description: "Input: key label from keymap" },
        { type: 'char&', name:'ch', description: "Output: resulting character" },
        { type: 'bool', name:'applyShift', description: "Whether to apply SHIFT transformations (default: true)" }
    ]}
/>

<!--
<CenteredImage src="/img/tca8418/serial-keyboard-poll.png" alt="Serial Monitor output" caption="Serial Monitor output showing key events" width="400px"/>
-->