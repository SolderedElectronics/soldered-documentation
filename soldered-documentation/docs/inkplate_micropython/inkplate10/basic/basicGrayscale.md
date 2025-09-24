---
slug: /inkplate_micropython/inkplate10/basic/basic-grayscale
title: Inkplate 10 MicroPython - Grayscale
id: basic-grayscale
pagination_prev: NULL

---

Inkplate 10 lets you render 2-bit grayscale graphics (0–7) on a 1200 × 825 px canvas.

<CenteredImage src="/img/inkplate10-micropython/grayscale.jpg" alt="Inkplate 10 running the example code" caption="Inkplate 10 running the example code" width="800px" />

---

## Drawing in Grayscale

Below is an example demonstrating the the grayscale functionality on text.

<InfoBox>In grayscale mode, pass an integer from **0 (black) to 3(white)** as the `color` parameter.</InfoBox>

```python
from inkplate10 import Inkplate
import time

inkplate=Inkplate(Inkplate.INKPLATE_2BIT)
inkplate.begin()
inkplate.clearDisplay()
inkplate.display()
inkplate.setTextSize(3)

inkplate.setTextColor(1)
inkplate.print("Hel")

inkplate.setTextColor(0)
inkplate.print("lo W")

inkplate.setTextColor(2)
inkplate.print("orld!")

inkplate.display()
```
 
---

<FunctionDocumentation
  functionName="inkplate = Inkplate(Inkplate.INKPLATE_2BIT)"
  description="Create an Inkplate object in 2-bit grayscale mode."
  returnDescription="Nothing"
  parameters={[
    { type: 'Number', name: 'mode', description: 'Display mode: INKPLATE_1BIT (BW) or INKPLATE_2BIT (2-bit grayscale).' }
  ]}
/>

<FunctionDocumentation
  functionName="inkplate.begin()"
  description="Initialize the display hardware and internal state. Call once after creating the object."
  returnDescription="Nothing"
/>

<FunctionDocumentation
  functionName="inkplate.clearDisplay()"
  description="Clear the internal frame buffer (the panel won’t change until you refresh)."
  returnDescription="Nothing"
/>

<FunctionDocumentation
  functionName="inkplate.display()"
  description="Perform a full refresh, sending the current frame buffer to the e-paper panel."
  returnDescription="Nothing"
/>

<FunctionDocumentation
  functionName="inkplate.setTextSize(size)"
  description="Set the text size scaling factor for subsequent printed text."
  returnDescription="Nothing"
  parameters={[
    { type: 'Number', name: 'size', description: 'Scale factor (1 = default, 2 = double size, 3 = triple, …).' }
  ]}
/>

<FunctionDocumentation
  functionName="inkplate.setTextColor(color)"
  description="Set the text color (grayscale level) used by subsequent text rendering."
  returnDescription="Nothing"
  parameters={[
    { type: 'Number', name: 'color', description: 'Grayscale value for text (0 = white to 3 = black in 2-bit mode).' }
  ]}
/>

<FunctionDocumentation
  functionName="inkplate.print(text)"
  description="Write text to the display buffer at the current cursor position."
  returnDescription="Nothing"
  parameters={[
    { type: 'String', name: 'text', description: 'String to render.' }
  ]}
/>
---

## Full example
<QuickLink title="Inkplate10_basicGrayscale.py" description="Official example showing how to draw grayscale shades and render a bitmap on Inkplate 10." 
url="https://github.com/SolderedElectronics/Inkplate-micropython/blob/micropython-library-revamp/Examples/Inkplate10/basicGrayscale.py" 
/>