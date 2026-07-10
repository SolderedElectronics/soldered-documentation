---
slug: /button_led_buzzer_board/arduino/buttons
title: Button, LED & Buzzer Board - Buttons
sidebar_label: Buttons
id: button_led_buzzer_board-arduino-2
hide_title: false
---

This page covers reading the three onboard buttons.

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

<InfoBox>If you only care about one button, the library also has `isButton1Pressed()`, `isButton2Pressed()`, and `isButton3Pressed()`, each returning a plain `bool`.</InfoBox>

---

## Full example

Prints a message to the Serial Monitor every time a button is pressed or released:

```cpp
#include "ButtonLedBuzzerBoard-SOLDERED.h"

ButtonLedBuzzerBoard_Soldered board;

uint8_t lastButtons = 0;

void setup()
{
    Serial.begin(115200);
    Wire.begin();
    board.begin();
    delay(2000);

    Serial.println("Button, LED & Buzzer Board - Button Test");
    Serial.println("Press any button...");
}

void loop()
{
    uint8_t buttons = board.readButtons();

    if (buttons != lastButtons)
    {
        for (uint8_t i = 0; i < 3; i++)
        {
            uint8_t mask = 1 << i;
            if ((buttons & mask) && !(lastButtons & mask))
            {
                Serial.print("BTN"); Serial.print(i + 1); Serial.println(" pressed");
            }
            else if (!(buttons & mask) && (lastButtons & mask))
            {
                Serial.print("BTN"); Serial.print(i + 1); Serial.println(" released");
            }
        }
        lastButtons = buttons;
    }

    delay(20);
}
```

Open the **Serial Monitor** at **115200 baud** and press the buttons to see the output.

<CenteredImage src="/img/button_led_buzzer_board/buttons.png" alt="Serial Monitor output showing button presses and releases" caption="Serial Monitor output while pressing BTN1, BTN2, and BTN3" width="600px" />

<QuickLink
  title="Buttons.ino"
  description="Full button test example for the Soldered Button, LED & Buzzer Board"
  url="https://github.com/SolderedElectronics/Soldered-Button-LED-Buzzer-Board-Arduino-Library/blob/main/examples/Buttons/Buttons.ino"
/>
