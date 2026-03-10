---
slug: /bmp388/micropython/continuous-measurement-via-interrupt
title: BMP388 Pressure & Temperature Sensor -  Continuous measurement via Interrupt
sidebar_label: Continuous measurement via Interrupt
id: bmp388-micropython-3 
hide_title: False
---

In this example we will be configuring the sensor to take continuous measurements every time set by the interval, and notify the Microcontroller that data is available via the sensors onboard INT pin


## Setting up
Firstly, we include the module and initialize it (as was done in the previous example). Next, we set up the Interrupt handler function which will notify us when the data is ready via a boolean variable:

```python
from machine import Pin, I2C
from bmp388 import BMP388
from bmp388_constants import TIME_STANDBY_1280MS
import time

dataReady = False

def interruptHandler(pin):
    global dataReady
    dataReady = True
```
Next, we initialize the sensor, set up its configuration, attach the interrupt function to a rising impulse on GPIO2 and enable the interrupt functionalities of the BMP388 sensor:

```python
# If you aren't using the Qwiic connector, manually enter your I2C pins
# i2c = I2C(0, scl=Pin(22), sda=Pin(21))
# bmp388 = BMP388(i2c)

# Initialize sensor over Qwiic
bmp388 = BMP388()

# Set sea level pressure for accurate altitude readings
bmp388.setSeaLevelPressure(1025.0)

# Set standby time to roughly 1.3 seconds
bmp388.setTimeStandby(TIME_STANDBY_1280MS)

# Enable data-ready interrupt
bmp388.enableInterrupt()

# Connect sensor INT pin to GPIO2 (adjust for your board)
intPin = Pin(2, Pin.IN, Pin.PULL_UP)
intPin.irq(trigger=Pin.IRQ_RISING, handler=interruptHandler)
```

---

## Taking Measurements
Next, in an infinite loop, we are checking the global dataReady variable, whihc is set to true when an interrupt is triggered. If the interrupt was triggered, then a measurement is taken and printed to the REPL:

```python
# Start continuous measurement in normal mode
bmp388.startNormalConversion()

while True:
    if dataReady:
        temperature, pressure, altitude = bmp388.getMeasurements()
        if temperature is not None:
            print(
                "{:.2f}*C   {:.2f}hPa   {:.2f}m".format(temperature, pressure, altitude)
            )
        dataReady = False
    time.sleep(0.01)
```

<CenteredImage src="/img/bmp388/repl2.png" alt="REPL readings" caption="REPL output" width="100%" />

---

## Full Example
You can find the full example below:

```python
from machine import Pin, I2C
from bmp388 import BMP388
from bmp388_constants import TIME_STANDBY_1280MS
import time

dataReady = False


def interruptHandler(pin):
    global dataReady
    dataReady = True


# If you aren't using the Qwiic connector, manually enter your I2C pins
# i2c = I2C(0, scl=Pin(22), sda=Pin(21))
# bmp388 = BMP388(i2c)

# Initialize sensor over Qwiic
bmp388 = BMP388()

# Set sea level pressure for accurate altitude readings
bmp388.setSeaLevelPressure(1025.0)

# Set standby time to roughly 1.3 seconds
bmp388.setTimeStandby(TIME_STANDBY_1280MS)

# Enable data-ready interrupt
bmp388.enableInterrupt()

# Connect sensor INT pin to GPIO2 (adjust for your board)
intPin = Pin(2, Pin.IN, Pin.PULL_UP)
intPin.irq(trigger=Pin.IRQ_RISING, handler=interruptHandler)

# Start continuous measurement in normal mode
bmp388.startNormalConversion()

while True:
    if dataReady:
        temperature, pressure, altitude = bmp388.getMeasurements()
        if temperature is not None:
            print(
                "{:.2f}*C   {:.2f}hPa   {:.2f}m".format(temperature, pressure, altitude)
            )
        dataReady = False
    time.sleep(0.01)
```
