---  
slug: /inkplate/6color/micropython/read-battery
title: Inkplate 6COLOR – Read Battery Voltage
sidebar_label: Read Battery Voltage
id: read-battery
hide_title: true
---

<SectionTitle title="Read Battery Voltage" backgroundImage="/img/deepsleep.jpg" />

When running your Inkplate 6COLOR board on a Li-ion battery, it's helpful to know the battery's condition. Inkplate 6COLOR lets you measure the battery voltage directly, giving you an estimate of remaining capacity and help you decide if it's time to recharge.

<CenteredImage src="/img/6color/battery-connection.jpg" alt="Battery connection" caption="Battery connection" />

<WarningBox>Connecting and using the battery correctly is important! Please refer to the **Inkplate battery page** for detailed info. </WarningBox>

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

<CenteredImage src="/img/6color/read-battery-voltage.jpg" alt="Battery info" caption="Fully charged battery example" />

<InfoBox> Expected values are around 4.2V when full and 3.7V when empty. </InfoBox>

<FunctionDocumentation
  functionName="inkplate.readBattery()"
  description="Reads the current battery voltage when running on battery power"
  returnType="float"
  returnDescription="Returns the measured battery voltage"
/>
