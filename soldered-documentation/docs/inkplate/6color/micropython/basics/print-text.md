---  
slug: /inkplate/6color/micropython/basics/print-text
title: Inkplate 6COLOR – Printing text
sidebar_label: Printing text
id: print-text
hide_title: false  
---

Printing text on Inkplate is simple and requires only a few functions. The library also supports custom fonts of different sizes.

## Simple colored text example

<InfoBox>
There are a total of **7 colors** to choose from:
| Color | Value | Int Value
|-------|-------|----------|
| BLACK | INKPLATE_BLACK | 0 |
| WHITE | INKPLATE_WHITE | 1 |
| GREEN | INKPLATE_GREEN | 2 |
| BLUE  | INKPLATE_BLUE  | 3 |
| RED   | INKPLATE_RED   | 4 |
| YELLOW | INKPLATE_YELLOW | 5 |
| ORANGE | INKPLATE_ORANGE | 6 |
</InfoBox>

To print text, use `set_cursor` followed by `print`. If you're using the default font, you may want to use `set_text_size` to increase the font size:

```python
from inkplate6_color import Inkplate  # Include the Inkplate module

inkplate = Inkplate()  # Create an instance of the display
inkplate.begin()  # Initialize the display

inkplate.set_text_size(2)  # Scale up the font size

inkplate.set_cursor(180, 180)  # Set the cursor from where the text will be written

hello_world = "Hello world!"  # Declare the string we want to print

i = 0  # Declare the counter we will use to iterate through the colors

# Iterate through each character in the string
for char in hello_world:
    # Change the color of every character
    inkplate.set_text_color(i)
    # Print a single character to the framebuffer
    inkplate.print(char)
    # Iterate the color counter
    i = i + 1
    if i == 1:  # If the color is white, skip it
        i = i + 1
    elif i // 7 > 0:  # If we displayed all 7 colors, return to the first one
        i = 0

inkplate.display()  # Display what is drawn to the buffer
```

<CenteredImage src="/img/6color/hello-world.jpg" alt="Expected output on Inkplate display" caption="Hello world output on display" />

<FunctionDocumentation
  functionName="inkplate.set_text_size()"
  description="Increases the text size by a given factor."
  returnType="none"
  parameters={[ 
    { type: 'int', name: 's', description: 'Size factor. 1 is default size, 2 is twice as large, 3 is three times larger, etc.' }
  ]}
/>
<FunctionDocumentation
  functionName="inkplate.set_cursor()"
  description="Move the cursor to point at given position on the screen starting from the upper left corner."
  returnType="none"
  parameters={[ 
    { type: 'int', name: 'x', description: 'X coordinate value' },
    { type: 'int', name: 'y', description: 'Y coordinate value' }
  ]}
/>
<FunctionDocumentation
  functionName="inkplate.print()"
  description="Prints text at the previously set cursor position. This is the standard print function."
  returnType="none"
  parameters={[ 
    { type: 'char', name: 'text', description: 'String to print on the display.' }
  ]}
/>
<FunctionDocumentation
  functionName="inkplate.set_text_color()"
  description="Sets the color of the text. Must be called before printing."
  returnType="none"
  parameters={[ 
    { type: 'int', name: 'color', description: 'Set text color.' }
  ]}
/>

## Alternative fonts example
Here we will print text using different fonts on our Inkplate board. All of the fonts are available on **[Inkplate-MicroPython GitHub](https://github.com/SolderedElectronics/Inkplate-micropython/tree/master/fonts)**, just upload **.py** file to your board and import it in your code:

```python
from inkplate6_color import Inkplate
# Import custom fonts
import FreeMono_12px as Mono12
import FreeSerifBold_18px as SerifBold18
import FreeSansOblique_24px as SansOblique24
import FreeSansBoldOblique_32px as SansBoldOblique32
import FreeSerifItalic_48px as SerifItalic48

# Create Inkplate object
inkplate = Inkplate()

# Initialize the display
inkplate.begin()

mono = "Mono 12px Text Example"
serifBold = "Serif Bold 18px Example"
sansOblique = "Sans Oblique 24px Example"
sansBoldOblique = "Sans Bold Oblique 32px Example"
serifExample = "Serif Italic 48px Example"

# Set cursor and print example texts using different font styles
inkplate.set_cursor(0, 20)

inkplate.set_font(Mono12)
inkplate.println(mono)

inkplate.set_font(SerifBold18)
inkplate.println(serifBold)

inkplate.set_font(SansOblique24)
inkplate.println(sansOblique)

inkplate.set_font(SansBoldOblique32)
inkplate.println(sansBoldOblique)

inkplate.set_font(SerifItalic48)
inkplate.print(serifExample)

inkplate.display() # Display what is drawn in the buffer
```

<CenteredImage src="/img/6color/custom-fonts.jpg" alt="Expected output on Inkplate display" caption="Custom Fonts Example" />

## Custom fonts
Alternatively, if you want to create your own custom font to use on your board you just take and **.ttf** or **.otf** font and turn it into a Python bytearray using the following command:

```
python font_to_py.py SourceSans3-Regular.ttf 20 output.py
```

where number 20 represents maximum font size.

<InfoBox> This external python script can be found on this **[GitHub repo](https://github.com/peterhinch/micropython-font-to-py)**. </InfoBox>

## Custom font example

```python
from inkplate6_color import Inkplate
import drippy as drippy

inkplate = Inkplate()

inkplate.begin()

inkplate.set_font(drippy)
inkplate.set_text_size(3)
inkplate.set_cursor(25, 140)
inkplate.println("Drippy font :D")

inkplate.display()


```

<CenteredImage src="/img/6color/drippy.jpg" alt="Expected output on Inkplate display" caption="Drippy Custom Font Example" />
