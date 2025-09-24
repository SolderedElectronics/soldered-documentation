---
slug: /inkplate_micropython/inkplate10/hardware/battery-and-temperature
title: Inkplate 10 MicroPython - Battery & Temperature Reading
id: battery-and-temperature
---

Inkplate 10 allows you to easily read the **battery voltage** and **temperature sensor** values.  
This is useful for monitoring device health, power status, or building applications that need basic environmental data.

<InfoBox>  
The battery voltage is returned in **Volts**, and the onboard temperature sensor reading is returned in **Celsius**.  
</InfoBox>


<CenteredImage src="/img/inkplate10-micropython/battery-volt-temp.jpg" alt="Inkplate 10 running the example code" caption="Inkplate 10 running the example code" width="800px" />

---

## Battery & Temperature Example

```python
from inkplate10 import Inkplate
import time

# Create Inkplate object in 1-bit mode, black & white
inkplate = Inkplate(Inkplate.INKPLATE_1BIT)

# Initialize the display
inkplate.begin()
inkplate.clearDisplay()
inkplate.display()

# Get battery reading
battery = str(inkplate.readBattery())

inkplate.setTextSize(2)
inkplate.printText(350, 350, "Battery voltage: " + battery + "V")
inkplate.partialUpdate()

# Get temperature reading
temperature = str(inkplate.readTemperature())
inkplate.printText(350, 400, "Temperature: " + temperature + "C")
inkplate.partialUpdate()
```

<FunctionDocumentation 
functionName="inkplate.readBattery()" 
description="Read the current battery voltage." 
returnDescription="Float value representing battery voltage in Volts." 
parameters={[]} />

<FunctionDocumentation 
functionName="inkplate.readTemperature()" 
description="Read the onboard temperature sensor." 
returnDescription="Float value representing temperature in degrees Celsius." 
parameters={[]} />

<FunctionDocumentation
functionName="inkplate.printText(x, y, text)"
description="Print a text string at a specific position without changing the cursor state."
returnDescription="Nothing"
parameters={[
{ type: 'Number', name: 'x', description: 'X coordinate for the text start.' },
{ type: 'Number', name: 'y', description: 'Y coordinate for the text baseline.' },
{ type: 'String', name: 'text', description: 'The string to render.' }
]}
/>