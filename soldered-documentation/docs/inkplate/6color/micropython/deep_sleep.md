---  
slug: /inkplate/6color/micropython/deep_sleep
title: Inkplate 6COLOR – Deep Sleep
sidebar_label: Deep Sleep
id: deep-sleep
hide_title: false  
---

Using deep sleep on Inkplate 6COLOR is crucial for writing a sketch that maximizes battery efficiency. Since e-Paper does not require any power to retain the displayed image, Inkplate 6COLOR can consume little or no current while in deep sleep mode, enabling a sketch to run for months on battery.

PROVJERI CURRENT CONSUMPTION ZA DEEP SLEEP SA MICROPYTHONOM

---

## Simple Deep Sleep

<InfoBox> When your ESP32 wakes up from deep sleep, it performs a reset and runs **main.py** again. That means your main script is executed on every every wake-up. </InfoBox>

<InfoBox> Make sure you’ve uploaded a **main.py** file to the ESP32. Place in it main logic you want to run after each wake-up.</InfoBox>

Basic example keeping a counter in **RTC memory** using **raw bytes.**

```python
from inkplate6COLOR import Inkplate
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

inkplate.clearDisplay()

# Check for reset reason and print message accordingly
if machine.reset_cause() == machine.DEEPSLEEP_RESET:
    inkplate.println("Woke up from sleep")
    # Increment to counter 0...255 (Same as count = (count + 1) % 256
    count = (count + 1) & 0xFF
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

See [constants](https://docs.micropython.org/en/latest/library/machine.html#machine-constants) for possible return values.

<FunctionDocumentation
    functionName="machine.deepsleep()"
    description="This function puts the ESP32 in deep sleep mode for a predetermined number of seconds"
    parameters={[  
    { type: "int", name: "sleep_time_ms", description: "Deep sleep duration in milliseconds" }
  ]}
/>

## Wake on Button press

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
    returnType="None"
    parameters={[  
    { type: "machine.Pin", name: "Pin", description: "GPIO number used as wakeup source. Only GPIOs with RTC functionality can be used." },
    { type: "int", name: "level", description: "The input level that triggers wake-up" }
  ]}
/>
