---
slug: /vl53l1x-laser-sensor/micropython/interrupt
title: VL53L1X - Measure on Interrupt
id: sensor-micropython-interrupt
sidebar_label: Measure on Interrupt
hide_title: False
---

An example showing how to configure the sensor to initiate an interrupt when the measurement is within, outside, below or above a certain threshold. Useful because it lets the MCU react immediately to changes without constantly checking the sensor, saving power and improving efficiency.


## Interrupt Example

```python
from machine import I2C, Pin
from VL53L1X import VL53L1X
import time

# Global variable that checks if an interrupt was detected
detected = 0

# Function that executes when an interrupt happens
def my_interrupt_handler(pin):
    global detected
    # Set the variable to 1 if an interrupt was triggered
    detected = 1

# Initialize the sensor and define the interrupt pin as well as the handler function
# that will be called. The pin defined must be connected to the GPIO1 pin on the breakout board!
sensor = VL53L1X(interruptPin=34, interruptCallback=my_interrupt_handler)

# Set the threshold when the interrupt will be triggered in a range of millimeters
sensor.set_distance_threshold_interrupt(
    100, 300, window="out"
)  # Trigger when outside of 100–300mm

# Infinite loop
while True:
    # The sensor itself starts taking continous measurements, must be called when using interrupts
    sensor.start_ranging()
    # If the 'detected' variable was set to 1
    if detected:
        dist = sensor.read()  # Save the sensor measurement into a variable
        print("Object outside of range window!")
        print("Distance:", dist, "mm")  # Print out the distance to the console

        detected = 0  # reset the detection variable
```

<FunctionDocumentation
  functionName="sensor.set_distance_threshold_interrupt()"
  description="Configure distance threshold interrupt window. Based on measured range and specified threshold trigger an interrupt."
  parameters={[
    { name: "low_mm", type: "int", description: "Lower threshold." },
    { name: "high_mm", type: "int", description: "Upper threshold." },
    { name: "window", type: "string", description: "Parameter to specify when to trigger an interrupt. " }
  ]}
/>

| Value | Description |
|:-------:|:---------------------------------------------------------------:|
| In | Will be triggered if the range is within the threshold specified     |
| Out | Will be triggered if the range is outside the threshold specified   |
| Above | Triggered if the measurement is above the upper defined threshold |
| Below | Triggered if the measurement is below the lower defined threshold |

<FunctionDocumentation
  functionName="sensor.start_ranging()"
  description="Start continuous ranging mode."
  returnType="None"
/>

<QuickLink  
  title="MeasureOnInterrupt.py"  
  description="Measure on interrupt full example on GitHub"  
  url="https://github.com/SolderedElectronics/Soldered-MicroPython-Modules/blob/main/Sensors/LaserDistanceSensor/LaserDistanceSensor/Examples/LaserDistanceSensor-MeasureOnInterrupt.py"  
/>