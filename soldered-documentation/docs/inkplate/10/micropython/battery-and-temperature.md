---
slug: /inkplate/10/micropython/battery-temperature
title: Inkplate 10 MicroPython - Battery and temperature
sidebar_label: Battery and temperature
id: battery-temperature
---

Inkplate 10 includes built-in functions for measuring **battery voltage** and **board temperature**. This example shows how to read these values and display them on screen.

<WarningBox>You need a Li-ion battery for this example to work, to learn more, check out [**battery docs page**](/inkplate/10/hardware/battery/). </WarningBox>

Battery should be connected like this:
<CenteredImage src="/img/inkplate10-micropython/batt-connection.jpg" alt="Inkplate 10 running the example code" caption="Battery connected to Inkplate 10." width="1000px" />
---

## Reading battery voltage and temperature

```python
from inkplate10 import Inkplate
import time

inkplate = Inkplate(Inkplate.INKPLATE_1BIT)
inkplate.begin()
inkplate.clear_display()
inkplate.display()

# Get battery voltage as a string
battery = str(inkplate.read_battery())
inkplate.set_text_size(2)
inkplate.print_text(350, 350, "Battery voltage: " + battery + "V")
inkplate.partial_update()

# Get temperature reading as a string
temperature = str(inkplate.read_temperature())
inkplate.print_text(350, 400, "Temperature: " + temperature + "C")
inkplate.partial_update()
```

<FunctionDocumentation 
functionName="inkplate.read_battery()" 
description="Measure the current battery voltage of the Inkplate board." 
returnType="float" 
returnDescription="Battery voltage in volts." />

<FunctionDocumentation 
functionName="inkplate.read_temperature()" 
description="Measure the temperature of the Inkplate board's internal sensor." 
returnType="float" 
returnDescription="Temperature in degrees Celsius." />

<CenteredImage src="/img/inkplate10-micropython/battery-volt-temp.jpg" alt="Inkplate 10 running the example code" caption="Displaying battery and temperature data on Inkplate display." width="1000px" />