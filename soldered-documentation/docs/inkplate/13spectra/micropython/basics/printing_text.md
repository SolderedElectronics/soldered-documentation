---
slug: /inkplate/13spectra/micropython/basics/printing-text
title: Inkplate 13SPECTRA MicroPython - Printing text
sidebar_label: Printing text
id: 13spectra-printing-text
---

Inkplate 13SPECTRA allows you to print text on a **1600 x 1200px canvass**.

## Displaying basic information

Below is a simple example demonstrating the simple way of displaying the information on the Inkplate display.

```python
from inkplate13SPECTRA import Inkplate
import time

inkplate = Inkplate()
inkplate.begin()
inkplate.clearDisplay()
inkplate.display()

# Putting the text in display buffer
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

[IMAGE PLACEHOLDER] done 

---

## Displaying text in different colors and more text parameters

Inkplate 13SPECTRA also lets you render color graphics on its canvas. You can also modify different text parameters, such as text color, text size and text wrapping. Below is a simple example demonstrating different text colors and different text styles:

<InfoBox>
Color parameter in 'setTextColor()' changes text color as per table below:

| **VALUE** 	| **COLOR** 	|
|---	|---	|
| 0 	| Black 	|
| 1 	| White 	|
| 2 	| Yellow 	|
| 3 	| Red 	|
| 4 	| Blue 	|
| 5 	| Green 	|
</InfoBox>

```python
from inkplate13SPECTRA import inkplate
import time

inkplate=Inkplate()
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

[IMAGE PLACEHOLDER - display output]

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
