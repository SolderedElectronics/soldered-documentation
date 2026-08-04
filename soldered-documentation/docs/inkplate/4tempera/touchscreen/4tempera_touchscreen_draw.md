---
slug: /inkplate/4tempera/touchscreen/draw
title: Inkplate 4TEMPERA - Touchscreen draw
sidebar_label: Touchscreen draw
id: 4tempera-touchscreen-draw
hide_title: true
---

<SectionTitle title="Touchscreen draw" backgroundImage="/img/touchscreen.jpg" />

This example demonstrates how to use the built-in touchscreen on the Inkplate 4TEMPERA to draw directly on the screen. It turns the device into a simple sketchpad using finger or stylus input.

<InfoBox>The touchscreen on Inkplate 4TEMPERA uses a capacitive controller and supports multi-touch gestures. This example focuses on basic single-point drawing.</InfoBox>

---

## Example code

The following sketch initializes the display and touchscreen and allows the user to draw by touching the screen. Touch coordinates are used to draw small black circles at the touched location.

```cpp
/*
    Inkplate4TEMPERA_Touchscreen_Draw example for Soldered Inkplate 4TEMPERA

    This sketch shows how to draw using the touchscreen on Inkplate 4TEMPERA.
    Touch the screen to leave a trail of black dots wherever you move your finger.

    Select "Soldered Inkplate 4TEMPERA" from Tools -> Board menu.

    Want to learn more about Inkplate? Visit www.inkplate.io
    Looking to get support? Ask on the Soldered community: https://community.soldered.com/
*/

#include "Inkplate.h" // Include Inkplate library

Inkplate display(INKPLATE_1BIT); // Create display object in monochrome mode

void setup()
{
    display.begin();               // Initialize the display
    display.clearDisplay();        // Clear the display
    display.display();             // Update the screen

    // Initialize the touchscreen and keep it powered on
    display.touchscreen.init(true);
}

void loop()
{
    // Check if the touchscreen detects any touch
    if (display.touchscreen.available())
    {
        uint8_t n;
        uint16_t x[2], y[2];
        n = display.touchscreen.getData(x, y); // Get touch point coordinates (up to 2 fingers)

        if (n != 0)
        {
            // Draw a small circle at the first touch point
            display.fillCircle(x[0], y[0], 2, BLACK);
            display.display(); // Refresh the screen to show the change
        }
    }

    delay(20); // Small delay to reduce CPU usage
}
```

---

<FunctionDocumentation
  functionName="display.touchscreen.init()"
  description="Initializes the touchscreen controller."
  returnType="bool"
  parameters={[
    { type: 'uint8_t', name: 'powerState', description: 'Power state to leave the touchscreen in after initialization.' }
  ]}
/>

<FunctionDocumentation
  functionName="display.touchscreen.available()"
  description="Checks if the touchscreen has new touch data available."
  returnType="bool"
/>

<FunctionDocumentation
  functionName="display.touchscreen.getData()"
  description="Reads the coordinates of up to two simultaneous touch points into the provided arrays."
  returnDescription="Returns the number of touch points detected."
  returnType="uint8_t"
  parameters={[
    { type: 'uint16_t*', name: 'xPos', description: 'Array (size 2) that will be filled with the X coordinates of the detected touch points.' },
    { type: 'uint16_t*', name: 'yPos', description: 'Array (size 2) that will be filled with the Y coordinates of the detected touch points.' }
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