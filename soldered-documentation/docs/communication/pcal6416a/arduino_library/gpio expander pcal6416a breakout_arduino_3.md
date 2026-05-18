---
slug: /gpio expander pcal6416a breakout/arduino/readwrite
title: PCAL6416AHF - ReadWrite
sidebar_label: ReadWrite
id: gpio expander pcal6416a breakout-arduino-3
hide_title: False
---

This page contains a simple example demonstrating digital input and output control using the PCAL6416A GPIO expander.

---

## Read and Write

In this code snippet, the `loop()` function continuously reads the state of a pushbutton connected to pin A0. Since A0 is configured with an internal pull-up resistor, the pin reads `LOW` when the button is pressed and `HIGH` when the button is released. Based on the button state, pin A1 is used to turn an LED on or off.

```cpp
void loop()
{
    // Read state of button connected to A0
    bool buttonState = expander.digitalReadPCAL(PCAL6416A_A0);

    Serial.print("State of pin A0 is: ");

    if (buttonState == LOW)
    {
        // Button pressed
        Serial.println("LOW - Button Pressed");

        // Turn LED ON
        expander.digitalWritePCAL(PCAL6416A_A1, HIGH);
    }
    else
    {
        // Button released
        Serial.println("HIGH - Button Released");

        // Turn LED OFF
        expander.digitalWritePCAL(PCAL6416A_A1, LOW);
    }

    delay(100);
}
```

<FunctionDocumentation
  functionName="expander.digitalReadPCAL()"
  description="Reads the current logic state of a selected GPIO pin on the PCAL6416A expander."
  returnDescription="Returns HIGH or LOW depending on the state of the selected input pin."
  parameters={[]}
/>

<FunctionDocumentation
  functionName="expander.digitalWritePCAL()"
  description="Sets the output state of a selected GPIO pin on the PCAL6416A expander."
  returnDescription="Sets the selected pin to HIGH or LOW."
  parameters={[]}
/>

| Input pin A0 state | Button state | Output pin A1 state | LED state |
| :----------------: | :----------: | :-----------------: | :-------: |
|        LOW         |   Pressed    |        HIGH         |    ON     |
|        HIGH        |   Released   |         LOW         |    OFF    |

---

## Full example

Connect a pushbutton between A0 and GND, and connect an LED with a resistor to A1 and GND. Open the Serial Monitor at 115200 baud to observe the input state.

```cpp
// Include required libraries
#include <Wire.h>
#include "PCAL6416A-SOLDERED.h"

// Create PCAL6416A object
PCAL6416A expander;

void setup()
{
    Serial.begin(115200); // Start serial communication with PC

    // Required for ESP32-C6 easyC board
    Wire.begin(6, 7);

    // Initialize PCAL6416A GPIO Expander
    expander.begin(0x20);

    // Set A0 as input with internal pull-up resistor
    expander.pinModePCAL(PCAL6416A_A0, INPUT_PULLUP);

    // Set A1 as output
    expander.pinModePCAL(PCAL6416A_A1, OUTPUT);
}

void loop()
{
    // Read state of button connected to A0
    bool buttonState = expander.digitalReadPCAL(PCAL6416A_A0);

    Serial.print("State of pin A0 is: ");

    if (buttonState == LOW)
    {
        // Button pressed
        Serial.println("LOW - Button Pressed");

        // Turn LED ON
        expander.digitalWritePCAL(PCAL6416A_A1, HIGH);
    }
    else
    {
        // Button released
        Serial.println("HIGH - Button Released");

        // Turn LED OFF
        expander.digitalWritePCAL(PCAL6416A_A1, LOW);
    }

    delay(100);
}
```

<CenteredImage src="/img/pcal6416a/ReadWrite.JPG"  caption="Read and Write Connection"/>

<CenteredImage src="/img/pcal6416a/ReadWrite_test.png" alt="Serial Monitor" caption="Read and Write Serial Monitor output"/>


[link placeholder]
{/*github link za example*/}
