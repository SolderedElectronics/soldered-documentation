---
slug: /inkplate/6/micropython/basics/printing-text
title: Inkplate 6 MicroPython - Printing text
sidebar_label: Printing text
id: printing-text
---

Inkplate 6 allows you to print text on a **800 x 600 px canvas**.

## Displaying basic information

Below is a simple example demonstrating the simple way of displaying the information on the Inkplate display.

```python
from inkplate6 import Inkplate
import time

inkplate = Inkplate(Inkplate.INKPLATE_1BIT)
inkplate.begin()
inkplate.clearDisplay()
inkplate.display()

#Putting the text in display buffer
inkplate.print("Hello World!")
inkplate.display()

```

<FunctionDocumentation
  functionName="inkplate.print()"
  description="Puts the text in display buffer at the current position on display"
  parameters={[
    { type: 'String', name: 'text', description: 'String to render.' }
  ]}
/>

<CenteredImage src="/img/inkplate10-micropython/helloworld.jpg" alt="Inkplate 10 running the example code" caption="Displaying basic information" width="800px" />

---

## Displaying text in Grayscale and more text parameters

Inkplate 6 also lets you render 2-bit grayscale graphics (0-3) on its canvas. You can also modify different text parameters, such as: text color, text size and text wrapping. Below is a simple example demonstrating different text colors using grayscale and different text styles:


<InfoBox>
Color parameter in 'setTextColor()' changes text color as per table below:

| **VALUE** 	| **COLOR** 	|
|---	|---	|
| 0 	| Black 	|
| 1 	| Dark grey 	|
| 2 	| Dark grey 	|
| 3 	| White 	|
</InfoBox>

```python
from inkplate6 import Inkplate
import time

# Create Inkplate object in 2-bit grayscale mode
inkplate = Inkplate(Inkplate.INKPLATE_2BIT)

# Initialize the display, needs to be called only once
inkplate.begin()

# Clear the frame buffer
inkplate.clearDisplay()
inkplate.display()


inkplate.setCursor(50, 50)       
inkplate.setTextSize(1)          
inkplate.setTextColor(0)         # black
inkplate.print("Size 1")

inkplate.setCursor(50, 100)
inkplate.setTextSize(2)          
inkplate.setTextColor(1)         # dark gray
inkplate.print("Size 2")

inkplate.setCursor(50, 180)
inkplate.setTextSize(3)          
inkplate.setTextColor(2)         # light gray
inkplate.print("Size 3")

inkplate.setTextColor(0)         # black
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

inkplate.setCursor(50, 480)
inkplate.setTextSize(1)
inkplate.setTextWrapping(False)      
inkplate.print(long_text)

inkplate.display()
```

---
<FunctionDocumentation
  functionName="inkplate.setCursor()"
  description="Set the cursor position for the next text to be rendered."
  parameters={[
    { type: 'Number', name: 'x', description: 'X coordinate for the text start.' },
    { type: 'Number', name: 'y', description: 'Y coordinate for the text baseline.' }
  ]}
/>

<FunctionDocumentation
  functionName="inkplate.setTextSize()"
  description="Set the text size scaling factor."
  parameters={[
    { type: 'Number', name: 'size', description: 'Scale factor (1 = normal, 2 = double, 3 = triple, …).' }
  ]}
/>

<FunctionDocumentation
  functionName="inkplate.setTextColor"
  description="Set the text color (grayscale level) used for text rendering."
  parameters={[
    { type: 'Number', name: 'color', description: 'Grayscale value for text (0 = white to 3 = black in 2-bit mode).' }
  ]}
/>

<FunctionDocumentation
  functionName="inkplate.setTextWrapping()"
  description="Enable or disable automatic text wrapping when reaching the display edge."
  returnDescription="Nothing"
  parameters={[
    { type: 'Boolean', name: 'wrap', description: 'True to wrap text, False to let it continue off-screen.' }
  ]}
/>

<CenteredImage src="/img/inkplate10-micropython/text.jpg" alt="Inkplate 10 running the example code" caption="Simple grayscale example with different text styles." width="800px" />