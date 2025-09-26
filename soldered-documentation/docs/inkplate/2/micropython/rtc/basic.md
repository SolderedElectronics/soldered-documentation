---
slug: /inkplate/2/micropython/rtc/basic-usage
title: Inkplate 2
sidebar_label: Basic usage
id: basic
hide_title: true
---

<SectionTitle title="RTC Basic usage" backgroundImage="img/arduino_bg.jpg" />

This page shows how to get time from NTP server and keep track using RTC.

<InfoBox> The RTC can drift a little each day, so in order to keep time accurate it's best to resync with NTP once a day. </InfoBox>

---

## Example fetching time from the Internet
```python
from inkplate2 import Inkplate
import network
import ntptime
import time

# WiFi credentials
SSID = ""
PASSWORD = ""

inkplate = Inkplate()

inkplate.begin()

# Connect to WiFi (connection process explained on previous page)
if not do_connect():
    raise SystemExit("WiFi connection failed")

# Sync with NTP server and set the RTC time
try:
    ntptime.settime()
except:
    print("Failed to sync with NTP")

while True:
    # Clear the display buffer and set cursor at upper left corner
    inkplate.clearDisplay()
    inkplate.setCursor(0, 0)
        
    # Get UTC time
    utc_time = time.localtime()

    # Convert UTC -> local time (e.g., UTC+2
    # Offset in seconds (hours * 3600)
    timezone_offset = (2 * 3600)

    # Apply timezone offset
    local_time = time.localtime(time.mktime(utc_time) + timezone_offset)

    # Extract year, month, day, hour, minute, second from the tuple, excludes weekday, yearday
    year, month, mday, hour, minute, second, *_ = local_time
    inkplate.print(f"{year}-{month:02d}-{mday:02d} {hour:02d}:{minute:02d}:{second:02d}")
    
    # Update display
    inkplate.display()
    
    time.sleep(30)
```

<FunctionDocumentation
    functionName="ntptime.settime()"
    description="Fetch current UTC time and set Real Time Clock"
/>
<FunctionDocumentation
    functionName="time.localtime()"
    description="Convert current time in seconds into a tuple format"
    returnDescription="Return time as a tuple: (year, month, mday, hour, minute, second, weekday, yearday)"
    parameters={[  
    { type: "int", name: "secs", description: "If secs is not provided or None, then return current time from the RTC" }
  ]}
/>
<FunctionDocumentation
    functionName="time.mktime()"
    description="Inverse function of localtime."
    returnDescription="Returns an integer which is the number of seconds since the time epoch (UNIX timestamp)."
    parameters={[  
    { type: "tuple", name: "date_time_tuple", description: "8-tuple which expresses a time as localtime" }
  ]}
/>