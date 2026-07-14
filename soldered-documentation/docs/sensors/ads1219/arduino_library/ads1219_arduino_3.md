---
slug: /ads1219/arduino/multiplexer 
title: ADS1219 24-bit ADC - Channel Selection
sidebar_label: Channel Selection
id: ads1219-arduino-3 
hide_title: False
---

This page covers selecting which of the ADS1219's four input channels (or which differential pair) actually gets converted, using the input multiplexer.

---

## Connections

Connect the ADS1219 board via Qwiic, and wire REFP/REFN to your chosen reference (see [Single-Shot Reading](/ads1219/arduino/single-shot) for reference-voltage options).

Connect a signal source to **AIN0** and GND - this example reads AIN0 single-ended, but any of the mux options below can be swapped in instead.

---

## Selecting a channel

```cpp
#include <Wire.h>
#include "ADS1219-SOLDERED.h"

ADS1219_Soldered adc;

void setup()
{
    Serial.begin(115200);
    Wire.begin();

    while (!adc.begin())
    {
        Serial.println("ADS1219 not found. Check wiring! Retrying...");
        delay(1000);
    }

    // Use REFP/REFN as the reference (tie them to VCC/GND, or a precision source)
    adc.setVoltageReference(ADS1219_VREF_EXTERNAL);

    // AIN0 vs GND (single-ended)
    adc.setMux(ADS1219_MUX_SINGLE_0);
}

void loop()
{
    if (!adc.startSync())
    {
        Serial.println("Failed to start conversion. Check wiring! Retrying...");
        delay(1000);
        return;
    }

    while (!adc.dataReady())
        delay(10);

    adc.readConversion();

    // 3300.0f is the reference voltage in millivolts (3.3V here) - change this
    // to match whatever you actually wired to REFP/REFN
    float mV = adc.getConversionMillivolts(3300.0f);

    Serial.print("Voltage (mV): ");
    Serial.println(mV, 3);
}
```

<FunctionDocumentation
  functionName="adc.setMux()"
  description="Selects which input channel or differential pair is routed to the ADC."
  returnDescription="Boolean value, true on success."
  parameters={[
  { type: 'ads1219_mux_t', name: 'mux', description: "ADS1219_MUX_SINGLE_0 through _3 for single-ended channels (each measured against GND), ADS1219_MUX_DIFF_P0_N1 / _P1_N2 / _P2_N3 for differential pairs, or ADS1219_MUX_SHORTED to measure the internal offset (AVDD/2 vs itself)." },
  ]}
/>

<InfoBox>Swap `ADS1219_MUX_SINGLE_0` for any of the other mux constants to read a different channel or pair - everything else in the sketch stays the same. `ADS1219_MUX_DIFF_P0_N1` (AIN0 vs AIN1) is the default at power-on.</InfoBox>

Open the **Serial Monitor** at **115200 baud** to see the reading for whichever channel you selected.

<QuickLink
  title="Multiplexer.ino"
  description="Full input-multiplexer example for the ADS1219 24-bit ADC"
  url="https://github.com/SolderedElectronics/Soldered-ADS1219-Arduino-Library/blob/main/examples/Multiplexer/Multiplexer.ino"
/>
