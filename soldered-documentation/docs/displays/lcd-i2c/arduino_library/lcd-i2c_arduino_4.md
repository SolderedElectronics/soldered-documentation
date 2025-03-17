---
slug: /lcd-i2c/arduino/advanced-examples
title: Advanced Examples
id: lcd-i2c-arduino-4
hide_title: False
---


This section covers features like **autoscrolling**, **cursor control**, and **screen shifting**, allowing for dynamic text movement and improved readability. These functions help create smoother user interactions and animated effects on the display.

<WarningBox>Don't forget to initialize the LCD display first!</WarningBox>

---

## Autoscroll

This section demonstrates the use of **autoscrolling** on the LCD. When enabled, new characters automatically shift to the left as they are printed, creating a continuous scrolling effect. The `autoscroll()` function allows for smooth dynamic text flow, while `noAutoscroll()` can be used to stop the effect.

```cpp
void loop()
{
    // Autoscroll
    lcd.setCursor(5, 0); //Set cursor to 6th (starts from 0) place in row, 1st row
    lcd.print(F("Autoscrolling")); //Print text to LCD
    lcd.setCursor(10, 1);   //Set cursor
    lcd.autoscroll();   //Enable autoscroll

    for (int i = 0; i < 10; i++)    //Print first 10 integers
    {
        lcd.print(i);   
        delay(200);
    }
}
```


<FunctionDocumentation
  functionName="lcd.autoscroll()"
  description="Enables automatic scrolling when printing new characters. The display shifts left as new characters are added, creating a scrolling effect."
  returnDescription="None"
  parameters={[]}
/>

<FunctionDocumentation
  functionName="lcd.noAutoscroll()"
  description="Disables automatic scrolling, keeping new characters stationary when printed."
  returnDescription="None"
  parameters={[]}
/>

---

## Horizontal scrolling

This section demonstrates how to shift the displayed content left and right on the LCD screen. The `scrollDisplayLeft()` and `scrollDisplayRight()` functions allow for smooth **horizontal scrolling** of text.

```cpp
void loop()
{
    // Scroll left and right
    lcd.setCursor(10, 0); 
    lcd.print(F("To the left!"));
    for (int i = 0; i < 10; i++)
    {
        lcd.scrollDisplayLeft();    //This command shifts al content to left by 1 place
        delay(200);
    }
    lcd.clear(); //Clear content from LCD
    lcd.print(F("To the right!"));
    for (int i = 0; i < 10; i++)
    {
        lcd.scrollDisplayRight();   //This command shifts al content to right by 1 place
        delay(200);
    }
    lcd.clear();
}
```

<FunctionDocumentation
  functionName="lcd.scrollDisplayLeft()"
  description="Shifts all displayed content one position to the left."
  returnDescription="None"
  parameters={[]}
/>

<FunctionDocumentation
  functionName="lcd.scrollDisplayRight()"
  description="Shifts all displayed content one position to the right."
  returnDescription="None"
  parameters={[]}
/>

---

## Cursor control

This section demonstrates how to control the cursor on the LCD display, including **enabling and disabling** the cursor, making it **blink**, and **hiding** it completely. These functions allow for enhanced text display and interaction on the screen.

```cpp
void loop()
{
  // Cursor
    lcd.setCursor(0, 0);
    lcd.cursor();
    lcd.print(F("Cursor"));
    delay(3000);
    lcd.clear();

    // Cursor blink
    lcd.setCursor(0, 0);
    lcd.blink();    //This command enables cursor blink
    lcd.print(F("Cursor blink"));
    delay(3000);
    lcd.clear();

    // Blink without cursor
    lcd.setCursor(0, 0);
    lcd.noCursor(); //Disable cursor, so it is no longer shown on screen
    lcd.print(F("Just blink"));
    delay(3000);
    lcd.noBlink();  //Stop cursor blinking
    lcd.clear();
}
```

<FunctionDocumentation
  functionName="lcd.cursor()"
  description="Displays the cursor as a solid underscore at the current position."
  returnDescription="None"
  parameters={[]}
/>

<FunctionDocumentation
  functionName="lcd.noCursor()"
  description="Hides the cursor from the display."
  returnDescription="None"
  parameters={[]}
/>

<FunctionDocumentation
  functionName="lcd.blink()"
  description="Makes the cursor blink on and off at its current position."
  returnDescription="None"
  parameters={[]}
/>

<FunctionDocumentation
  functionName="lcd.noBlink()"
  description="Stops the cursor from blinking."
  returnDescription="None"
  parameters={[]}
/>

---

## Full example

This code demonstrates each of the functions mentioned above, providing a complete showcase of LCD display control in action.

```cpp
// Include the library
#include "16x2-LCD-SOLDERED.h"

LCD lcd; // LCD object


void setup()
{
    lcd.begin();     // Initialize LCD
    lcd.backlight(); // Turn on LCD backlight
}

void loop()
{
    // Autoscroll
    lcd.setCursor(5, 0); //Set cursor to 6th (starts from 0) place in row, 1st row
    lcd.print(F("Autoscrolling")); //Print text to LCD
    lcd.setCursor(10, 1);   //Set cursor
    lcd.autoscroll();   //Enable autoscroll

    for (int i = 0; i < 10; i++)    //Print first 10 integers
    {
        lcd.print(i);   
        delay(200);
    }

    lcd.noAutoscroll(); //Disable autoscroll
    lcd.clear();    //Clear content from LCD

    // Scroll left and right
    lcd.setCursor(10, 0); 
    lcd.print(F("To the left!"));
    for (int i = 0; i < 10; i++)
    {
        lcd.scrollDisplayLeft();    //This command shifts al content to left by 1 place
        delay(200);
    }
    lcd.clear(); //Clear content from LCD
    lcd.print(F("To the right!"));
    for (int i = 0; i < 10; i++)
    {
        lcd.scrollDisplayRight();   //This command shifts al content to right by 1 place
        delay(200);
    }
    lcd.clear();

    // Cursor
    lcd.setCursor(0, 0);
    lcd.cursor();
    lcd.print(F("Cursor"));
    delay(3000);
    lcd.clear();

    // Cursor blink
    lcd.setCursor(0, 0);
    lcd.blink();    //This command enables cursor blink
    lcd.print(F("Cursor blink"));
    delay(3000);
    lcd.clear();

    // Blink without cursor
    lcd.setCursor(0, 0);
    lcd.noCursor(); //Disable cursor, so it is no longer shown on screen
    lcd.print(F("Just blink"));
    delay(3000);
    lcd.noBlink();  //Stop cursor blinking
    lcd.clear();
}
```

<QuickLink 
  title="Functions.ino" 
  description="Example file for using some functions with the LCD I2C display"
  url="https://github.com/SolderedElectronics/Soldered-16x2-LCD-Arduino-Library/blob/main/examples/Functions/Functions.ino" 
/>