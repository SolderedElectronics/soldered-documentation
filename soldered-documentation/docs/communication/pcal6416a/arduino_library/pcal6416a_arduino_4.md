---
slug: /pcal6416a/arduino/interrupts
title: PCAL6416A - Interrupts
sidebar_label: Interrupts
id: pcal6416a-arduino-4
hide_title: false
---

This page covers using the PCAL6416A's interrupt output to detect pin changes without polling every pin over I2C.

---

## Interrupts

The PCAL6416A's **INT** pin pulls low whenever an enabled input pin changes state. Instead of continuously reading every pin over I2C, connect **INT** to a microcontroller pin and let it tell you when something changed.

Connect a pushbutton between **A0** and GND, and another between **A1** and GND. Connect the PCAL6416A's **INT** pin to pin **IO4** on your development board.

```cpp
#include "PCAL6416A-SOLDERED.h"

PCAL6416A expander;

#define INT_PIN 4

bool intFlag = 0;

void myISR()
{
    intFlag = 1;
}

void setup()
{
    Serial.begin(115200);

    expander.begin();

    expander.pinModePCAL(PCAL6416A_A0, INPUT_PULLUP);
    expander.pinModePCAL(PCAL6416A_A1, INPUT_PULLUP);

    pinMode(INT_PIN, INPUT_PULLUP);

    expander.setInterruptPCAL(PCAL6416A_A0, true);
    expander.setInterruptPCAL(PCAL6416A_A1, true);

    // Enabling interrupts above can immediately latch one against the pins'
    // power-on state, so clear it before arming the falling-edge interrupt -
    // otherwise INT can start out already low, with no edge left to catch.
    expander.getInterruptsPCAL();
    expander.digitalReadPCAL(PCAL6416A_A0);
    expander.digitalReadPCAL(PCAL6416A_A1);

    attachInterrupt(digitalPinToInterrupt(INT_PIN), myISR, FALLING);
}

void loop()
{
    if (intFlag)
    {
        intFlag = 0;
        uint16_t intReg = expander.getInterruptsPCAL();

        if (intReg & 1 << PCAL6416A_A0)
        {
            Serial.print("Interrupt detected on pin A0! Pin state is now: ");
            expander.digitalReadPCAL(PCAL6416A_A0) ? Serial.println("HIGH") : Serial.println("LOW");
        }

        if (intReg & 1 << PCAL6416A_A1)
        {
            Serial.print("Interrupt detected on pin A1! Pin state is now: ");
            expander.digitalReadPCAL(PCAL6416A_A1) ? Serial.println("HIGH") : Serial.println("LOW");
        }
    }
}
```

<FunctionDocumentation
  functionName="expander.setInterruptPCAL()"
  description="Enables or disables the interrupt for a single GPIO pin on the PCAL6416A expander."
  returnDescription="None."
  parameters={[
    {
      name: "pin",
      type: "uint8_t",
      description: "The GPIO pin to configure. Use a constant such as PCAL6416A_A0-PCAL6416A_A7 or PCAL6416A_B0-PCAL6416A_B7."
    },
    {
      name: "enable",
      type: "bool",
      description: "true to enable interrupts on this pin, false to disable."
    }
  ]}
/>

<FunctionDocumentation
  functionName="expander.getInterruptsPCAL()"
  description="Reads the interrupt status register, which pin triggered the last interrupt."
  returnDescription="uint16_t bitmask - bit N set means pin N (PCAL6416A_A0-A7 = bits 0-7, PCAL6416A_B0-B7 = bits 8-15) triggered an interrupt."
  parameters={[]}
/>

Open the **Serial Monitor** at **115200 baud** and press either button. The callback (`myISR`) just sets a flag, since interrupt callbacks should stay as short as possible - the actual work of checking which pin changed happens in `loop()`.

<CenteredImage src="/img/pcal6416a/interrupt.png" alt="Serial Monitor output of the interrupts example" caption="Serial Monitor output showing interrupts firing on A0 and A1" />

<QuickLink
  title="interrupts.ino"
  description="Full interrupts example for the PCAL6416A GPIO expander"
  url="https://github.com/SolderedElectronics/Soldered-PCAL6416A-IO-Expander-Arduino-Library/blob/main/examples/interrupts/interrupts.ino"
/>
