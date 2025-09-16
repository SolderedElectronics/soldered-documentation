---
slug: /inkplate_micropython/inkplate10/examples/drawing-shapes
title: Drawing shapes
id: drawing-shapes
---

Inkplate 10 allows you to draw different geometric shapes anywhere on it's **1200 x 825 px canvas**. The shapes can be **filled** or **hollow**.

---

## Drawing Shapes
Below is an example showing how to draw basic shapes in **BW display mode**:

<InfoBox> If you want to use the grayscale mode, simply change the constructor value and instead of using `inkplate.BLACK` use a numeric value: 0-3</InfoBox>

```python
inkplate.drawPixel(100, 100, inkplate.BLACK)
inkplate.drawRect(50, 50, 75, 75, inkplate.BLACK)
inkplate.drawCircle(200, 200, 30, inkplate.BLACK)
inkplate.fillCircle(300, 300, 30, inkplate.BLACK)
inkplate.drawFastHLine(20, 100, 50, inkplate.BLACK)
inkplate.drawFastVLine(100, 20, 50, inkplate.BLACK)
inkplate.drawLine(100, 100, 400, 400, inkplate.BLACK)
inkplate.drawRoundRect(100, 10, 100, 100, 10, inkplate.BLACK)
inkplate.fillRoundRect(10, 100, 100, 100, 10, inkplate.BLACK)
inkplate.drawTriangle(300, 100, 400, 150, 400, 100, inkplate.BLACK)
```

---

<FunctionDocumentation
functionName="inkplate.drawPixel(x, y, color)"
description="Set a single pixel in the frame buffer."
returnDescription="Nothing"
parameters={[
{ type: 'Number', name: 'x', description: 'X coordinate.' },
{ type: 'Number', name: 'y', description: 'Y coordinate.' },
{ type: 'Const', name: 'color', description: 'Color constant (BLACK or WHITE in BW mode).' }
]}
/>

<FunctionDocumentation
functionName="inkplate.drawRect(x, y, w, h, color)"
description="Draw an unfilled rectangle outline."
returnDescription="Nothing"
parameters={[
{ type: 'Number', name: 'x', description: 'Left X.' },
{ type: 'Number', name: 'y', description: 'Top Y.' },
{ type: 'Number', name: 'w', description: 'Width in pixels.' },
{ type: 'Number', name: 'h', description: 'Height in pixels.' },
{ type: 'Const', name: 'color', description: 'Outline color.' }
]}
/>

<FunctionDocumentation
functionName="inkplate.drawCircle(x0, y0, r, color)"
description="Draw an unfilled circle."
returnDescription="Nothing"
parameters={[
{ type: 'Number', name: 'x0', description: 'Center X.' },
{ type: 'Number', name: 'y0', description: 'Center Y.' },
{ type: 'Number', name: 'r', description: 'Radius in pixels.' },
{ type: 'Const', name: 'color', description: 'Outline color.' }
]}
/>

<FunctionDocumentation
functionName="inkplate.fillCircle(x0, y0, r, color)"
description="Draw a filled circle."
returnDescription="Nothing"
parameters={[
{ type: 'Number', name: 'x0', description: 'Center X.' },
{ type: 'Number', name: 'y0', description: 'Center Y.' },
{ type: 'Number', name: 'r', description: 'Radius in pixels.' },
{ type: 'Const', name: 'color', description: 'Fill color.' }
]}
/>

<FunctionDocumentation
functionName="inkplate.drawFastHLine(x, y, w, color)"
description="Draw a horizontal line quickly."
returnDescription="Nothing"
parameters={[
{ type: 'Number', name: 'x', description: 'Start X.' },
{ type: 'Number', name: 'y', description: 'Y position.' },
{ type: 'Number', name: 'w', description: 'Line width in pixels.' },
{ type: 'Const', name: 'color', description: 'Line color.' }
]}
/>

<FunctionDocumentation
functionName="inkplate.drawFastVLine(x, y, h, color)"
description="Draw a vertical line quickly."
returnDescription="Nothing"
parameters={[
{ type: 'Number', name: 'x', description: 'X position.' },
{ type: 'Number', name: 'y', description: 'Start Y.' },
{ type: 'Number', name: 'h', description: 'Line height in pixels.' },
{ type: 'Const', name: 'color', description: 'Line color.' }
]}
/>

<FunctionDocumentation
functionName="inkplate.drawLine(x0, y0, x1, y1, color)"
description="Draw a line from one point to another."
returnDescription="Nothing"
parameters={[
{ type: 'Number', name: 'x0', description: 'Start X.' },
{ type: 'Number', name: 'y0', description: 'Start Y.' },
{ type: 'Number', name: 'x1', description: 'End X.' },
{ type: 'Number', name: 'y1', description: 'End Y.' },
{ type: 'Const', name: 'color', description: 'Line color.' }
]}
/>

<FunctionDocumentation
functionName="inkplate.drawRoundRect(x, y, w, h, radius, color)"
description="Draw an unfilled rectangle with rounded corners."
returnDescription="Nothing"
parameters={[
{ type: 'Number', name: 'x', description: 'Left X.' },
{ type: 'Number', name: 'y', description: 'Top Y.' },
{ type: 'Number', name: 'w', description: 'Width in pixels.' },
{ type: 'Number', name: 'h', description: 'Height in pixels.' },
{ type: 'Number', name: 'radius', description: 'Corner radius in pixels.' },
{ type: 'Const', name: 'color', description: 'Outline color.' }
]}
/>

<FunctionDocumentation
functionName="inkplate.fillRoundRect(x, y, w, h, radius, color)"
description="Draw a filled rectangle with rounded corners."
returnDescription="Nothing"
parameters={[
{ type: 'Number', name: 'x', description: 'Left X.' },
{ type: 'Number', name: 'y', description: 'Top Y.' },
{ type: 'Number', name: 'w', description: 'Width in pixels.' },
{ type: 'Number', name: 'h', description: 'Height in pixels.' },
{ type: 'Number', name: 'radius', description: 'Corner radius in pixels.' },
{ type: 'Const', name: 'color', description: 'Fill color.' }
]}
/>

<FunctionDocumentation
functionName="inkplate.drawTriangle(x0, y0, x1, y1, x2, y2, color)"
description="Draw a triangle outline using three vertices."
returnDescription="Nothing"
parameters={[
{ type: 'Number', name: 'x0', description: 'Vertex A X.' },
{ type: 'Number', name: 'y0', description: 'Vertex A Y.' },
{ type: 'Number', name: 'x1', description: 'Vertex B X.' },
{ type: 'Number', name: 'y1', description: 'Vertex B Y.' },
{ type: 'Number', name: 'x2', description: 'Vertex C X.' },
{ type: 'Number', name: 'y2', description: 'Vertex C Y.' },
{ type: 'Const', name: 'color', description: 'Outline color.' }
]}
/>

---

## Full example

<QuickLink 
  title="Inkplate10 basicBW.py" 
  description="An example showing how to draw basic black and white shapes also, it will draw a bitmap of the Soldered logo in the middle"
  url="https://github.com/SolderedElectronics/Inkplate-micropython/blob/micropython-library-revamp/Examples/Inkplate10/basicBW.py" 
/>