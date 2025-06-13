---
slug: /inkplate/6color/basics/drawing-graphics
title: Inkplate 6COLOR – Drawing colorful graphics
sidebar_label: Drawing colorful graphics
id: graphics
---

Inkplate 6COLOR allows you to draw colorful graphics on a **600 x 448px canvas**.

<InfoBox>**Adafruit GFX** is the graphics library included in the Inkplate library for drawing graphics. For more details, refer to the **official repository**:<QuickLink title="Adafruit GFX Library" 
  description="The core graphics library for Inkplate library, created by Adafruit."
  url="https://github.com/adafruit/Adafruit-GFX-Library" 
/></InfoBox>

---

## Drawing Geometric Shapes

Below is an example demonstrating functions for drawing graphics on the Inkplate 6COLOR:

<InfoBox>There are a total of 7 colors to choose from: INKPLATE_BLACK, INKPLATE_WHITE, INKPLATE_GREEN, INKPLATE_BLUE, INKPLATE_RED, INKPLATE_YELLOW, INKPLATE_ORANGE</InfoBox>

```cpp
#include "Inkplate.h"

#ifndef ARDUINO_INKPLATECOLOR
#error "Wrong board selection for this example, please select Soldered Inkplate 6COLOR in the boards menu."
#endif

// Declare Inkplate object
Inkplate display;

void setup()
{
    // Initialize the Inkplate
    display.begin();

    // Draw a full screen of all colors
    display.fillRect(0, 0, 600 / 7 + 2, 448, INKPLATE_BLACK);
    display.fillRect(1 * 600 / 7, 0, 600 / 7 + 2, 448, INKPLATE_WHITE);
    display.fillRect(2 * 600 / 7, 0, 600 / 7 + 2, 448, INKPLATE_GREEN);
    display.fillRect(3 * 600 / 7, 0, 600 / 7 + 2, 448, INKPLATE_BLUE);
    display.fillRect(4 * 600 / 7, 0, 600 / 7 + 2, 448, INKPLATE_RED);
    display.fillRect(5 * 600 / 7, 0, 600 / 7 + 2, 448, INKPLATE_YELLOW);
    display.fillRect(6 * 600 / 7, 0, 600 / 7 + 2, 448, INKPLATE_ORANGE);

    // Show the image on the screen
    display.display();
}

void loop()
{
    // Loop forever
}
```

<CenteredImage src="/img/6color/graphics.png" alt="Expected output on Inkplate display" caption="Expected output on Inkplate display." width="750px" />

Below are the detailed references for these functions:

<FunctionDocumentation
  functionName="inkplate.fillRect()"
  description="Draws a filled rectangle on the display."
  returnDescription="none"
  parameters={[
    { type: 'int', name: 'x', description: 'The x-coordinate of the top-left corner.' },
    { type: 'int', name: 'y', description: 'The y-coordinate of the top-left corner.' },
    { type: 'int', name: 'width', description: 'The width of the rectangle.' },
    { type: 'int', name: 'height', description: 'The height of the rectangle.' },
    { type: 'uint8_t', name: 'color', description: 'The fill color.' },
  ]}
/>


