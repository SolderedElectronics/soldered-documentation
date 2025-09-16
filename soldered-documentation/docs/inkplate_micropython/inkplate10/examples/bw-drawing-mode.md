---
slug: /inkplate_micropython/inkplate10/examples/bw-drawing-mode
title: Black & White
id: bw-drawing-mode
pagination_prev: NULL
---

Inkplate 10 allows you to draw graphics on a **1200 x 825px canvas.**

---


## Displaying basic information 
Below is a simple example demonstrating the procedure of displaying the information on the Inkplate display.

```python
from inkplate10 import Inkplate
import time

inkplate = Inkplate(Inkplate.INKPLATE_1BIT)
inkplate.begin()
inkplate.clearDisplay()
inkplate.display()
inkplate.print("Hello World!")
inkplate.display()

```

---

<FunctionDocumentation
  functionName="inkplate = Inkplate(Inkplate.INKPLATE_1BIT)"
  description="Creating Inkplate object in 1-bit mode, black and white colors only."
  returnDescription="Nothing"
  parameters={[
    { type: 'Number', name: 'mode', description: 'Value that sets the display mode as either Black-White (INKPLATE_1BIT) or 2bit Grayscale (INKPLATE_2bit) ' }
  ]}
/>

<FunctionDocumentation
  functionName="inkplate.begin()"
  description="Initializing the display, this must be called only once after creating the Inkplate object."
  returnDescription="Nothing"
/>

<FunctionDocumentation
  functionName="inkplate.clearDisplay()"
  description="Clears the internal frame buffer (does not change the panel until you update)."
  returnDescription="Nothing"
/>

<FunctionDocumentation
  functionName="inkplate.display()"
  description="Performs a full-screen refresh, sending the current frame buffer to the panel."
  returnDescription="Nothing"
/>

---

## Full example

<QuickLink 
  title="Inkplate10_basicBW.py" 
  description="An example showing how to draw basic black and white shapes."
  url="https://github.com/SolderedElectronics/Inkplate-micropython/blob/micropython-library-revamp/Examples/Inkplate10/basicBW.py" 
/>