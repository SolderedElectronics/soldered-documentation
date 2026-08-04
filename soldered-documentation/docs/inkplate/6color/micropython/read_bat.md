---  
slug: /inkplate/6color/micropython/read-battery
title: Inkplate 6COLOR – Read Battery Voltage
sidebar_label: Read Battery Voltage
id: read-battery
hide_title: true
---

<SectionTitle title="Read Battery Voltage" />

When running your Inkplate 6COLOR board on a Li-ion battery, it's helpful to know the battery's condition. Inkplate 6COLOR lets you measure the battery voltage directly, giving you an estimate of remaining capacity and help you decide if it's time to recharge.

<CenteredImage src="/img/6color/battery-connection.jpg" alt="Battery connection" caption="Battery connection" />

<WarningBox>Connecting and using the battery correctly is important! Please refer to the <a href="/inkplate/6color/hardware/battery">battery usage page</a> for guidance before use.</WarningBox>

## Reading battery voltage

```python
# Include needed libraries
from inkplate6_color import Inkplate

# Creates an Inkplate object
inkplate = Inkplate()

# Initialize the display, needs to be called only once
inkplate.begin()

# Clear the frame buffer
inkplate.clear_display()

# Get the battery reading as a string
battery = str(inkplate.read_battery())

# Keep the text at its original size
inkplate.set_text_size(1)

# Print the text at coordinates 150,190 (from the upper left corner)
inkplate.print_text(150, 190, "Battery voltage: " + battery + "V")

# Show it on the display
inkplate.display()
```

<CenteredImage src="/img/6color/read-battery-voltage.jpg" alt="Battery info" caption="Fully charged battery example" />

<InfoBox> Expect about 4.2V on a full cell. 3.7V is the nominal voltage, so a reading there means the battery is roughly half used. Protected cells cut off near 3.0V. </InfoBox>

<FunctionDocumentation
  functionName="inkplate.read_battery()"
  description="Reads the current battery voltage when running on battery power"
  returnType="float"
  returnDescription="Returns the measured battery voltage"
/>
