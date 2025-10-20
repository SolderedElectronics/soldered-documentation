---
slug: /bme688/arduino/examples 
title: BME688 Environmental Sensor - Taking measurements (Arduino)
sidebar_label: Taking measurements
id: bme688-arduino-2 
hide_title: False
---

## Connections for this example
<CenteredImage src="/img/bme688/connections.jpg" alt="Connections"/>

---

## Initialization

To use the BME688 sensor, first include the required library, create the sensor object, and initialize the sensor in the `setup()` function.
```cpp 
#include "BME688-Soldered.h"

BME688 sensor;

void setup(){
    Serial.begin(115200);
    if(sensor.begin()){
        Serial.println("BME688 Initialized Successfully!");
    }
    else{
        Serial.println("Failed to initialize BME688!");
        while(1);
    }
}
```

<FunctionDocumentation
    functionName="sensor.begin()"
    description="Initializes the BME688 sensor, setting up communication over I2C and configuring oversampling values for each sensor"
    returnDescription="Boolean value. True if the sensor was successfully initialized, False otherwise."
    parameters={[]}
/>

---

## Temperature

To get temperature value, use the `readTemperature()` function. The sensor samples temperature in degrees Celsius.

```cpp
void loop(){
    Serial.print("Temperature: ");
    Serial.print(sensor.readTemperature()); // Read temperature in °C
    Serial.println(" °C");
}
```
<WarningBox> Because the sensor by itself generates heat, a temperature offset may be needed. Make an independent temperature reading and add an offset if needed!</WarningBox>

<FunctionDocumentation
    functionName="sensor.readTemperature()"
    description="Reads the value from the sensor and returns the scaled Celsius value"
    returnDescription= "Float value of the temperature reading in degrees Celsius"
    parameters={[]}
/>
---

## Pressure

To get pressure value, use the `readPressure()` function. The sensor samples the pressure in Pascals (Pa).

```cpp
void loop(){
    Serial.print("Pressure: ");
    Serial.print(sensor.readPressure()); // Read pressure in Pascals
    Serial.print(" Pa");
}
```

<FunctionDocumentation
    functionName="sensor.readPressure()"
    description="Reads the value from the sensor and returns the scaled Pa value"
    return description="Float value of the temperature reading in Pa"
    paratemers={[]}
/>

---

## Humidity

To get humidity value, use the `readHumidity()` function. The sensor samples humidity as a percentage.

```cpp
void loop(){
    Serial.print("Humidity: ");
    Serial.print(sensor.readHumidity());
    Serial.print(" %");
}
```
<FunctionDocumentation
    functionName="sensor.readHumidity()"
    description="Reads the value from the sensor and returns the scaled percentage value"
    returnDescription="Float value of the humidity reading in %"
    parameters={[]}
/>

---

## Gas Resistance

To get gas resistance value, use the `sensor.readGas()` function. The sensor samples gas resistance in ohms.

```cpp
void loop(){
    Serial.print("Gas Resistance: ");
    Serial.print(sensor.readGas(0)); // Read gas resistance in ohms
    Serial.println(" Ω");

}
```

<FunctionDocumentation
    functionName="sensor.readGas()"
    description="Reads the value from the sensor and returns the scaled value in ohms"
    returnDescription="Float value of the gas resistance in ohms"
    parameters={[
    { type: 'integer', name:'profile', description: "Selects which of the BME688's up to 10 configured heater profiles (0-9)" },
    ]}
/>

<CenteredImage src="/img/bme688/serial-output.png" alt="Combined Serial Monitor output" caption="Combined Serial Monitor output" width="300px"/>