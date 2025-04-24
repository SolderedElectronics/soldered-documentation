---
slug: /inkplate/6motion/basics/drawing-graphics
title: Drawing graphics
id: 6motion-graphics
---

Inkplate 6 MOTION allows you to draw graphics on a **1024x758px canvas**.

<InfoBox>**Adafruit GFX** is the graphics library included in the Inkplate MOTION library for drawing graphics. For more details, refer to the **official repository**:<QuickLink title="Adafruit GFX Library" 
  description="The core graphics library for Inkplate MOTION, created by Adafruit."
  url="https://github.com/adafruit/Adafruit-GFX-Library" 
/></InfoBox>

---

## Drawing Geometric Shapes

Below is an example demonstrating functions used for drawing graphics on the Inkplate 6 MOTION:

<InfoBox>The **color** parameter in these functions depends on the display mode. In black-and-white mode, use `BLACK` or `WHITE`. In grayscale mode, use values from 0 to 15. Refer to the [**display modes**](/inkplate/6motion/basics/basic-display-modes) page for more details.</InfoBox>

```cpp
inkplate.begin(INKPLATE_BLACKWHITE); // Initialize Inkplate

// Draw a single pixel
inkplate.drawPixel(100, 50, BLACK);
// Draw a line
inkplate.drawLine(0, 0, 1023, 757, BLACK);
// Draw a rectangle
inkplate.drawRect(300, 300, 400, 300, BLACK);
// Draw a filled rectangle
inkplate.fillRect(300, 300, 400, 300, BLACK);
// Draw a circle
inkplate.drawCircle(512, 379, 75, BLACK);
// Draw a filled circle
inkplate.fillCircle(512, 379, 75, BLACK);
// Draw a rounded rectangle
inkplate.drawRoundRect(300, 300, 400, 300, 10, BLACK);
// Draw a filled rounded rectangle
inkplate.fillRoundRect(300, 300, 400, 300, 10, BLACK);
// Draw a triangle
inkplate.drawTriangle(300, 500, 700, 500, 512, 200, BLACK);
// Draw a filled triangle
inkplate.fillTriangle(350, 467, 650, 467, 512, 250, BLACK);

inkplate.display(); // Update the display to render the drawings
```


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

## Full examples

<QuickLink 
  title="Inkplate_6_Motion_Simple_BW" 
  description="Example on how to draw simple graphics in black and white mode"
  url="https://github.com/SolderedElectronics/Inkplate_Motion_Arduino_Library/blob/main/examples/Inkplate6Motion/Basic/Inkplate_6_Motion_Simple_BW/Inkplate_6_Motion_Simple_BW.ino" 
/>
<QuickLink 
  title="Inkplate_6_Motion_Simple_Grayscale" 
  description="Example on how to draw simple graphics in grayscale"
  url="https://github.com/SolderedElectronics/Inkplate_Motion_Arduino_Library/blob/main/examples/Inkplate6Motion/Basic/Inkplate_6_Motion_Simple_Grayscale/Inkplate_6_Motion_Simple_Grayscale.ino" 
/>
