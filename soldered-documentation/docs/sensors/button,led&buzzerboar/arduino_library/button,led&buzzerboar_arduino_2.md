---
slug: /button,led&buzzerboar/arduino/examples
title: Button, LED & Buzzer Board - Button Interaction
sidebar_label: Button Interaction
id: button,led&buzzerboar-arduino-2
hide_title: false
---

This page contains a simple example with function documentation on how to interact with the buttons, LEDs, and buzzer on the board.

---

## Initialization

To use the board, first include the required library, create the board object and initialize it in the `setup()` function:

```cpp
#include "ButtonLedBuzzerBoard-SOLDERED.h"

ButtonLedBuzzerBoard_Soldered board;

void setup()
{
    Wire.begin(); // If not using Qwiic, specify I2C pins: Wire.begin(21, 22)
    board.begin();
    delay(2000);

    board.setAllLEDs(0, 0, 0); // Turn off all LEDs
    board.setBuzzer(0);         // Make sure buzzer is off
}
```

<FunctionDocumentation
  functionName="board.begin()"
  description="Initializes the Button, LED & Buzzer Board and sets up I2C communication."
  returnDescription="None."
  parameters={[]}
/>

<FunctionDocumentation
  functionName="board.setAllLEDs(r, g, b)"
  description="Sets all onboard LEDs to the specified RGB color at once."
  returnDescription="None."
  parameters={[
    { type: 'uint8_t', name: 'r', description: 'Red channel value (0–255).' },
    { type: 'uint8_t', name: 'g', description: 'Green channel value (0–255).' },
    { type: 'uint8_t', name: 'b', description: 'Blue channel value (0–255).' },
  ]}
/>

<FunctionDocumentation
  functionName="board.setBuzzer(frequency)"
  description="Drives the buzzer at the specified frequency in Hz. Pass 0 to turn the buzzer off."
  returnDescription="None."
  parameters={[
    { type: 'uint16_t', name: 'frequency', description: 'Frequency in Hz (e.g. 1000 for 1 kHz). 0 turns the buzzer off.' },
  ]}
/>

---

## Reading buttons

Use `readButtons()` to get the state of all three buttons as a bitmask. Each bit corresponds to one button:

```cpp
uint8_t buttons = board.readButtons();

bool btn1 = buttons & 0x01; // Button 1
bool btn2 = buttons & 0x02; // Button 2
bool btn3 = buttons & 0x04; // Button 3
```

<FunctionDocumentation
  functionName="board.readButtons()"
  description="Reads the state of all buttons and returns them as a bitmask. Bit 0 = BTN1, Bit 1 = BTN2, Bit 2 = BTN3. A bit is set (1) when the corresponding button is pressed."
  returnDescription="uint8_t bitmask representing the button states."
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
  functionName="board.setLED(index, r, g, b)"
  description="Sets the RGB color of a single onboard LED."
  returnDescription="None."
  parameters={[
    { type: 'uint8_t', name: 'index', description: 'LED index: 0, 1, or 2.' },
    { type: 'uint8_t', name: 'r', description: 'Red channel value (0–255).' },
    { type: 'uint8_t', name: 'g', description: 'Green channel value (0–255).' },
    { type: 'uint8_t', name: 'b', description: 'Blue channel value (0–255).' },
  ]}
/>

---

## Full example

Press any button to light its corresponding LED and sound the buzzer at a unique frequency. Multiple buttons can be pressed simultaneously — the buzzer plays the highest button's frequency.

```cpp
#include "ButtonLedBuzzerBoard-SOLDERED.h"

ButtonLedBuzzerBoard_Soldered board;

void setup()
{
    Wire.begin();
    board.begin();
    delay(2000);

    board.setAllLEDs(0, 0, 0);
    board.setBuzzer(0);
}

void loop()
{
    uint8_t buttons = board.readButtons();

    bool btn1 = buttons & 0x01;
    bool btn2 = buttons & 0x02;
    bool btn3 = buttons & 0x04;

    board.setLED(0, btn3 ? 255 : 0, 0, 0);
    board.setLED(1, 0, btn2 ? 255 : 0, 0);
    board.setLED(2, 0, 0, btn1 ? 255 : 0);

    if (btn3)      board.setBuzzer(3000);
    else if (btn2) board.setBuzzer(2000);
    else if (btn1) board.setBuzzer(1000);
    else           board.setBuzzer(0);

    delay(20);
}
```

<QuickLink
  title="ButtonInteraction.ino"
  description="Full button interaction example for the Soldered Button, LED & Buzzer Board"
  url="https://github.com/SolderedElectronics/Soldered-Button-LED-Buzzer-Board-Arduino-Library/blob/main/examples/ButtonInteraction/ButtonInteraction.ino"
/>
