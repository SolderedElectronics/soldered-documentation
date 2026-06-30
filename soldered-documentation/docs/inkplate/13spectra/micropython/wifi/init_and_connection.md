---
slug: /inkplate/13spectra/micropython/wifi/init-and-connection
title: Inkplate 13SPECTRA MicroPython - Initialization and connection
sidebar_label: Initialization and connection
id: 13spectra-init-and-connection
---

Inkplate 13SPECTRA can use its built-in ESP32-S3 WiFi capabilities to connect to the internet. This page demonstrates a simple way to connect to a WiFi network.

---

## Connecting to WiFi

Below is a simple example demonstrating how to connect to a WiFi network.

<InfoBox> You only need to enter your **SSID** and **password** in the code example. </InfoBox>

```python
# Include needed libraries
import network
import time
from inkplate13SPECTRA import Inkplate

# Enter your WiFi credentials here
ssid = "YOUR_SSID_HERE"
password = "YOUR_PASSWORD_HERE"

# Function which connects to WiFi
# More info here: https://docs.micropython.org/en/latest/esp8266/tutorial/network_basics.html
def do_connect():
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print("connecting to network...")
        sta_if.active(True)
        sta_if.connect(ssid, password)
        while not sta_if.isconnected():
            pass
    print("network config:", sta_if.ifconfig())
    return True

inkplate=Inkplate()
inkplate.begin()
inkplate.setTextSize(2)

if do_connect():
    inkplate.print("Wifi connected")
else:
    inkplate.print("Wifi failed")

inplate.display()

```

<CenteredImage src="/img/13spectra/DSC00716.jpg" alt="Example output displayed on e-paper display" caption="Example output displayed on e-paper display" width="1200px" />

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