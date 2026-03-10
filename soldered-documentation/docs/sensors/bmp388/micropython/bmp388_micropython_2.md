---
slug: /bmp388/micropython/continuous-measurement
title: BMP388 Pressure & Temperature Sensor -  Continuous measurement
sidebar_label: Basic continuous measurements
id: bmp388-micropython-2 
hide_title: False
---

This page contains a simple example showing how to take continuous measurements with the BMP388 and printing it to the REPL.

---

## Connections for this example

<CenteredImage src="/img/bmp388/connections.jpg" alt="Connections"  />

---

## Initialization

To use the BMP388 sensor, first include the required module, create the sensor object, and initialize the sensor in the `setup()` function, along with setting its calibration parameters
```python
from machine import Pin, I2C
from bmp388 import BMP388
from bmp388_constants import TIME_STANDBY_1280MS
import time

# If you aren't using the Qwiic connector, manually enter your I2C pins
# i2c = I2C(0, scl=Pin(22), sda=Pin(21))
# bmp388 = BMP388(i2c)

# Initialize sensor over Qwiic
bmp388 = BMP388()

# Set sea level pressure for accurate altitude readings
bmp388.setSeaLevelPressure(1025.0)

# Set standby time to roughly 1.3 seconds
bmp388.setTimeStandby(TIME_STANDBY_1280MS)

# Start continuous measurement in normal mode
bmp388.startNormalConversion()

```

<FunctionDocumentation
  functionName="bmp388.BMP388()"
  description="Initializes the BMP388 sensor, setting up communication over I2C"
  returnDescription="1 if initialization was successfull, 0 if not"
  parameters={[]}
/>

<FunctionDocumentation
  functionName="bmp388.setSeaLevelPressure(float pressure)"
  description="Sets the sea level value of pressure, used in calculating altitude"
  returnDescription="None"
  parameters={[
  { type: 'float', name: 'pressure', description: "Pressure value in hPa" },
  ]}
/>

<FunctionDocumentation
  functionName="bmp388.setTimeStandby(enum TimeStandby standby)"
  description="Set the standby time of each sample"
  returnDescription="None"
  parameters={[
  { type: 'enum TimeStandby', name: 'standby', description: "Time the sensor will be asleep between each measurement" },
  ]}
/>

<FunctionDocumentation
  functionName="bmp388.startNormalConversion()"
  description="Start BMP388 continuous conversion in normal mode."
  returnDescription="None"
  parameters={[]}
/>

## Getting all readings

In an infinite loop, we get measurements from the sensor and print them out to the REPL:

```cpp
while True:
    temperature, pressure, altitude = bmp388.getMeasurements()
    if temperature is not None:
        print("{:.2f}*C   {:.2f}hPa   {:.2f}m".format(temperature, pressure, altitude))
    time.sleep(0.25)
```

<FunctionDocumentation
  functionName="bmp388.getMeasurements();"
  description="Gets measurements from the sensor if the sensor is ready to do so"
  returnDescription="Returns a tuple of the temperature (in degrees celsius), pressure (in hPa) and altitude (in meters)"
  parameters={[]}
/>

<CenteredImage src="/img/bmp388/repl.png" alt="REPL readings" caption="REPL output" width="100%" />

---

## Full Example
You can find the full example below:

```cpp
// Include Soldered BMP388 library.
#include <BMP388-SOLDERED.h>

// Create BMP388 sensor object.
Soldered_BMP388 bmp388;

void setup()
{
    // Initialize serial communication at 115200 bauds.
    Serial.begin(115200);

    // Initialize sensor (check for sensor). Notify if init failed.
    // Also, this will set BMP388 sensor into sleep mode.
    if (!bmp388.begin())
    {
        // Print error message.
        Serial.println("Sensor not found! Check your wiring!");

        // Stop the code!
        while (1)
        {
            // Delay for ESP8266.
            delay(10);
        }
    }

    // Set current pressure at sea level to get accurate altitude readings.
    bmp388.setSeaLevelPressure(1025.0);

    // Set the standby time of each sample to be roughly 1.3 seconds.
    bmp388.setTimeStandby(TIME_STANDBY_1280MS);

    // Start BMP388 continuous conversion in normal mode.
    bmp388.startNormalConversion();
}

void loop()
{
    // Variables for storing measurement data.
    float temperature, pressure, altitude;

    // Check if the data is ready.
    if (bmp388.getMeasurements(temperature, pressure, altitude))
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

