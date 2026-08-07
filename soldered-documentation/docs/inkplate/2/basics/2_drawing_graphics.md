---  
slug: /inkplate/2/basics/drawing-graphics  
title: Inkplate 2 – Drawing graphics
sidebar_label: Drawing graphics
id: 2-graphics  
hide_title: true  
---

<SectionTitle title="Drawing Graphics" />

Inkplate 2 features a 2.13″ three-color e-paper display capable of rendering black, white, and red pixels. Draw geometric shapes using the Adafruit GFX functions built into the Inkplate library.

<InfoBox>**Adafruit GFX** is the graphics library included in the Inkplate library for drawing graphics. For more details, refer to the **official repository**:<QuickLink title="Adafruit GFX Library" 
  description="The core graphics library for Inkplate library, created by Adafruit."
  url="https://github.com/adafruit/Adafruit-GFX-Library" 
/></InfoBox>

---

## Drawing geometric shapes

The example below uses these functions to draw pixels, lines, rectangles, circles, and more. Inkplate 2 supports three colors:
- `INKPLATE2_BLACK`
- `INKPLATE2_RED`
- `INKPLATE2_WHITE` (background/erase)

```cpp
#include "Inkplate.h"
Inkplate inkplate;

void setup() {
  inkplate.begin();
  inkplate.clearDisplay();
  inkplate.display();

  // Pixel replacements with small filled rectangles for visibility
  inkplate.fillRect(10, 2, 6, 6, INKPLATE2_BLACK);
  inkplate.fillRect(110, 2, 6, 6, INKPLATE2_RED);

  // Lines
  inkplate.drawLine(10, 14, 200, 14, INKPLATE2_BLACK);
  inkplate.drawLine(10, 20, 200, 20, INKPLATE2_RED);

  // Rectangles
  inkplate.drawRect(10, 26, 70, 16, INKPLATE2_BLACK);
  inkplate.fillRect(115, 26, 70, 16, INKPLATE2_RED);

  // Circles
  inkplate.drawCircle(45, 52, 8, INKPLATE2_BLACK);
  inkplate.fillCircle(150, 52, 8, INKPLATE2_RED);

  // Rounded rectangles
  inkplate.drawRoundRect(10, 64, 70, 16, 4, INKPLATE2_BLACK);
  inkplate.fillRoundRect(115, 64, 70, 16, 4, INKPLATE2_RED);

  // Triangles
  inkplate.drawTriangle(10, 100, 40, 100, 25, 84, INKPLATE2_BLACK);
  inkplate.fillTriangle(115, 100, 145, 100, 130, 84, INKPLATE2_RED);

  inkplate.display();
}

void loop() {}
```

<CenteredImage src="/img/inkplate_2/drawing_graphics_preview.png" alt="Expected output on Inkplate display" caption="Expected output on Inkplate display." width="750px" />

Below are the detailed references for these functions:

<FunctionDocumentation
  functionName="inkplate.drawPixel()"
  description="Draws a single pixel on the display at the specified coordinates."
  returnDescription="none"
  parameters={[
    { type: 'int', name: 'x', description: 'The x-coordinate of the pixel.' },
    { type: 'int', name: 'y', description: 'The y-coordinate of the pixel.' },
    { type: 'uint8_t', name: 'color', description: 'The color of the pixel.' },
  ]}
/>

<FunctionDocumentation
  functionName="inkplate.drawLine()"
  description="Draws a straight line between two points on the display."
  returnDescription="none"
  parameters={[
    { type: 'int', name: 'x0', description: 'The x-coordinate of the starting point.' },
    { type: 'int', name: 'y0', description: 'The y-coordinate of the starting point.' },
    { type: 'int', name: 'x1', description: 'The x-coordinate of the ending point.' },
    { type: 'int', name: 'y1', description: 'The y-coordinate of the ending point.' },
    { type: 'uint8_t', name: 'color', description: 'The color of the line.' },
  ]}
/>

<FunctionDocumentation
  functionName="inkplate.drawRect()"
  description="Draws a rectangle outline on the display."
  returnDescription="none"
  parameters={[
    { type: 'int', name: 'x', description: 'The x-coordinate of the top-left corner.' },
    { type: 'int', name: 'y', description: 'The y-coordinate of the top-left corner.' },
    { type: 'int', name: 'width', description: 'The width of the rectangle.' },
    { type: 'int', name: 'height', description: 'The height of the rectangle.' },
    { type: 'uint8_t', name: 'color', description: 'The color of the rectangle outline.' },
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
    { type: 'uint8_t', name: 'color', description: 'The fill color.' },
  ]}
