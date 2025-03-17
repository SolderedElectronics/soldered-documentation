---
slug: /bmp180/arduino/examples 
title: Initialization
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

