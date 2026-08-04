---  
slug: /inkplate/6/basics/drawing-graphics  
title: Inkplate 6 – Drawing graphics
sidebar_label: Drawing graphics
id: graphics  
---  
Inkplate 6 allows you to draw graphics on a **800 x 600px canvas**.

<InfoBox>**Adafruit GFX** is the graphics library included in the Inkplate library for drawing graphics. For more details, refer to the **official repository**:<QuickLink title="Adafruit GFX Library" 
  description="The core graphics library for Inkplate library, created by Adafruit."
  url="https://github.com/adafruit/Adafruit-GFX-Library" 
/></InfoBox>

---

## Drawing geometric shapes

Below is an example demonstrating the functions used for drawing graphics on the Inkplate 6:

<InfoBox>The **color** parameter in these functions depends on the display mode. In black-and-white mode, use `BLACK` or `WHITE`. In grayscale mode, use values from 0 to 7. Refer to the [**display modes**](/inkplate/6/basics/basic-display-modes/) page for more details.</InfoBox>

```cpp
#include "Inkplate.h"
Inkplate display(INKPLATE_3BIT);
void setup() {
    display.begin();
    display.clearDisplay();
    display.display();
    // Draw a pixel
    display.drawPixel(100, 50, 0);
    // Draw a line
    display.drawLine(0, 0, 799, 599, 1);
    // Draw a rectangle
    display.drawRect(100, 100, 200, 200, 2);
    // Draw a filled rectangle
    display.fillRect(300, 100, 200, 300, 3);
    // Draw a circle
    display.drawCircle(512, 100, 75, 4);
    // Draw a filled circle
    display.fillCircle(512, 100, 75, 5);
    // Draw a rounded rectangle
    display.drawRoundRect(310, 300, 400, 300, 10, 4);
    // Draw a filled rounded rectangle
    display.fillRoundRect(310, 300, 400, 300, 10, 3);
    // Draw a triangle
    display.drawTriangle(300, 500, 700, 500, 512, 200, 2);
    // Draw a filled triangle
    display.fillTriangle(350, 467, 650, 467, 512, 250, 1);
    // Update the display to render the drawings
    display.display();
}
void loop() {
}
```

<CenteredImage src="/img/6/drawing_graphics.png" alt="Expected output on Inkplate display" caption="Expected output on Inkplate display." width="750px" />

Below are the detailed references for these functions:

<FunctionDocumentation
  functionName="display.drawPixel()"
  description="Draws a single pixel on the display at the specified coordinates."
  returnType="none"
  parameters={[ 
    { type: 'int', name: 'x', description: 'The x-coordinate of the pixel.' },
    { type: 'int', name: 'y', description: 'The y-coordinate of the pixel.' },
    { type: 'uint8_t', name: 'color', description: 'The color of the pixel.' },
  ]}
/>

<FunctionDocumentation
  functionName="display.drawLine()"
  description="Draws a straight line between two points on the display."
  returnType="none"
  parameters={[
    { type: 'int', name: 'x0', description: 'The x-coordinate of the starting point.' },
    { type: 'int', name: 'y0', description: 'The y-coordinate of the starting point.' },
    { type: 'int', name: 'x1', description: 'The x-coordinate of the ending point.' },
    { type: 'int', name: 'y1', description: 'The y-coordinate of the ending point.' },
    { type: 'uint8_t', name: 'color', description: 'The color of the line.' },
  ]}
/>

<FunctionDocumentation
  functionName="display.drawRect()"
  description="Draws a rectangle outline on the display."
  returnType="none"
  parameters={[
    { type: 'int', name: 'x', description: 'The x-coordinate of the top-left corner.' },
    { type: 'int', name: 'y', description: 'The y-coordinate of the top-left corner.' },
    { type: 'int', name: 'width', description: 'The width of the rectangle.' },
    { type: 'int', name: 'height', description: 'The height of the rectangle.' },
    { type: 'uint8_t', name: 'color', description: 'The color of the rectangle outline.' },
  ]}
/>

<FunctionDocumentation
  functionName="display.fillRect()"
  description="Draws a filled rectangle on the display."
  returnType="none"
  parameters={[
    { type: 'int', name: 'x', description: 'The x-coordinate of the top-left corner.' },
    { type: 'int', name: 'y', description: 'The y-coordinate of the top-left corner.' },
    { type: 'int', name: 'width', description: 'The width of the rectangle.' },
    { type: 'int', name: 'height', description: 'The height of the rectangle.' },
    { type: 'uint8_t', name: 'color', description: 'The fill color.' },
  ]}
/>

<FunctionDocumentation
  functionName="display.drawCircle()"
  description="Draws a circle outline on the display."
  returnType="none"
  parameters={[
    { type: 'int', name: 'x', description: 'The x-coordinate of the circle center.' },
    { type: 'int', name: 'y', description: 'The y-coordinate of the circle center.' },
    { type: 'int', name: 'radius', description: 'The radius of the circle.' },
    { type: 'uint8_t', name: 'color', description: 'The color of the circle outline.' },
  ]}
/>

<FunctionDocumentation
  functionName="display.fillCircle()"
  description="Draws a filled circle on the display."
  returnType="none"
  parameters={[
    { type: 'int', name: 'x', description: 'The x-coordinate of the circle center.' },
    { type: 'int', name: 'y', description: 'The y-coordinate of the circle center.' },
    { type: 'int', name: 'radius', description: 'The radius of the circle.' },
    { type: 'uint8_t', name: 'color', description: 'The fill color.' },
  ]}
/>

<FunctionDocumentation
  functionName="display.drawRoundRect()"
  description="Draws a rounded rectangle outline on the display."
  returnType="none"
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
  functionName="display.fillRoundRect()"
  description="Draws a filled rounded rectangle on the display."
  returnType="none"
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
  functionName="display.drawTriangle()"
  description="Draws a triangle outline on the display."
  returnType="none"
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
  functionName="display.fillTriangle()"
  description="Draws a filled triangle on the display."
  returnType="none"
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
  title="Inkplate6_Black_And_White.ino" 
  description="Full example using a black-and-white display mode on Inkplate 6." 
  url="https://github.com/SolderedElectronics/Inkplate-Arduino-library/blob/master/examples/Inkplate6/Basic/Inkplate6_Black_And_White/Inkplate6_Black_And_White.ino" 
/>

<QuickLink 
  title="Inkplate6_Grayscale.ino" 
  description="Full example using grayscale display mode on Inkplate 6." 
  url="https://github.com/SolderedElectronics/Inkplate-Arduino-library/tree/master/examples/Inkplate6/Basic/Inkplate6_Grayscale" 
/>