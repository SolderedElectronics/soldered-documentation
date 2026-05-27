---
slug: /ads1219/arduino/interrupt
title: ADS1219 24-bit ADC - Interrupt
sidebar_label: Interrupt 
id: ads1219-arduino-3 
hide_title: False
---

This page contains an example of reading ADC values from the ADS1219 using the **DRDY interrupt pin**, where the microcontroller is notified by the sensor when a new conversion result is ready.

---

## Connections for this example

<CenteredImage src="/img/ads1219/interrupt.JPG" alt="Connections" />

---

## Initialization

Include the library and create the ADC object:

```cpp
#include "ADS1219-SOLDERED.h"

ADS1219 adc;
```

In the `setup()` function, initialize and configure the sensor:

```cpp
void setup()
{
    Serial.begin(115200);

    if (adc.begin() == false)
    {
        Serial.println("ADS1219 not detected. Please check wiring. Freezing.");
        while (1);
    }

    // Set gain to 1 (full-scale range ±2.048 V with internal reference)
    adc.setGain(ADS1219_GAIN_1);

    // Set data rate to 90 SPS
    adc.setDataRate(ADS1219_DR_90);

    // Select single-ended input on channel 0
    adc.setInputMultiplexer(ADS1219_MUX_SINGLE_0);

    // Use internal 2.048 V reference
    adc.setVoltageReference(ADS1219_VREF_INTERNAL);

    // Enable interrupt-driven mode and start conversions
    adc.setConversionMode(ADS1219_CM_CONTINUOUS);
    adc.start();
}
```

<FunctionDocumentation
  functionName="adc.begin()"
  description="Initializes the ADS1219 and establishes I2C communication"
  returnDescription="Boolean value, true if the device is detected and communication succeeds, false otherwise"
  parameters={[]}
/>

<FunctionDocumentation
  functionName="adc.setGain(uint8_t gain)"
  description="Sets the programmable gain amplifier (PGA). Higher gain narrows the input range but increases resolution for small signals"
  returnDescription="None"
  parameters={[
  { type: 'uint8_t', name: 'gain', description: "Gain setting: ADS1219_GAIN_1 (±2.048 V), ADS1219_GAIN_2 (±1.024 V), ADS1219_GAIN_4 (±0.512 V), ADS1219_GAIN_8 (±0.256 V)" },
  ]}
/>

<FunctionDocumentation
  functionName="adc.setDataRate(uint8_t rate)"
  description="Sets the output data rate (samples per second). Lower rates give less noise; higher rates give faster updates"
  returnDescription="None"
  parameters={[
  { type: 'uint8_t', name: 'rate', description: "Data rate: ADS1219_DR_20 (20 SPS), ADS1219_DR_90 (90 SPS), ADS1219_DR_330 (330 SPS), ADS1219_DR_1000 (1000 SPS)" },
  ]}
/>

<FunctionDocumentation
  functionName="adc.setInputMultiplexer(uint8_t mux)"
  description="Selects which input channel or differential pair is routed to the ADC"
  returnDescription="None"
  parameters={[
  { type: 'uint8_t', name: 'mux', description: "Input selection: ADS1219_MUX_SINGLE_0-3 for single-ended channels, ADS1219_MUX_DIFF_0_1 / ADS1219_MUX_DIFF_2_3 for differential pairs" },
  ]}
/>

<FunctionDocumentation
  functionName="adc.setVoltageReference(uint8_t ref)"
  description="Selects the voltage reference source used for conversion"
  returnDescription="None"
  parameters={[
  { type: 'uint8_t', name: 'ref', description: "ADS1219_VREF_INTERNAL for the built-in 2.048 V reference, ADS1219_VREF_EXTERNAL to use REFP/REFN pins" },
  ]}
/>

<FunctionDocumentation
  functionName="adc.setConversionMode(uint8_t mode)"
  description="Sets the conversion mode. In continuous mode the ADC converts back-to-back without needing a new trigger for each sample"
  returnDescription="None"
  parameters={[
  { type: 'uint8_t', name: 'mode', description: "ADS1219_CM_SINGLE for single-shot mode, ADS1219_CM_CONTINUOUS for continuous mode" },
  ]}
/>

<FunctionDocumentation
  functionName="adc.start()"
  description="Sends the START/SYNC command to begin conversions. In continuous mode, conversions run automatically after this call"
  returnDescription="None"
  parameters={[]}
/>

---

## Reading Data

In the `loop()` function, wait for the DRDY flag and read each new result:

```cpp
void loop()
{
    // Wait until a new conversion result is ready
    if (adc.isDataReady())
    {
        long raw = adc.readData();
        float voltage = adc.toVoltage(raw);

        Serial.print("Raw: ");
        Serial.print(raw);
        Serial.print("  Voltage: ");
        Serial.print(voltage, 6);
        Serial.println(" V");
    }
}
```

<CenteredImage src="/img/ads1219/readings.png" alt="Serial monitor output" caption="Serial monitor" width="100%" />

<FunctionDocumentation
  functionName="adc.isDataReady()"
  description="Checks whether a new conversion result is available by reading the DRDY status"
  returnDescription="Boolean value, true if a new result is ready to be read"
  parameters={[]}
/>

<FunctionDocumentation
  functionName="adc.readData()"
  description="Reads the latest 24-bit conversion result from the DATA register"
  returnDescription="Long (int32_t) value, the signed raw ADC result"
  parameters={[]}
/>

<FunctionDocumentation
  functionName="adc.toVoltage(long raw)"
  description="Converts a raw 24-bit ADC result to a voltage in volts, based on the configured gain and voltage reference"
  returnDescription="Float value, the measured voltage in Volts"
  parameters={[
  { type: 'long', name: 'raw', description: "The signed raw ADC value returned by readData()" },
  ]}
/>

---

## Full example

You can find the full sketch below:

<QuickLink  
  title="Interrupt.ino"  
  description="An example of reading ADC values using the interrupt (DRDY) pin with the ADS1219"  
  url="https://github.com/SolderedElectronics/Soldered-ADS1219-Arduino-Library/blob/main/examples/Interrupt/Interrupt.ino"  
/>











