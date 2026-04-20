---  
slug: /inkplate/6color/micropython/basics/print-text
title: Inkplate 6COLOR – Printing text
sidebar_label: Printing text
id: print-text
hide_title: false  
---

Printing text on Inkplate is simple and requires only a few functions. The library also supports custom fonts of different sizes.

## Simple Colored Text Example

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

To print text, use `setCursor` followed by `print`. If you're using the default font, you may want to use `setTextSize` to increase the font size:

```python
inkplate.setTextSize(2) # Scale up the font size

inkplate.setCursor(180,180) # Set the cursor from where the text will be written

helloWorld = "Hello world!" # Declare the string we want to print

i = 0 # Declare the counter we will use to iterate through the colors

# Iterate through each character in the string
for char in helloWorld:
    # Change the color of every character
    inkplate.setTextColor(i)
    # Print a single character to the framebuffer
    inkplate.print(char)
    # Iterate the color counter
    i = i + 1
    if (i == 1): # If the color is white, skip it
        i = i + 1
    elif (i // 7 > 0): # If we displayed all 7 colors, return to the first one
        i = 0

inkplate.display() # Display what is drawn to the buffer
```

<CenteredImage src="/img/6color/hello-world.jpg" alt="Expected output on Inkplate display" caption="Hello world output on display" />

<FunctionDocumentation
  functionName="inkplate.setTextSize()"
  description="Increases the text size by a given factor."
  returnDescription="None"
  parameters={[ 
    { type: 'int', name: 's', description: 'Size factor. 1 is default size, 2 is twice as large, 3 is three times larger, etc.' }
  ]}
/>
<FunctionDocumentation
  functionName="inkplate.setCursor()"
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
<FunctionDocumentation
  functionName="inkplate.setTextColor()"
  description="Sets the color of the text. Must be called before printing."
  returnDescription="None"
  parameters={[ 
    { type: 'int', name: 'color', description: 'Set text color.' }
  ]}
/>

## Alternative fonts example
Here we will print text using different fonts on our Inkplate board. All of the fonts are available on **[Inkplate-MicroPython GitHub](https://github.com/SolderedElectronics/Inkplate-micropython/tree/master/Fonts)**, just upload **.py** file to your board and import it in your code:

```python
from inkplate6COLOR import Inkplate
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
inkplate.setCursor(0, 20)

inkplate.setFont(Mono12)
inkplate.println(mono)

inkplate.setFont(SerifBold18)
inkplate.println(serifBold)

inkplate.setFont(SansOblique24)
inkplate.println(sansOblique)

inkplate.setFont(SansBoldOblique32)
inkplate.println(sansBoldOblique)

inkplate.setFont(SerifItalic48)
inkplate.print(serifExample)

inkplate.display() # Display what is drawn in the buffer
```

<CenteredImage src="/img/6color/custom-fonts.jpg" alt="Expected output on Inkplate display" caption="Custom Fonts Example" />

## Custom Fonts
Alternatively, if you want to create your own custom font to use on your board you just take and **.ttf** or **.otf** font and turn it into a Python bytearray using the following command:

```
python font_to_py.py SourceSans3-Regular.ttf 20 output.py
```

where number 20 represents maximum font size.

<InfoBox> This external python script can be found on this **[GitHub repo](https://github.com/peterhinch/micropython-font-to-py)**. </InfoBox>

## Example of Custom Font

```python
from inkplate6COLOR import Inkplate
import drippy as drippy

inkplate = Inkplate()

inkplate.begin()

inkplate.setFont(drippy)
inkplate.setTextSize(3)
inkplate.setCursor(25, 140)
inkplate.println("Drippy font :D")

inkplate.display()


```

<CenteredImage src="/img/6color/drippy.jpg" alt="Expected output on Inkplate display" caption="Drippy Custom Font Example" />
