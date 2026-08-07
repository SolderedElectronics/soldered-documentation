---
slug: /inkplate/6flick/frontlight/basic
title: Inkplate 6FLICK – Simple Frontlight
sidebar_label: Simple Frontlight
id: 6flick-frontlight
hide_title: true
---

<SectionTitle title="Simple Frontlight Control" />

This basic example demonstrates how to control the **frontlight brightness** of the Inkplate 6FLICK using simple function calls.

The frontlight allows for better visibility in dim environments while preserving the paper-like appearance of the e-paper screen.

---

## Example overview

Two calls do the work. `frontlight.setState()` powers the frontlight circuit on or off, and `frontlight.setBrightness()` sets the level. Brightness runs from `0` to `63`, giving you 64 steps.

<WarningBox>Nothing will light up until you call `display.frontlight.setState(true)`. The brightness value on its own does not enable the circuit.</WarningBox>

```cpp
#include "Inkplate.h" //Include Inkplate library

Inkplate display(INKPLATE_1BIT); // Create an object on Inkplate class

int b = 31; // Variable that holds intensity of the frontlight

void setup()
{
    Serial.begin(115200);    // Set up a serial communication of 115200 baud
    display.begin();         // Init Inkplate library
    display.frontlight.setState(true); // Enable frontlight circuit
    display.frontlight.setBrightness(b); // Set frontlight intensity
}

void loop()
{
    if (Serial.available()) // Change frontlight value by sending "+" sign into serial monitor to increase frontlight or
                            // "-" sign to decrese frontlight
                            // try to find hidden lightshow ;)
    {
        bool change = false;    // Variable that indicates that frontlight value has changed and intessity has to be updated
        char c = Serial.read(); // Read incomming serial data

        if (c == '+' && b < 63) // If is received +, increase frontlight
        {
            b++;
            change = true;
        }
        if (c == '-' && b > 0) // If is received -, decrease frontlight
        {
            b--;
            change = true;
        }

        if (c == 's')
        {
            for (int j = 0; j < 4; ++j)
            {
                for (int i = 0; i < 64; ++i)
                {
                    display.frontlight.setBrightness(i);
                    delay(30);
                }

                for (int i = 63; i >= 0; --i)
                {
                    display.frontlight.setBrightness(i);
                    delay(30);
                }
            }

            change = true;
        }

        if (change) // If frontlight valuse has changed, update the intensity and show current value of frontlight
        {
            display.frontlight.setBrightness(b);
            Serial.print("Frontlight:");
            Serial.print(b, DEC);
            Serial.println("/63");
        }
    }
}
```

---

<FunctionDocumentation
  functionName="display.frontlight.setState()"
  description="Turns the frontlight circuit on or off. This must be enabled before any brightness value has an effect."
  returnType="void"
  parameters={[
    { type: 'bool', name: '_e', description: 'true turns the frontlight on, false turns it off.' }
  ]}
/>

<FunctionDocumentation
  functionName="display.frontlight.setBrightness()"
  description="Sets the frontlight brightness. The value is written to the on-board MCP47A1 DAC over I2C."
  returnType="void"
  parameters={[
    { type: 'uint8_t', name: '_v', description: 'Brightness level from 0 to 63. Values above 63 are masked, so 64 behaves as 0.' }
  ]}
/>

---

## Notes

- The frontlight is off after every reset, so call `setState(true)` again in `setup()`.
- Brightness is set by an I2C DAC rather than PWM, so there is no flicker at intermediate levels.
- Turn the frontlight off before deep sleep. It stays lit otherwise and will drain the battery.

---

## Full example

You can find the complete example in the Inkplate Arduino library repository:

<QuickLink 
  title="Inkplate6FLICK_Simple_Frontlight" 
  description="Basic usage example of the frontlight on Inkplate 6FLICK." 
  url="https://github.com/SolderedElectronics/Inkplate-Arduino-library/blob/master/examples/Inkplate6FLICK/Basic/Inkplate6FLICK_Simple_Frontlight/Inkplate6FLICK_Simple_Frontlight.ino" 
/>