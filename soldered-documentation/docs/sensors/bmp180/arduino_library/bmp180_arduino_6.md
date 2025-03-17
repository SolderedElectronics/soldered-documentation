---
slug: /bmp180/arduino/examples4
title: Calculating altitude
id: bmp180-arduino-6
hide_title: False
---

Altitude can be calculated by taking a pressure measurement and knowing the pressure at baseline and putting them in the `altitude()` function

<WarningBox>To calculate altitude you should have a recent reading of the pressure at sea level at your relative geolocation. Not having it will result in very inaccurate values</WarningBox>

```cpp
    //...

    bmp180.getPressure(pressure, temperature);

    //Average sealevel pressure (Getting a location specific pressure is far more precise)
    double pressure_at_sea_level = 1013.25;

    double altitude = bmp180.altitude(pressure, pressure_at_sea_level);

    Serial.println("Current altitude: "+String(altitude)+" m");

    //...
```
<CenteredImage src="/img/bmp180/bmp180_altitude.png" alt="Serial monitor altitude readings" caption="Serial monitor" width="100%" />

<FunctionDocumentation
  functionName="bmp180.altitude(double P, double P0)"
  description="Calculates altitude in meter depending on the pressure reading and baseline pressure at sealevel"
  returnDescription="Double value, the altitude in meters"
  parameters={[
  { type: 'double', name: 'P', description: "Absolute pressure value in mbars" },
  { type: 'double', name: 'P0', description: "Baseline pressure at sealevel in mbars" },

  ]}
/>

## Full example
Try all of the mentioned functions in this documentation in this example:

<QuickLink 
  title="TempAndPressure.ino" 
  description="Example file for using BMP180 sensor with easyC/Qwiic/I2C"
  url="https://github.com/SolderedElectronics/Soldered-BMP180-Temperature-Pressure-Sensor-Arduino-Library/blob/main/examples/TempAndPressure/TempAndPressure.ino" 
/>