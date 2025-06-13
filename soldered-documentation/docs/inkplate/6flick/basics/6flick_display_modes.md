---
slug: /inkplate/6flick/basics/basic-display-modes
title: Inkplate 6FLICK – Display modes
id: 6flick-display-modes
hide_title: true
---

<SectionTitle title="Display Modes" backgroundImage="/img/inkplate_2/hardware.png" />

As mentioned on the previous page, Inkplate 6FLICK has two different display modes: black and white (1-bit) mode and grayscale (3-bit) mode. This page contains more information on both.

---

## Black and white mode

1-bit or black and white mode is the simpler and faster display mode. In this mode, pixels are either black or white. You can use shorthand defines `BLACK` and `WHITE` when selecting colors in this mode. For example, to draw and display a single black pixel and a single white pixel:

```cpp
#include "Inkplate.h"
Inkplate inkplate(INKPLATE_1BIT);
void setup() {
  inkplate.begin();
  // Clear the display
  inkplate.clearDisplay();
  inkplate.display();
  // Draw a black pixel at x=100, y=100
  inkplate.drawPixel(100,100,BLACK);
  // Draw a white pixel at x=200, y=200
  inkplate.drawPixel(200,200,WHITE);
  inkplate.display(); // Show on the display
}
void loop() {
}
```

<InfoBox>The clear e-Paper, the blank canvas, is WHITE in this context. The white pixel in the above code snippet will not be visible when drawn on an already clear screen.</InfoBox>

---

## Grayscale mode

3-bit or grayscale mode offers the possibility to draw in 8 different levels of brightness, not just black and white. See below for an approximate visualization of black levels corresponding to their numerical values in code:

<CenteredImage src="/img/inkplate_6_flick/grayscale.png" alt="3bit grayscale" caption="Black levels in 3-bit mode" width="450px" />

```cpp
#include "Inkplate.h"
Inkplate inkplate(INKPLATE_3BIT);
void setup() {
  inkplate.begin();
  // Clear the display
  inkplate.clearDisplay();
  inkplate.display();
  // Draw a black pixel at x=100, y=100
  inkplate.drawPixel(100,100,0);
  // Draw a filled rectangle
  inkplate.fillRect(300, 100, 100, 100, 6);
  inkplate.fillRect(300, 300, 100, 100, 4);
  inkplate.fillRect(300, 500, 100, 100, 2);
  inkplate.display(); // Show on the display
}
void loop() {
}
```
---

## Full example

<QuickLink 
  title="Inkplate6FLICK_Black_And_White.ino" 
  description="Full example using black and white display mode on Inkplate 6FLICK." 
  url="https://github.com/SolderedElectronics/Inkplate-Arduino-library/blob/dev/examples/Inkplate6FLICK/Basic/Inkplate6FLICK_Black_And_White/Inkplate6FLICK_Black_And_White.ino" 
/>

<QuickLink 
  title="Inkplate6FLICK_Grayscale.ino" 
  description="Full example using grayscale display mode on Inkplate 6FLICK." 
  url="https://github.com/SolderedElectronics/Inkplate-Arduino-library/tree/dev/examples/Inkplate6FLICK/Basic/Inkplate6FLICK_Grayscale" 
/>