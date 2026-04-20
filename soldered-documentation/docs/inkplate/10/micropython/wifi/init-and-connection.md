---
slug: /inkplate/10/micropython/wifi/init-and-connection
title: Inkplate 10 MicroPython - Initialization and connection
sidebar_label: Initialization and connection
id: init-and-connection
---

Inkplate 10 can use its built-in ESP32 WiFi capabilities to connect to the internet. This page demonstrates a simple way to connect to a WiFi network.

## Connecting to WiFi

Below is a simple example demonstrating how to connect to a WiFi network.

<InfoBox>You only need to enter your **SSID** and **password** in the code example.</InfoBox>

```python
import network
import time
from inklate10 import Inkplate

#Enter your WiFi credentials here
SSID="YOUR SSID"
PASSWORD="YOUR PASSWORD"

def connect_wifi():
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print("Connecting to network...")
        sta_if.active(True)
        sta_if.connect(SSID, PASSWORD)

        # Wait for connection with timeout (10 seconds)
        start = time.ticks_ms()
        while not sta_if.isconnected():
            if time.ticks_diff(time.ticks_ms(), start) > 10_000:
                print("Failed to connect within timeout")
                return False
            time.sleep(0.5)
    print("Network config:", sta_if.ifconfig())
    return True

inkplate=Inkplate(Inkplate.INKPLATE_1BIT)
inkplate.begin()
inkplate.setTextSize(2)
inkplate.setCursor(100,100)

if connect_wifi():
    inkplate.print("Wifi connected!")
else:
    inkplate.print("Wifi failed")

inkplate.display()
```

<FunctionDocumentation
functionName="network.WLAN()"
description="Create or access a WiFi network interface object."
parameters={[
{ type: 'Constant', name: 'network.STA_IF', description: 'Use WiFi in station (client) mode.' }
]}
/>

<FunctionDocumentation
functionName="sta_if.connect()"
description="Connects to a WiFi network with the given SSID and password."
parameters={[
{ type: 'String', name: 'SSID', description: 'The WiFi network name.' },
{ type: 'String', name: 'PASSWORD', description: 'The WiFi password.' }
]}
/>
