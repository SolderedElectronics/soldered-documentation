---
slug: /bmp388/micropython/continuous-measurement-with-fifo
title: BMP388 Pressure & Temperature Sensor -  Continuous measurement using FIFO
sidebar_label: Continuous measurement using FIFO
id: bmp388-micropython-4 
hide_title: False
---

In this example we will be showing how to use the built-in FIFO buffer on the BMP388 sensor to store measurements and print them out when needed.

## Setting Up

Initialization is done in a similar way as in the previous examples, with the main difference being that we initialize the FIFO with a set number of measurements which will be saved into the FIFO:

```python
from machine import Pin, I2C
from bmp388 import BMP388
from bmp388_constants import TIME_STANDBY_1280MS, FIFO_DATA_READY, FIFO_CONFIG_ERROR
import time

NO_OF_MEASUREMENTS = 10

# If you aren't using the Qwiic connector, manually enter your I2C pins
# i2c = I2C(0, scl=Pin(22), sda=Pin(21))
# bmp388 = BMP388(i2c)

# Initialize sensor over Qwiic
bmp388 = BMP388()

# Set sea level pressure for accurate altitude readings
bmp388.setSeaLevelPressure(1025.0)

# Set standby time to roughly 1.3 seconds
bmp388.setTimeStandby(TIME_STANDBY_1280MS)

# Enable FIFO and set watermark
bmp388.enableFIFO()
bmp388.setFIFONoOfMeasurements(NO_OF_MEASUREMENTS)
```

<FunctionDocumentation
  functionName="bmp388.enableFIFO()"
  description="Enables the FIFO functionalities of the sensor"
  returnDescription="None"
  parameters={[]}
/>

<FunctionDocumentation
  functionName="bmp388.setFIFONoOfMeasurements(noOfMeasurements)"
  description="Sets how many measurements will be saved into the FIFO buffer"
  returnDescription="None"
  parameters={[
  { type: 'int', name: 'noOfMeasurements', description: "Number if measurement samples which will be saved into the FIFO buffer" },
  ]}
/>

## Taking measurements

Next, in an infinite loop, we wait until the FIFO buffer is full, then we print out the measured values:

```python
# Start continuous measurement in normal mode
bmp388.startNormalConversion()

print("Please wait for 13 seconds...")

while True:
    status, temperatures, pressures, altitudes, sensorTime = bmp388.getFIFOData()

    if status == FIFO_DATA_READY:
        for i in range(len(temperatures)):
            altitude = altitudes[i] if i < len(altitudes) else 0.0
            print(
                "{}: {:.2f}*C   {:.2f}hPa   {:.2f}m".format(
                    i + 1, temperatures[i], pressures[i], altitude
                )
            )

        print("Sensor Time: {} ms".format(sensorTime))
        print()
        print("Please wait for 13 seconds...")
    elif status == FIFO_CONFIG_ERROR:
        print("FIFO configuration error.")

    time.sleep(0.05)
```

<CenteredImage src="/img/bmp388/repl2.png" alt="REPL readings" caption="REPL output" width="100%" />

---

## Full Example
You can find the full example below:

```python
from machine import Pin, I2C
from bmp388 import BMP388
from bmp388_constants import TIME_STANDBY_1280MS, FIFO_DATA_READY, FIFO_CONFIG_ERROR
import time

NO_OF_MEASUREMENTS = 10

# If you aren't using the Qwiic connector, manually enter your I2C pins
# i2c = I2C(0, scl=Pin(22), sda=Pin(21))
# bmp388 = BMP388(i2c)

# Initialize sensor over Qwiic
bmp388 = BMP388()

# Set sea level pressure for accurate altitude readings
bmp388.setSeaLevelPressure(1025.0)

# Set standby time to roughly 1.3 seconds
bmp388.setTimeStandby(TIME_STANDBY_1280MS)

# Enable FIFO and set watermark
bmp388.enableFIFO()
bmp388.setFIFONoOfMeasurements(NO_OF_MEASUREMENTS)

# Start continuous measurement in normal mode
bmp388.startNormalConversion()

print("Please wait for 13 seconds...")

while True:
    status, temperatures, pressures, altitudes, sensorTime = bmp388.getFIFOData()

    if status == FIFO_DATA_READY:
        for i in range(len(temperatures)):
            altitude = altitudes[i] if i < len(altitudes) else 0.0
            print(
                "{}: {:.2f}*C   {:.2f}hPa   {:.2f}m".format(
                    i + 1, temperatures[i], pressures[i], altitude
                )
            )

        print("Sensor Time: {} ms".format(sensorTime))
        print()
        print("Please wait for 13 seconds...")
    elif status == FIFO_CONFIG_ERROR:
        print("FIFO configuration error.")

    time.sleep(0.05)
```