/>

<FunctionDocumentation
  functionName="inkplate.drawCircle()"
  description="Draws a circle outline on the display."
  returnDescription="none"
  parameters={[
    { type: 'int', name: 'x', description: 'The x-coordinate of the circle center.' },
    { type: 'int', name: 'y', description: 'The y-coordinate of the circle center.' },
    { type: 'int', name: 'radius', description: 'The radius of the circle.' },
    { type: 'uint8_t', name: 'color', description: 'The color of the circle outline.' },
  ]}
/>

<FunctionDocumentation
  functionName="inkplate.fillCircle()"
  description="Draws a filled circle on the display."
  returnDescription="none"
  parameters={[
    { type: 'int', name: 'x', description: 'The x-coordinate of the circle center.' },
    { type: 'int', name: 'y', description: 'The y-coordinate of the circle center.' },
    { type: 'int', name: 'radius', description: 'The radius of the circle.' },
    { type: 'uint8_t', name: 'color', description: 'The fill color.' },
  ]}
/>

<FunctionDocumentation
  functionName="inkplate.drawRoundRect()"
  description="Draws a rounded rectangle outline on the display."
  returnDescription="none"
  parameters={[
    { type: 'int', name: 'x', description: 'The x-coordinate of the top-left corner.' },
    { type: 'int', name: 'y', description: 'The y-coordinate of the top-left corner.' },
    { type: 'int', name: 'width', description: 'The width of the rectangle.' },
    { type: 'int', name: 'height', description: 'The height of the rectangle.' },
    { type: 'int', name: 'radius', description: 'The radius of the rounded corners.' },
    { type: 'uint8_t', name: 'color', description: 'The color of the rectangle outline.' },
  ]}
/>

<FunctionDocumentation
  functionName="inkplate.fillRoundRect()"
  description="Draws a filled rounded rectangle on the display."
  returnDescription="none"
  parameters={[
    { type: 'int', name: 'x', description: 'The x-coordinate of the top-left corner.' },
    { type: 'int', name: 'y', description: 'The y-coordinate of the top-left corner.' },
    { type: 'int', name: 'width', description: 'The width of the rectangle.' },
    { type: 'int', name: 'height', description: 'The height of the rectangle.' },
    { type: 'int', name: 'radius', description: 'The radius of the rounded corners.' },
    { type: 'uint8_t', name: 'color', description: 'The fill color.' },
  ]}
/>

<FunctionDocumentation
  functionName="inkplate.drawTriangle()"
  description="Draws a triangle outline on the display."
  returnDescription="none"
  parameters={[
    { type: 'int', name: 'x0', description: 'The x-coordinate of the first vertex.' },
    { type: 'int', name: 'y0', description: 'The y-coordinate of the first vertex.' },
    { type: 'int', name: 'x1', description: 'The x-coordinate of the second vertex.' },
    { type: 'int', name: 'y1', description: 'The y-coordinate of the second vertex.' },
    { type: 'int', name: 'x2', description: 'The x-coordinate of the third vertex.' },
    { type: 'int', name: 'y2', description: 'The y-coordinate of the third vertex.' },
    { type: 'uint8_t', name: 'color', description: 'The color of the triangle outline.' },
  ]}
/>

<FunctionDocumentation
  functionName="inkplate.fillTriangle()"
  description="Draws a filled triangle on the display."
  returnDescription="none"
  parameters={[
    { type: 'int', name: 'x0', description: 'The x-coordinate of the first vertex.' },
    { type: 'int', name: 'y0', description: 'The y-coordinate of the first vertex.' },
    { type: 'int', name: 'x1', description: 'The x-coordinate of the second vertex.' },
    { type: 'int', name: 'y1', description: 'The y-coordinate of the second vertex.' },
    { type: 'int', name: 'x2', description: 'The x-coordinate of the third vertex.' },
    { type: 'int', name: 'y2', description: 'The y-coordinate of the third vertex.' },
    { type: 'uint8_t', name: 'color', description: 'The fill color.' },
  ]}
/>

## Full example

<QuickLink 
  title="Inkplate2_Black_White_Red.ino" 
  description="Example drawing graphics using all three Inkplate 2 colors."
  url="https://github.com/SolderedElectronics/Inkplate-Arduino-library/blob/master/examples/Inkplate2/Basic/Inkplate2_Black_White_Red/Inkplate2_Black_White_Red.ino" 
/>

<InfoBox>For more advanced usage, visit the [Inkplate 2 examples directory](https://github.com/SolderedElectronics/Inkplate-Arduino-library/tree/master/examples/Inkplate2).</InfoBox>