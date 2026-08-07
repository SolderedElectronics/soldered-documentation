---
slug: /inkplate/6/micropython/basics/printing-text
title: Inkplate 6 MicroPython - Printing text
sidebar_label: Printing text
id: printing-text
---

Inkplate 6 allows you to print text on a **800 x 600 px canvas**.

## Displaying basic information

Here is the shortest way to get text onto the display.

```python
from inkplate6 import Inkplate  # Include the Inkplate module

inkplate = Inkplate(Inkplate.INKPLATE_2BIT)  # Create a display instance (8-level grayscale)

inkplate.begin()  # Initialize the display

inkplate.set_text_size(2)  # Scale up the font size

inkplate.set_cursor(250, 250)  # Set the cursor from where the text will be written

inkplate.print("Hello world!")  # Print to the display buffer

inkplate.display()  # Display what is drawn to the buffer
```

<FunctionDocumentation
  functionName="inkplate.print()"
  description="Puts the text in display buffer at the current position on display"
  parameters={[
    { type: 'String', name: 'text', description: 'String to render.' }
  ]}
/>

<CenteredImage src="/img/inkplate6-micropython/helloworld.jpg" alt="Inkplate 6 running the example code" caption="Displaying basic information" width="800px" />

---

## Displaying text in grayscale and more text parameters

Inkplate 6 also lets you render grayscale graphics on its canvas, using 8 shades from 0 to 7. You can also modify different text parameters, such as: text color, text size and text wrapping. Below is a simple example demonstrating different text colors using grayscale and different text styles:

<InfoBox>The grayscale mode enum is still named `INKPLATE_2BIT` for backwards compatibility, but the panel is driven with the full 8-level (3-bit) waveform.</InfoBox>

<InfoBox>
Color parameter in 'set_text_color()' changes text color as per table below:

| **VALUE** 	| **COLOR** 	|
|---	|---	|
| 0 	| Black 	|
| 1-3 	| Dark greys 	|
| 4-6 	| Light greys 	|
| 7 	| White 	|
</InfoBox>

```python
from inkplate6 import Inkplate
import time

# Create Inkplate object in grayscale mode (8 shades, 0-7)
inkplate = Inkplate(Inkplate.INKPLATE_2BIT)

# Initialize the display, needs to be called only once
inkplate.begin()

# Clear the frame buffer
inkplate.clear_display()
inkplate.display()


inkplate.set_cursor(50, 50)       
inkplate.set_text_size(1)          
inkplate.set_text_color(0)         # black
inkplate.print("Size 1")

inkplate.set_cursor(50, 100)
inkplate.set_text_size(2)          
inkplate.set_text_color(1)         # dark gray
inkplate.print("Size 2")

inkplate.set_cursor(50, 180)
inkplate.set_text_size(3)          
inkplate.set_text_color(5)         # light gray
inkplate.print("Size 3")

inkplate.set_text_color(0)         # black
long_text = (
    "This is a very long line of text intended to demonstrate how wrapping works. "
    "When wrap mode is enabled, the text will continue onto the next line once it "
    "reaches the edge of the display. This makes it possible to write paragraphs "
    "or larger blocks of text without worrying about manually inserting line breaks. "
    "It is especially useful for rendering user interfaces, menus, or e-books."
)
inkplate.set_cursor(50, 340)
inkplate.set_text_size(1)
inkplate.set_text_wrapping(True)       
inkplate.print(long_text)

inkplate.set_cursor(50, 480)
inkplate.set_text_size(1)
inkplate.set_text_wrapping(False)      
inkplate.print(long_text)

inkplate.display()
```

---
<FunctionDocumentation
  functionName="inkplate.set_cursor()"
  description="Set the cursor position for the next text to be rendered."
  parameters={[
    { type: 'Number', name: 'x', description: 'X coordinate for the text start.' },
    { type: 'Number', name: 'y', description: 'Y coordinate for the text baseline.' }
  ]}
/>

<FunctionDocumentation
  functionName="inkplate.set_text_size()"
  description="Set the text size scaling factor."
  parameters={[
    { type: 'Number', name: 'size', description: 'Scale factor (1 = normal, 2 = double, 3 = triple, …).' }
  ]}
/>

<FunctionDocumentation
  functionName="inkplate.set_text_color"
  description="Set the text color (grayscale level) used for text rendering."
  parameters={[
    { type: 'Number', name: 'color', description: 'Grayscale value for text (0 = black to 7 = white in grayscale mode).' }
  ]}
/>

<FunctionDocumentation
  functionName="inkplate.set_text_wrapping()"
  description="Enable or disable automatic text wrapping when reaching the display edge."
  returnType="none"
  parameters={[
    { type: 'Boolean', name: 'wrap', description: 'True to wrap text, False to let it continue off-screen.' }
  ]}
/>

<CenteredImage src="/img/inkplate6-micropython/text.jpg" alt="Inkplate 6 running the example code" caption="Simple grayscale example with different text styles." width="800px" />

---

## Full examples

<QuickLink title="hello_world.py" 
description="Sets the text size and cursor position, then prints text to the display." 
url="https://github.com/SolderedElectronics/Inkplate-micropython/blob/master/examples/inkplate6/hello_world.py" />

<QuickLink title="custom_font.py" 
description="Swaps the default font for one of the typefaces shipped under fonts/ in the library." 
url="https://github.com/SolderedElectronics/Inkplate-micropython/blob/master/examples/inkplate6/custom_font.py" />
