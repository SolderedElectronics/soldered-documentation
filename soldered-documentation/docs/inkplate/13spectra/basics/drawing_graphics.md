---
slug: /inkplate/13spectra/basics/drawing-graphics
title: Inkplate 13SPECTRA – Drawing colorful graphics
sidebar_label: Drawing colorful graphics
id: 13spectra-graphics
---

Inkplate 13SPECTRA allows you to draw colorful grahpics on a **1600 x 1200px canvas**. 

<InfoBox>**Adafruit GFX** is the graphics library included in the Inkplate library for drawing graphics. For more details, refer to the **official repository**:<QuickLink title="Adafruit GFX Library" 
  description="The core graphics library for Inkplate library, created by Adafruit."
  url="https://github.com/adafruit/Adafruit-GFX-Library" 
/></InfoBox>

---

## Color spectrum

Below is an example demonstrating drawing in all available colors on the Inkplate 13SPECTRA:

<InfoBox>There are total of 6 colors to choose from:
`INKPLATE_BLACK`, `INKPLATE_WHITE`, `INKPLATE_YELLOW`, `INKPLATE_RED`, `INKPLATE_BLUE`, `INKPLATE_GREEN`</InfoBox>

```cpp

#include "Inkplate.h"

// Declare Inkplate object
Inkplate display;

void setup(){
    // Initialize Inkplate
    display.begin();

    display.clearDisplay();
    // Draw a full screen of all colors
    display.fillRect(0, 0, 1600 / 6 + 2, 1200, INKPLATE_BLACK);
    display.fillRect(1 * 1600 / 6, 0, 1600 / 6 + 2, 1200, INKPLATE_WHITE);
    display.fillRect(2 * 1600 / 6, 0, 1600 / 6 + 2, 1200, INKPLATE_YELLOW);
    display.fillRect(3 * 1600 / 6, 0, 1600 / 6 + 2, 1200, INKPLATE_RED);
    display.fillRect(4 * 1600 / 6, 0, 1600 / 6 + 2, 1200, INKPLATE_BLUE-1);
    display.fillRect(5 * 1600 / 6, 0, 1600 / 6 + 2, 1200, INKPLATE_GREEN-1);

    // Show the Image on the screen
    display.display();
}

void loop(){
    // Loop forever
}
```

<CenteredImage src="/img/13spectra/DSC00700.jpg" alt="Example output displayed on e-paper display" caption="Example output displayed on e-paper display" width="1200px" />


elow are the detailed references for these functions:

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

---

## Drawing graphics

Below is an example demonstrating functions for drawing graphics on the Inkplate 13SPECTRA:

```cpp
void setup(){
    display.clear();
    display.clearDisplay();
    display.fillScreen(INKPLATE_WHITE);

    // Rectangles
    display.drawRect(40, 40, 520, 240, INKPLATE_BLACK);
    display.fillRect(60, 60, 200, 80, INKPLATE_YELLOW);
    display.drawRect(60, 60, 200, 80, INKPLATE_BLACK);
    display.fillRoundRect(290, 60, 240, 80, 16, INKPLATE_RED);
    display.drawRoundRect(290, 60, 240, 80, 16, INKPLATE_BLACK);

    // Circles
    display.drawCircle(160, 220, 60, INKPLATE_BLUE);
    display.fillCircle(380, 220, 60, INKPLATE_GREEN);
    display.drawCircle(380, 220, 60, INKPLATE_BLACK);

    // Triangle
    display.fillTriangle(520, 320, 640, 160, 760, 320, INKPLATE_YELLOW);
    display.drawTriangle(520, 320, 640, 160, 760, 320, INKPLATE_BLACK);

    // Lines
    display.drawLine(40, 360, 760, 520, INKPLATE_BLACK);
    display.drawLine(40, 390, 760, 550, INKPLATE_RED);
    display.drawLine(40, 420, 760, 580, INKPLATE_YELLOW);
    display.drawLine(40, 450, 760, 610, INKPLATE_BLUE);
    display.drawLine(40, 480, 760, 640, INKPLATE_GREEN);

    for (int x = 40; x < 760; x += 8) {
    uint16_t color = INKPLATE_BLACK;

    if (x % 48 == 0) {
      color = INKPLATE_RED;
    } else if (x % 40 == 0) {
      color = INKPLATE_YELLOW;
    } else if (x % 32 == 0) {
      color = INKPLATE_GREEN;
    } else if (x % 24 == 0) {
      color = INKPLATE_BLUE;
    }

    // Simple text
    display.setTextSize(3);
    display.setTextColor(INKPLATE_BLACK);
    display.setCursor(40, 760);
    display.print("Inkplate 13 Spectra");

    display.setTextSize(2);
    display.setCursor(40, 800);
    display.print("Adafruit_GFX shapes & colors");

    // Update e-paper
    display.display();
}
}

```

[IMAGE PLACEHOLDER - inkplate13 shapes example] 

Below are the detailed references to these functions:

