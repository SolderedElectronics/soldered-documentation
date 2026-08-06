---
slug: /inkplate/10/basics/basic-display-modes
title: Inkplate 10 – Display modes
sidebar_label: Display modes
id: 10-display-modes
---

As mentioned on the previous page, Inkplate 10 has two different display modes: black and white (1-bit) mode and grayscale (3-bit) mode. This page contains more information on both.

---

## Black and white mode

1-bit or black and white mode is the simpler and faster display mode. In this mode, pixels are either black or white. You can use shorthand defines `BLACK` and `WHITE` when selecting colors in this mode. For example, to draw and display a single black and a single white pixel:

```cpp
#include "Inkplate.h"
Inkplate display(INKPLATE_1BIT);
void setup() {
  display.begin();
  // Clear the display
  display.clearDisplay();
  display.display();
  // Draw a black pixel at x=100, y=100
  display.drawPixel(100,100,BLACK);
  // Draw a white pixel at x=200, y=200
  display.drawPixel(200,200,WHITE);
  display.display(); // Show on the display
}
void loop() {
}
```

<InfoBox>The clear e-Paper, the blank canvas, is WHITE in this context. The white pixel in the above code snippet will not be visible when drawn on an already clear screen.</InfoBox>

---

## Grayscale mode

In 3-bit or grayscale mode you get 8 levels of brightness instead of only black and white, where 0 is black and 7 is white. Below is an approximate visualization of those levels and the numerical value each one has in code:

<CenteredImage src="/img/inkplate10/grayscale.png" alt="3bit grayscale" caption="Black levels in 3-bit mode" width="450px" />

Let's draw a couple of rectangles (with a black outline) of different brightness levels:

```cpp
#include "Inkplate.h"
Inkplate display(INKPLATE_3BIT);

void setup() 
{
  display.begin();
  // Clear the display
  display.clearDisplay();
  display.display();

  // Draw a filled rectangle with a black outline at (100, 100)
  display.fillRect(100, 100, 10, 10, 0); // Black fill
  display.drawRect(100, 100, 10, 10, 0); // Black outline

  // Draw a filled rectangle with a black outline at (200, 200)
  display.fillRect(200, 200, 10, 10, 7); // White fill
  display.drawRect(200, 200, 10, 10, 0); // Black outline

  // Draw a filled rectangle with a black outline at (200, 250)
  display.fillRect(200, 250, 10, 10, 3); // Mid gray fill
  display.drawRect(200, 250, 10, 10, 0); // Black outline

  // Draw a filled rectangle with a black outline at (250, 200)
  display.fillRect(250, 200, 10, 10, 2); // Dark gray fill
  display.drawRect(250, 200, 10, 10, 0); // Black outline

  display.display(); // Show on the display
}

void loop() 
{
}
```
---

## Full example

<QuickLink 
  title="Inkplate10_Black_And_White.ino" 
  description="Full example using black and white display mode on Inkplate 10." 
  url="https://github.com/SolderedElectronics/Inkplate-Arduino-library/blob/master/examples/Inkplate10/Basic/Inkplate10_Black_And_White/Inkplate10_Black_And_White.ino" 
/>

<QuickLink 
  title="Inkplate10_Grayscale.ino" 
  description="Full example using grayscale display mode on Inkplate 10." 
  url="https://github.com/SolderedElectronics/Inkplate-Arduino-library/blob/master/examples/Inkplate10/Basic/Inkplate10_Grayscale/Inkplate10_Grayscale.ino" 
/>