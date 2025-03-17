---
slug: /lcd-i2c/arduino/examples 
title: Basic Examples
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

This code snippet shows how the **cursor** is used with the `setCursor()` function and how we can `print()` out words and sentences.

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
  functionName="lcd.setCursor()"
  description="Sets the position of the cursor on the LCD display. The parameters 'col' and 'row' determine the column and row where the next character will be displayed. The cursor is positioned by updating the DDRAM address of the LCD."
  returnDescription="None"
  parameters={[
    { type: 'uint8_t', name: 'col', description: "The column position (0-15) where the cursor will be placed." },
    { type: 'uint8_t', name: 'row', description: "The row position (0-1) where the cursor will be placed." }
  ]}
/>

<QuickLink 
  title="Hello_World.ino" 
  description="Example file for a Hello World printout using the LCD I2C display"
  url="https://github.com/SolderedElectronics/Soldered-16x2-LCD-Arduino-Library/blob/main/examples/Custom_Chars/Custom_Chars.ino" 
/>
