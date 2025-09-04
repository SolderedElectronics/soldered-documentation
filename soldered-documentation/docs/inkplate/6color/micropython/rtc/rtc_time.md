---
slug: /inkplate/6color/micropython/rtc/rtc_measure_time
title: Inkplate 6COLOR – Measure Time
sidebar_label: Measure Time
id: rtc-measure-time
hide_title: false
---

Now we will explore how to use onboard RTC to measure time and preserve it even during reboots.

```python
from inkplate6COLOR import Inkplate
import time

# Create Inkplate object
inkplate = Inkplate()

# Initialize the display
inkplate.begin()

# Set the RTC's time
inkplate.rtcSetTime(9,39,10)
# Set the RTC's date
inkplate.rtcSetDate(5,9,2,2024)

# Infinite loop
while True:

    # Show the set time
    print(inkplate.rtcGetData())

    # Wait 10 seconds
    time.sleep(10)
```

<FunctionDocumentation
  functionName="inkplate.rtcSetTime()"
  description="Sets the RTC's time"
  parameters={[ 
    { type: 'int', name: 'rtc_hour', description: 'Set hour' },
    { type: 'int', name: 'rtc_minute', description: 'Set minutes' },
    { type: 'int', name: 'rtc_second', description: 'Set seconds' }
  ]}
/>

<FunctionDocumentation
  functionName="inkplate.rtcSetDate()"
  description="Sets the RTC's specified date"
  parameters={[ 
    { type: 'int', name: 'rtc_weekday', description: 'Set weekday' },
    { type: 'int', name: 'rtc_day', description: 'Set day in a month' },
    { type: 'int', name: 'rtc_month', description: 'Set month' },
    { type: 'int', name: 'rtc_yr', description: 'Set year' }
  ]}
/>