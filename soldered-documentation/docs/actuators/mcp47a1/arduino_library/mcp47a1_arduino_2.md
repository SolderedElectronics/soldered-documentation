---
slug: /mcp47a1/arduino/examples 
title: Setting specific voltages
id: mcp47a1-arduino-2 
hide_title: False
---

We can set the DAC to output a specific voltage at any time. 
First, we have to include the library and create an instance of the DAC object:

```cpp

#include "MCP47A1-SOLDERED.h" // Include Soldered library for MCP47A1 DAC.
MCP47A1_SOLDERED dac; // Create instance of an object

```

Next, in the `setup()` function, we are initializing the I2C communication with the DAC:

```cpp
void setup()
{
    dac.begin();          // Initialize DACs library.
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
  description="Set voltage at DACs output."
  returnDescription="None"
  parameters={[
  { type: 'float', name: '_volts', description: "Voltage at DACs output in range from 0V to VCC." },
  ]}
/>

## Full example

See the full example below:

```cpp
#include "MCP47A1-SOLDERED.h" // Include Soldered library for MCP47A1 DAC.

MCP47A1_SOLDERED dac; // Create instance of an object

void setup()
{
    dac.begin();          // Initialize DACs library.
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