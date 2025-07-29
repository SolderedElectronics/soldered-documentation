---
slug: /bmp180/arduino/calculating-altitude
title: Bmp180 - Calculating altitude
sidebar_label: Calculating altitude
id: bmp180-arduino-6
hide_title: false
---

Altitude can be calculated by measuring the pressure, knowing the baseline pressure, and then using the `altitude()` function.

<WarningBox>To calculate altitude, you should have a recent reading of the pressure at sea level for your location. Without it, the values will be very inaccurate.</WarningBox>

```cpp
    //...

    bmp180.getPressure(pressure, temperature);

    // Average sea level pressure (Getting a location-specific pressure is far more precise)
    double pressure_at_sea_level = 1013.25;

    double altitude = bmp180.altitude(pressure, pressure_at_sea_level);

    Serial.println("Current altitude: "+String(altitude)+" m");

    //...
```
<CenteredImage src="/img/bmp180/bmp180_altitude.png" alt="Serial monitor altitude readings" caption="Serial monitor" width="100%" />

<FunctionDocumentation
  functionName="bmp180.altitude(double P, double P0)"
  description="Calculates altitude in meters based on the pressure reading and the baseline pressure at sea level."
  returnDescription="Double value, the altitude in meters"
  parameters={[
  { type: 'double', name: 'P', description: "Absolute pressure value in mbars" },
  { type: 'double', name: 'P0', description: "Baseline pressure at sea level in mbars" },

  ]}
/>

## Full example
Try all the functions mentioned in this documentation through this example:

<QuickLink 
  title="TempAndPressure.ino" 
  description="Example file for using BMP180 sensor with easyC/Qwiic/I2C"
  url="https://github.com/SolderedElectronics/Soldered-BMP180-Temperature-Pressure-Sensor-Arduino-Library/blob/main/examples/TempAndPressure/TempAndPressure.ino" 
/>