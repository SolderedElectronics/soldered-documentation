---  
slug: /inkplate/6/basics/basic-display-modes  
title: Display modes  
id: display-modes  
---  

As mentioned on the previous page, Inkplate 6 has two different display modes: black and white (1-bit) mode and grayscale (3-bit) mode. This page contains more information on both.

---  

## Black and white mode

1-bit, or black and white mode, is the simpler and faster display mode. In this mode, pixels are either black or white. You can use the shorthand defines `BLACK` and `WHITE` when selecting colors. For example, to draw and display a single black pixel and a single white pixel:

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

3-bit, or grayscale mode, allows you to draw in eight different levels of brightness, not just black and white. See below for an approximate visualization of black levels as they correspond to their numerical value in the code:

<CenteredImage src="/img/inkplate10/grayscale.png" alt="3bit grayscale" caption="Black levels in 3-bit mode" width="450px" />

Let's draw a couple of pixels with different brightness levels:

```cpp
#include "Inkplate.h"
Inkplate inkplate(INKPLATE_1BIT);
void setup() {
  inkplate.begin();
  // Clear the display
  inkplate.clearDisplay();
  inkplate.display();
  // Draw a pixel with brightness level 0 at x=100, y=100
  inkplate.drawPixel(100,100,0);
  // Draw a pixel with brightness level 7 at x=200, y=200
  inkplate.drawPixel(200,200,7);
  // Draw a pixel with brightness level 3 at x=200, y=250
  inkplate.drawPixel(200,250,3);
  // Draw a pixel with brightness level 2 at x=250, y=200
  inkplate.drawPixel(250,200,2);
  inkplate.display(); // Show on the display
}
void loop() {
}
```

---  

## Full example

<QuickLink 
  title="Inkplate6_Black_And_White.ino" 
  description="Full example using black and white display mode on Inkplate 6." 
  url="https://github.com/SolderedElectronics/Inkplate-Arduino-library/blob/master/examples/Inkplate6/Basic/Inkplate6_Black_And_White/Inkplate6_Black_And_White.ino" 
/>

<QuickLink 
  title="Inkplate6_Grayscale.ino" 
  description="Full example using grayscale display mode on Inkplate 6." 
  url="https://github.com/SolderedElectronics/Inkplate-Arduino-library/tree/master/examples/Inkplate6/Basic/Inkplate6_Grayscale" 
/>