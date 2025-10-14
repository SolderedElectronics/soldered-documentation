---
slug: /vl53l1x-laser-sensor/micropython/read-distance
title: VL53L1X - Read Distance
id: sensor-micropython-read-continuous
sidebar_label: Read Distance
hide_title: False
---

## Initialization

To start using VL53L1X sensor, first import the required sensor library and other libraries for communication and timing. After importing, initialize the sensor by creating a sensor object.

## Read Continuous Distance Example

```python
from machine import I2C, Pin
from VL53L1X import VL53L1X
import time

# Initialize the sensor
sensor = VL53L1X()

# If you aren't using the Qwiic connector, manually enter your I2C pins
# i2c = I2C(0, scl=Pin(22), sda=Pin(21))
# sensor = VL53L1X(i2c)

# Infinite loop
while True:
    # Print out the distance measurement for the sensor in millimeters
    print("range: ", sensor.read(), "mm")
    # Pause for 50 milliseconds
    time.sleep_ms(50)
```

<FunctionDocumentation
  functionName="sensor.read()"
  description="Read the current measured distance."
  returnType="int"
  returnDescription="Returns distance from objects in millimeters."
/>

<QuickLink 
  title="ContinuousMeasurement.py"
  description="Read continuous measurement example on GitHub"
  url="https://github.com/SolderedElectronics/Soldered-MicroPython-Modules/blob/main/Sensors/LaserDistanceSensor/LaserDistanceSensor/Examples/LaserDistanceSensor-ContinousMeasurement.py"
/>