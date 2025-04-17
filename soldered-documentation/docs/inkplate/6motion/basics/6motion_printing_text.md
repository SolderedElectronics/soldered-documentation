---
slug: /inkplate/6motion/basics/printing-text
title: Printing Text
id: 6motion-text
---

Printing text on Inkplate is simple and requires only a few functions. The library also supports custom fonts.

<InfoBox>For complete examples of text printing, most Arduino projects in the [**library**](https://github.com/SolderedElectronics/Inkplate_Motion_Arduino_Library/tree/main/examples/Inkplate6Motion) include some form of text output.</InfoBox>

---

## Simple Text Printing

To print text, use `setCursor` followed by `print`. If you're using the default font, you may want to use `setTextSize` to increase the font size: 

```cpp
// Set the printing cursor to x=100, y=100
inkplate.setCursor(100, 100);
// Increase text size by a factor of 3 for better visibility
inkplate.setTextSize(3);
// Print the text
inkplate.print("Hi Inkplate!");

inkplate.display(); // As always, call display to render the text on the e-Paper
```
<FunctionDocumentation
  functionName="inkplate.setCursor()"
  description="Sets the cursor position for text printing."
  returnDescription="None"
  parameters={[ 
    { type: 'int16_t', name: '_x', description: 'X-coordinate where text printing starts.' },
    { type: 'int16_t', name: '_y', description: 'Y-coordinate where text printing starts.' }
  ]}
/>
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

---

## Text Background Color

To change the text color, use `setTextColor`. This function can also optionally set a background color, which prints a rectangle in that color behind the text. This can improve visibility in some cases.
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
// Include the Inkplate Motion Arduino Library
#include <InkplateMotion.h>
#include "FreeSerif9pt7b.h" // Include the custom font
Inkplate inkplate; // Create an Inkplate object

void setup() 
{
  // Initialize Inkplate
  inkplate.begin(INKPLATE_BLACKWHITE);
  // Set the font
  inkplate.setFont(&FreeSerif9pt7b);
  // Print a message
  inkplate.setCursor(100, 100);
  inkplate.print("Hello world!");
  // Update the display
  inkplate.display();
}

void loop() 
{
  // Do nothing
}
```
<FunctionDocumentation
  functionName="inkplate.setFont()"
  description="Sets a custom font for text printing. Must be called before printing."
  returnDescription="None"
  parameters={[ 
    { type: 'const GFXfont *', name: 'f', description: 'Pointer to the GFXfont structure of the font to be set.' }
  ]}
/>

---

## Additional Text Printing Options

Use `setTextWrap` to enable or disable automatic text wrapping when reaching the edge of the e-Paper display:
<FunctionDocumentation
  functionName="inkplate.setTextWrap()"
  description="Enables or disables automatic text wrapping."
  returnDescription="None"
  parameters={[ 
    { type: 'bool', name: 'w', description: 'True enables text wrapping, false disables it.' }
  ]}
/>
