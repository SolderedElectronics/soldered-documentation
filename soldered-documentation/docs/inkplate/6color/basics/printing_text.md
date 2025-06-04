---
slug: /inkplate/6color/basics/printing-text
title: Printing Text
id: text
---

Printing text on Inkplate is simple and requires only a few functions. The library also supports custom fonts.

<InfoBox>For complete examples of text printing, most Arduino projects in the [**library**](https://github.com/SolderedElectronics/Inkplate-Arduino-library/tree/master/examples/Inkplate6COLOR) include some form of text output.</InfoBox>

---

## Simple Text Printing 

To print text, use `setCursor` followed by `print`. If you're using the default font, you may want to use `setTextSize` to increase the font size: 

```cpp
// Declare Inkplate object
Inkplate inkplate;

void setup()
{
    inkplate.begin();
    inkplate.clearDisplay();
    inkplate.setCursor(0,100);
    inkplate.setTextSize(4);
    inkplate.setTextColor(INKPLATE_RED);
    inkplate.print("Hi inkplate (in size 4)!");
    inkplate.setCursor(0,150);
    inkplate.setTextSize(3);
    inkplate.setTextColor(INKPLATE_YELLOW);
    inkplate.print("Hi inkplate (in size 3)!");
    inkplate.setCursor(0,200);
    inkplate.setTextSize(2);
    inkplate.setTextColor(INKPLATE_ORANGE);
    inkplate.print("Hi inkplate (in size 2)!");
    inkplate.setCursor(0,250);
    inkplate.setTextSize(1);
    inkplate.setTextColor(INKPLATE_BLACK);
    inkplate.print("Hi inkplate (in size 1)!");
    inkplate.display();
}

void loop()
{}
```

<CenteredImage src="/img/6color/text_size.png" alt="Expected output on Inkplate display" caption="Expected output on Inkplate display." width="1000px" />

<FunctionDocumentation
  functionName="inkplate.setTextSize()"
  description="Increases the text size by a given factor."
  returnDescription="None"
  parameters={[ 
    { type: 'uint8_t', name: 's', description: 'Size factor. 1 is default size, 2 is twice as large, 3 is three times larger, etc.' }
  ]}
/>
<FunctionDocumentation
  functionName="inkplate.print()"
  description="Prints text at the previously set cursor position. This is the standard Arduino print function used in many native Arduino objects and libraries."
  returnDescription="size_t, number of bytes printed."
  parameters={[ 
    { type: 'const char *', name: '_c', description: 'The C-style string to print on the display.' }
  ]}
/>
<FunctionDocumentation
  functionName="inkplate.setTextColor()"
  description="Sets the color of the text. Must be called before printing."
  returnDescription="None"
  parameters={[ 
    { type: 'uint16_t', name: 'c', description: 'Text color.' },
    { type: 'uint16_t', name: 'bg', description: 'Optional background color. Default is transparent.' }
  ]}
/>

---

## Custom Fonts

The default font appears blocky as it is optimized for minimal memory usage. You can use custom fonts by downloading them from the [Adafruit GFX official repository](https://github.com/adafruit/Adafruit-GFX-Library/tree/master/Fonts). Adafruit provides well-documented examples on using custom fonts [**here**](https://learn.adafruit.com/adafruit-gfx-graphics-library/using-fonts). 

After downloading a font, place it in your sketch folder, include it, and use `setFont`:

```cpp
#include "Inkplate.h"
#include "FreeMono9pt7b.h"

Inkplate inkplate;

void setup() {
  inkplate.begin();
  inkplate.clearDisplay();
  inkplate.display();
  inkplate.setFont(&FreeMono9pt7b);
  inkplate.setCursor(100,100);
  inkplate.setTextColor(BLACK);
  inkplate.setTextSize(3);
  inkplate.print("Hello World!");
  inkplate.display();
}

void loop() {
}
```

<CenteredImage src="/img/6color/custom_font.png" alt="Expected output on Inkplate display" caption="Expected output on Inkplate display." width="1000px" />

<FunctionDocumentation
  functionName="inkplate.setFont()"
  description="Sets a custom font for text printing. Must be called before printing."
  returnType="None"
  parameters={[
    {type: 'const GFXfont *', name:'f', description: 'Pointer to the GFXfont structure of the font to be set.'}
  ]}
/>

---

## TextBox

You can manually define the area in which text will appear by using the `drawTextBox()` function.

```cpp
#include "Inkplate.h"            // Include the Inkplate library in the sketch
#include "FreeMono24pt7b.h"

// Create an Inkplate object and set the library to 1 Bit mode (BW)
Inkplate inkplate;

const char* text = "This is an example of a text written in a textbox. When a word doesn't fit into the current row, it goes to the next one." \
" If the text reaches the lower bound, it ends with three dots (...) to mark that the text isn't displayed fully";

void setup()
{
    inkplate.begin();        // Initialize Inkplate library (you should call this function ONLY ONCE)
    inkplate.clearDisplay(); // Clear the display's frame buffer
    inkplate.display();      // Put a clear image on the display
    inkplate.setTextColor(INKPLATE_BLACK);

    // Create a text box without any optional parameters
    // x0 - x coordinate of the upper left corner
    // y0 - y coordinate of the upper left corner
    // x1 - x coordinate of the bottom right corner
    // y1 - y coordinate of the bottom right corner
    // text - text we want to display
    inkplate.drawTextBox(50,100,250,300,text);

    // Create a text box with all parameters
    // x0 - x coordinate of the upper left corner
    // y0 - y coordinate of the upper left corner
    // x1 - x coordinate of the bottom right corner
    // y1 - y coordinate of the bottom right corner
    // text - text we want to display
    // textSizeMultiplier - factor by which we want to enlarge the font size
    // font - address of the selected custom font
    // verticalSpacing - number of pixels between each row of text
    // showBorder - create a visible rectangle around the box
    // fontSize - size of the used font in pt
    int offset = 32; // Note: some custom fonts are drawn from bottom-to-top, which requires an offset. Use an offset that best suits the font you use.
    inkplate.drawTextBox(300,100 + offset,488,300,text,1,&FreeMono24pt7b,27,false,24);

    // Display both text boxes
    inkplate.display();
}

void loop()
{
    // Nothing...
}
```

<CenteredImage src="/img/6color/textbox.png" alt="Expected output on Inkplate display" caption="Expected output on Inkplate display." width="1000px" />

<FunctionDocumentation
  functionName="inkplate.drawTextBox()"
  description="This function creates a TextBox."
  returnType="void"
  parameters={[
    { type: 'uint16_t', name: 'x0', description: 'X coordinate of the upper left corner.' },
    { type: 'uint16_t', name: 'y0', description: 'Y coordinate of the upper left corner.' },
    { type: 'uint16_t', name: 'x1', description: 'X coordinate of the bottom right corner.' },
    { type: 'uint16_t', name: 'y1', description: 'Y coordinate of the bottom right corner.' },
    { type: 'const char*', name: 'text', description: 'Text we want to display.' },
    { type: 'uint16_t', name: 'textSize', description: 'Factor by which we want to enlarge the font size.' },
    { type: 'const GFXfont*', name: 'font', description: 'Address of the selected custom font.' },
    { type: 'uint16_t', name: 'verticalSpacing', description: 'Number of pixels between each row of text.' },
    { type: 'bool', name: 'showBorder', description: 'Create a visible rectangle around the box.' },
    { type: 'uint16_t', name: 'fontSize', description: 'Size of the used font in pt.' },
  ]}
/>