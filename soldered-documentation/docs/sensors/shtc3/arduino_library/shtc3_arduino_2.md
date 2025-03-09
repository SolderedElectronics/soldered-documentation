---
slug: /shtc3/arduino/examples 
title: Measuring temperature and humidity (examples)
id: shtc3-arduino-2 
hide_title: False
---

This page contains some simple examples with function documentation on how to take measurements using the SHTC3 temperature and humidity sensor.

---

## Initialization

To use the SHTC3 sensor, first, include the required library, create the sensor object and initialize the sensor in the `setup()` function. You can use the return of `begin()` to check if everything is connected correctly:
```cpp
// Include the library
#include "SHTC3-SOLDERED.h"

// Create an SHTC3 object
SHTC3 shtcSensor;

// Setup function, runs once
void setup()
{
    Serial.begin(115200);
    // Initialize sensor
    if(!shtcSensor.begin())
    {
        // 'begin' returned false, there is an error
        Serial.println("Can't init SHTC3!");
        Serial.println("Check connection!");
        while(true)
            ;
    }
}
// ...
```

<FunctionDocumentation
  functionName="shtcSensor.begin()"
  description="Initializes the SHTC3 sensor, setting up communication over I2C and verifying its presence."
  returnDescription="Returns true if initialization is successful, false otherwise."
  parameters={[]}
/>

---

## Sampling new measurements

Before reading temperature or humidity, call `sample()` to request a new measurement from the sensor:

```cpp
shtcSensor.sample(); // Request new temperature and humidity readings
```

<FunctionDocumentation
  functionName="shtcSensor.sample()"
  description="Requests a new temperature and humidity measurement from the SHTC3 sensor. It wakes up the sensor, performs the measurement, checks CRC validation, and puts the sensor back to sleep."
  returnDescription="Returns true if the sampling operation is successful and the CRC check passes, false otherwise."
  parameters={[
    { type: 'uint16_t', name: 'readcmd', description: "Optional, default is SHTC3_READ_LP. Command specifying the type of measurement to be performed. See table below for details." },
    { type: 'uint8_t', name: 'pause', description: "Optional, time delay in milliseconds between issuing the command and reading data from the sensor." }
  ]}
/>

The available commands to send are as follows:

| Command Macro   | Value    | Description                                                                                                                    |
| --------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------ |
| `SHTC3_READ`    | `0x7CA2` | Initiates a temperature-first measurement with clock stretching enabled.                                                       |
| `SHTC3_READ_LP` | `0x6458` | Default, similar to `SHTC3_READ`, but after measuring, puts the SHTC3 in **low power mode**. Clock stretching remains enabled. |


---

## Measuring temperature

To measure the temperature, use the `readTempC()` function. The sensor samples temperature in degrees Celsius.

```cpp
void loop()
{
    shtcSensor.sample(); // Request new measurements

    Serial.print("Temp: ");
    Serial.println(shtcSensor.readTempC(), 2); // Read and print temperature

    delay(5000); // Wait 5 seconds before next reading
}
```

<FunctionDocumentation
  functionName="shtcSensor.readTempC()"
  description="Reads the current temperature from the SHTC3 sensor in degrees Celsius."
  returnDescription="Returns a float value representing the temperature in degrees Celsius."
  parameters={[]}
/>

---

## Measuring humidity

To measure humidity, use the `readHumidity()` function. The sensor provides humidity readings as a percentage.

```cpp title="Measuring humidity"
void loop()
{
    shtcSensor.sample(); // Request new measurements

    Serial.print("Hum: ");
    Serial.println(shtcSensor.readHumidity(), 2); // Read and print humidity

    delay(5000); // Wait 5 seconds before next reading
}
```

Below is the detailed function explanation:

<FunctionDocumentation
  functionName="shtcSensor.readHumidity()"
  description="Reads the current relative humidity from the SHTC3 sensor as a percentage."
  returnDescription="Returns a float value representing the relative humidity in percentage (%)."
  parameters={[]}
/>

---

## Full example

Try all of the above mentioned functions in this full example which prints out the measured temperature and humidity over Serial at 115200 baud:

```cpp
#include "SHTC3-SOLDERED.h"

SHTC3 shtcSensor;

void setup()
{
    shtcSensor.begin(); //Initialize sensor
    Serial.begin(115200); //Start serial communication with PC using 115200 baudrate
}

void loop()
{
    shtcSensor.sample(); //Initialize sensor

    // For temperature use function readTempC
    Serial.print("Temp: ");
    Serial.println(shtcSensor.readTempC(), 2); //Get temperature and print

    // For geting humidity use function readHumidity
    Serial.print("Hum: ");
    Serial.println(shtcSensor.readHumidity(), 2); //Get humidity and print

    delay(5000);
}
```
<QuickLink 
  title="TempAndHumidity.ino" 
  description="Example file for using SHTC3 sensor with easyC/Qwiic/I2C"
  url="https://github.com/SolderedElectronics/Soldered-SHTC3-Temperature-Humidity-Sensor-Arduino-Library/blob/main/examples/TempAndHumidity/TempAndHumidity.ino" 
/>
