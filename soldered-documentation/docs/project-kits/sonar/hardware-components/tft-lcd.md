---
slug: /sonar/hardware/tft
title: Sonar Project Kit - Components
sidebar_label: TFT LCD Display
id: tft-lcd
hide_title: false
pagination_prev: null
---

## 2.4'' TFT LCD with Touchscreen
This is a **2.4'' vibrant full-color TFT display** with **capacitive touchscreen** capabilities. The display has a built in controller with RAM buffering to take the load off your microcontroller. It features an **SPI interface** along with **microSD socket** for data logging, image display, etc.

<CenteredImage src="/img/tft-lcd/tftlcd.png" alt="Image of TFT LCD Breakout" caption="2.4 inch TFT LCD Touch Breakout" width="600px"/>

---
## Explore the product on our store

<QuickLink 
  title="2.4'' TFT LCD Breakout with Touchscreen" description="333211"
  url="https://soldered.com/product/tft-lcd-breakout-2-4-with-touch/"
  image="/img/tft-lcd/tftlcd.png" 
/>

---

## Key features
- **Display & Touch:** 2.4'' diagonal, 240x320 resolution, resistive  touchscreen
- **Backlight:** 4 bright white-LED
- **Interface:**
  - **Display:** SPI
  - **Touch:** I²C (default address 0x38)
- **Operates at:** Works with 3.3V and 5V logic (onboard level shifting)

---

## What is TFT?
TFT stands for **Thin-Film Transistor**, a display technology that provides active matrix control over each pixel using dedicated transistors. This results in:
- Faster refresh rates
- Higher brightness and contrast
- Better responsivness compared to passive matrix LCDs

---

## Onboard components
- **ILI9341:** Main TFT display controller (SPI)
- **XPT2046:** Resistive touchscreen controller (SPI)
- **microSD socket:** SPI interface for data logging, image display, etc.
- **Level-shifter** for 3.3V and 5V compatibility

---

## Pin Connection Table

| TFT LCD Pin | MCU Role / Pin Type | ESP32 Pin | Notes |
|:---:|:---:|:---:|:---:|
| **VCC** | VCC | VCC or 3V3 | 3.3V or 5V depending on board |
| **GND** | GND | Ground | Common ground connection |
| **CLK** | SPI Clock (SCK)| IO18 | Clock line |
| **DI** | SPI MOSI | IO23 | Sends data to the display |
| **D0** | SPI MISO	 | IO19 | Needed for reading touch data |
| **CSL** | Any free digital GPIO | IO25 | Chip Select for TFT |
| **DC** | Any free digital GPIO| IO33 | Data/Command |
| **RST** | Any GPIO or `-1` | Any GPIO or `-1` | Optional hardware reset |
| **CST** | Any free digital GPIO | IO5 | Chip Select for Touch | 
| **BL** | VCC or PWM-capable GPIO | Power or GPIO | Connect to 3.3V or 5V for always-on, or a PWM pin for dimming |

---

## Working example

<CenteredImage src="/img/under_construction.png" alt="TFT LCD working example" caption="Video of working example" width="600px"/>

---

## Example code

