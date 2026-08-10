---
slug: /pcal6416a/arduino/digital-read
title: PCAL6416A - Digital Read
sidebar_label: Digital Read
id: pcal6416a-arduino-2
hide_title: false
---

This page covers reading a digital input pin on the PCAL6416A GPIO expander.

---

## Initialization

To use the PCAL6416A GPIO expander, first include the required library, create an expander object, and initialize communication in the `setup()` function. The `begin()` function starts I2C communication with the device and doesn't need any manual `Wire.begin()` call before it.

<FunctionDocumentation
  functionName="expander.begin()"
  description="Initializes communication with the PCAL6416A GPIO expander over I2C. Uses the default address 0x20 unless a different address is passed in."
  returnDescription="None."
  parameters={[
    {
      "name": "address",
      "type": "uint8_t",
      "description": "Optional I2C address of the PCAL6416A device. Defaults to 0x20. Pass 0x21 if JP3 has been cut and bridged to VDD."
    }
  ]}
/>

---

## Reading a pin

Connect a pushbutton between **A0** and GND. Since A0 is configured with an internal pull-up resistor, the pin reads `LOW` when the button is pressed and `HIGH` when released.

```cpp
#include "PCAL6416A-SOLDERED.h"

PCAL6416A expander;

void setup()
{
    Serial.begin(115200);
    expander.begin();

    expander.pinModePCAL(PCAL6416A_A0, INPUT_PULLUP);
}

void loop()
{
    Serial.print("State of pin A0 is: ");
    expander.digitalReadPCAL(PCAL6416A_A0) ? Serial.println("HIGH.") : Serial.println("LOW.");
    delay(1000);
}
```

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

<InfoBox>Besides `INPUT`, `OUTPUT`, and `INPUT_PULLUP`, the library also defines `INPUT_PULLDOWN`, using the PCAL6416A's internal pull-down resistors instead of pull-up.</InfoBox>

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

Open the **Serial Monitor** at **115200 baud** and press the button to see the pin state change.

<CenteredImage src="/img/pcal6416a/read.png" alt="Serial Monitor output of the digital read example" caption="Serial Monitor output showing pin A0 switching between HIGH and LOW" />

<QuickLink
  title="digitalRead.ino"
  description="Full digital read example for the PCAL6416A GPIO expander"
  url="https://github.com/SolderedElectronics/Soldered-PCAL6416A-IO-Expander-Arduino-Library/blob/main/examples/digitalRead/digitalRead.ino"
/>
