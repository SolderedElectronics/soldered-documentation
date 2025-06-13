---
slug: /inkplate/4tempera/touchscreen/draw
title: Inkplate 4TEMPERA – Touchscreen Draw
id: 4tempera-touchscreen-draw
hide_title: true
---

<SectionTitle title="Touchscreen Draw" backgroundImage="/img/touchscreen.jpg" />

This example demonstrates how to use the built-in touchscreen on the Inkplate 4TEMPERA to draw directly on the screen. It turns the device into a simple sketchpad using finger or stylus input.

<InfoBox>The touchscreen on Inkplate 4TEMPERA uses a capacitive controller and supports multi-touch gestures. This example focuses on basic single-point drawing.</InfoBox>

---

## Example Code

The following sketch initializes the display and touchscreen and allows the user to draw by touching the screen. Touch coordinates are used to draw small black circles at the touched location.

```cpp
/*
    Inkplate4TEMPERA_Touchscreen_Draw example for Soldered Inkplate 4TEMPERA

    This sketch shows how to draw using the touchscreen on Inkplate 4TEMPERA.
    Touch the screen to leave a trail of black dots wherever you move your finger.

    Select "Soldered Inkplate 4TEMPERA" from Tools -> Board menu.

    Want to learn more about Inkplate? Visit www.inkplate.io
    Looking to get support? Write on our forums: https://forum.soldered.com/
*/

#include "Inkplate.h" // Include Inkplate library

Inkplate display; // Create display object

void setup()
{
    display.begin();               // Initialize the display
    display.clearDisplay();        // Clear the display
    display.display();             // Update the screen
}

void loop()
{
    // Check if the screen is being touched
    if (display.ts.touched())
    {
        TPPoint p = display.ts.getPoint(0); // Get the first touch point

        // Draw a small circle at the touch location
        display.fillCircle(p.x, p.y, 2, BLACK);
        display.display(); // Refresh the screen to show the change
    }

    delay(20); // Small delay to reduce CPU usage
}
```

---

<FunctionDocumentation
  functionName="display.ts.touched()"
  description="Checks if the touchscreen is being touched."
  returnType="bool"
/>

<FunctionDocumentation
  functionName="display.ts.getPoint()"
  description="Returns the TPPoint (touch point) at a given index. Typically only index 0 is used for single touch."
  returnType="TPPoint"
  parameters={[
    { type: 'int', name: 'index', description: 'Touch point index (0 for the first point).' }
  ]}
/>

<FunctionDocumentation
  functionName="display.fillCircle()"
  description="Draws a filled circle at the specified coordinates."
  returnType="void"
  parameters={[
    { type: 'int16_t', name: 'x', description: 'X-coordinate of the circle center.' },
    { type: 'int16_t', name: 'y', description: 'Y-coordinate of the circle center.' },
    { type: 'int16_t', name: 'r', description: 'Radius of the circle.' },
    { type: 'uint16_t', name: 'color', description: 'Color of the circle.' }
  ]}
/>

---

## Full example

You can find the complete example in the Inkplate Arduino library repository:

<QuickLink 
  title="Inkplate4TEMPERA_Touchscreen_Draw" 
  description="Draw on the screen using your finger with Inkplate 4TEMPERA's touchscreen." 
  url="https://github.com/SolderedElectronics/Inkplate-Arduino-library/blob/master/examples/Inkplate4TEMPERA/Basic/Inkplate4TEMPERA_Touchscreen_Draw/Inkplate4TEMPERA_Touchscreen_Draw.ino" 
/>
