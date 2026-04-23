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
from inkplate6FLICK import Inkplate
import time

# Create Inkplate object in 1-bit (black and white) mode
display = Inkplate(Inkplate.INKPLATE_1BIT)

# Initialize the display
display.begin()

# Clear display buffer and refresh once
display.clearDisplay()
display.display()

# Enable the frontlight
display.frontlight(True)
display.display()

# Set frontlight brightness (0–64)
display.setFrontlight(0)

# Gradually increase brightness
for i in range(0, 64):
    display.setFrontlight(i)
    time.sleep(0.5)

# Gradually decrease brightness
for v in range(0, 64):
    display.setFrontlight(60 - v)
    time.sleep(0.5)

# Turn off the frontlight
display.frontlight(False)
```

<FunctionDocumentation
functionName="display.frontlight(state)"
description="Enable or disable the frontlight on the Inkplate board."
parameters={[
  { type: 'bool', name: 'state', description: 'Pass True to turn on the frontlight, or False to turn it off.' }
]}
/>

<FunctionDocumentation
functionName="display.setFrontlight(level)"
description="Set the frontlight brightness level."
parameters={[
  { type: 'int', name: 'level', description: 'Brightness value between 0 (off) and 64 (maximum brightness).' }
]}
/>

<CenteredImage src="/img/inkplate6flick-micropython/frontlight.jpg" alt="Inkplate 6flick running the example code" caption="Displaying battery and temperature data on Inkplate display." width="1000px" />