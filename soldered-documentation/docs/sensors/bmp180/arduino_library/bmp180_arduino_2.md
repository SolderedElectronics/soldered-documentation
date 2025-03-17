---
slug: /bmp180/arduino/examples 
title: Measuring temperature and humidity (examples)
id: bmp180-arduino-2 
hide_title: False
---

This page contains some simple examples with function documentation on how to take measurements using the BMP180 temperature and pressure sensor.

---

## Initialization

To use the BMP180 sensor, first, include the required library, create the sensor object and initialize the sensor in the `setup()` function.

```cpp
//Include the library
#include <BMP180-SOLDERED.h>

//Create an instance of the sensor
Bmp_180 bmp180;

void setup() {
  //Initialize communication to serial monitor
  Serial.begin(9600);

  //Initialize the sensor
  if(bmp180.begin())
  {
    //If sensor returns 1, then it has succesfully initialized
    Serial.println("BMP180 sensor successfully initialized!");
  }
  else
  {
    //If not, inform the user
    Serial.println("BMP180 sensor failed to initialize, check connection.");
  }

}
```

<FunctionDocumentation
  functionName="bmp180.begin()"
  description="Initializes the BMP180 sensor, setting up communication over I2C and retrieving calibration data from device"
  returnDescription="Char value, returns 1 if sensor was properly initialized, 0 if not. (While the type being char seems unintuitive when it returns 1 or 0, the char datatype is basically an 8-bit unsigned integer)"
  parameters={[]}
/>

---

## Getting measurements

## Temperature

To get temperature values, first you must begin a reading using the `startTemperature()` function, then after a short delay get the value of that reading using the `getTemperature()` function.

```cpp
void loop() {
  double temperature;
  //Start temperature reading
  char return_value=bmp180.startTemperature();
  //If the return value is 0, then the measurement failed
  if(return_value==0)
  {
    Serial.println("Failed to get temperature reading from BMP180!");
  }
  else
  {
    /*If it succeeded, take a small delay equal to the return value
      of the startTemperature() function before getting value*/
    delay(return_value);
    //Store the read value into temperature variable
    bmp180.getTemperature(temperature);
    Serial.println("Temperature: "+String(temperature)+" C");
  }
  //Take a measurement every 5s
  delay(5000);

}
```

<CenteredImage src="/img/bmp180/bmp180_temperature.png" alt="Serial monitor temperature readings" caption="Serial monitor" width="100%" />

<FunctionDocumentation
  functionName="bmp180.startTemperature()"
  description="Begins a temperature reading"
  returnDescription="Char value, returns 5 if the temperature was successfully read, which should be used as a delay value in ms before getting the measurement, and a 0 if there was a problem communicating with the sensor"
  parameters={[]}
/>

<FunctionDocumentation
  functionName="bmp180.getTemperature(double &T)"
  description="Retrieves a previously started temperature reading"
  returnDescription="Char value, returns 1 if the retrieval of data was successful, 0 if not"
  parameters={[
  { type: 'double', name: 'T', description: "Variable in which the temperature measurement will be stored" },
  ]}
/>

## Pressure

To get pressure values, first you must begin a reading using the `startPressure()` function, then after a short delay get the value of that reading using the `getPressure()` function.

```cpp
//Include the library
#include <BMP180-SOLDERED.h>

//Create an instance of the sensor
Bmp_180 bmp180;

void setup() {
  //Initialize communication to serial monitor
  Serial.begin(9600);

  //Initialize the sensor
  if(bmp180.begin())
  {
    //If sensor returns true, then it ha succesfully initialized
    Serial.println("BMP180 sensor successfully initialized!");
  }
  else
  {
    //If not, inform the user
    Serial.println("BMP180 sensor failed to initialize, check connection.");
  }

}

void loop() {
  double temperature;
  double pressure;
  /*Defines how accurate the measurement will be, 0 for fast but not that accurate, 
    3 for most accurate but slowest*/
  char pressure_oversampling=0;
  //Start temperature reading
  char return_value_temperature=bmp180.startTemperature();
  //Start pressure reading
  char return_value_pressure=bmp180.startPressure(pressure_oversampling);
  //If the return value is 0, then the measurement failed
  if(return_value_temperature==0)
  {
    Serial.println("Failed to get temperature reading from BMP180!");
  }
  else
  {
    /*If it succeeded, take a small delay equal to the return value
      of the startTemperature() function before getting value*/
    delay(return_value_temperature);
    //Store the read value into temperature variable
    bmp180.getTemperature(temperature);
  }
  //If the return value is 0, then the measurement failed
  if(return_value_pressure==0)
  {
    Serial.println("Failed to get pressure reading from BMP180!");
  }
  else
  {
    /*If it succeeded, take a small delay equal to the return value
      of the startPressure() function before getting value*/
    delay(return_value_pressure);

    bmp180.getPressure(pressure, temperature);

    Serial.println("Pressure: "+String(pressure)+" mBar");

  }

  //Take a measurement every 2s
  delay(2000);
}
```
<CenteredImage src="/img/bmp180/bmp180_pressure.png" alt="Serial monitor pressure readings" caption="Serial monitor" width="100%" />

<FunctionDocumentation
  functionName="bmp180.startPressure(char oversampling)"
  description="Begins a pressure reading"
  returnDescription="Char value, returns a value different if the temperature was successfully read, which should be used as a delay value in ms before getting the measurement, and a 0 if there was a problem communicating with the sensor. The delay values are decided by the oversampling value"
  parameters={[
   { type: 'char', name: 'oversampling', description: "The degree of oversampling the sensor will take, ranges from 0 to 3, the bigger the number the bigger the oversampling and also with that the delay before reading the measurement" },
  ]}
/>

<FunctionDocumentation
  functionName="bmp180.getPressure(double &P, double &T)"
  description="Retrieves a previously started pressure reading in absolute mbars"
  returnDescription="Char value, returns 1 if the retrieval of data was successful, 0 if not"
  parameters={[
  { type: 'double', name: 'P', description: "Variable in which the pressure measurement will be stored" },
  { type: 'double', name: 'T', description: "Previously calculated temperature reading" },

  ]}
/>

<WarningBox>Note that calculated pressure value is absolute mbars, to compensate for altitude call sealevel() function: </WarningBox>

```cpp
    bmp180.getPressure(pressure, temperature);
    //Altitude of our office in Osijek :)
    double altitude = 94;
    //Getting the relative pressure by taking the last pressure measurement and altitude
    double relative_pressure = bmp180.sealevel(pressure, altitude);

    Serial.println("Relative pressure: " + String(relative_pressure)+ " mBar");
```

<CenteredImage src="/img/bmp180/bmp180_relative.png" alt="Serial monitor relative pressure readings" caption="Serial monitor" width="100%" />

<FunctionDocumentation
  functionName="bmp180.sealevel(double P, double A)"
  description="Gives relative pressure depending on the absolute pressure and current altitude"
  returnDescription="Double value, the relative pressure in mbar"
  parameters={[
  { type: 'double', name: 'P', description: "Absolute pressure value in mbars" },
  { type: 'double', name: 'A', description: "Current altitude in meters" },

  ]}
/>

## Altitude

Altitude can be calculated by taking a pressure measurement and knowing the pressure at baseline and putting them in the `altitude()` function

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