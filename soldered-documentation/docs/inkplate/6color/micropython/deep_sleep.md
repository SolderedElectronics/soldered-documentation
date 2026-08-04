---  
slug: /inkplate/6color/micropython/deep_sleep
title: Inkplate 6COLOR – Deep Sleep
sidebar_label: Deep Sleep
id: deep-sleep
hide_title: false  
---

Deep sleep is how you get a sketch to run for months on a battery. E-paper needs no power to hold its image, so between refreshes the board can sit at about 18 µA.

---

## Simple deep sleep

<InfoBox> When your ESP32 wakes up from deep sleep, it performs a reset and runs **main.py** again. That means your main script runs again on every wake-up. </InfoBox>

<WarningBox> Make sure you've uploaded a **main.py** file to the ESP32. Put the code you want to run after each wake-up inside it.</WarningBox>

Basic example of keeping a counter in **RTC memory** using **raw bytes** while ESP32 is in deep sleep.

```python
from inkplate6_color import Inkplate
import machine
import time

# Create a RTC object that stores states between deep sleep cycles
rtc = machine.RTC()

# Read stored bytes from memory
raw = rtc.memory()

# If we have at least 1 stored byte, set as counter,
# otherwise start from 0
count = raw[0] if raw and len(raw) >= 1 else 0

inkplate = Inkplate()

inkplate.begin()

inkplate.clear_display()

# Check for reset reason and print message accordingly
if machine.reset_cause() == machine.DEEPSLEEP_RESET:
    inkplate.println("Woke up from sleep")
    # Increment counter
    count = count + 1
else:
    count = 1
    inkplate.println("Cold boot / soft reset")

# Write one byte back to RTC memory
rtc.memory(bytes([count]))

inkplate.print(f"Count: {count}")
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
    description="Puts the ESP32 into deep sleep for the given number of milliseconds. Call it with no argument to sleep until a wake source fires."
    parameters={[  
    { type: "int", name: "sleep_time_ms", description: "Deep sleep duration in milliseconds" }
  ]}
/>

## Wake on button press

```python
import esp32
import machine
import time

# Define a wake up pin on GPIO 36 (wake button)
wake1 = machine.Pin(36, mode = machine.Pin.IN)

# Set ext0 as a wake up source when pin goes LOW
esp32.wake_on_ext0(pin = wake1, level = esp32.WAKEUP_ALL_LOW)

print('Im awake. Going to sleep in 10 seconds')
time.sleep(10)

print('Going to sleep now')
machine.deepsleep()
```

<FunctionDocumentation
    functionName="esp32.wake_on_ext0()"
    description="This function uses the external wakeup feature of the RTC_IO peripheral."
    returnType="none"
    parameters={[  
    { type: "machine.Pin", name: "Pin", description: "GPIO number used as wakeup source. Only GPIOs with RTC functionality can be used." },
    { type: "int", name: "level", description: "The input level that triggers wake-up" }
  ]}
/>
