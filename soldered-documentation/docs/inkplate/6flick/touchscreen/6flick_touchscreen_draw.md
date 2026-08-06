---
slug: /inkplate/6flick/touchscreen/draw
title: Inkplate 6FLICK – Touchscreen Draw
sidebar_label: Touchscreen Draw
id: 6flick-touchscreen-draw
hide_title: true
---

<SectionTitle title="Touchscreen Draw" />

This example demonstrates how to draw on the screen using the **capacitive touchscreen** on Inkplate 6FLICK. By dragging your finger across the screen, lines are drawn in real time, allowing basic interaction with the display.

---

## Example Overview

This example checks for touch input and draws lines between the last touch position and the current one. You can use your finger or a stylus to draw directly onto the e-paper display.

```cpp
#include "Inkplate.h"

// Select to draw a line on screen or filled circle
#define DRAW_LINE
// #define DRAW_CIRCLE

Inkplate display(INKPLATE_1BIT);

#ifdef DRAW_LINE
uint16_t xOld, yOld;
#endif

void setup()
{
    // put your setup code here, to run once:
    Serial.begin(115200);
    display.begin();
    display.display();
    // Init touchscreen and power it on after init (send false as argument to put it in deep sleep right after init)
    if (display.touchscreen.init(true))
    {
        Serial.println("Touchscreen init ok");
    }
    else
    {
        Serial.println("Touchscreen init fail");
        while (true)
            ;
    }
}

void loop()
{
    // Check if there is any touch detected
    if (display.touchscreen.available())
    {
        uint8_t n;
        uint16_t x[2], y[2];
        // See how many fingers are detected (max 2) and copy x and y position of each finger on touchscreen
        n = display.touchscreen.getData(x, y);
        if (n != 0)
        {
#ifdef DRAW_LINE // Draw line from old point to new
            display.drawLine(xOld, yOld, x[0], y[0], BLACK);

            // Save coordinates to use as old next time
            xOld = x[0];
            yOld = y[0];
#endif

#ifdef DRAW_CIRCLE // Draw circle on touch event coordinates
            display.fillCircle(x[0], y[0], 20, BLACK);
#endif
            display.partialUpdate();
        }
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

- The touchscreen on Inkplate 6FLICK is a **capacitive** touch sensor that works best with bare fingers.
- `partialUpdate()` allows fast screen refreshes while interacting, avoiding full refresh flashes.

---

## Full example

You can find the complete example in the Inkplate Arduino library here:

<QuickLink 
  title="Inkplate6FLICK_Touchscreen_Draw" 
  description="Touchscreen drawing demo for Inkplate 6FLICK." 
  url="https://github.com/SolderedElectronics/Inkplate-Arduino-library/blob/master/examples/Inkplate6FLICK/Basic/Inkplate6FLICK_Touchscreen_Draw/Inkplate6FLICK_Touchscreen_Draw.ino" 
/>