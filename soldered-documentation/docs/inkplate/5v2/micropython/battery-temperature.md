---
slug: /inkplate/5v2/micropython/battery-temperature
title: Inkplate 5v2 MicroPython - Battery and temperature
sidebar_label: Battery and temperature
id: battery-temperature
---

Inkplate 5v2 has built-in functions for measuring battery voltage and board temperature. This example reads both values and shows them on screen.

<WarningBox>You need a Li-ion battery for this example to work. For more details, see the [battery docs page](/inkplate/5v2/hardware/battery/). </WarningBox>

Connect the battery like this:
<CenteredImage src="/img/inkplate5v2-micropython/batt-connection.jpg" alt="Inkplate 5v2 running the example code" caption="Battery connected to Inkplate 5v2." width="1000px" />
---

## Reading battery voltage and temperature

```python
from inkplate5v2 import Inkplate

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

<CenteredImage src="/img/inkplate5v2-micropython/battery-volt-temp.jpg" alt="Inkplate 5v2 running the example code" caption="Displaying battery and temperature data on Inkplate display." width="1000px" />

---

## Full example

<QuickLink title="battery_and_temperature.py" 
description="Read the battery voltage and temperature and display them on the screen." 
url="https://github.com/SolderedElectronics/Inkplate-micropython/blob/master/examples/inkplate5v2/battery_and_temperature.py" />
