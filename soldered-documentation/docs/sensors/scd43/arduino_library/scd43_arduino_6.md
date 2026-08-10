---
slug: /scd43/arduino/signal-compensation
title: SCD43 - Signal compensation
sidebar_label: Signal compensation
id: scd43-arduino-6
hide_title: false
---

This page walks through the `SignalCompensation` example: adjusting the temperature offset, sensor altitude, and ambient pressure settings the SCD43 uses to correct its readings.

---

## Temperature offset

Any nearby heat source, including the microcontroller itself, can make the SCD43 report a temperature slightly higher than the actual ambient air, which the troubleshooting page also notes under self-heating. The temperature offset setting corrects for this. As with any configuration change, the sensor needs to be in idle mode first:

```cpp
#include "SCD43-SOLDERED.h"

SCD43 sensor;

void setup()
{
    Serial.begin(115200);
    Serial.println("SCD43 - Signal Compensation");

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

    Serial.print("Temperature offset before: ");
    Serial.print(sensor.getTemperatureOffset(), 2);
    Serial.println(" C");

    sensor.setTemperatureOffset(4.0f); // default is 4 C; adjust for your enclosure

    Serial.print("Temperature offset after:  ");
    Serial.print(sensor.getTemperatureOffset(), 2);
    Serial.println(" C");
```

<FunctionDocumentation
  functionName="sensor.getTemperatureOffset()"
  description="Returns the temperature compensation offset currently used by the sensor. Only available in idle mode."
  returnDescription="Temperature offset in degrees Celsius as a float."
  parameters={[]}
/>

<FunctionDocumentation
  functionName="sensor.setTemperatureOffset()"
  description="Sets the temperature compensation offset, correcting for self-heating from nearby components. The factory default is 4 degrees C. Only available in idle mode."
  returnDescription="Returns true on success, false otherwise."
  parameters={[
    { type: 'float', name: 'offsetCelsius', description: 'Temperature offset in degrees Celsius, 0-20 C recommended' },
  ]}
/>

---

## Sensor altitude

CO2 measurements also depend on atmospheric pressure, which drops with elevation. If the sensor is installed somewhere well above sea level, telling it the altitude improves accuracy:

```cpp
    Serial.print("Sensor altitude before: ");
    Serial.print(sensor.getSensorAltitude());
    Serial.println(" m");

    sensor.setSensorAltitude(150); // set to your installation altitude in metres

    Serial.print("Sensor altitude after:  ");
    Serial.print(sensor.getSensorAltitude());
    Serial.println(" m");
```

<FunctionDocumentation
  functionName="sensor.getSensorAltitude()"
  description="Returns the sensor altitude currently used for pressure compensation. Only available in idle mode."
  returnDescription="Altitude in meters above sea level as a uint16_t."
  parameters={[]}
/>

<FunctionDocumentation
  functionName="sensor.setSensorAltitude()"
  description="Sets the installation altitude used for pressure compensation. The factory default is 0 m. Only available in idle mode."
  returnDescription="Returns true on success, false otherwise."
  parameters={[
    { type: 'uint16_t', name: 'altitudeMeters', description: 'Altitude in meters above sea level, 0-3000 m' },
  ]}
/>

---

## Ambient pressure

If a barometer is available, feeding the SCD43 a live pressure reading is more accurate than a fixed altitude, and overrides it:

```cpp
    if (sensor.setAmbientPressure(101300)) // 101300 Pa = standard sea-level pressure
    {
        Serial.println("Ambient pressure set to 101300 Pa.");
    }
```

<FunctionDocumentation
  functionName="sensor.setAmbientPressure()"
  description="Sets the ambient pressure for continuous compensation, overriding altitude-based compensation. Can be called during periodic measurements for dynamic updates, unlike temperature offset and altitude. The factory default is 101300 Pa."
  returnDescription="Returns true on success, false otherwise."
  parameters={[
    { type: 'uint32_t', name: 'pressurePa', description: 'Ambient pressure in Pascals, 70000-120000 Pa' },
  ]}
/>

<InfoBox>
Unlike the temperature offset and altitude, ambient pressure isn't saved by `persistSettings()`. If you have a live barometer feeding this value, that's fine since you'd set it fresh on every boot anyway.
</InfoBox>

---

## Saving the settings and finishing up

```cpp
    if (sensor.persistSettings())
    {
        Serial.println("Temperature offset and altitude saved to EEPROM.");
    }

    uint64_t serialNumber = 0;
    if (sensor.getSerialNumber(serialNumber))
    {
        Serial.print("Sensor serial number: 0x");
        Serial.println((uint32_t)(serialNumber >> 16), HEX);
        Serial.println((uint32_t)(serialNumber & 0xFFFF), HEX);
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
  functionName="sensor.getSerialNumber()"
  description="Reads the sensor's unique 48-bit serial number. Only available in idle mode."
  returnDescription="Returns true on success, false otherwise. The serial number is written to the output parameter."
  parameters={[
    { type: 'uint64_t&', name: 'serialNumber', description: 'Output: receives the 48-bit serial number' },
  ]}
/>

---

## Confirming readings still work

With all three compensation settings applied and periodic measurement resumed, `loop()` reads and prints CO2, temperature, and humidity exactly the same way as the `BasicReadings` example. The compensation settings adjust the numbers behind the scenes, they don't change how you read them:

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

<CenteredImage src="/img/scd43/signal_comp.png" alt="SCD43 Serial Monitor output after signal compensation setup" caption="Serial Monitor output showing the compensation setup, saved settings, serial number, and resumed periodic readings" width="1000px" />

---

## Full example

<QuickLink
  title="SignalCompensation.ino"
  description="Full example sketch for configuring temperature offset, altitude, and ambient pressure compensation on the SCD43."
  url="https://github.com/SolderedElectronics/Soldered-SCD43-Arduino-Library/blob/main/examples/SignalCompensation/SignalCompensation.ino"
/>
