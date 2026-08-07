---  
slug: /inkplate/4tempera/touchscreen/touch-in-area  
title: Inkplate 4TEMPERA - Touch in area
sidebar_label: Touch in area
id: 4tempera-touch-in-area  
hide_title: true  
---

<SectionTitle title="Touch in area" backgroundImage="img/touch_area.jpg" />

The `Inkplate4TEMPERA_Touch_In_Area` example demonstrates how to detect touch input within a specific rectangular area of the Inkplate 4TEMPERA's screen. This is useful for creating interactive buttons or UI zones without relying on predefined widgets.

---

## Touch in area

This example uses `inkplate.touchscreen.touchInArea(x1, y1, w, h)` to determine if the screen has been touched within a specific region, enabling basic interactive UI design.

<InfoBox>You can use `touchscreen.touchInArea()` in both black-and-white (1-bit) and grayscale (3-bit) modes. For optimal responsiveness, avoid calling display updates within tight touch polling loops unless needed.</InfoBox>

```cpp
#include "Inkplate.h"

int x_position = 50;
int y_position = 50;

Inkplate inkplate(INKPLATE_1BIT);

void setup()
{
    Serial.begin(115200);
    inkplate.begin();
    inkplate.clearDisplay();
    inkplate.setCursor(30, 300);
    inkplate.setTextSize(3);
    inkplate.print("Touch button example. Touch the black button.");
    inkplate.display();
    delay(3000);
    inkplate.clearDisplay();

    // Initialize touchscreen and keep it powered on
    if (inkplate.touchscreen.init(true))
    {
        Serial.println("Touchscreen init ok");
    }
    else
    {
        Serial.println("Touchscreen init fail");
        while (true);
    }

    // Draw the initial rectangle
    inkplate.fillRect(x_position, y_position, 100, 50, BLACK);
    inkplate.display();
}

void loop()
{
    if (inkplate.touchscreen.touchInArea(x_position, y_position, 100, 50))
    {
        x_position += 100;
        y_position += 100;

        // Stay within 600x600 screen bounds
        if (y_position + 50 <= 600 && x_position + 100 <= 600)
        {
            inkplate.clearDisplay();
            inkplate.fillRect(x_position, y_position, 100, 50, BLACK);
            inkplate.partialUpdate();
            delay(100);
        }
        else // Reset to top-left and perform full refresh
        {
            x_position = 50;
            y_position = 50;

            inkplate.clearDisplay();
            inkplate.fillRect(x_position, y_position, 100, 50, BLACK);
            inkplate.display();
        }
    }
}
```

<FunctionDocumentation
functionName="inkplate.touchscreen.touchInArea()"
description="Checks if a touch event occurred within a defined rectangular area on the screen."
returnDescription="Returns true if a touch is detected within the specified area, false otherwise."
parameters={[ 
{ type: 'int16_t', name: 'x1', description: 'X coordinate of the top-left corner of the area.' },
{ type: 'int16_t', name: 'y1', description: 'Y coordinate of the top-left corner of the area.' },
{ type: 'int16_t', name: 'w', description: 'Width of the area, in pixels.' },
{ type: 'int16_t', name: 'h', description: 'Height of the area, in pixels.' }
]}
/>

## Full examples
Check out the full examples:

<QuickLink title="Inkplate4TEMPERA_Touch_In_Area.ino" description="Example showing how to detect if a touch event occurs within a rectangular area." url="https://github.com/SolderedElectronics/Inkplate-Arduino-library/blob/master/examples/Inkplate4TEMPERA/Basic/Inkplate4TEMPERA_Touch_In_Area/Inkplate4TEMPERA_Touch_In_Area.ino" />