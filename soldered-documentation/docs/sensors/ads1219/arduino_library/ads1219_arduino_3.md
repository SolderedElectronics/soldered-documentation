---
slug: /ads1219/arduino/continuous 
title: ADS1219 24-bit ADC - Continuous Reading
sidebar_label: Continuous Reading
id: ads1219-arduino-3 
hide_title: False
---

This page covers continuous conversion mode, where the ADS1219 converts back-to-back on its own at the configured data rate, instead of waiting for a `startSync()` call before each result.

---

## Connections

Connect the ADS1219 board via Qwiic, and wire REFP/REFN to your chosen reference (see the [previous page](/ads1219/arduino/single-shot) for reference-voltage options).

Connect a signal source to **AIN0** and **AIN1** - this example reads the voltage difference between them.

---

## Continuous reading

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

    adc.setConversionMode(ADS1219_MODE_CONTINUOUS);

    // In continuous mode, this single call starts the ongoing sequence
    adc.startSync();
}

void loop()
{
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
  functionName="adc.setConversionMode()"
  description="Sets the conversion mode. In continuous mode, the ADC converts back-to-back at the configured data rate without needing startSync() called again for each sample."
  returnDescription="Boolean value, true on success."
  parameters={[
  { type: 'ads1219_conv_mode_t', name: 'mode', description: "ADS1219_MODE_SINGLE_SHOT for one conversion per startSync() call, ADS1219_MODE_CONTINUOUS for back-to-back conversions." },
  ]}
/>

<FunctionDocumentation
  functionName="adc.startSync()"
  description="Starts or restarts conversions. In continuous mode, one call is enough to start the ongoing sequence - it doesn't need to be called again before each result."
  returnDescription="Boolean value, true on success."
  parameters={[]}
/>

<InfoBox>Since the default data rate is **20 SPS**, results come in relatively slowly out of the box (once every 50 ms). Combine this with `setDataRate()` from the next page if you need faster updates.</InfoBox>

Open the **Serial Monitor** at **115200 baud** to see a steady stream of readings, without needing to trigger each one yourself.

<QuickLink
  title="Continuous.ino"
  description="Full continuous-conversion example for the ADS1219 24-bit ADC"
  url="https://github.com/SolderedElectronics/Soldered-ADS1219-Arduino-Library/blob/main/examples/Continuous/Continuous.ino"
/>
