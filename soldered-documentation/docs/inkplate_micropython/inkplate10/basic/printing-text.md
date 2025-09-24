---
slug: /inkplate_micropython/inkplate10/basic/printing-text
title: Inkplate 10 MicroPython - Printing Text
id: printing-text
---

inkplate 10 allows you to modify different text parameters, such as: text color, text size and more.

<CenteredImage src="/img/inkplate10-micropython/text.jpg" alt="Inkplate 10 running the example code" caption="Inkplate 10 running the example code" width="800px" />
---

## Printing text

Below is a simple example showcasing some of the basic text manipulation capabilities:

```python
from inkplate10 import Inkplate
import time

# Create Inkplate object in 1-bit mode, black and white colors only
inkplate = Inkplate(Inkplate.INKPLATE_1BIT)

# Initialize the display, needs to be called only once
inkplate.begin()

# Clear the frame buffer
inkplate.clearDisplay()
inkplate.display()


inkplate.setCursor(50, 50)       
inkplate.setTextSize(1)          
inkplate.setTextColor(0)         # lightest text (white)
inkplate.print("Size 1")

inkplate.setCursor(50, 100)
inkplate.setTextSize(2)          
inkplate.setTextColor(1)         # light gray
inkplate.print("Size 2")

inkplate.setCursor(50, 180)
inkplate.setTextSize(3)          
inkplate.setTextColor(2)         # dark gray
inkplate.print("Size 3")

inkplate.setTextColor(3)         # darkest text (black)
long_text = (
    "This is a very long line of text intended to demonstrate how wrapping works. "
    "When wrap mode is enabled, the text will continue onto the next line once it "
    "reaches the edge of the display. This makes it possible to write paragraphs "
    "or larger blocks of text without worrying about manually inserting line breaks. "
    "It is especially useful for rendering user interfaces, menus, or e-books."
)
inkplate.setCursor(50, 340)
inkplate.setTextSize(1)
inkplate.setTextWrapping(True)       
inkplate.print(long_text)

inkplate.setCursor(50, 460)
inkplate.setTextSize(1)
inkplate.setTextWrapping(False)      
inkplate.print(long_text)

inkplate.display()
```

---

<FunctionDocumentation
  functionName="inkplate.setCursor(x, y)"
  description="Set the cursor position for the next text to be rendered."
  returnDescription="Nothing"
  parameters={[
    { type: 'Number', name: 'x', description: 'X coordinate for the text start.' },
    { type: 'Number', name: 'y', description: 'Y coordinate for the text baseline.' }
  ]}
/>

<FunctionDocumentation
  functionName="inkplate.setTextSize(size)"
  description="Set the text size scaling factor."
  returnDescription="Nothing"
  parameters={[
    { type: 'Number', name: 'size', description: 'Scale factor (1 = normal, 2 = double, 3 = triple, …).' }
  ]}
/>

<FunctionDocumentation
  functionName="inkplate.setTextColor(color)"
  description="Set the text foreground color (grayscale level)."
  returnDescription="Nothing"
  parameters={[
    { type: 'Number', name: 'color', description: 'Text color, grayscale value (0 = white to 3 = black in 2-bit mode).' }
  ]}
/>

<FunctionDocumentation
  functionName="inkplate.setTextWrapping(wrap)"
  description="Enable or disable automatic text wrapping when reaching the display edge."
  returnDescription="Nothing"
  parameters={[
    { type: 'Boolean', name: 'wrap', description: 'True to wrap text, False to let it continue off-screen.' }
  ]}
/>

<FunctionDocumentation
  functionName="inkplate.print(text)"
  description="Write text to the display buffer at the current cursor position."
  returnDescription="Nothing"
  parameters={[
    { type: 'String', name: 'text', description: 'The text string to render.' }
  ]}
/>

---
