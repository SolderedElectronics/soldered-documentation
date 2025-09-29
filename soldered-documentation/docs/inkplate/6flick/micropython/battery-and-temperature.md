---
slug: /inkplate/6flick/micropython/battery-temperature
title: Inkplate 6FLICK MicroPython - Battery and temperature
sidebar_label: Battery and temperature
id: battery-temperature
---

Inkplate 6FLICK includes built-in functions for measuring **battery voltage** and **board temperature**. This example shows how to read these values and display them on screen.

<WarningBox>You need a Li-ion battery for this example to work, to learn more, check out [**battery docs page**](/documentation/inkplate/6flick/hardware/battery/). </WarningBox>

Battery should be connected like this:
<CenteredImage src="/img/inkplate6flick-micropython/batt-connection.jpg" alt="Inkplate 6flick running the example code" caption="Battery connected to Inkplate 6FLICK." width="1000px" />
---

## Reading battery voltage and temperature

```python
from inkplate6FLICK import Inkplate
import time

inkplate = Inkplate(Inkplate.INKPLATE_1BIT)
inkplate.begin()
inkplate.clearDisplay()
inkplate.display()

# Get battery voltage as a string
battery = str(inkplate.readBattery())
inkplate.setTextSize(2)
inkplate.printText(100,100, "Battery voltage: " + battery + "V")
inkplate.partialUpdate()

# Get temperature reading as a string
temperature = str(inkplate.readTemperature())
inkplate.printText(100,150, "Temperature: " + temperature + "C")
inkplate.partialUpdate()
```

<FunctionDocumentation 
functionName="inkplate.readBattery()" 
description="Measure the current battery voltage of the Inkplate board." 
returnType="float" 
returnDescription="Battery voltage in volts." />

<FunctionDocumentation 
functionName="inkplate.readTemperature()" 
description="Measure the temperature of the Inkplate board’s internal sensor." 
returnType="float" 
returnDescription="Temperature in degrees Celsius." />

<CenteredImage src="/img/inkplate6flick-micropython/battery-volt-temp.jpg" alt="Inkplate 6flick running the example code" caption="Displaying battery and temperature data on Inkplate display." width="1000px" />