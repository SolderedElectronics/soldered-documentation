---
slug: /inkplate/10/basics/printing-text
title: Printing Text
id: 10-text
---
Printing text on Inkplate is simple and requires only a few functions. The library also supports custom fonts.

<InfoBox>For complete examples of text printing, most Arduino projects in the [**library**](https://github.com/SolderedElectronics/Inkplate-Arduino-library/tree/master/examples/Inkplate10) include some form of text output.</InfoBox>

---

## Simple Text Printing 

To print text, use `setCursor` followed by `print`. If you're using the default font, you may want to use `setTextSize` to increase the font size: 

```cpp
#include "Inkplate.h"
Inkplate inkplate(INKPLATE_3BIT);
void setup() {
  inkplate.begin();
  inkplate.clearDisplay();
  inkplate.display();
  inkplate.setTextColor(BLACK);
  inkplate.setCursor(100,100);
  inkplate.setTextSize(6);
  inkplate.print("Hi inkplate (in size 6)!");
  inkplate.setCursor(100,150);
  inkplate.setTextSize(5);
  inkplate.print("Hi inkplate (in size 5)!");
  inkplate.setCursor(100,200);
  inkplate.setTextSize(4);
  inkplate.print("Hi inkplate (in size 4)!");
  inkplate.setCursor(100,250);
  inkplate.setTextSize(3);
  inkplate.print("Hi inkplate (in size 3)!");
  inkplate.setCursor(100,300);
  inkplate.setTextSize(2);
  inkplate.print("Hi inkplate (in size 2)!");
  inkplate.setCursor(100,350);
  inkplate.setTextSize(1);
  inkplate.print("Hi inkplate (in size 1)!");
  inkplate.display();
}
void loop() {
}
```

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
#include "Inkplate.h"
#include "FreeMono9pt7b.h"
Inkplate inkplate(INKPLATE_3BIT);
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

<FunctionDocumentation
  functionName="inkplate.setFont()"
  description="Sets a custom font for text printing. Must be called before printing."
  returnType="None"
  parameters={[
    {type: 'const GFXfont *', name:'f', description: 'pointer to the GFXfont structure of the font to be set.'}
  ]}
/>