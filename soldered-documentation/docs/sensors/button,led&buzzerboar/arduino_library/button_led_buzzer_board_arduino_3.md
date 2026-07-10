---
slug: /button_led_buzzer_board/arduino/buzzer
title: Button, LED & Buzzer Board - Buzzer
sidebar_label: Buzzer
id: button_led_buzzer_board-arduino-3
hide_title: false
---

This page covers driving the onboard buzzer.

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
}
```

<FunctionDocumentation
  functionName="board.begin()"
  description="Initializes the Button, LED & Buzzer Board and sets up I2C communication."
  returnDescription="None."
  parameters={[]}
/>

---

## Controlling the buzzer

Use `setBuzzer()` to drive the buzzer at a specific frequency in Hz. Pass `0` to turn it off:

```cpp
board.setBuzzer(1000); // Play a 1 kHz tone
delay(500);
board.setBuzzer(0);    // Turn the buzzer off
```

<FunctionDocumentation
  functionName="board.setBuzzer()"
  description="Drives the buzzer at the specified frequency in Hz. Pass 0 to turn the buzzer off."
  returnDescription="None."
  parameters={[
    { type: 'uint16_t', name: 'frequency', description: 'Frequency in Hz (e.g. 1000 for 1 kHz). 0 turns the buzzer off.' },
  ]}
/>

---

## Full example

Plays a sweep of frequencies to test the buzzer:

```cpp
#include "ButtonLedBuzzerBoard-SOLDERED.h"

ButtonLedBuzzerBoard_Soldered board;

const uint16_t frequencies[] = {500, 1000, 2000, 3000, 4000};
const uint8_t numFreqs = sizeof(frequencies) / sizeof(frequencies[0]);

void setup()
{
    Wire.begin();
    board.begin();
    delay(2000);
}

void loop()
{
    for (uint8_t i = 0; i < numFreqs; i++)
    {
        board.setBuzzer(frequencies[i]);
        delay(400);
        board.setBuzzer(0);
        delay(200);
    }

    delay(1000);
}
```

<QuickLink
  title="Buzzer.ino"
  description="Full buzzer test example for the Soldered Button, LED & Buzzer Board"
  url="https://github.com/SolderedElectronics/Soldered-Button-LED-Buzzer-Board-Arduino-Library/blob/main/examples/Buzzer/Buzzer.ino"
/>
