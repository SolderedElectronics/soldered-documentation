---
slug: /lcd-i2c/arduino/examples 
title: Using the LCD display (examples)
id: lcd-i2c-arduino-2 
hide_title: False
---

This page contains some simple examples with function documentation on how to use the LCD display in different ways.

---

## Initialization

To use the LCD display include the **required library**, create the **LCD object** and **initialize** the LCD in the `setup.()` function with `begin.()`. **Backlight** is also initialized here.

<InfoBox> Our library uses the [**Wire.h**](https://docs.arduino.cc/language-reference/en/functions/communication/wire/) library!</InfoBox>

```cpp
// Include the library
#include "16x2-LCD-SOLDERED.h"

LCD lcd; // Create the LCD object

void setup()
{
    lcd.begin();     // Initialize LCD
    lcd.backlight(); // Turn the backlight on
}
// ...
```

<FunctionDocumentation
  functionName="lcd.begin()"
  description="Calls the Wire.begin() function which initializes the Wire library and joins the I2C bus as a controller or a peripheral."
  returnDescription="None"
  parameters={[]}
/>

---

## Hello World

This code snipper shows how the **cursor** is used with the `setCursor()` function and how we can `print()` out words and sentences.

```cpp
// Include the library
#include "16x2-LCD-SOLDERED.h"

LCD lcd; // Define LCD object

void setup()
{
    lcd.begin();     // Initialize LCD
    lcd.backlight(); // Turn the backlight on
}

void loop()
{
    lcd.print("     Hello"); // Prints Hello on the LCD 
    lcd.setCursor(5, 1);     // set cursor to 5th character in line 1
    lcd.print("World!");     // Prints World! on the LCD
    delay(500);

    lcd.clear();     // Clear the LCD
    delay(500);
}
```

<InfoBox>Numbering of both **row** and **column** starts at **0**. For printing a character in the first column and the first row we would set the cursor to (0, 0) which is also the **default position**. </InfoBox>

<FunctionDocumentation
  functionName="lcd.setCursor(uint8_t col, uint8_t row)"
  description="Sets the cursor position on the LCD display by updating the DDRAM (Display Data RAM) address, which determines where the next character will appear. The parameters col and row specifiy the column (0 - 15) and row (0 - 1)"
  returnDescription="None"
  parameters={[]}
/>

<QuickLink 
  title="Hello_World.ino" 
  description="Example file for a Hello World printout using the LCD I2C display"
  url="https://github.com/SolderedElectronics/Soldered-16x2-LCD-Arduino-Library/blob/main/examples/Custom_Chars/Custom_Chars.ino" 
/>

---

## Custom Characters

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
  functionName="lcd.createChar(uint8_t location, uint8_t charmap[])"
  description="Stores a custom character in the LCD's CGRAM (Character Generator RAM). The 'location' parameter specifies which of the 8 slots (0 - 7) to store the character, and 'charmap' is an 8-byte array defining its pixel pattern."
  returnDescription="None"
  parameters={[]}
/>

<QuickLink 
  title="Custom_Chars.ino" 
  description="Example file for displaying custom characters using the LCD I2C display"
  url="https://github.com/SolderedElectronics/Soldered-16x2-LCD-Arduino-Library/blob/main/examples/Custom_Chars/Custom_Chars.ino" 
/>