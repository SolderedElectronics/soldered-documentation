---
slug: /inputronic-keyboard/arduino/oled-type 
title: Inputronic Keyboard - Live typing to OLED
sidebar_label: Typing to OLED
id: inputronic-keyboard-arduino-4 
hide_title: False
---

## Overview

This example demonstrates live typing using the Inputronic Keyboard with output to an **OLED display** (SSD1306-compatible). Text is rendered in real-time on the screen as you type.

---

## Hardware Requirements

- **Inputronic Keyboard** (I²C address: 0x34)
- **SSD1306 OLED Display** (I²C address: 0x3C)
- Both devices connected via Qwiic/easyC or I²C

<InfoBox>
This example uses the **Soldered OLED Display library**. You can install it from the Arduino Library Manager or GitHub.
</InfoBox>

---

## Key Features

- **Real-time rendering**: Text updates immediately on the OLED
- **Newline support**: ENTER key inserts line breaks
- **Backspace**: Removes the last character from the buffer
- **SHIFT and CAPS**: Handled automatically by the library

---

## Complete Example

```cpp
#include <Arduino.h>
#include <Wire.h>
#include <OLED-Display-SOLDERED.h>
#include "SOLDERED-Inputronic-Keyboard.h"

#define SCREEN_WIDTH   128
#define SCREEN_HEIGHT   64
#define SCREEN_ADDRESS  0x3C

OLED_Display display;
InputronicKeyboard kbd;

String typedText;

void redrawOled(){
    display.clearDisplay();
    display.setCursor(0, 0);
    display.print(typedText);
    display.display();
}

void setup(){
    Serial.begin(115200);
    
    if(!display.begin()){
        Serial.println("OLED not found!");
        while(1);
    }
    
    display.clearDisplay();
    display.setTextSize(1);
    display.setTextColor(SSD1306_WHITE);
    display.display();
    
    typedText.reserve(256);
    
    if(!kbd.begin()){
        Serial.println("Keyboard not found!");
        while(1);
    }
    
    redrawOled();
}

void loop(){
    bool changed = false;
    
    while(kbd.eventsAvailable() > 0){
        bool isRelease = false;
        uint8_t row = 0, col = 0;
        const char *label = nullptr;
        
        if(!kbd.readMappedEvent(isRelease, row, col, label))
            break;
            
        if(!label || isRelease)
            continue;
        
        if(!strcmp(label, "SPACE")){
            typedText += ' ';
            changed = true;
            continue;
        }
        
        if(!strcmp(label, "BACK")){
            if(typedText.length() > 0){
                typedText.remove(typedText.length() - 1);
                changed = true;
            }
            continue;
        }
        
        if(!strcmp(label, "ENTER")){
            typedText += '\n';
            changed = true;
            continue;
        }
        
        if(!strcmp(label, "CAPS") || !strcmp(label, "SHIFT"))
            continue;
        
        char ch;
        if(kbd.labelToChar(label, ch, true)){
            typedText += ch;
            changed = true;
        }
    }
    
    if(changed){
        redrawOled();
    }
    
    delay(1);
}
```

<!--
<CenteredImage src="/img/tca8418/oled-type-example.jpg" alt="OLED live typing" caption="Live typing displayed on SSD1306 OLED" width="500px"/>
-->

---

## Additional Examples

<QuickLink
    title="Inkplate E-paper Example"
    description="For e-paper displays like Inkplate, see the InkplateType.ino example in the library. It demonstrates how to minimize refresh cycles for e-paper longevity."
    url="https://github.com/SolderedElectronics/Soldered-Inputronic-Keyboard-Arduino-Library"
/>

---

## Key Functions Reference

### Text Buffer Management

```cpp
String typedText;              // Store all typed characters
typedText += ch;               // Append character
typedText.remove(length - 1);  // Remove last character (backspace)
```

### Display Update

```cpp
display.clearDisplay();        // Clear framebuffer
display.setCursor(0, 0);       // Reset cursor position
display.print(typedText);      // Draw text
display.display();             // Update screen
```

<WarningBox>
Only call `display.display()` when the text changes to reduce unnecessary screen updates and I²C traffic!
</WarningBox>