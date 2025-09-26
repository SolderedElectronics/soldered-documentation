---
slug: /inkplate/10/micropython/basics/drawing-graphics
title: Inkplate 10 MicroPython - Drawing Graphics
sidebar_label: Drawing Graphics
id: drawing-graphics
---

Inkplate 10 allows you to draw different geometric shapes anywhere on its **1200 x 825px canvas**. The shapes can be **filled** or **hollow**

---

## Drawing Shapes
Below is a example that demonstrates how to draw basic shapes in **Black-White display mode**.

<InfoBox> If you want to use the grayscale mode, simply change the constructor value and instead of using `inkplate.BLACK` use a numeric value: 0-3</InfoBox>

```python
from inkplate10 import Inkplate
import time

inkplate = Inkplate(Inkplate.INKPLATE_1BIT)
inkplate.begin()
inkplate.clearDisplay()
inkplate.display()

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

inkplate.display()
```

<FunctionDocumentation
functionName="inkplate.drawPixel()"
description="Set a single pixel in the frame buffer."
parameters={[
{ type: 'Number', name: 'x', description: 'X coordinate.' },
{ type: 'Number', name: 'y', description: 'Y coordinate.' },
{ type: 'Const', name: 'color', description: 'Color constant (BLACK or WHITE in BW mode).' }
]}
/>

<FunctionDocumentation
functionName="inkplate.drawRect()"
description="Draw an unfilled rectangle outline."
parameters={[
{ type: 'Number', name: 'x', description: 'Left X.' },
{ type: 'Number', name: 'y', description: 'Top Y.' },
{ type: 'Number', name: 'w', description: 'Width in pixels.' },
{ type: 'Number', name: 'h', description: 'Height in pixels.' },
{ type: 'Const', name: 'color', description: 'Outline color.' }
]}
/>

<FunctionDocumentation
functionName="inkplate.drawCircle()"
description="Draw an unfilled circle."
parameters={[
{ type: 'Number', name: 'x0', description: 'Center X.' },
{ type: 'Number', name: 'y0', description: 'Center Y.' },
{ type: 'Number', name: 'r', description: 'Radius in pixels.' },
{ type: 'Const', name: 'color', description: 'Outline color.' }
]}
/>

<FunctionDocumentation
functionName="inkplate.fillCircle()"
description="Draw a filled circle."
parameters={[
{ type: 'Number', name: 'x0', description: 'Center X.' },
{ type: 'Number', name: 'y0', description: 'Center Y.' },
{ type: 'Number', name: 'r', description: 'Radius in pixels.' },
{ type: 'Const', name: 'color', description: 'Fill color.' }
]}
/>

<FunctionDocumentation
functionName="inkplate.drawFastHLine()"
description="Draw a horizontal line quickly."
parameters={[
{ type: 'Number', name: 'x', description: 'Start X.' },
{ type: 'Number', name: 'y', description: 'Y position.' },
{ type: 'Number', name: 'w', description: 'Line width in pixels.' },
{ type: 'Const', name: 'color', description: 'Line color.' }
]}
/>

<FunctionDocumentation
functionName="inkplate.drawFastVLine()"
description="Draw a vertical line quickly."
parameters={[
{ type: 'Number', name: 'x', description: 'X position.' },
{ type: 'Number', name: 'y', description: 'Start Y.' },
{ type: 'Number', name: 'h', description: 'Line height in pixels.' },
{ type: 'Const', name: 'color', description: 'Line color.' }
]}
/>

<FunctionDocumentation
functionName="inkplate.drawLine()"
description="Draw a line from one point to another."
parameters={[
{ type: 'Number', name: 'x0', description: 'Start X.' },
{ type: 'Number', name: 'y0', description: 'Start Y.' },
{ type: 'Number', name: 'x1', description: 'End X.' },
{ type: 'Number', name: 'y1', description: 'End Y.' },
{ type: 'Const', name: 'color', description: 'Line color.' }
]}
/>

<FunctionDocumentation
functionName="inkplate.drawRoundRect()"
description="Draw an unfilled rectangle with rounded corners."
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
functionName="inkplate.fillRoundRect()"
description="Draw a filled rectangle with rounded corners."
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
functionName="inkplate.drawTriangle()"
description="Draw a triangle outline using three vertices."
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

<CenteredImage src="/img/inkplate10-micropython/shapes.jpg" alt="Inkplate 10 running the example code" caption="Simple predefined shapes." width="800px" />