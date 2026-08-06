---
slug: /inkplate/6flick/micropython/battery-temperature
title: Inkplate 6FLICK MicroPython - Battery and temperature
sidebar_label: Battery and temperature
id: battery-temperature
---

Inkplate 6FLICK includes built-in functions for measuring **battery voltage** and **board temperature**. This example shows how to read these values and display them on screen.

<WarningBox>You need a Li-ion battery for this example to work, to learn more, check out [**battery docs page**](/inkplate/6flick/hardware/battery/). </WarningBox>

Battery should be connected like this:
<CenteredImage src="/img/inkplate6flick-micropython/batt-connection.jpg" alt="Inkplate 6FLICK running the example code" caption="Battery connected to Inkplate 6FLICK." width="1000px" />
---

## Reading battery voltage and temperature

```python
# Include needed libraries
from inkplate6_flick import Inkplate

# Create Inkplate object in 1-bit mode, black and white colors only
# For 8-level grayscale, see basic_grayscale.py
inkplate = Inkplate(Inkplate.INKPLATE_1BIT)

# Initialize the display, needs to be called only once
inkplate.begin()

# Clear the frame buffer
inkplate.clear_display()

# This has to be called every time you want to update the screen
# Drawing or printing text will have no effect on the display itself before you call this function
inkplate.display()

# Get the battery reading as a string
battery = str(inkplate.read_battery())

# Set text size to double from the original size, so we can see the text better
inkplate.set_text_size(2)

# Print the text at coordinates 100,100 (from the upper left corner)
inkplate.print_text(100, 100, "Battery voltage: " + battery + "V")

# Show it on the display
inkplate.partial_update()

# Get the temperature reading, also as a string
temperature = str(inkplate.read_temperature())

# Print the text at coordinates 100, 150, and also add the measurement unit
inkplate.print_text(100, 150, "Temperature: " + temperature + "C")

# Show it on the display
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

<CenteredImage src="/img/inkplate6flick-micropython/battery-volt-temp.jpg" alt="Inkplate 6FLICK running the example code" caption="Displaying battery and temperature data on Inkplate display." width="1000px" />