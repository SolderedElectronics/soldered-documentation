---
slug: /lcd-i2c/arduino/custom-characters
title: Custom Characters
id: lcd-i2c-arduino-3
hide_title: False
---

LCD displays with an HD44780 controller support custom characters, which are stored in **CGRAM (Character Generator RAM)**. These characters are defined using an **8-byte array**, where **each byte** represents a **row** of a **5x8 pixel grid**. By setting the pixels with binary values (1 for on, 0 for off), you can design unique symbols like faces, icons, or symbols.

<InfoBox>If you have trouble creating custom characters you can use a [**custom character generator**](https://maxpromer.github.io/LCD-Character-Creator/). </InfoBox>

```cpp
// Include the library
#include "16x2-LCD-SOLDERED.h"

LCD lcd; // create LCD object


uint8_t happy[8] = {
    // happy face
    0b00000, 0b10001, 0b00000, 0b00000, 0b10001, 0b01110, 0b00000, 0b00000,
};

uint8_t wow[8] = {
    // wow face
    0b00000, 0b10001, 0b00000, 0b01110, 0b10001, 0b01110, 0b00000, 0b00000,
};

uint8_t anchor[8] = {
    // anchor bit array
    0b01110, 0b01010, 0b01110, 0b00100, 0b10101, 0b10101, 0b01110, 0b00100};

uint8_t snow[8] = {
    // snow bit array
    0b01000, 0b11101, 0b01011, 0b00001, 0b00100, 0b01110, 0b00100, 0b10000};

void setup()
{
    lcd.begin();     // begin the LCD
    lcd.backlight(); // turn on the backlight

    lcd.createChar(0, happy);  // create happy face on char 0
    lcd.createChar(1, wow);    // create wow face on char 1
    lcd.createChar(2, anchor); //  create anchor bit array on char 2
    lcd.createChar(3, snow);   //  create snow bit array on char 3


    lcd.write(0); // write happy face (char 0)
    lcd.write(1); // write wow face (char 1)
    lcd.write(2); // write anchor bit array (char 2)
    lcd.write(3); // write snow bit array (char 3)
}

void loop()
{
}
```

<FunctionDocumentation
  functionName="lcd.createChar()"
  description="Stores a custom character in the LCD's CGRAM (Character Generator RAM). The 'location' parameter specifies the slot (0-7) where the character will be stored, and 'charmap' is an 8-byte array that defines the pixel pattern of the character."
  returnDescription="None"
  parameters={[
    { type: 'uint8_t', name: 'location', description: "The slot (0-7) in the CGRAM where the custom character will be stored." },
    { type: 'uint8_t[]', name: 'charmap', description: "An 8-byte array representing the pixel pattern of the custom character." }
  ]}
/>


<QuickLink 
  title="Custom_Chars.ino" 
  description="Example file for displaying custom characters using the LCD I2C display"
  url="https://github.com/SolderedElectronics/Soldered-16x2-LCD-Arduino-Library/blob/main/examples/Custom_Chars/Custom_Chars.ino" 
/>