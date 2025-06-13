---
slug: /mcp47a1/arduino/examples
title: MCP47A1 - Setting specific voltages
sidebar_label: Setting specific voltages
id: mcp47a1-arduino-2
hide_title: false
---

We can set the DAC to output a specific voltage at any time.  

---

## Connections for each example

<CenteredImage src="/img/mcp47a1/connections.png" alt="Connections" />

---
First, we have to include the library and create an instance of the DAC object:

```cpp
#include "MCP47A1-SOLDERED.h" // Include Soldered library for MCP47A1 DAC.
MCP47A1_SOLDERED dac; // Create an instance of the object
```

Next, in the `setup()` function, we initialize the I2C communication with the DAC:

```cpp
void setup()
{
    dac.begin();          // Initialize the DAC library.
}
```

<FunctionDocumentation
  functionName="dac.begin()"
  description="Initializes the I/O DAC via I2C"
  returnDescription="None"
  parameters={[]}
/>

Finally, in the `loop()` function, we can hook up an LED to the VOUT and GND connectors and change the voltage every 2 seconds:

```cpp
void loop()
{
    float volts;

    // Set DAC output voltage to 0 V
    volts = 0;
    dac.setVoltage(volts);
    delay(2000);

    // Set DAC output voltage to 1 V
    volts = 1;
    dac.setVoltage(volts);
    delay(2000);

    // Set DAC output voltage to 2.5 V
    volts = 2.5;
    dac.setVoltage(volts);
    delay(2000);

    // Set DAC output voltage to 3.3 V
    volts = 3.3;
    dac.setVoltage(volts);
    delay(2000);
}
```

<FunctionDocumentation
  functionName="dac.setVoltage(float _volts)"
  description="Sets the voltage at the DAC's output."
  returnDescription="None"
  parameters={[
  { type: 'float', name: '_volts', description: "Voltage at the DAC's output in the range from 0V to VCC." },
  ]}
/>

## Full example

See the full example below:

```cpp
#include "MCP47A1-SOLDERED.h" // Include Soldered library for MCP47A1 DAC.

MCP47A1_SOLDERED dac; // Create an instance of the object

void setup()
{
    dac.begin();          // Initialize the DAC library.
}

void loop()
{
    float volts;

    // Set DAC output voltage to 0 V
    volts = 0;
    dac.setVoltage(volts);
    delay(2000);

    // Set DAC output voltage to 1 V
    volts = 1;
    dac.setVoltage(volts);
    delay(2000);

    // Set DAC output voltage to 2.5 V
    volts = 2.5;
    dac.setVoltage(volts);
    delay(2000);

    // Set DAC output voltage to 3.3 V
    volts = 3.3;
    dac.setVoltage(volts);
    delay(2000);
}
```