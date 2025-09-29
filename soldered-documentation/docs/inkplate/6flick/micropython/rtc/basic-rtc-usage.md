---
slug: /inkplate/6/micropython/rtc/basic-rtc-usage
title: Inkplate 6 MicroPython - Basic RTC usage
sidebar_label: Basic RTC usage
id: basic-rtc-usage
---

Inkplate 6 comes with an onboard **RTC (Real-Time Clock)**, which allows the board to keep track of the time and date even across reboots **(as long as the backup battery is present)**.

<InfoBox>  
To preserve time while the Inkplate is powered off, make sure a **coin cell battery (CR2032)** is installed in the RTC holder. Without it, the clock will reset when power is lost.  
</InfoBox>

This example shows how to set the RTC time and date, and then continuously display the current time on the screen.


---

## Basic RTC Example

```python
# Include all the required libraries
from inkplate6FLICK import Inkplate
import time

# Create Inkplate object in 1-bit mode, black and white colors only
# For 2-bit grayscale, see basicGrayscale.py
inkplate = Inkplate(Inkplate.INKPLATE_1BIT)

    
# Initialize the display, needs to be called only once
inkplate.begin()

inkplate.clearDisplay()

inkplate.display()

inkplate.setTextSize(2)

# This is how to set the RTC's time
# Arguments are hour, minute, seconds
inkplate.rtcSetTime(9,39,10)
# And this is the date
# Arguments are weekday, day in month, month and year
inkplate.rtcSetDate(5,9,2,2024)

# Infinite loop
while True:
    inkplate.clearDisplay()
    rtcData = inkplate.rtcGetData()
    
    hour = rtcData['hour']
    minute = rtcData['minute']
    second = rtcData['second']
    
    if hour < 10:
        hour="0"+str(hour)
    if minute < 10:
        minute="0"+str(minute)
    if second < 10:
        second="0"+str(second)
    
    inkplate.setCursor(450,300)
    current_time=str(hour)+":"+str(minute)+":"+str(second)
    inkplate.print(current_time)
    inkplate.partialUpdate()

```

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

<CenteredImage src="/img/inkplate6flick-micropython/rtc.jpg" alt="Inkplate 10 running the example code" caption="Inkplate 10 running the example code" width="800px" />

---

## Full example

<QuickLink title="Inkplate6FLICK-RTC.py" 
description="An example showing how to set and read time/date using the onboard RTC, and display it continuously on the screen." 
url="https://github.com/SolderedElectronics/Inkplate-micropython/blob/master/Examples/Inkplate6FLICK/RTC.py" />