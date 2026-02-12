---
slug: /inkplate/13spectra/micropython/basics/drawing-graphics
title: Inkplate 13SPECTRA MicroPython - Drawing Graphics
sidebar_label: Drawing Graphics
id: 13spectra-drawing-graphics
---

Inkplate 13SPECTRA allows you to draw different geometric shapes anywhere on its **1600 x 1200px canvas**. The shapes can be **filled** or **hollow**.

---

## Drawing shapes
Below is a example that demonstates how to draw basic shapes in **different colors**.

```python
from inkplate13SPECTRA import Inkplate
import time

inkplate = Inkplate()
inkplate.begin()
inkplate.clearDisplay()
inkplate.display()

inkplate.drawPixel(800, 600, inkplate.BLACK);

inkplate.drawRect(60, 60, 1480, 1080, inkplate.BLACK);
inkplate.drawRect(80, 80, 1440, 1040, inkplate.BLUE);
inkplate.drawRoundRect(110, 110, 1380, 980, 40, inkplate.YELLOW);

inkplate.drawLine(60, 60, 1540, 1140, inkplate.BLACK);
inkplate.drawLine(1540, 60, 60, 1140, inkplate.BLACK);

inkplate.drawFastHLine(60, 600, 1480, inkplate.RED);
inkplate.drawFastVLine(800, 60, 1080, inkplate.GREEN);

inkplate.drawCircle(400, 300, 120, inkplate.BLUE);
inkplate.fillCircle(1200, 300, 120, inkplate.GREEN);
inkplate.drawCircle(1200, 300, 120, inkplate.BLACK);

inkplate.fillRoundRect(220, 760, 420, 300, 35, inkplate.YELLOW);
inkplate.drawRoundRect(220, 760, 420, 300, 35, inkplate.BLACK);

inkplate.fillRect(980, 760, 420, 300, inkplate.WHITE);
inkplate.drawRect(980, 760, 420, 300, inkplate.BLACK);

inkplate.drawTriangle(800, 140, 680, 360, 920, 360, inkplate.RED);
inkplate.fillTriangle(800, 520, 650, 720, 950, 720, inkplate.BLUE);
inkplate.drawTriangle(800, 520, 650, 720, 950, 720, inkplate.BLACK);

inkplate.drawFastHLine(200, 180, 1200, inkplate.YELLOW);
inkplate.drawFastHLine(200, 1020, 1200, inkplate.YELLOW);
inkplate.drawFastVLine(220, 200, 800, inkplate.BLUE);
inkplate.drawFastVLine(1380, 200, 800, inkplate.BLUE);

inkplate.fillCircle(100, 100, 18, inkplate.RED);
inkplate.fillCircle(1500, 100, 18, inkplate.GREEN);
inkplate.fillCircle(100, 1100, 18, inkplate.BLUE);
inkplate.fillCircle(1500, 1100, 18, inkplate.BLACK);

inkplate.drawRect(50, 50, 75, 75, inkplate.BLUE);
inkplate.drawCircle(200, 200, 30, inkplate.GREEN);
inkplate.fillCircle(300, 300, 30, inkplate.BLACK);
inkplate.drawFastHLine(20, 100, 50, inkplate.RED);
inkplate.drawFastVLine(100, 20, 50, inkplate.BLACK);
inkplate.drawLine(100, 100, 400, 400, inkplate.BLACK);
inkplate.drawRoundRect(100, 10, 100, 100, 10, inkplate.YELLOW);
inkplate.fillRoundRect(10, 100, 100, 100, 10, inkplate.BLACK);
inkplate.drawTriangle(300, 100, 400, 150, 400, 100, inkplate.BLACK);


inkplate.display()
```

[LINK PLACEHOLDER - display output]

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