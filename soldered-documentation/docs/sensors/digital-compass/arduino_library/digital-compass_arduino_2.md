---
slug: /digital-compass/arduino/examples 
title: Digital Compass - Taking measurements
sidebar_label: Taking measurements
id: digital-compass-arduino-2 
hide_title: False
---

This page contains some simple examples with function documentation on how to take measurements using the Digital Compass.

## Connections for this example

<CenteredImage src="/img/digital-compass/connection-scheme.jpg" alt="Connection scheme for the following examples" caption="Connection scheme for the following example" />

---

## Initialization

To start working with the **Digital Compass AK09918C 3-Axis Magnetometer breakout**, you need to set up your Arduino enviroment. Firstly, include the **required library**, create the sensor object, and **initialize** the sensor in the `setup()` function. You can use the return of the `begin()` to check if everything is connected correctly:

```cpp
#include "AK09918-SOLDERED.h"

AK09918 compass;

void setup()
{
    Serial.begin(115200);

    AK09918_err_type_t err = compass.begin(Wire, AK09918_CONT_MEASURE_MODE1);
    if (err != AK09918_ERR_OK)
    {
        Serial.print("Sensor init failed: ");
        Serial.println(compass.strError(err));
        while (true)
            ;
    }

    Serial.println("AK09918 compass heading — keep the board flat!");
    Serial.println("Heading\t\tDirection\tX\t\tY\t\tZ");
}
```

<FunctionDocumentation
functionName="compass.begin()"
description="Initializes the sesnor and configures the I2C bus."
returnDescription="Returns AK09918_ERR_OK on success, error code on failure."
parameters={[
{ type: 'TwoWire', name: '&wire', description: "Optional, sets the reference to the TwoWire instance that will be used, Wire is default" },
{ type: 'AK09918_mode_type_t', name: 'mode', description:"Optional, sets the initial operating mode, default is AK09918_POWER_DOWN" },
]}
/>

<InfoBox>
Check out all the supported operating modes in the table below:
| **Measurement mode** 	| **Description** 	|
|---	|---	|
| AK09918_POWER_DOWN 	| Power down  	|
| AK09918_NORMAL 	| Triggers a single measurement 	|
| AK09918_CONT_MEASURE_MODE1 	| Sets the continuous output mode an 10Hz data rate 	|
| AK09918_CONT_MEASURE_MODE2 	| Sets the continuous output mode an 20Hz data rate 	|
| AK09918_CONT_MEASURE_MODE3 	| Sets the continuous output mode an 50Hz data rate 	|
| AK09918_CONT_MEASURE_MODE4 	| Sets the continuous output mode an 100Hz data rate 	|
| AK09918_SELF_TEST 	| Runs the self test 	|
</InfoBox>

---

## Taking a measurement
To take a single measurement, first you need to create variables in which the values will be stored. After that, call the `getData()` function.

```cpp

void loop(){
    int32_t x,y,z;
    AK09918_err_type_t err = compass.getData(&x,&y,&z);
    if (err == AK09918_ERR_TIMEOUT)
    {
        Serial.println("Timeout — sensor did not respond");
    }
    else if (err == AK09918_ERR_OVERFLOW)
    {
        Serial.println("Overflow — field too strong to measure");
    }
    else if (err != AK09918_ERR_OK)
    {
        Serial.print("Error: ");
        Serial.println(compass.strError(err));
    }
    else
    {
        Serial.print(x);
        Serial.print('\t');
        Serial.print(y);
        Serial.print('\t');
        Serial.println(z);
    }

    delay(1000);
}

```

<FunctionDocumentation
functionName="compass.getData()"
description="Reads the calibrated magnetic field values."
returnDescription="Returns AK09918_ERR_OK on success, error code on failure."
parameters={[
{ type: 'uint32_t', name: '*axis_x', description: "Pointer to store X-Axis result." },
{ type: 'uint32_t', name: '*axis_y', description: "Pointer to store Y-Axis result." },
{ type: 'uint32_t', name: '*axis_z', description: "Pointer to store Z-Axis result." },
]}
/>

---

## Taking continuous measurements

It is also possible to take continuous measurement by changing the operating mode in `compass.begin()` to any of the continuous measurement modes. While in continuous measurement, it is required to call the `isDataReady()` function that checks out if the measurement has finnished. Check out the full example code:

```cpp
#include "AK09918-SOLDERED.h"

AK09918 compass;

void setup()
{
    Serial.begin(115200);

    AK09918_err_type_t err = compass.begin(Wire, AK09918_CONT_MEASURE_MODE1);
    if (err != AK09918_ERR_OK)
    {
        Serial.print("Sensor init failed: ");
        Serial.println(compass.strError(err));
        while (true)
            ;
    }

    Serial.println("AK09918 ready — reading at 10 Hz");
    Serial.println("X (uT*10)\tY (uT*10)\tZ (uT*10)");
}

void loop()
{
    if (compass.isDataReady() != AK09918_ERR_OK)
    {
        return;
    }

    int32_t x, y, z;
    AK09918_err_type_t err = compass.getData(&x, &y, &z);
    if (err != AK09918_ERR_OK)
    {
        Serial.print("Read error: ");
        Serial.println(compass.strError(err));
        return;
    }

    Serial.print(x);
    Serial.print('\t');
    Serial.print(y);
    Serial.print('\t');
    Serial.println(z);
}
```


<CenteredImage src="/img/digital-compass/serial-monitor-output.png" alt="Serial Monitor output" caption="Serial Monitor output" width="200px"/>

<FunctionDocumentation
    functionName="compass.isDataReady()"
    description="Checks whether new measurement data is available."
    returnDescription="Returns AK09918_ERR_OK if data is ready, error code on failure."
    parameters={[]}
/>

