---
slug: /mcp47a1/arduino/generating-a-waveform
title: Mcp47A1 - Generating a waveform
id: mcp47a1-arduino-4
hide_title: false
---

In this example, we will be generating a sine wave with the MCP47A1:

First, we have to include the library and create an instance of the DAC object:

```cpp
#include "MCP47A1-SOLDERED.h" // Include Soldered library for MCP47A1 DAC.
MCP47A1_SOLDERED dac; // Create an instance of the DAC object.
```

We also have to create a lookup table. We will use an array of 65 bytes that will hold the samples of the voltage at a given time in the period. Essentially, we are setting 65 different values of the voltage in a given period. The delay determines how long a specific sample is outputted:

```cpp
uint8_t waveformLUT[65]; // Array for storing samples of the desired waveform.
int delay_ms = 100;       // Delay between samples.
```

Next, in the `setup()` function, we are initializing the I2C communication with the DAC:

```cpp
void setup()
{
    dac.begin();               // Initialize DAC's library.
    makeLut();                 // Fill LUT (lookup table) with sine wave values.
}
```

<FunctionDocumentation
  functionName="dac.begin()"
  description="Initializes the I/O DAC via I2C"
  returnDescription="None"
  parameters={[]}
/>

In the `makeLut()` function, we are populating the lookup table with values from the sine function and multiplying them so they range from 0 to 64:

```cpp
void makeLut()
{
  for (int i = 0; i < 65; i++)
  {
    // Populate with sine values ranging from 0 to 64.
    waveformLUT[i] = 32 * sin(2.0 * PI * i/sizeof(waveformLUT)) + 32;
  }
}
```

In the `loop()` function, we are iterating through all the samples:

```cpp
int k = 0; // Counter variable for selecting samples from the LUT.
void loop()
{
    dac.setByte(waveformLUT[k]); // Send waveform samples stored in LUT one by one to the DAC.
    k++;
    if (k > 64)
        k = 0;
    delay(delay_ms); // Wait a little bit between samples. A smaller delay produces a higher frequency for the generated signal.
}
```

<FunctionDocumentation
  functionName="dac.setByte(uint8_t byte)"
  description="Set voltage via byte value (from 0 to 64 since the DAC is 6-bit)"
  returnDescription="None"
  parameters={[ 
    { type: 'uint8_t', name: 'byte', description: "Voltage as byte value, 0 for 0V and 63 for 5V" },
  ]}
/>

## Full example

See the full example below:

```cpp
#include "MCP47A1-SOLDERED.h" // Include Soldered library for MCP47A1 DAC.

MCP47A1_SOLDERED dac;    // Create object for DAC library.
uint8_t waveformLUT[65]; // Array for storing samples of the desired waveform.

int delay_ms = 100;       // Delay between samples.

void setup()
{
    dac.begin();               // Initialize DAC's library.
    makeLut();                 // Fill LUT (lookup table) with sine wave values.
}

int k = 0; // Counter variable for selecting samples from the LUT.
void loop()
{
    dac.setByte(waveformLUT[k]); // Send waveform samples stored in LUT one by one to the DAC.
    k++;
    if (k > 64)
        k = 0;
    delay(delay_ms); // Wait a little bit between samples. A smaller delay produces a higher frequency for the generated signal.
}

// Function calculates values for each sample of the waveform and stores those values in the LUT.
void makeLut()
{
  for (int i = 0; i < 65; i++)
  {
    waveformLUT[i] = 32 * sin(2.0 * PI * i/sizeof(waveformLUT)) + 32;
  }
}
```