<FunctionDocumentation
  functionName="inkplate.drawRect()"
  description="Draws the outline of a rectangle on the display."
  returnDescription="none"
  parameters={[
    { type: 'int', name: 'x', description: 'The x-coordinate of the top-left corner.' },
    { type: 'int', name: 'y', description: 'The y-coordinate of the top-left corner.' },
    { type: 'int', name: 'width', description: 'The width of the rectangle.' },
    { type: 'int', name: 'height', description: 'The height of the rectangle.' },
    { type: 'uint16_t', name: 'color', description: 'The outline color.' },
  ]}
/>

<FunctionDocumentation
  functionName="inkplate.fillRect()"
  description="Draws a filled rectangle on the display."
  returnDescription="none"
  parameters={[
    { type: 'int', name: 'x', description: 'The x-coordinate of the top-left corner.' },
    { type: 'int', name: 'y', description: 'The y-coordinate of the top-left corner.' },
    { type: 'int', name: 'width', description: 'The width of the rectangle.' },
    { type: 'int', name: 'height', description: 'The height of the rectangle.' },
    { type: 'uint16_t', name: 'color', description: 'The fill color.' },
  ]}
/>

<FunctionDocumentation
  functionName="inkplate.drawRoundRect()"
  description="Draws the outline of a rectangle with rounded corners."
  returnDescription="none"
  parameters={[
    { type: 'int', name: 'x', description: 'The x-coordinate of the top-left corner.' },
    { type: 'int', name: 'y', description: 'The y-coordinate of the top-left corner.' },
    { type: 'int', name: 'width', description: 'The width of the rectangle.' },
    { type: 'int', name: 'height', description: 'The height of the rectangle.' },
    { type: 'int', name: 'radius', description: 'The radius of the rounded corners.' },
    { type: 'uint16_t', name: 'color', description: 'The outline color.' },
  ]}
/>

<FunctionDocumentation
  functionName="inkplate.fillRoundRect()"
  description="Draws a filled rectangle with rounded corners."
  returnDescription="none"
  parameters={[
    { type: 'int', name: 'x', description: 'The x-coordinate of the top-left corner.' },
    { type: 'int', name: 'y', description: 'The y-coordinate of the top-left corner.' },
    { type: 'int', name: 'width', description: 'The width of the rectangle.' },
    { type: 'int', name: 'height', description: 'The height of the rectangle.' },
    { type: 'int', name: 'radius', description: 'The radius of the rounded corners.' },
    { type: 'uint16_t', name: 'color', description: 'The fill color.' },
  ]}
/>

<FunctionDocumentation
  functionName="inkplate.drawTriangle()"
  description="Draws the outline of a triangle using three points."
  returnDescription="none"
  parameters={[
    { type: 'int', name: 'x0', description: 'The x-coordinate of the first vertex.' },
    { type: 'int', name: 'y0', description: 'The y-coordinate of the first vertex.' },
    { type: 'int', name: 'x1', description: 'The x-coordinate of the second vertex.' },
    { type: 'int', name: 'y1', description: 'The y-coordinate of the second vertex.' },
    { type: 'int', name: 'x2', description: 'The x-coordinate of the third vertex.' },
    { type: 'int', name: 'y2', description: 'The y-coordinate of the third vertex.' },
    { type: 'uint16_t', name: 'color', description: 'The outline color.' },
  ]}
/>

<FunctionDocumentation
  functionName="inkplate.fillTriangle()"
  description="Draws a filled triangle using three points."
  returnDescription="none"
  parameters={[
    { type: 'int', name: 'x0', description: 'The x-coordinate of the first vertex.' },
    { type: 'int', name: 'y0', description: 'The y-coordinate of the first vertex.' },
    { type: 'int', name: 'x1', description: 'The x-coordinate of the second vertex.' },
    { type: 'int', name: 'y1', description: 'The y-coordinate of the second vertex.' },
    { type: 'int', name: 'x2', description: 'The x-coordinate of the third vertex.' },
    { type: 'int', name: 'y2', description: 'The y-coordinate of the third vertex.' },
    { type: 'uint16_t', name: 'color', description: 'The fill color.' },
  ]}
/>

<FunctionDocumentation
  functionName="inkplate.drawLine()"
  description="Draws a straight line between two points."
  returnDescription="none"
  parameters={[
    { type: 'int', name: 'x0', description: 'The x-coordinate of the starting point.' },
    { type: 'int', name: 'y0', description: 'The y-coordinate of the starting point.' },
    { type: 'int', name: 'x1', description: 'The x-coordinate of the ending point.' },
    { type: 'int', name: 'y1', description: 'The y-coordinate of the ending point.' },
    { type: 'uint16_t', name: 'color', description: 'The line color.' },
  ]}
/>

<FunctionDocumentation
  functionName="inkplate.drawPixel()"
  description="Draws a single pixel at the specified coordinates."
  returnDescription="none"
  parameters={[
    { type: 'int', name: 'x', description: 'The x-coordinate of the pixel.' },
    { type: 'int', name: 'y', description: 'The y-coordinate of the pixel.' },
    { type: 'uint16_t', name: 'color', description: 'The pixel color.' },
  ]}
/>
