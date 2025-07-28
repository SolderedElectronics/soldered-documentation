---
slug: /tft-lcd/arduino/geting-started
title: 2.4" TFT LCD Breakout with Touch - getting started
sidebar_label: Getting started
id: tft-lcd-arduino-1
hide_title: false
---

This page provides the essential information for getting started, including board and library installation.

--- 

## Arduino library

To install the Arduino library, you can use the **Arduino library manager** or download it from the GitHub repository:

<QuickLink  
  title="Soldered TFT LCD Arduino Library"  
  description="TFT LCD Arduino library by Soldered"  
  url="https://github.com/SolderedElectronics/Soldered-TFT-LCD-Breakout-2.4-With-Touch-Arduino-Library/tree/main"  
/>  

<InfoBox>

**First-time Arduino user?** For a detailed tutorial on how to get started with Arduino, see this section of our docs:

<QuickLink  
  title="Getting started with Arduino"  
  description="A full, comprehensive tutorial on how to fully set up and upload code for the first time on an Arduino board, from scratch!"  
  url="/documentation/arduino/quick-start-guide"  
/>  

</InfoBox>

--- 

## How to Connect the TFT LCD Breakout 2.4"

The **TFT LCD Breakout 2.4" with Touch** display can be connected to any **ESP32 or other microcontroller** with SPI support. It uses standard SPI for display data and an additional SPI chip select pin for touch input. Below is a general guide for wiring and initializing the display and touchscreen using user-defined GPIO pins.

---

## Pin Connection Table

| TFT LCD Pin | Function            | Microcontroller Role / Pin Type | Notes                                                                              |
| ----------- | ------------------- | ------------------------------- | ---------------------------------------------------------------------------------- |
| **VCC**     | Power               | 3.3V or 5V power output         | Powers the display and backlight.                                                  |
| **GND**     | Ground              | GND                             | Common ground connection.                                                          |
| **CLK**     | SPI Clock           | SPI Clock (SCK)                 | Shared with other SPI devices if needed.                                           |
| **DI**      | SPI Data (MOSI)     | SPI MOSI                        | Sends data to the display.                                                         |
| **D0**      | SPI Data (MISO)     | SPI MISO                        | Required for touchscreen functionality.                                            |
| **CSL**     | TFT Chip Select     | Any free digital GPIO           | Used in display constructor as `TFT_CSL`.                                          |
| **DC**      | Data/Command Select | Any free digital GPIO           | Used in display constructor as `TFT_DC`.                                           |
| **RST**     | Reset (optional)    | Any GPIO or `-1`                | Set to `-1` in code if not connected. Optional hardware reset.                     |
| **CST**     | Touch Chip Select   | Any free digital GPIO           | Used in touchscreen constructor: `TFTTouch ts(<pin>)`.                             |
| **BL**      | Backlight           | VCC or PWM-capable GPIO         | Connect to 3.3V or 5V for always-on, or a PWM pin for dimming.                     |

---

## Example Code

```cpp
#include "SPI.h"
#include "Adafruit_GFX.h"
#include "TFT-LCD-Breakout-2.4-With-Touch-SOLDERED.h"

// User-defined pins
#define TFT_CSL  25  // TFT Chip Select
#define TFT_DC   33  // TFT Data/Command
#define TFT_RST  -1  // Use -1 if RST not connected
#define TOUCH_CS 5   // Touchscreen Chip Select

// Use VSPI on ESP32
SPIClass vspi(VSPI);

// Initialize display and touchscreen
TFTDisplay tft(TFT_CSL, TFT_DC, TFT_RST);
TFTTouch ts(TOUCH_CS);

void setup() {
  Serial.begin(115200);

  // Initialize VSPI with SCK, MISO, MOSI
  vspi.begin(18, 19, 23);

  // Optionally set SPI speed (e.g., 40 MHz)
  vspi.setFrequency(40000000);

  // Begin display and touch
  tft.begin();
  ts.begin();

  // Optional touchscreen calibration
  ts.calibrate(540, 1000, 34, 460); // Adjust values as needed

  // Clear screen
  tft.fillScreen(ILI9341_BLACK);
}

void loop() {
  // Your code here: draw shapes, detect touch, etc.
}

```

---

## Tips

- The **D0/MISO** pin must be connected for the touchscreen to function properly.
- Use `vspi.setFrequency(40000000);` to manually adjust SPI speed if necessary.
- Ensure your board has stable power—some displays may require up to 100mA during full backlight and drawing operations.
