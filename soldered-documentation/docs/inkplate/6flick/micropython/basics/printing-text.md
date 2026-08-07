---
slug: /inkplate/6flick/micropython/basics/printing-text
title: Inkplate 6FLICK MicroPython - Printing text
sidebar_label: Printing text
id: printing-text
---

Inkplate 6FLICK allows you to print text on a **1024 x 758 px canvas**.

## Displaying basic information

Below is a simple example demonstrating the simple way of displaying the information on the Inkplate display.

```python
from inkplate6_flick import Inkplate  # Include the Inkplate module

inkplate = Inkplate(Inkplate.INKPLATE_1BIT)  # Create a display instance (8-level grayscale)

inkplate.begin()  # Initialize the display

inkplate.set_text_size(2)  # Scale up the font size

inkplate.set_cursor(380, 350)  # Set the cursor from where the text will be written

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

<CenteredImage src="/img/inkplate6flick-micropython/helloworld.jpg" alt="Inkplate 6FLICK running the example code" caption="Displaying basic information" width="800px" />

---

## Displaying text in Grayscale and more text parameters

Inkplate 6FLICK also lets you render 2-bit grayscale graphics (0-3) on its canvas. You can also modify different text parameters, such as: text color, text size and text wrapping. Below is a simple example demonstrating different text colors using grayscale and different text styles:


<InfoBox>
Color parameter in 'set_text_color()' changes text color as per table below:

| **VALUE** 	| **COLOR** 	|
|---	|---	|
| 0 	| Black 	|
| 1 	| Dark grey 	|
| 2 	| Dark grey 	|
| 3 	| White 	|
</InfoBox>

```python
from inkplate6_flick import Inkplate
import time

# Create Inkplate object in 2-bit grayscale mode
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
inkplate.set_text_color(2)         # light gray
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
    { type: 'Number', name: 'color', description: 'Grayscale value for text (0 = white to 3 = black in 2-bit mode).' }
  ]}
/>

<FunctionDocumentation
  functionName="inkplate.set_text_wrapping()"
  description="Enable or disable automatic text wrapping when reaching the display edge."
  returnDescription="Nothing"
  parameters={[
    { type: 'Boolean', name: 'wrap', description: 'True to wrap text, False to let it continue off-screen.' }
  ]}
/>

<CenteredImage src="/img/inkplate6flick-micropython/text.jpg" alt="Inkplate 6FLICK running the example code" caption="Simple grayscale example with different text styles." width="800px" />

---

## Full examples

<QuickLink title="hello_world.py" 
description="Display text on the screen." 
url="https://github.com/SolderedElectronics/Inkplate-micropython/blob/master/examples/inkplate6flick/hello_world.py" />

<QuickLink title="custom_font.py" 
description="Swap in one of the extra typefaces shipped under fonts/ instead of the default font." 
url="https://github.com/SolderedElectronics/Inkplate-micropython/blob/master/examples/inkplate6flick/custom_font.py" />
