---  
slug: /inkplate/4tempera/touchscreen/touch-in-area  
title: Touch in Area  
id: 4tempera-touch-in-area  
hide_title: true  
---

<SectionTitle title="Touch in Area" backgroundImage="img/touch_area.jpg" />

The `Inkplate4TEMPERA_Touch_In_Area` example demonstrates how to detect touch input within a specific rectangular area of the Inkplate 4TEMPERA's screen. This is useful for creating interactive buttons or UI zones without relying on predefined widgets.

---

## Touch in Area

This example uses `inkplate.touchInArea(x1, y1, x2, y2)` to determine if the screen has been touched within a specific region, enabling basic interactive UI design.

<InfoBox>You can use `touchInArea()` in both black-and-white (1-bit) and grayscale (3-bit) modes. For optimal responsiveness, avoid calling display updates within tight touch polling loops unless needed.</InfoBox>

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
    if (inkplate.tsInit(true))
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
    if (inkplate.touchInArea(x_position, y_position, x_position + 100, y_position + 50))
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
functionName="inkplate.touchInArea()"
description="Checks if a touch event occurred within a defined rectangular area on the screen."
returnDescription="Returns true if a touch is detected within the specified area, false otherwise."
parameters={[ 
{ type: 'int', name: 'x1', description: 'X coordinate of the top-left corner of the area.' },
{ type: 'int', name: 'y1', description: 'Y coordinate of the top-left corner of the area.' },
{ type: 'int', name: 'x2', description: 'X coordinate of the bottom-right corner of the area.' },
{ type: 'int', name: 'y2', description: 'Y coordinate of the bottom-right corner of the area.' }
]}
/>

## Full examples
Check out the full examples:

<QuickLink title="Inkplate4TEMPERA_Touch_In_Area.ino" description="Example showing how to detect if a touch event occurs within a rectangular area." url="https://github.com/SolderedElectronics/Inkplate-Arduino-library/blob/master/examples/Inkplate4TEMPERA/Basic/Inkplate4TEMPERA_Touch_In_Area/Inkplate4TEMPERA_Touch_In_Area.ino" />