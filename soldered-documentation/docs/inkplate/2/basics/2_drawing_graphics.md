---  
slug: /inkplate/2/basics/drawing-graphics  
title: Inkplate 2 – Drawing graphics
sidebar_label: Drawing graphics
id: 2-graphics  
hide_title: true  
---

<SectionTitle title="Drawing Graphics" backgroundImage="/img/inkplate_2/hardware.png" />

Inkplate 2 features a 2.13″ three-color e-paper display capable of rendering black, white, and red pixels. You can draw geometric shapes using the built-in Adafruit GFX functions, which are compatible with the Inkplate library.

Inkplate 2 supports the Adafruit GFX graphics library for drawing.

<InfoBox>**Adafruit GFX** is the graphics library included in the Inkplate library for drawing graphics. For more details, refer to the **official repository**:<QuickLink title="Adafruit GFX Library" 
  description="The core graphics library for Inkplate library, created by Adafruit."
  url="https://github.com/adafruit/Adafruit-GFX-Library" 
/></InfoBox>

---

## Drawing Geometric Shapes

Below is an example demonstrating functions used for drawing graphics on the Inkplate 2:

Use these functions to draw pixels, lines, rectangles, circles, and more. Inkplate 2 supports three colors:
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
  inkplate.fillRect(30, 5, 5, 5, INKPLATE2_BLACK);
  inkplate.fillRect(50, 5, 5, 5, INKPLATE2_RED);

  // Lines
  inkplate.drawLine(10, 15, 100, 15, INKPLATE2_BLACK);
  inkplate.drawLine(10, 25, 100, 25, INKPLATE2_RED);

  // Rectangles
  inkplate.drawRect(10, 35, 40, 20, INKPLATE2_BLACK);
  inkplate.fillRect(60, 35, 40, 20, INKPLATE2_RED);

  // Circles
  inkplate.drawCircle(30, 65, 10, INKPLATE2_BLACK);
  inkplate.fillCircle(70, 65, 10, INKPLATE2_RED);

  // Rounded rectangles
  inkplate.drawRoundRect(10, 85, 40, 20, 5, INKPLATE2_BLACK);
  inkplate.fillRoundRect(60, 85, 40, 20, 5, INKPLATE2_RED);

  // Triangles
  inkplate.drawTriangle(10, 125, 40, 125, 25, 105, INKPLATE2_BLACK);
  inkplate.fillTriangle(60, 125, 90, 125, 75, 105, INKPLATE2_RED);

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
  url="https://github.com/SolderedElectronics/Inkplate-Arduino-library/blob/dev/examples/Inkplate2/Basic/Inkplate2_Black_White_Red/Inkplate2_Black_White_Red.ino" 
/>

<InfoBox>For more advanced usage, visit the [Inkplate 2 examples directory](https://github.com/SolderedElectronics/Inkplate-Arduino-library/tree/dev/examples/Inkplate2).</InfoBox>