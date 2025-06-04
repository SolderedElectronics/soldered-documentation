---
slug: /inkplate/6flick/touchscreen/draw
title: Touchscreen Draw
id: 6flick-touchscreen-draw
hide_title: true
---

<SectionTitle title="Touchscreen Draw" backgroundImage="/img/touchscreen.jpg" />

This example demonstrates how to draw on the screen using the **capacitive touchscreen** on Inkplate 6Flick. By dragging your finger across the screen, lines are drawn in real time, allowing basic interaction with the display.

---

## Example Overview

This example checks for touch input and draws lines between the last touch position and the current one. You can use your finger or a stylus to draw directly onto the e-paper display.

```cpp
/*
    Inkplate6FLICK_Touchscreen_Draw example for Soldered Inkplate 6Flick

    This example shows how to draw with your finger on the touchscreen.

    Select "Soldered Inkplate 6Flick" from Tools -> Board menu.

    Want to learn more about Inkplate? Visit www.inkplate.io
    Looking to get support? Write on our forums: https://forum.soldered.com/
*/

#include "Inkplate.h"

Inkplate display; // Create Inkplate display object

int x, y, oldX = -1, oldY = -1;

void setup()
{
    display.begin();               // Initialize display and touchscreen
    display.clearDisplay();        // Clear display buffer
    display.display();             // Apply blank frame to screen
}

void loop()
{
    // Read current finger position
    if (display.touchDetected()) // Check if touchscreen is being touched
    {
        display.touchCoordinates(&x, &y); // Get touch coordinates

        if (oldX != -1 && oldY != -1)
        {
            // Draw a line from previous to current point
            display.drawLine(oldX, oldY, x, y, BLACK);
        }

        oldX = x;
        oldY = y;

        display.partialUpdate(); // Update the area that was drawn
    }
    else
    {
        // Reset the old coordinates if no touch
        oldX = -1;
        oldY = -1;
    }
}
```

---

<FunctionDocumentation
  functionName="touchDetected()"
  description="Returns true if the capacitive touchscreen detects input."
  returnType="bool"
/>

<FunctionDocumentation
  functionName="touchCoordinates()"
  description="Gets the X and Y position of the last touch point."
  returnType="void"
  parameters={[
    { type: 'int*', name: 'x', description: 'Pointer to store the X coordinate' },
    { type: 'int*', name: 'y', description: 'Pointer to store the Y coordinate' }
  ]}
/>

<FunctionDocumentation
  functionName="partialUpdate()"
  description="Refreshes only the updated section of the screen to save power and time."
  returnType="void"
/>

---

## Notes

- The touchscreen on Inkplate 6Flick is a **capacitive** touch sensor that works best with bare fingers.
- `partialUpdate()` allows fast screen refreshes while interacting, avoiding full refresh flashes.

---

## Full Example

You can find the complete example in the Inkplate Arduino library here:

<QuickLink 
  title="Inkplate6FLICK_Touchscreen_Draw" 
  description="Touchscreen drawing demo for Inkplate 6Flick." 
  url="https://github.com/SolderedElectronics/Inkplate-Arduino-library/blob/dev/examples/Inkplate6FLICK/Basic/Inkplate6FLICK_Touchscreen_Draw/Inkplate6FLICK_Touchscreen_Draw.ino" 
/>
