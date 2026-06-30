---
slug: /inkplate/13spectra/micropython/rtc/basic-rtc-usage
title: Inkplate 13SPECTRA MicroPython - Basic RTC usage
sidebar_label: Basic RTC usage
id: 13spectra-basic-rtc-usage
---

Inkplate 13SPECTRA comes with an onboard **RTC (Real-Time Clock)**, which allows the board to keep track of the time and date even across reboots **(as long as the backup battery is present)**

<InfoBox>
To preserve time while the Inkplate is powered off, make sure a **coin cell battery (CR2032)** is installed in the RTC holder. Without it, the clck will reset when power is lost.
</InfoBox>

This example shows how to set the RTC time and date, and then continuously display the current time on the screen.

---

## Basic RTC Example

```python
# Include all the required libraries
from inkplate13SPECTRA import Inkplate
import time

# Create Inkplate object
inkplate = Inkplate()

# Initialize the display, needs to be called only once
inkplate.begin()

# This is how to set the RTC's time
# Arguments are hour, minute, seconds
inkplate.rtcSetTime(9,39,10)
# And this is the date
# Arguments are weekday, day in month, month and year
inkplate.rtcSetDate(2,9,2,2026)

# Infinite loop
while True:

    # Show the set time
    print(inkplate.rtcGetData())

    # Let's wait 10 seconds
    time.sleep(10)
```
<CenteredImage src="/img/13spectra/micropython_rtc_example.png" alt="Example output printed in console" caption="Example output printed in console" width="1200px" />

<FunctionDocumentation
functionName="inkplate.rtcSetTime()"
description="Set the RTC's current time."
parameters={[
{ type: 'Number', name: 'hour', description: 'Hour (0–23).' },
{ type: 'Number', name: 'minute', description: 'Minute (0–59).' },
{ type: 'Number', name: 'second', description: 'Second (0–59).' }
]}
/>

<FunctionDocumentation
functionName="inkplate.rtcSetDate()"
description="Set the RTC's current date."
parameters={[
{ type: 'Number', name: 'weekday', description: 'Day of the week (1 = Monday … 7 = Sunday).' },
{ type: 'Number', name: 'day', description: 'Day of the month (1–31).' },
{ type: 'Number', name: 'month', description: 'Month (1–12).' },
{ type: 'Number', name: 'year', description: 'Full year (e.g., 2025).' }
]}
/>

<FunctionDocumentation 
functionName="inkplate.rtcGetData()" 
description="Read the current RTC date and time." 
returnDescription="Dictionary containing keys: `hour`, `minute`, `second`, `weekday`, `day`, `month`, `year`." 
parameters={[]} />

---

## Full example

[LINK PLACEHOLDER - link to 13spectra rtc example]
