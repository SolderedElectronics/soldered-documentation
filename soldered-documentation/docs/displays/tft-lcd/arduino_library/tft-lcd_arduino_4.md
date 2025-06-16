---
slug: /tft-lcd/arduino/touchpaint
title: TFT LCD - Touch Paint
sidebar_label: Touch paint
id: tft-lcd-arduino-4
hide_title: false
---

This advanced example demonstrates how to build a basic **touchscreen paint app** using the **TFT LCD Breakout 2.4" with Touch**. It includes color selection, pressure detection, and drawing circles as a brush.

<InfoBox>This sketch uses the touchscreen and drawing functionalities provided by the Soldered TFT library.</InfoBox>

---

## Touchscreen Paint

This sketch enables full interaction via touch: select a color by tapping a color box and draw on the screen by dragging your finger.

### Core Setup and Logic

```cpp
#include "Adafruit_GFX.h"
#include "SPI.h"
#include "TFT-LCD-Breakout-2.4-With-Touch-SOLDERED.h"

#define TFT_CSL 6
#define TFT_DC  9
#define TFT_RST -1
#define CST_PIN 10

TFTDisplay tft(TFT_CSL, TFT_DC, TFT_RST);
TFTTouch ts(CST_PIN);

#define BOXSIZE   40
#define PENRADIUS 3
int oldcolor, currentcolor;

struct point {
    int x, y;
} p;

void setup() {
    Serial.begin(115200);
    tft.begin();
    ts.begin();
    ts.calibrate(540, 1000, 34, 460);
    tft.fillScreen(ILI9341_BLACK);

    tft.fillRect(0, 0, BOXSIZE, BOXSIZE, ILI9341_RED);
    tft.fillRect(BOXSIZE, 0, BOXSIZE, BOXSIZE, ILI9341_YELLOW);
    tft.fillRect(BOXSIZE * 2, 0, BOXSIZE, BOXSIZE, ILI9341_GREEN);
    tft.fillRect(BOXSIZE * 3, 0, BOXSIZE, BOXSIZE, ILI9341_CYAN);
    tft.fillRect(BOXSIZE * 4, 0, BOXSIZE, BOXSIZE, ILI9341_BLUE);
    tft.fillRect(BOXSIZE * 5, 0, BOXSIZE, BOXSIZE, ILI9341_MAGENTA);

    tft.drawRect(0, 0, BOXSIZE, BOXSIZE, ILI9341_WHITE);
    currentcolor = ILI9341_RED;
}
```

<FunctionDocumentation
  functionName="ts.calibrate()"
  description="Calibrates the touchscreen by mapping raw analog input values to screen coordinates. Essential for accurate touch point detection."
  returnDescription="None"
  parameters={[
    { type: 'int', name: 'xMin', description: "Raw minimum value for X" },
    { type: 'int', name: 'xMax', description: "Raw maximum value for X" },
    { type: 'int', name: 'yMin', description: "Raw minimum value for Y" },
    { type: 'int', name: 'yMax', description: "Raw maximum value for Y" }
  ]}
/>

---

### Drawing Logic

The `loop()` function handles reading touch points, determining brush position, and rendering colored circles.

```cpp
void loop() {
    ts.service();
    if (!ts.getPressure()) return;

    p.x = ts.getX();
    p.y = ts.getY();
    Serial.print("X = "); Serial.print(p.x); Serial.print("	Y = "); Serial.println(p.y);

    if (p.y < BOXSIZE) {
        oldcolor = currentcolor;
        int colorIndex = p.x / BOXSIZE;
        switch (colorIndex) {
            case 0: currentcolor = ILI9341_RED; break;
            case 1: currentcolor = ILI9341_YELLOW; break;
            case 2: currentcolor = ILI9341_GREEN; break;
            case 3: currentcolor = ILI9341_CYAN; break;
            case 4: currentcolor = ILI9341_BLUE; break;
            case 5: currentcolor = ILI9341_MAGENTA; break;
        }
        tft.drawRect(colorIndex * BOXSIZE, 0, BOXSIZE, BOXSIZE, ILI9341_WHITE);
        if (oldcolor != currentcolor)
            tft.fillRect(oldcolor / BOXSIZE * BOXSIZE, 0, BOXSIZE, BOXSIZE, oldcolor);
    }
    if ((p.y > BOXSIZE) && (p.y < tft.height()))
        tft.fillCircle(p.x, p.y, PENRADIUS, currentcolor);
}
```

<FunctionDocumentation
  functionName="ts.getX() / ts.getY()"
  description="Returns the last X or Y coordinate from the touchscreen input after mapping and calibration."
  returnDescription="int — Coordinate value in screen pixels."
  parameters={[]}
/>

<FunctionDocumentation
  functionName="tft.fillCircle()"
  description="Draws a filled circle on the screen at the given coordinates with the specified radius and color."
  returnDescription="None"
  parameters={[
    { type: 'int', name: 'x', description: "X coordinate" },
    { type: 'int', name: 'y', description: "Y coordinate" },
    { type: 'int', name: 'r', description: "Radius of the circle" },
    { type: 'uint16_t', name: 'color', description: "Color of the filled circle" }
  ]}
/>

<CenteredImage src="/img/tft-lcd/touchpaint.png" alt="tft touchpaint" caption="Example drawing using touchpaint" />

---

<QuickLink 
  title="TouchPaint.ino" 
  description="Paint on the screen using your finger with full color selection and circle brush." 
  url="https://github.com/SolderedElectronics/Soldered-TFT-LCD-Breakout-2.4-With-Touch-Arduino-Library/blob/main/examples/TouchPaint/TouchPaint.ino" 
/>