---
slug: /scd43/arduino/disable-auto-calibration
title: SCD43 - Disabling automatic self-calibration
sidebar_label: Disabling automatic self-calibration
id: scd43-arduino-5
hide_title: false
---

This page walks through the `DisableAutoCalibration` example: turning off the SCD43's Automatic Self-Calibration (ASC) and saving that setting so it survives a power cycle.

---

## Why disable ASC

As covered on the [how it works](/scd43/how-it-works) page, ASC assumes the sensor is periodically exposed to fresh outdoor air at its calibration target (400 ppm by default) and uses that to correct long-term drift. That assumption doesn't hold everywhere: a sensor sealed inside an enclosure, or installed in an industrial space that never sees outdoor-level CO2, will have ASC calibrating against air that never actually shows up, which can make readings drift the wrong way over time. Turning ASC off avoids that.

---

## Checking and changing the ASC setting

Reading or changing the ASC setting requires the sensor to be in idle mode, so stop periodic measurement first:

```cpp
#include "SCD43-SOLDERED.h"

SCD43 sensor;

void setup()
{
    Serial.begin(115200);
    Serial.println("SCD43 - Disable Auto Calibration");

    Wire.begin();

    if (!sensor.begin())
    {
        Serial.println("Sensor not found. Check wiring. Halting.");
        while (1)
            ;
    }

    if (!sensor.stopPeriodicMeasurement())
    {
        Serial.println("Could not stop periodic measurement. Halting.");
        while (1)
            ;
    }

    Serial.print("ASC enabled before change: ");
    Serial.println(sensor.getAutomaticSelfCalibrationEnabled() ? "yes" : "no");

    if (!sensor.setAutomaticSelfCalibrationEnabled(false))
    {
        Serial.println("Failed to disable ASC.");
    }
    else
    {
        Serial.println("ASC disabled successfully.");
    }
```

<FunctionDocumentation
  functionName="sensor.getAutomaticSelfCalibrationEnabled()"
  description="Checks whether automatic self-calibration is currently enabled on the sensor. Only available in idle mode."
  returnDescription="Returns true if ASC is enabled, false if disabled."
  parameters={[]}
/>

<FunctionDocumentation
  functionName="sensor.setAutomaticSelfCalibrationEnabled()"
  description="Enables or disables the automatic self-calibration algorithm. Only available in idle mode."
  returnDescription="Returns true on success, false otherwise."
  parameters={[
    { type: 'bool', name: 'enabled', description: 'True to enable ASC, false to disable it' },
  ]}
/>

---

## Making it stick

Disabling ASC only changes the setting in the sensor's volatile memory. Power-cycle the board without saving it, and it goes back to the factory default (ASC enabled). `persistSettings()` writes the current settings to EEPROM so they survive a reset:

```cpp
    if (!sensor.persistSettings())
    {
        Serial.println("Failed to persist settings.");
    }
    else
    {
        Serial.println("Settings saved to EEPROM.");
    }

    if (!sensor.startPeriodicMeasurement())
    {
        Serial.println("Could not restart periodic measurement. Halting.");
        while (1)
            ;
    }

    Serial.println("Periodic measurements restarted.");
}
```

<FunctionDocumentation
  functionName="sensor.persistSettings()"
  description="Saves the current configuration, including the ASC enabled state, temperature offset, and sensor altitude, to the sensor's EEPROM. Blocks for about 800 ms."
  returnDescription="Returns true on success, false otherwise."
  parameters={[]}
/>

<WarningBox>
The EEPROM supports at least 2000 write cycles. Don't call `persistSettings()` on every boot or in a loop, only after actually changing a setting you want to keep.
</WarningBox>

---

## Confirming readings still work

With ASC disabled and periodic measurement resumed, `loop()` reads and prints CO2, temperature, and humidity exactly the same way as the `BasicReadings` example. Disabling ASC only changes how the sensor corrects long-term drift in the background, it doesn't change how you read measurements:

```cpp
void loop()
{
    if (sensor.readMeasurement())
    {
        Serial.println();
        Serial.print("CO2 (ppm):       ");
        Serial.println(sensor.getCO2());
        Serial.print("Temperature (C): ");
        Serial.println(sensor.getTemperature(), 1);
        Serial.print("Humidity (%RH):  ");
        Serial.println(sensor.getHumidity(), 1);
    }
    else
    {
        Serial.print(".");
    }

    delay(500);
}
```

<CenteredImage src="/img/scd43/auto_cali.png" alt="SCD43 Serial Monitor output after disabling ASC" caption="Serial Monitor output showing normal readings continue after ASC is disabled and periodic measurement resumes" width="1000px" />

---

## Full example

<QuickLink
  title="DisableAutoCalibration.ino"
  description="Full example sketch for disabling and persisting the SCD43's automatic self-calibration setting."
  url="https://github.com/SolderedElectronics/Soldered-SCD43-Arduino-Library/blob/main/examples/DisableAutoCalibration/DisableAutoCalibration.ino"
/>
