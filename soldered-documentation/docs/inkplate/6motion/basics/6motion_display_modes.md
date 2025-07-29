---
slug: /inkplate/6motion/basics/basic-display-modes
title: 6Motion - Display modes
sidebar_label: Display modes
id: 6motion-display-modes
---


As mentioned on the previous page, Inkplate MOTION has two different display modes: black and white (1-bit) mode and grayscale (4-bit) mode. This page contains more information on both.

---

## Black and white mode

1-bit or black and white mode is the simpler and faster display mode. In this mode, pixels are either black or white. You can use shorthand defines `BLACK` and `WHITE` when selecting colors in this mode. For example, to draw and display a single black and a single white pixel:

```cpp
inkplate.begin(INKPLATE_BLACKWHITE);

// Draw a black pixel at x=100, y=100
inkplate.drawPixel(100, 100, BLACK);
// Draw a white pixel at x=200, y=100
inkplate.drawPixel(200, 100, WHITE);

inkplate.display(); // Show on the display
```

<InfoBox>The clear e-Paper, the blank canvas, is WHITE in this context. The white pixel in the above code snippet will not be visible when drawn on an already clear screen.</InfoBox>

---

## Grayscale mode

4-bit or grayscale mode offers the possibility to draw in 16 different levels of brightness, not just black and white. See below for an approximate visualization of black levels as they correspond to their numerical value in code:

<CenteredImage src="/img/inkplate_6_motion/4bit_grayscale.png" alt="4bit grayscale" caption="Black levels in 4-bit mode" width="450px" />

Let's draw a couple of pixels of different brightness levels:

```cpp
inkplate.begin(INKPLATE_GRAYSCALE);

// Draw a couple of different pixels in a horizontal line
inkplate.drawPixel(100, 100, 1);
inkplate.drawPixel(200, 100, 4);
inkplate.drawPixel(300, 100, 8);
inkplate.drawPixel(400, 100, 13);

inkplate.display(); // Show on the display
```

---

## Full examples

<QuickLink 
  title="Inkplate_6_Motion_Simple_BW.ino" 
  description="Full example using black and white display mode on Inkplate 6 MOTION." 
  url="https://github.com/SolderedElectronics/Inkplate_Motion_Arduino_Library/blob/main/examples/Inkplate6Motion/Basic/Inkplate_6_Motion_Simple_BW/Inkplate_6_Motion_Simple_BW.ino" 
/>

<QuickLink 
  title="Inkplate_6_Motion_Simple_Grayscale.ino" 
  description="Full example using grayscale display mode on Inkplate 6 MOTION." 
  url="https://github.com/SolderedElectronics/Inkplate_Motion_Arduino_Library/blob/main/examples/Inkplate6Motion/Basic/Inkplate_6_Motion_Simple_Grayscale/Inkplate_6_Motion_Simple_Grayscale.ino" 
/>