```cpp
// Include needed libraries
#include "Adafruit_GFX.h"
#include "SPI.h"
#include "TFT-LCD-Breakout-2.4-With-Touch-SOLDERED.h"

// Define pins for DC, CSL, CST, and Reset
#define TFT_DC 33
#define TFT_CSL 25
#define TFT_RST -1 // If not used, use -1
#define TFT_CST 5

// Create the display object
TFTDisplay tft(TFT_CSL, TFT_DC, TFT_RST);

// Create the touchscreen object
TFTTouch ts(TFT_CST);

// Size of the color selection boxes and the paintbrush size
#define BOXSIZE   40
#define PENRADIUS 3
int oldcolor, currentcolor;

// Struct for the points in the coordinate system
struct point
{
    int x;
    int y;
} p;

void setup(void)
{
    // Init serial communication
    Serial.begin(115200);
    Serial.println(F("Touch Paint!"));

    // Init tft display and touchscreen
    tft.begin();
    ts.begin();
    Serial.println("Touchscreen started");

    // Calibrate your touch screen to get pressed pixel value instead of raw data
    ts.calibrate(540, 1000, 34, 460);

    // Put black background
    tft.fillScreen(ILI9341_BLACK);

    // Make the color selection boxes
    tft.fillRect(0, 0, BOXSIZE, BOXSIZE, ILI9341_RED);
    tft.fillRect(BOXSIZE, 0, BOXSIZE, BOXSIZE, ILI9341_YELLOW);
    tft.fillRect(BOXSIZE * 2, 0, BOXSIZE, BOXSIZE, ILI9341_GREEN);
    tft.fillRect(BOXSIZE * 3, 0, BOXSIZE, BOXSIZE, ILI9341_CYAN);
    tft.fillRect(BOXSIZE * 4, 0, BOXSIZE, BOXSIZE, ILI9341_BLUE);
    tft.fillRect(BOXSIZE * 5, 0, BOXSIZE, BOXSIZE, ILI9341_MAGENTA);

    // Select the current color 'red'
    tft.drawRect(0, 0, BOXSIZE, BOXSIZE, ILI9341_WHITE);
    currentcolor = ILI9341_RED;
}

void loop()
{
    // Read data from the touchscreen
    ts.service();

    // Check if the touchscreen is touched
    // NOTE: The screen must be pressed a bit more than on a smartphone to detect touch
    if (!ts.getPressure())
    {
        return;
    }

    // Get pressed coordinates
    p.x = ts.getX();
    p.y = ts.getY();

    // Print the coordinates of the pressed point on the screen
    Serial.print("X = ");
    Serial.print(p.x);
    Serial.print("\tY = ");
    Serial.println(p.y);

    if (p.y < BOXSIZE)
    {
        oldcolor = currentcolor;

        if (p.x < BOXSIZE)
        {
            currentcolor = ILI9341_RED;
            tft.drawRect(0, 0, BOXSIZE, BOXSIZE, ILI9341_WHITE);
        }
        else if (p.x < BOXSIZE * 2)
        {
            currentcolor = ILI9341_YELLOW;
            tft.drawRect(BOXSIZE, 0, BOXSIZE, BOXSIZE, ILI9341_WHITE);
        }
        else if (p.x < BOXSIZE * 3)
        {
            currentcolor = ILI9341_GREEN;
            tft.drawRect(BOXSIZE * 2, 0, BOXSIZE, BOXSIZE, ILI9341_WHITE);
        }
        else if (p.x < BOXSIZE * 4)
        {
            currentcolor = ILI9341_CYAN;
            tft.drawRect(BOXSIZE * 3, 0, BOXSIZE, BOXSIZE, ILI9341_WHITE);
        }
        else if (p.x < BOXSIZE * 5)
        {
            currentcolor = ILI9341_BLUE;
            tft.drawRect(BOXSIZE * 4, 0, BOXSIZE, BOXSIZE, ILI9341_WHITE);
        }
        else if (p.x < BOXSIZE * 6)
        {
            currentcolor = ILI9341_MAGENTA;
            tft.drawRect(BOXSIZE * 5, 0, BOXSIZE, BOXSIZE, ILI9341_WHITE);
        }

        if (oldcolor != currentcolor)
        {
            if (oldcolor == ILI9341_RED)
                tft.fillRect(0, 0, BOXSIZE, BOXSIZE, ILI9341_RED);
            if (oldcolor == ILI9341_YELLOW)
                tft.fillRect(BOXSIZE, 0, BOXSIZE, BOXSIZE, ILI9341_YELLOW);
            if (oldcolor == ILI9341_GREEN)
                tft.fillRect(BOXSIZE * 2, 0, BOXSIZE, BOXSIZE, ILI9341_GREEN);
            if (oldcolor == ILI9341_CYAN)
                tft.fillRect(BOXSIZE * 3, 0, BOXSIZE, BOXSIZE, ILI9341_CYAN);
            if (oldcolor == ILI9341_BLUE)
                tft.fillRect(BOXSIZE * 4, 0, BOXSIZE, BOXSIZE, ILI9341_BLUE);
            if (oldcolor == ILI9341_MAGENTA)
                tft.fillRect(BOXSIZE * 5, 0, BOXSIZE, BOXSIZE, ILI9341_MAGENTA);
        }
    }
    if (((p.y - PENRADIUS) > BOXSIZE) && ((p.y + PENRADIUS) < tft.height()))
    {
        tft.fillCircle(p.x, p.y, PENRADIUS, currentcolor);
    }
}
```
