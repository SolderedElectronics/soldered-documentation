---  
slug: /inkplate/2/basics/printing-text  
title: Printing Text  
id: 2-text  
hide_title: true  
---

<SectionTitle title="Printing Text" backgroundImage="/img/inkplate_2/hardware.png" />

Printing text on Inkplate 2 is simple and intuitive. With support for **three colors** (black, white, red) and compatibility with the **Adafruit GFX** library, text rendering is flexible and customizable.

<InfoBox>For complete examples of text printing, most Arduino projects in the [**Inkplate library**](https://github.com/SolderedElectronics/Inkplate-Arduino-library/tree/master/examples/Inkplate2) include some form of text output.</InfoBox>

---

## Basic Text Printing

To print text, use `setCursor`, `setTextSize`, and `print`. Below is a basic usage example:

```cpp
#include "Inkplate.h"
Inkplate inkplate;

void setup() {
  inkplate.begin();
  inkplate.clearDisplay();
  inkplate.setCursor(10, 10);
  inkplate.setTextSize(2);
  inkplate.setTextColor(INKPLATE2_BLACK);
  inkplate.print("Black text!");

  inkplate.setCursor(10, 40);
  inkplate.setTextColor(INKPLATE2_RED);
  inkplate.print("Red text!");

  inkplate.setCursor(10, 70);
  inkplate.setTextColor(INKPLATE2_WHITE, INKPLATE2_BLACK); // white text on black background
  inkplate.print("Text w/ background");

  inkplate.display();
}

void loop() {}
```

<CenteredImage src="/img/inkplate_2/basic_text.png" alt="Expected output on Inkplate display" caption="Expected output on Inkplate display." width="750px" />

<FunctionDocumentation
  functionName="inkplate.setCursor()"
  description="Sets the cursor position where the next text will be drawn."
  returnDescription="none"
  parameters={[
    { type: 'int', name: 'x', description: 'X coordinate of the cursor.' },
    { type: 'int', name: 'y', description: 'Y coordinate of the cursor.' },
  ]}
/>

<FunctionDocumentation
  functionName="inkplate.setTextSize()"
  description="Sets the multiplier for text size (1 is default, 2 is double size, etc.)."
  returnDescription="none"
  parameters={[
    { type: 'uint8_t', name: 's', description: 'Text size multiplier.' },
  ]}
/>

<FunctionDocumentation
  functionName="inkplate.setTextColor()"
  description="Sets the text color, with an optional background color."
  returnDescription="none"
  parameters={[
    { type: 'uint16_t', name: 'color', description: 'Text color.' },
    { type: 'uint16_t', name: 'background', description: 'Optional background color.' },
  ]}
/>

---

## Custom Fonts

Inkplate 2 also supports custom fonts from the Adafruit GFX library. Download a font, include it in your sketch, and pass it to `setFont()`:

```cpp
#include "Inkplate.h"
#include "FreeMono9pt7b.h"

Inkplate inkplate;

void setup() {
  inkplate.begin();
  inkplate.clearDisplay();
  inkplate.setFont(&FreeMono9pt7b);
  inkplate.setCursor(10, 40);
  inkplate.setTextColor(INKPLATE2_RED);
  inkplate.print("Custom Font!");
  inkplate.display();
}

void loop() {}
```

<CenteredImage src="/img/inkplate_2/custom_font.png" alt="Expected output on Inkplate display" caption="Expected output on Inkplate display." width="750px" />

<FunctionDocumentation
  functionName="inkplate.setFont()"
  description="Sets a custom font from the GFX font collection."
  returnDescription="none"
  parameters={[
    { type: 'const GFXfont *', name: 'font', description: 'Pointer to the font struct.' },
  ]}
/>