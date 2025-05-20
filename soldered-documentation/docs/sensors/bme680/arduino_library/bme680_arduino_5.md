---
slug: /bme680/arduino/initializing
title: Bme680 - Initializing
id: bme680-arduino-5
hide_title: false
---

## Connections for this example

<CenteredImage src="/img/bme680/connections.png" alt="Connections"  />

---

## Initialization

To use the BME680 sensor, first include the required library, create the sensor object, and initialize the sensor in the `setup()` function.

```cpp
//Include the library
#include <BME680-SOLDERED.h>

//Create an instance of the sensor
BME680 bme680;

void setup() {
  Serial.begin(9600);
  //Initialize an I2C connection with the sensor
  if (!bme680.begin())
  {
    Serial.println("Failed to initialize sensor! Check connection.");
  }
}
//...
```

<FunctionDocumentation
  functionName="bme680.begin()"
  description="Initializes the BME680 sensor, setting up communication over I2C and configuring oversampling values for each sensor"
  returnDescription="Boolean value. True if the sensor was successfully initialized, False otherwise"
  parameters={[]}
/>