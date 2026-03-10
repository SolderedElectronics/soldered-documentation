---
slug: /bmp280/arduino/measurements
title: Bmp280 - Taking measurements
sidebar_label: Taking measurements
id: bmp280-arduino-3 
hide_title: False
---

The BMP280 has **Two measuring modes:** **Normal** and **Forced**.

## Normal mode

Normal mode continuously cycles between an (active) measurement period and an (inactive) standby period, whose time is defined by `t_standby`. To set the board into normal mode, call `bmp280.startNormalConversion()` and `bmp.setTimeStandby()` in `setup()`. To take a measurement, first create 3 float variables and then call `bmp280.getMeasurements()`.

```cpp

void setup(){

    //...

    bmp280.startNormalConversion();
    bmp280.setTimeStandby(TIME_STANDBY_2000MS);
}

void loop(){
    //Variables for storing measurement data
    float temperature, pressure, altitude;

    // Check if the data is ready
    if (bmp280.getMeasurements(temperature, pressure, altitude))
    {
        // Print the results.
        Serial.print(temperature);
        Serial.print(F("*C   "));
        Serial.print(pressure);
        Serial.print(F("hPa   "));
        Serial.print(altitude);
        Serial.println(F("m"));
    }
}
```

[IMAGE PLACEHOLDER - Serial monitor output]

<FunctionDocumentation
    functionName="bmp280.startNormalConversion();"
    description="Starts continuous measurement in NORMAL MODE"
/>

<FunctionDocumentation
    functionName="bmp280.setTimeStandby()"
    description="Sets the time interval between measurements"
    parameters={[
    { type: 'TimeStandby', name: 'timeStandby', description: "Enum for time standby bit field in the configurator register" },
    ]}
/>

<InfoBox>
All available values: `TIME_STANDBY_05MS`, `TIME_STANDBY_62MS`, `TIME_STANDBY_125MS`, `TIME_STANDBY_250MS`, `TIME_STANDBY_500MS`, `TIME_STANDBY_1000MS`, `TIME_STANDBY_2000MS`, `TIME_STANDBY_4000MS` 
</InfoBox>


---

## Forced mode

In forced mode, a single measurement is performed according to selected measurement options. When the measurement is finished, the sensor returnt to sleep mode and the measurement can be obtained from the data registers. **For the next measurement, forced mode needs to be selected again**. To perform an forced measurement, call `bmp280.startForcedConversion()` in `loop()`.

```cpp
void loop(){
    // Variables for storing measurement data.
    float temperature, pressure, altitude;

    // Make a request for new measurement!
    bmp280.startForcedConversion();

    // Check if the measurement is complete.
    if (bmp280.getMeasurements(temperature, pressure, altitude))
    {
        Serial.print(temperature);
        Serial.print(F("*C   "));
        Serial.print(pressure);
        Serial.print(F("hPa   "));
        Serial.print(altitude);
        Serial.println(F("m"));
    }
}
```

[IMAGE PLACEHOLDER - serial monitor output]

<FunctionDocumentation
    functionName="bmp280.startForcedConversion()"
    description="Forces a single measurement"
/>

