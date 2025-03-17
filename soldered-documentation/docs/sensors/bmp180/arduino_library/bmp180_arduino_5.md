---
slug: /bmp180/arduino/examples3
title: Measuring pressure
id: bmp180-arduino-5
hide_title: False
---

To get pressure values, first you must begin a reading using the `startPressure()` function, then after a short delay get the value of that reading using the `getPressure()` function.

```cpp
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