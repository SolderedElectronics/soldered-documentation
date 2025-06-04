---
slug: /inkplate/6flick/frontlight/basic
title: Simple Frontlight
id: 6flick-frontlight
hide_title: true
---

<SectionTitle title="Simple Frontlight Control" backgroundImage="/img/frontlight.jpg" />

This basic example demonstrates how to control the **frontlight/backlight brightness** of the Inkplate 6Flick using simple function calls.

The frontlight allows for better visibility in dim environments while preserving the paper-like appearance of the e-paper screen.

---

## Example Overview

This sketch shows how to control the brightness of the frontlight using `setFrontlight()` from the Inkplate API. You can control the brightness using PWM values from `0` (off) to `255` (maximum brightness).

```cpp
/*
    Inkplate6FLICK_Simple_Frontlight example for Soldered Inkplate 6Flick

    This example shows how to control the frontlight on Inkplate 6Flick.

    Select "Soldered Inkplate 6Flick" from Tools -> Board menu.

    Want to learn more about Inkplate? Visit www.inkplate.io
    Looking to get support? Write on our forums: https://forum.soldered.com/
*/

#include "Inkplate.h"

Inkplate display; // Create the display object

void setup()
{
    display.begin();              // Initialize the display
    display.clearDisplay();       // Clear the screen buffer
    display.setTextSize(2);
    display.setCursor(0, 20);
    display.println("Frontlight test!");
    display.display();            // Refresh screen

    delay(1000);

    display.setFrontlight(0);     // Turn off frontlight
    delay(1000);
    display.setFrontlight(50);    // Set low brightness
    delay(1000);
    display.setFrontlight(150);   // Medium brightness
    delay(1000);
    display.setFrontlight(255);   // Full brightness
}

void loop()
{
    // Nothing to do in loop
}
```

---

<FunctionDocumentation
  functionName="setFrontlight()"
  description="Sets the brightness of the frontlight/backlight on the Inkplate 6Flick."
  returnType="void"
  parameters={[
    { type: 'uint8_t', name: 'level', description: 'Brightness level (0 = off, 255 = full brightness).' }
  ]}
/>

---

## Notes

- The **frontlight is automatically turned off** after sleep or reboot, so be sure to call `setFrontlight()` again in `setup()` if needed.
- The frontlight controller uses PWM to set brightness, so intermediate values may cause visible flickering depending on environment lighting.

---

## Full Example

You can find the complete example in the Inkplate Arduino library repository:

<QuickLink 
  title="Inkplate6FLICK_Simple_Frontlight" 
  description="Basic usage example of the frontlight on Inkplate 6Flick." 
  url="https://github.com/SolderedElectronics/Inkplate-Arduino-library/blob/dev/examples/Inkplate6FLICK/Basic/Inkplate6FLICK_Simple_Frontlight/Inkplate6FLICK_Simple_Frontlight.ino" 
/>
