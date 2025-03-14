---
slug: /lcd-i2c/arduino/examples 
title: Using the LCD display (examples)
id: lcd-i2c-arduino-2 
hide_title: False
---

This page contains some simple examples with function documentation on how to use the LCD display in different ways.

---

## Initialization

To use the LCD display, first, include the required library, create the LCD object and initialize the LCD in the `setup.()` function with `begin.()`. Backlight is also initialized here.

<InfoBox> Our library includes the [**Wire.h**](https://docs.arduino.cc/language-reference/en/functions/communication/wire/) library!</InfoBox>

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
  returnDescription="None (it's a void function)"
  parameters={[]}
/>
