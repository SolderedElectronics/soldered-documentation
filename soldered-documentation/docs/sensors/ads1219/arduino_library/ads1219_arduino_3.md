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

This example is wired with a bench supply on two channels: CH1 provides the reference voltage, CH2 provides the signal being measured. Driving the reference from something other than your supply rail is deliberate. It shows the ADS1219 measuring against a reference you picked rather than against whatever VCC happens to be, and 2.500 V sits clear of both the 2.048 V internal reference and the 3.3 V rail, so a reference that isn't working can't accidentally produce a believable number.

| Generator channel | Set to    | Goes to                     |
| ----------------- | --------- | --------------------------- |
| **CH1**           | **2.500 V** | **REFP** (+) and **REFN** (-) |
| **CH2**           | **1.000 V** | **AIN0** (+) and **GND** (-)  |

<CenteredImage src="/img/ads1219/mux_connections.webp" alt="ADS1219 wired to a NULA DeepSleep and a two-channel bench supply" caption="The four labelled leads go to the bench supply - the Qwiic cable handles power and I2C" width="100%" />

Connect the board to your development board with a **Qwiic cable** for power and I2C, then wire the generator as above. Two things are easy to get wrong:

- **REFN must be tied to the board's GND.** The ADS1219 measures REFP and REFN against its own internal ground, so a generator output left floating has no defined level relative to the chip and the reading becomes meaningless. With REFN grounded, the reference is simply whatever you dial into CH1.
- **The signal on AIN0 must stay below the reference.** At gain 1 the full-scale input range *is* the reference voltage, so 1.000 V against a 2.500 V reference leaves comfortable headroom.

<WarningBox>The reference voltage must be between **0.75 V** and **AVDD** (3.3 V on a 3V3 system, since AVDD is tied to VCC through JP2). Set the supply's voltage **before** enabling its output, and never apply more than AVDD to REFP.</WarningBox>

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

    // Use REFP/REFN as the reference - CH1 of the generator, 2.500 V
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

    // 2500.0f is the reference voltage in millivolts, matching CH1 - change this
    // to match whatever you actually wired to REFP/REFN
    float mV = adc.getConversionMillivolts(2500.0f);

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

Open the **Serial Monitor** at **115200 baud** to see the reading for whichever channel you selected. Expect a value matching the voltage you **measured** on AIN0, not the one you dialled in - our supply was set to 1.000 V but actually delivering about 0.989 V, so readings landed at roughly **989 mV**, which is correct.

<CenteredImage src="/img/ads1219/an0.png" alt="Serial Monitor output reading AIN0" caption="ADS1219_MUX_SINGLE_0 - AIN0 against a 2.500 V external reference, settled to within 0.1 mV" width="100%" />

To read a different channel, swap `ADS1219_MUX_SINGLE_0` for `ADS1219_MUX_SINGLE_1`, `_2` or `_3` and move the CH2 wire to the matching AIN pin. Nothing else in the sketch changes.

<InfoBox>If the printed value is **exactly** your reference voltage (2500.000 mV here), the input is at or above full scale and the reading is clipped, not measured - lower the signal on AIN0 or raise the reference.</InfoBox>


---

## Confirming the reference is really being used

If you want to prove the external reference is actually driving the conversion, and not silently falling back to the internal one, compare the same input against two different references. Run the sketch once with `ADS1219_VREF_INTERNAL` and `getConversionMillivolts(2048.0f)`, then again with `ADS1219_VREF_EXTERNAL` and your measured reference value. Leave the signal on AIN0 untouched between the two.

Printing the raw code alongside the millivolts is what makes this readable:

```cpp
Serial.print(adc.getConversionRaw());
Serial.print('\t');
Serial.println(mV, 3);
```

These are the readings from our bench, with the same unchanged signal on AIN0:

| Reference          | Raw code  | Reported    | Noise (peak-to-peak) |
| ------------------ | --------- | ----------- | -------------------- |
| Internal 2.048 V   | 4,057,900 | 990.70 mV   | 43 µV                |
| External 2.500 V   | 3,322,500 | 990.20 mV   | 112 µV               |

The **raw code must change** and the **reported millivolts must not**. Here the raw ratio is 4,057,900 / 3,322,500 = **1.2213**, against a reference ratio of 2500 / 2048 = **1.2207** - agreement to 0.05%, while the reported voltage held at ~990 mV across both. That's the reference being applied exactly as configured.

If the raw code *doesn't* move when you switch references, the external reference isn't taking effect - check that `setVoltageReference()` succeeded and that REFP/REFN are really connected.

<InfoBox>The 0.5 mV difference between the two rows isn't converter error. Working backwards from the raw codes, the supply was actually delivering **2501.3 mV** rather than the 2500.0 we passed in - a 0.05% error in the reference *value* we told the library about, not in the measurement. It's a neat illustration of why the exact reference voltage matters.</InfoBox>

### Checking the noise floor

Shorting a channel straight to GND and reading it separates the converter's own noise from everything your reference and signal source contribute. Tie **AIN1** to GND, select `ADS1219_MUX_SINGLE_1`, and you're measuring the ADC against itself.

On our bench that read **within 22 µV of zero**, with about 5 µV of offset - against the datasheet's figure of 19.71 µV peak-to-peak at 20 SPS and gain 1. So the 0.1 mV spread seen on a driven channel above is the bench supply and reference, not the ADS1219.

<CenteredImage src="/img/ads1219/an1.png" alt="Serial Monitor output with AIN1 shorted to GND" caption="ADS1219_MUX_SINGLE_1 - AIN1 tied to GND, reading within 22 µV of zero" width="100%" />

<InfoBox>If a grounded channel reads far worse than a few tens of µV, the problem is upstream of the chip - grounding, lead dress, or a marginal solder joint - and no amount of averaging in software will recover it.</InfoBox>

<QuickLink
  title="Multiplexer.ino"
  description="Full input-multiplexer example for the ADS1219 24-bit ADC"
  url="https://github.com/SolderedElectronics/Soldered-ADS1219-Arduino-Library/blob/main/examples/Multiplexer/Multiplexer.ino"
/>
