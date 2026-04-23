---
slug: /inkplate/6color/micropython/rtc/basic
title: Inkplate 6COLOR – Basic RTC usage
sidebar_label: Basic RTC usage
id: basic-usage
hide_title: false
---

This page shows how to use the **onboard PCF85063A RTC** to measure and keep track of time.

---

## RTC Set Time/Date

```python
from inkplate6COLOR import Inkplate
import time

# Create Inkplate object
inkplate = Inkplate()

# Initialize the display
inkplate.begin()

# Set the RTC's time
inkplate.rtcSetTime(9, 39, 10)
# Set the RTC's date
inkplate.rtcSetDate(4, 24, 9, 2025)

# Infinite loop
while True:
  # Get RTC time data (returns dictionary)
  rtc_data = inkplate.rtcGetData()

  # Clear the display buffer
  inkplate.clearDisplay()
  inkplate.setCursor(5, 5) 

  # Print every RTC time parameter
  inkplate.println("RTC Date & Time:")
  inkplate.println(f"  Year    : {rtc_data['year']}")
  inkplate.println(f"  Month   : {rtc_data['month']}")
  inkplate.println(f"  Day     : {rtc_data['day']}")
  inkplate.println(f"  Weekday : {rtc_data['weekday']}")
  inkplate.println(f"  Hour    : {rtc_data['hour']}")
  inkplate.println(f"  Minute  : {rtc_data['minute']}")
  inkplate.print(f"  Second  : {rtc_data['second']}")
  inkplate.display()

  # Pause for 10 seconds before updating the display
  # Note: displayed time may not differ by exactly 10 seconds due to screen refresh time.
  time.sleep(10)
```

<CenteredImage src="/img/6color/rtc-date-time.jpg" alt="Time date display on Inkplate" caption="Time/Date display on Inkpalte"/>

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

<FunctionDocumentation
  functionName="inkplate.rtcGetData()"
  description="Returns current RTC time values"
  returnType="Dictionary"
  returnDescription="Return dictionary with RTC time values as integers"
/>