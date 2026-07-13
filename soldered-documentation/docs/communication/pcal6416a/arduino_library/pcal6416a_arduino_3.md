---
slug: /pcal6416a/arduino/readwrite
title: PCAL6416A - ReadWrite
sidebar_label: ReadWrite
id: pcal6416a-arduino-3
hide_title: false
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
  parameters={[
    {
      name: "pin",
      type: "uint8_t",
      description: "The GPIO pin to read. Use a constant such as PCAL6416A_A0-PCAL6416A_A7 or PCAL6416A_B0-PCAL6416A_B7."
    }
  ]}
/>

<FunctionDocumentation
  functionName="expander.digitalWritePCAL()"
  description="Sets the output state of a selected GPIO pin on the PCAL6416A expander."
  returnDescription="None."
  parameters={[
    {
      name: "pin",
      type: "uint8_t",
      description: "The GPIO pin to write. Use a constant such as PCAL6416A_A0-PCAL6416A_A7 or PCAL6416A_B0-PCAL6416A_B7."
    },
    {
      name: "value",
      type: "uint8_t",
      description: "Output level: HIGH or LOW."
    }
  ]}
/>

<FunctionDocumentation
  functionName="expander.pinModePCAL()"
  description="Configures a GPIO pin on the PCAL6416A expander as an input or output."
  returnDescription="None."
  parameters={[
    {
      name: "pin",
      type: "uint8_t",
      description: "The GPIO pin to configure. Use a constant such as PCAL6416A_A0-PCAL6416A_A7 or PCAL6416A_B0-PCAL6416A_B7."
    },
    {
      name: "mode",
      type: "uint8_t",
      description: "Pin mode: INPUT, OUTPUT, INPUT_PULLUP, or INPUT_PULLDOWN."
    }
  ]}
/>

<InfoBox>Besides `INPUT`, `OUTPUT`, and `INPUT_PULLUP`, the library also defines `INPUT_PULLDOWN` for `pinModePCAL()`, using the PCAL6416A's internal pull-down resistors instead of pull-up.</InfoBox>

| Input pin A0 state | Button state | Output pin A1 state | LED state |
| :----------------: | :----------: | :-----------------: | :-------: |
|        LOW         |   Pressed    |        HIGH         |    ON     |
|        HIGH        |   Released   |         LOW         |    OFF    |

---

## Full example

Connect a pushbutton between A0 and GND, and connect an LED with a resistor to A1 and GND. Open the Serial Monitor at 115200 baud to observe the input state.

```cpp
// Include required library
#include "PCAL6416A-SOLDERED.h"

// Create PCAL6416A object
PCAL6416A expander;

void setup()
{
    Serial.begin(115200); // Start serial communication with PC

    // Initialize PCAL6416A GPIO Expander
    expander.begin();

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


<QuickLink 
  title="PCAL6416A examples" 
  description="Arduino examples for the PCAL6416A GPIO expander"
  url="https://github.com/SolderedElectronics/Soldered-PCAL6416A-IO-Expander-Arduino-Library/tree/main/examples" 
/>
