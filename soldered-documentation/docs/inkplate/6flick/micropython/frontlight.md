---
slug: /inkplate/6flick/micropython/frontlight
title: Inkplate 6FLICK MicroPython - Frontlight
sidebar_label: Frontlight
id: frontlight
---

Inkplate 6FLICK includes a **built-in frontlight** that can be enabled, disabled, and adjusted in brightness. This example shows how to control the frontlight programmatically.

<WarningBox>Excessive use of maximum brightness can reduce battery life. Adjust brightness based on your application needs.</WarningBox>

---

## Controlling the frontlight

```python
# Include required libraries
from inkplate6_flick import Inkplate
import time

# Create Inkplate object in 1-bit (black and white) mode
display = Inkplate(Inkplate.INKPLATE_1BIT)

# Initialize the display, needs to be called only once
display.begin()

# Enable the frontlight
display.set_frontlight(True)

# Frontlight brightness can be set from 0 (dimmest) to 63 (brightest)
display.set_frontlight_brightness(0)

# Gradually increase the brightness, then decrease it back down
for i in range(0, 64):
    display.set_frontlight_brightness(i)
    time.sleep(0.05)
for i in range(63, -1, -1):
    display.set_frontlight_brightness(i)
    time.sleep(0.05)

# Turn the frontlight off
display.set_frontlight(False)
```

<FunctionDocumentation
functionName="display.frontlight(state)"
description="Enable or disable the frontlight on the Inkplate board."
parameters={[
  { type: 'bool', name: 'state', description: 'Pass True to turn on the frontlight, or False to turn it off.' }
]}
/>

<FunctionDocumentation
functionName="display.set_frontlight(level)"
description="Set the frontlight brightness level."
parameters={[
  { type: 'int', name: 'level', description: 'Brightness value between 0 (off) and 64 (maximum brightness).' }
]}
/>

<CenteredImage src="/img/inkplate6flick-micropython/frontlight.jpg" alt="Inkplate 6FLICK running the example code" caption="Displaying battery and temperature data on Inkplate display." width="1000px" />

---

## Full example

<QuickLink title="frontlight.py" 
description="Turn on the frontlight and ramp its brightness up and down." 
url="https://github.com/SolderedElectronics/Inkplate-micropython/blob/master/examples/inkplate6flick/frontlight.py" />
