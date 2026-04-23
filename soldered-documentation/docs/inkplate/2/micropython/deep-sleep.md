---
slug: /inkplate/2/micropython/deep-sleep
title: Inkplate 2 - Deep Sleep
sidebar_label: Deep Sleep
id: deep-sleep
hide_title: true
---

<SectionTitle title="Deep Sleep" backgroundImage="img/arduino_bg.jpg" />

Using deep sleep on Inkplate 2 is crucial for writing a sketch that maximizes battery efficiency. Since e-Paper does not require any power to retain the displayed image, Inkplate 2 can consume little or no current while in deep sleep mode, enabling a sketch to run for months on battery.

---

<InfoBox> When your ESP32 wakes up from deep sleep, it performs a reset and runs **main.py** again. That means your main script is executed on every every wake-up. </InfoBox>

<WarningBox> Make sure you’ve uploaded a **main.py** file to the ESP32. Put the code you want to run after each wake-up inside it.</WarningBox>

## Simple deep sleep

Basic example of using deep sleep on ESP32 and printing current RTC time.

<InfoBox> The RTC can drift a little each day, so in order to keep time accurate it's best to resync with NTP once a day. </InfoBox>

```python
from inkplate2 import Inkplate
import machine
import time

inkplate = Inkplate()

inkplate.begin()

inkplate.clearDisplay()

# Check for reset reason and print message accordingly
if machine.reset_cause() == machine.DEEPSLEEP_RESET:
    inkplate.println("Woke up from sleep")
else:
    inkplate.println("Cold boot / soft reset")

# Get UTC time
utc_time = time.localtime()

# Convert UTC -> local time (e.g., UTC+2
# Offset in seconds (hours * 3600)
timezone_offset = (2 * 3600)

# Apply timezone offset and print time
local_time = time.localtime(time.mktime(utc_time) + timezone_offset)
year, month, mday, hour, minute, second, *_ = local_time
inkplate.print(f"{year}-{month:02d}-{mday:02d} {hour:02d}:{minute:02d}:{second:02d}")

inkplate.display()

# Important delay before going to sleep when writing scripts
# Wait 10 seconds so you can 'catch' it awake to upload new code later on
time.sleep(10)

# Deep sleep for 10 seconds (10000 milliseconds)
machine.deepsleep(10000)
```

<FunctionDocumentation
    functionName="machine.reset_cause()"
    description="Get the reset cause."
    returnType="machine.CONSTANT"
/>

<InfoBox> See **[constants](https://docs.micropython.org/en/latest/library/machine.html#machine-constants)** for possible return values. </InfoBox>

<FunctionDocumentation
    functionName="machine.deepsleep()"
    description="This function puts the ESP32 in deep sleep mode for a predetermined number of seconds"
    parameters={[  
    { type: "int", name: "sleep_time_ms", description: "Deep sleep duration in milliseconds" }
  ]}
/>