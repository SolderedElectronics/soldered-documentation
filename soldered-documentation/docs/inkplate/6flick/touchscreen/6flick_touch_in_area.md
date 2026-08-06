---
slug: /inkplate/6flick/touchscreen/touch-in-area
title: Inkplate 6FLICK – Touch in Area
sidebar_label: Touch in Area
id: 6flick-touch-in-area
hide_title: true
---

<SectionTitle title="Touch in Area" />

The `Inkplate 6FLICK_Touch_In_Area` example shows how to detect touch input within a specific rectangular area of the Inkplate 6FLICK's screen. This is useful for creating interactive buttons or UI zones without relying on predefined widgets.

---

## Touch in Area

This example uses `display.touchInArea(x1, y1, x2, y2)` to determine if the screen has been touched within a specific region, enabling basic interactive UI design.

<InfoBox>You can use `touchInArea()` in both black-and-white (1-bit) and grayscale (3-bit) modes. For optimal responsiveness, avoid calling display updates within tight touch polling loops unless needed.</InfoBox>

```cpp
#include "Inkplate.h"

int x_position = 50;
int y_position = 50;

Inkplate display(INKPLATE_1BIT);

void setup()
{
    // put your setup code here, to run once:
    Serial.begin(115200);
    display.begin();
    display.clearDisplay();
    display.setCursor(100, 300);
    display.setTextSize(3);
    display.print("Touch button example. Touch the black button.");
    display.display();
    delay(3000);
    display.clearDisplay();
    // Init touchscreen and power it on after init (send false as argument to put it in deep sleep right after init)
    if (display.touchscreen.init(true))
    {
        Serial.println("Touchscreen init ok");
    }
    else
    {
        Serial.println("Touchscreen init fail");
        while (true);
    }

    //Draw initial rectangle
    display.fillRect(x_position, y_position, 100, 50, BLACK);
    display.display();
}

void loop()
{
    //Touch in area checks if touch ocured in given coordinates
    if(display.touchscreen.touchInArea(x_position, y_position, 100, 50))
    {
        x_position += 100;
        y_position += 100;

        if(y_position < 660)
        {
            display.clearDisplay();
            display.fillRect(x_position, y_position, 100, 50, BLACK);

            display.partialUpdate();
            delay(100);
        }
        else//Reseting rectangle position and doing full refresh
        {
            x_position = 50;
            y_position = 50;
            
            display.clearDisplay();
            display.fillRect(x_position, y_position, 100, 50, BLACK);
            display.display();
        }
    }

}
```

<FunctionDocumentation
functionName="display.touchInArea()"
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

<QuickLink title="Inkplate6FLICK_Touch_In_Area.ino" description="Example showing how to detect if a touch event occurs within a rectangular area on the Inkplate 6FLICK." url="https://github.com/SolderedElectronics/Inkplate-Arduino-library/blob/master/examples/Inkplate6FLICK/Basic/Inkplate6FLICK_Touch_In_Area/Inkplate6FLICK_Touch_In_Area.ino" />