---
slug: /vl53l1x-laser-sensor/micropython/detailed-measurement
title: VL53L1X - Detailed Measurement
id: sensor-micropython-detailed
sidebar_label: Detailed Measurement
hide_title: False
---

Example showing how to get detailed info about each measurement.

## Code Example

```python
from machine import I2C, Pin
from VL53L1X import VL53L1X
import time

# Initialize the sensor
sensor = VL53L1X()

# Infinite loop
while True:
    # Recieve all the data in the form of a tuple and save it to local variables
    range_mm, status, peakSignal, ambient = sensor.readDetailed()
    print(
        "range: ",
        range_mm,
        "mm",
        "\t status:",
        status,
        "\t peak signal:",
        peakSignal,
        "MCPS \t ambient: ",
        ambient,
        "MCPS",
    )
    # Pause for 50 milliseconds
    time.sleep_ms(50)
``` 

<FunctionDocumentation
  functionName="sensor.readDetailed()"
  description="Read detailed measurement data from sensor"
  returnType="tuple"
  returnDescription="Returns range, status, peak_signal_rate (Mcps), ambient_light_rate (Mcps)."
/>

<QuickLink  
  title="DetailedMeasurement.py"  
  description="Detailed measured example on GitHub"  
  url="https://github.com/SolderedElectronics/Soldered-MicroPython-Modules/blob/main/Sensors/LaserDistanceSensor/LaserDistanceSensor/Examples/LaserDistanceSensor-DetailedMeasurement.py"  
/>