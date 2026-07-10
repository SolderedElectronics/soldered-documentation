---
slug: /button_led_buzzer_board/arduino/leds
title: Button, LED & Buzzer Board - LEDs
sidebar_label: LEDs
id: button_led_buzzer_board-arduino-4
hide_title: false
---

This page covers controlling the three onboard RGB LEDs.

---

## Initialization

Include the library, create the board object, and initialize it in `setup()`:

```cpp
#include "ButtonLedBuzzerBoard-SOLDERED.h"

ButtonLedBuzzerBoard_Soldered board;

void setup()
{
    Wire.begin(); // If not using Qwiic, specify I2C pins: Wire.begin(21, 22)
    board.begin();
    delay(2000);

    board.setAllLEDs(0, 0, 0); // Turn off all LEDs
}
```

<FunctionDocumentation
  functionName="board.begin()"
  description="Initializes the Button, LED & Buzzer Board and sets up I2C communication."
  returnDescription="None."
  parameters={[]}
/>

---

## Controlling individual LEDs

Use `setLED()` to set the RGB color of a single LED by its index (0, 1, or 2):

```cpp
board.setLED(0, 255, 0, 0); // LED 0 → red
board.setLED(1, 0, 255, 0); // LED 1 → green
board.setLED(2, 0, 0, 255); // LED 2 → blue
```

<FunctionDocumentation
  functionName="board.setLED()"
  description="Sets the RGB color of a single onboard LED."
  returnDescription="None."
  parameters={[
    { type: 'uint8_t', name: 'index', description: 'LED index: 0, 1, or 2.' },
    { type: 'uint8_t', name: 'r', description: 'Red channel value (0-255).' },
    { type: 'uint8_t', name: 'g', description: 'Green channel value (0-255).' },
    { type: 'uint8_t', name: 'b', description: 'Blue channel value (0-255).' },
  ]}
/>

---

## Controlling all LEDs at once

Use `setAllLEDs()` to set every LED to the same color in a single call:

```cpp
board.setAllLEDs(255, 255, 255); // All LEDs white
```

<FunctionDocumentation
  functionName="board.setAllLEDs()"
  description="Sets all onboard LEDs to the specified RGB color at once."
  returnDescription="None."
  parameters={[
    { type: 'uint8_t', name: 'r', description: 'Red channel value (0-255).' },
    { type: 'uint8_t', name: 'g', description: 'Green channel value (0-255).' },
    { type: 'uint8_t', name: 'b', description: 'Blue channel value (0-255).' },
  ]}
/>

<InfoBox>To set all three LEDs to different colors in one call, the library also has `setLEDs(r1, g1, b1, r2, g2, b2, r3, g3, b3)`.</InfoBox>

---

## Full example

Cycles each LED through red, green, and blue individually, then cycles all LEDs together:

```cpp
#include "ButtonLedBuzzerBoard-SOLDERED.h"

ButtonLedBuzzerBoard_Soldered board;

void setup()
{
    Wire.begin();
    board.begin();
    delay(2000);

    board.setAllLEDs(0, 0, 0);
}

void loop()
{
    // Test each LED individually
    for (uint8_t i = 0; i < 3; i++)
    {
        board.setAllLEDs(0, 0, 0);
        board.setLED(i, 255, 0, 0); delay(400); // red
        board.setLED(i, 0, 255, 0); delay(400); // green
        board.setLED(i, 0, 0, 255); delay(400); // blue
    }

    // All LEDs together
    board.setAllLEDs(255,   0,   0); delay(500); // red
    board.setAllLEDs(  0, 255,   0); delay(500); // green
    board.setAllLEDs(  0,   0, 255); delay(500); // blue
    board.setAllLEDs(255, 255, 255); delay(500); // white
    board.setAllLEDs(  0,   0,   0); delay(500); // off
}
```

{/* TODO: Add a picture/video here showing the LEDs cycling through colors. */}

<QuickLink
  title="LEDs.ino"
  description="Full LED test example for the Soldered Button, LED & Buzzer Board"
  url="https://github.com/SolderedElectronics/Soldered-Button-LED-Buzzer-Board-Arduino-Library/blob/main/examples/LEDs/LEDs.ino"
/>
