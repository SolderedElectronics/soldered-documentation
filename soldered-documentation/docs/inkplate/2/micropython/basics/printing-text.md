---  
slug: /inkplate/2/micropython/basics/print-text
title: Inkplate 2 – Printing text
sidebar_label: Printing text
id: print-text
hide_title: false  
---

Printing text on Inkplate is simple and requires only a few functions. The library also supports custom fonts of different sizes.

To print text, use `setCursor` followed by `print`. If you're using the default font, you can use `setTextSize` to increase the font size:

```python
from inkplate2 import Inkplate # Include the Inkplate module

inkplate = Inkplate() # Create an instance of the display

inkplate.begin() # Initialize the display

inkplate.set_text_size(2) # Scale up the font size

inkplate.set_cursor(25,35) # Set the cursor from where the text will be written

inkplate.print("Hello world") # Print text to frame buffer

inkplate.display() # Display what is drawn to the buffer
```

<CenteredImage src="/img/inkplate_2/hello-world.jpg" alt="Expected output on Inkplate display" caption="Hello world output on display" />

<FunctionDocumentation
  functionName="inkplate.set_text_size()"
  description="Increases the text size by a given factor."
  returnDescription="None"
  parameters={[ 
    { type: 'int', name: 's', description: 'Size factor. 1 is default size, 2 is twice as large, 3 is three times larger, etc.' }
  ]}
/>
<FunctionDocumentation
  functionName="inkplate.set_cursor()"
  description="Move the cursor to point at given position on the screen starting from the upper left corner."
  returnDescription="None"
  parameters={[ 
    { type: 'int', name: 'x', description: 'X coordinate value' },
    { type: 'int', name: 'y', description: 'Y coordinate value' }
  ]}
/>
<FunctionDocumentation
  functionName="inkplate.print()"
  description="Prints text at the previously set cursor position. This is the standard print function."
  returnDescription="None"
  parameters={[ 
    { type: 'char', name: 'text', description: 'String to print on the display.' }
  ]}
/>

## Alternative fonts example
Here we will print text using different fonts on our Inkplate board. All of the fonts are available on **[Inkplate-MicroPython GitHub](https://github.com/SolderedElectronics/Inkplate-micropython/tree/master/fonts)**, just upload **.py** file to your board and import it in your code:

```python
from inkplate2 import Inkplate
# Import custom fonts
import free_serif_bold_italic_18px as SerifBoldItalic
import free_sans_bold_oblique_32px as SansBoldOblique
# Create Inkplate object
inkplate = Inkplate()

# Initialize the display
inkplate.begin()

# Set custom fonts and print example text
inkplate.set_font(SerifBoldItalic)
inkplate.set_cursor(5, 5)
inkplate.print("Serif Bold Italic")

inkplate.set_font(SansBoldOblique)
inkplate.set_cursor(5, 30) # The 32px font is much taller, so give it its own line
inkplate.print("Sans Bold")

# Display from buffer
inkplate.display()
```

<CenteredImage src="/img/inkplate_2/fonts.jpg" alt="Expected output on Inkplate display" caption="Custom Fonts Example" />

## Custom fonts
Alternatively, if you want to create your own custom font to use on your board, take a **.ttf** or **.otf** font and turn it into a Python bytearray using the following command:

```
python font_to_py.py SourceSans3-Regular.ttf 20 output.py
```

where number 20 represents maximum font size.

<InfoBox> This external python script can be found on this **[GitHub repo](https://github.com/peterhinch/micropython-font-to-py)**. </InfoBox>

## Example of custom font

```python
from inkplate2 import Inkplate
import drippy as drippy

# Create object and initialize Inkplate
inkplate = Inkplate()
inkplate.begin()

# Set custom font and print text
inkplate.set_font(drippy)
inkplate.set_cursor(5, 40)
inkplate.println("Drippy")

# Update the display
inkplate.display()
```

<CenteredImage src="/img/inkplate_2/drippy-font.jpg" alt="Expected output on Inkplate display" caption="Drippy Custom Font Example" />

---

## Full examples

<QuickLink title="hello_world.py" 
description="Displays 'Hello world!' text on the Inkplate 2 screen." 
url="https://github.com/SolderedElectronics/Inkplate-micropython/blob/master/examples/inkplate2/hello_world.py" />

<QuickLink title="custom_font.py" 
description="Swap in one of the extra typefaces shipped under fonts/ instead of the default font." 
url="https://github.com/SolderedElectronics/Inkplate-micropython/blob/master/examples/inkplate2/custom_font.py" />
