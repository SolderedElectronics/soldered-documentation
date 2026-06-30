---
slug: /inkplate/13spectra/basics/printing-text
title: Inkplate 13SPECTRA – Printing Text
sidebar_label: Printing Text
id: 13spectra-printing-text
---

Printing text on Inkplate is simple and requires only a few functions. The library also supports custom fonts.

<InfoBox>For complete examples of text printing, most Arduino projects in the [LINK PLACEHOLDER - link to spectra examples on github] include some form of text output.</InfoBox>

---

## Simple Text Printing

To print text, use `setCursor` followed by `print`. If you're using the default forn, you may want to use `setTextSize` to increase the font size:

```cpp
//Declare Inkplate object
Inkplate display;

void setup()
{
    display.begin();
display.clearDisplay();

// ---- Line 1 ----
display.setCursor(100, 250);
display.setTextSize(6);
display.setTextColor(INKPLATE_RED);
display.print("Hi inkplate (in size 6)!");

// ---- Line 2 ----
display.setCursor(100, 450);
display.setTextSize(5);
display.setTextColor(INKPLATE_YELLOW);
display.print("Hi inkplate (in size 5)!");

// ---- Line 3 ----
display.setCursor(100, 650);
display.setTextSize(4);
display.setTextColor(INKPLATE_GREEN - 1);
display.print("Hi inkplate (in size 4)!");

// ---- Line 4 ----
display.setCursor(100, 820);
display.setTextSize(3);
display.setTextColor(INKPLATE_BLACK);
display.print("Hi inkplate (in size 3)!");

display.display();
}

void loop(){}
```

<CenteredImage src="/img/13spectra/DSC00696.jpg" alt="Example output displayed on e-paper display" caption="Example output displayed on e-paper display" width="1200px" />

<FunctionDocumentation
  functionName="display.setTextSize()"
  description="Increases the text size by a given factor."
  returnDescription="None"
  parameters={[ 
    { type: 'uint8_t', name: 's', description: 'Size factor. 1 is default size, 2 is twice as large, 3 is three times larger, etc.' }
  ]}
/>
<FunctionDocumentation
  functionName="display.print()"
  description="Prints text at the previously set cursor position. This is the standard Arduino print function used in many native Arduino objects and libraries."
  returnDescription="size_t, number of bytes printed."
  parameters={[ 
    { type: 'const char *', name: '_c', description: 'The C-style string to print on the display.' }
  ]}
/>
<FunctionDocumentation
  functionName="display.setTextColor()"
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
  display.begin();
  display.clearDisplay();
  display.display();
  display.setFont(&FreeMono9pt7b);
  display.setCursor(100,100);
  display.setTextColor(BLACK);
  display.setTextSize(3);
  display.print("Hello World!");
  display.display();
}

void loop() {
}
```

<CenteredImage src="/img/13spectra/DSC00698.jpg" alt="Example output displayed on e-paper display" caption="Example output displayed on e-paper display" width="1200px" />

<FunctionDocumentation
  functionName="display.setFont()"
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
Inkplate display;

const char* text = "This is an example of a text written in a textbox. When a word doesn't fit into the current row, it goes to the next one." \
" If the text reaches the lower bound, it ends with three dots (...) to mark that the text isn't displayed fully";

void setup()
{
    display.begin();        // Initialize Inkplate library (you should call this function ONLY ONCE)
    display.clearDisplay(); // Clear the display's frame buffer
    display.display();      // Put a clear image on the display
    display.setTextColor(INKPLATE_BLACK);

    // Create a text box without any optional parameters
    // x0 - x coordinate of the upper left corner
    // y0 - y coordinate of the upper left corner
    // x1 - x coordinate of the bottom right corner
    // y1 - y coordinate of the bottom right corner
    // text - text we want to display
    display.drawTextBox(200,300,700,650,text);

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
    int offset = 48; // Note: some custom fonts are drawn from bottom-to-top, which requires an offset. Use an offset that best suits the font you use.
    display.drawTextBox(800,300 + offset,1400,700,text,1,&FreeMono24pt7b,36,false,32);

    // Display both text boxes
    display.display();
}

void loop()
{
    // Nothing...
}
```

<CenteredImage src="/img/13spectra/DSC00699.webp" alt="Example output displayed on e-paper display" caption="Example output displayed on e-paper display" width="1200px" />

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