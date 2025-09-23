---  
slug: /inkplate/6color/micropython/read-battery
title: Inkplate 6COLOR – Read Battery Voltage
sidebar_label: Read Battery Voltage
id: read-battery
hide_title: true
---

<SectionTitle title="Read Battery Voltage" backgroundImage="/img/deepsleep.jpg" />

When running your Inkplate 6COLOR board on a Li-ion battery, it's helpful to know the battery's condition. Inkplate 6COLOR lets you measure the battery voltage directly, giving you an estimate of remaining capacity and help you decide if it's time to recharge.

<WarningBox>Connecting and using the battery correctly is important! Please refer to the battery usage page for guidance before use. </WarningBox>

## Reading battery voltage

```python
from inkplate6COLOR import Inkplate

# Create Inkplate object
inkplate = Inkplate()

# Initialize the display
inkplate.begin()

# Get battery voltage
bat_capacity = inkplate.readBattery()

# Print current battery voltage
inkplate.print(f"Battery capacity: {bat_capacity:.2f} V")

# Update the display
inkplate.display()
```

<FunctionDocumentation
  functionName="inkplate.readBattery()"
  description="Reads the current battery voltage when running on battery power"
  returnType="float"
  returnDescription="Returns the measured battery voltage"
/>
