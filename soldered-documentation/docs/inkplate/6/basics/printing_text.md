---
slug: /inkplate/6/basics/printing-text
title: Inkplate 6 – Printing Text
sidebar_label: Printing Text
id: text
---

Printing text on Inkplate is simple and requires only a few functions. The library also supports custom fonts.

<InfoBox>For complete examples of text printing, most Arduino projects in the [**library**](https://github.com/SolderedElectronics/Inkplate-Arduino-library/tree/master/examples/Inkplate6) include some form of text output.</InfoBox>

---

## Simple text printing

To print text, use `setCursor` followed by `print`. If you're using the default font, you may want to use `setTextSize` to increase the font size: 

```cpp
#include "Inkplate.h"
Inkplate display(INKPLATE_3BIT);
void setup() {
  display.begin();
  display.clearDisplay();
  display.display();
  display.setTextColor(BLACK);
  display.setCursor(100,150);
  display.setTextSize(5);
  display.print("Hi inkplate (in size 5)!");
  display.setCursor(100,200);
  display.setTextSize(4);
  display.print("Hi inkplate (in size 4)!");
  display.setCursor(100,250);
  display.setTextSize(3);
  display.print("Hi inkplate (in size 3)!");
  display.setCursor(100,300);
  display.setTextSize(2);
  display.print("Hi inkplate (in size 2)!");
  display.setCursor(100,350);
  display.setTextSize(1);
  display.print("Hi inkplate (in size 1)!");
  display.display();
}
void loop() {
}
```

<CenteredImage src="/img/6/printing_text.png" alt="Expected output on Inkplate display" caption="Expected output on Inkplate display." width="1000px" />

<FunctionDocumentation
  functionName="display.setTextSize()"
  description="Increases the text size by a given factor."
  returnType="none"
  parameters={[ 
    { type: 'uint8_t', name: 's', description: 'Size factor. 1 is default size, 2 is twice as large, 3 is three times larger, etc.' }
  ]}
/>
<FunctionDocumentation
  functionName="display.print()"
  description="Prints text at the previously set cursor position. This is the standard Arduino print function used in many native Arduino objects and libraries."
  returnType="size_t"
  returnDescription="The number of bytes printed."
  parameters={[ 
    { type: 'const char *', name: '_c', description: 'The C-style string to print on the display.' }
  ]}
/>

---

## Text background color

To change the text color, use `setTextColor`. This function can also optionally set a background color by printing a rectangle in that color behind the text, which can improve visibility in some cases.

<FunctionDocumentation
  functionName="display.setTextColor()"
  description="Sets the color of the text. Must be called before printing."
  returnType="none"
  parameters={[ 
    { type: 'uint16_t', name: 'c', description: 'Text color.' },
    { type: 'uint16_t', name: 'bg', description: 'Optional background color. Default is transparent.' }
  ]}
/>

---

## Custom fonts

The default font appears blocky because it is optimized for minimal memory usage. You can use custom fonts by downloading them from the [Adafruit GFX official repository](https://github.com/adafruit/Adafruit-GFX-Library/tree/master/Fonts). Adafruit also provides well-documented examples on using custom fonts [**here**](https://learn.adafruit.com/adafruit-gfx-graphics-library/using-fonts).

After downloading a font, place it in your sketch folder, include it, and use `setFont`:

```cpp
#include "Inkplate.h"
#include "FreeMono9pt7b.h"
Inkplate display(INKPLATE_3BIT);
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

<CenteredImage src="/img/6/font.png" alt="Expected output on Inkplate display" caption="Expected output on Inkplate display." width="1000px" />

<FunctionDocumentation
  functionName="display.setFont()"
  description="Sets a custom font for text printing. Must be called before printing."
  returnType="none"
  parameters={[
    {type: 'const GFXfont *', name:'f', description: 'Pointer to the GFXfont structure of the font to be set.'}
  ]}
/>

---

## TextBox

You can manually define the area in which text will appear by using the `drawTextBox()` function.

```cpp
#include "Inkplate.h"            //Include Inkplate library to the sketch
#include "Roboto_Light_36.h"
Inkplate display(INKPLATE_1BIT); // Create an object on Inkplate library and also set library into 1 Bit mode (BW)

// Define the text you will show in the text box
const char* text="This is an example of a text written in a textbox. When a word doesn't fit into the current row, it goes to the next one."\
" If the text reaches the lower bound, it ends with three dots (...) to mark that the text isnt displayed fully";

void setup()
{
    display.begin();        // Init Inkplate library (you should call this function ONLY ONCE)
    display.clearDisplay(); // Clear frame buffer of display
    display.display();      // Put clear image on display

    // Create a text box without any optional parameters
    // x0- x coordinate of upper left corner
    // y0- y coordinate of upper left corner
    // x1- x coordinate of bottom right corner
    // y1- y coordinate of bottom right corner
    // text - text we want to display
    display.drawTextBox(100,100,300,300,text);

    // Create a text box with all parameters
    // x0- x coordinate of upper left corner
    // y0- y coordinate of upper left corner
    // x1- x coordinate of bottom right corner
    // y1- y coordinate of bottom right corner
    // text - text we want to display
    // textSizeMultiplier - by what factor we want to enlarge the size of a font
    // font - address of selected custom font
    // verticalSpacing - how many pixels between each row of text
    // showBorder - Create a visible rectangle around the box
    // fontSize - size of the used font in pt
    int offset=32; // Note - some custom fonts are drawn from bottom-to-top which requires an offset, use an offset that best suits the font you use 
    display.drawTextBox(400,100+offset,600,300,text,1,&Roboto_Light_36,27,false,36);

    // Display both text boxes
    display.display();
}

void loop()
{
    // Nothing...
}
```

<CenteredImage src="/img/6/textbox.png" alt="Expected output on Inkplate display" caption="Expected output on Inkplate display." width="1000px" />

<FunctionDocumentation
  functionName="display.drawTextBox()"
  description="This function creates a TextBox."
  returnType="void"
  parameters={[
    { type: 'uint16_t', name: 'x0', description: 'X coordinate of the upper left corner.' },
    { type: 'uint16_t', name: 'y0', description: 'Y coordinate of the upper left corner.' },
    { type: 'uint16_t', name: 'x1', description: 'X coordinate of the bottom right corner.' },
    { type: 'uint16_t', name: 'y1', description: 'Y coordinate of the bottom right corner.' },
    { type: 'const char*', name: 'text', description: 'Text we want to display.' },
    { type: 'uint16_t', name: 'textSize', description: 'Factor by which the font size is enlarged.' },
    { type: 'const GFXfont* ', name: 'font', description: 'Address of the selected custom font.' },
    { type: 'uint16_t', name: 'verticalSpacing', description: 'Number of pixels between each row of text.' },
    { type: 'bool', name: 'showBorder', description: 'Create a visible rectangle around the box.' },
    { type: 'uint16_t', name: 'fontSize', description: 'Size of the used font in pt.' },
  ]}
/>

---

## Full examples
Check out the full examples:

<QuickLink 
  title="Inkplate6_TextBox.ino" 
  description="This example will show you how to use the TextBox function with and without special parameters"
  url="https://github.com/SolderedElectronics/Inkplate-Arduino-library/blob/master/examples/Inkplate6/Basic/Inkplate6_TextBox/Inkplate6_TextBox.ino" 
/>