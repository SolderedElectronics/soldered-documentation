---
slug: /mq/arduino/initialization-qwiic 
title: Initialization (Qwiic)
id: mq-arduino-2 
hide_title: False
---

In this example, we will go over how to initialize the Qwiic version of the MQ sensor.

<CenteredImage src="/img/mq/connections1.png" caption="Connections for this example"/>

First, we have to include the library, specify the number of readings the sensor will take during the calibration procedure, and create an instance of the MQ sensor object:

```cpp
// Include the library
#include <MQ-Sensor-SOLDERED.h>

// How many R0 readings to take to get an average measurement
#define numOfCalibrations 10 

// Create an instance of the sensor object
MQ8 mq8;
```

Next, in the `setup()` function, we are initializing the serial communication as well as the sensor.

```cpp
// Initialize the serial port communication at 115200 baud. It's used to print measured data.
Serial.begin(115200);

// Initialize I2C connection with the sensor; if it fails, inform the user
if(!mq8.begin(0x30))
{
    Serial.println("Failed to initialize I2C communication, check wiring");
    while(1)
    {}
}
```

<FunctionDocumentation
  functionName="mq8.begin(int _addr)"
  description="Initializes the MQ sensor, setting up communication over I2C and configuring its regression method."
  returnDescription="Boolean value; returns true if the sensor was successfully initialized, false otherwise."
  parameters={[{ type: 'int', name: '_addr', description: "Specifies the I2C address of the sensor" }]}
/>

Next, we have to calibrate the sensor. Calibration is done in a clean air environment after the sensor has been heated. You can find preheat times for the sensor in their datasheets, which are linked [**here**](../hardware#datasheets). All the calibration does is take measurements of the resistance, which will be used later for resistance measurements in an environment with the specific gas calculated.

```cpp
// In the setup() function...

/*****************************  MQ Calibration ********************************************/
// Explanation:
// In this routine, the sensor will measure its resistance after it has been pre-heated for 48h
// and is now in a clean air environment, and it will set up the R0 value.
// This routine does not need to be executed on every restart; you can load your R0 into flash memory and read it on startup

Serial.print("Calibrating please wait.");
bool calibrationResult = mq8.calibrateSensor(numOfCalibrations);
if(!calibrationResult) // Check if the sensor was properly calibrated
{
  Serial.println("There was an error reading the sensor, check connection and try again");
  while(1)
  {}
}
Serial.print("Calibration done!");

/*****************************  MQ Calibration ********************************************/
```

<FunctionDocumentation
  functionName="mq8.calibrateSensor(int numOfCalibrations)"
  description="Calibrates the sensor by taking multiple readings and averaging them."
  returnDescription="Boolean value; true if calibration is successful, false if the calculated R0 is invalid."
  parameters={[{ type: 'int', name: 'numOfCalibrations', description: "Number of calibration readings to take" }]}
/>

## Full example 

See the full example below:

```cpp
// Include the library
#include <MQ-Sensor-SOLDERED.h>

// How many R0 readings to take to get an average measurement
#define numOfCalibrations 10 

// Create an instance of the sensor object
MQ8 mq8;

void setup()
{
    // Initialize the serial port communication at 115200 baud. It's used to print measured data.
    Serial.begin(115200);

    // Initialize I2C connection with the sensor; if it fails, inform the user
    if(!mq8.begin(0x30))
    {
      Serial.println("Failed to initialize I2C communication, check wiring");
      while(1)
      {}
    }

    /*****************************  MQ Calibration ********************************************/
    // Explanation:
    // In this routine, the sensor will measure its resistance after it has been pre-heated for 48h
    // and is now in a clean air environment, and it will set up the R0 value.
    // This routine does not need to be executed on every restart; you can load your R0 into flash memory and read it on startup
    
    Serial.print("Calibrating please wait.");
    bool calibrationResult = mq8.calibrateSensor(numOfCalibrations);
    if(!calibrationResult) // Check if the sensor was properly calibrated
    {
      Serial.println("There was an error reading the sensor, check connection and try again");
      while(1)
      {}
    }
    Serial.print("Calibration done!");

    /*****************************  MQ Calibration ********************************************/
}

void loop()
{
  
}
```