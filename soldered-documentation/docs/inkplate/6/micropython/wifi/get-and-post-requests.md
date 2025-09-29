---
slug: /inkplate/6/micropython/wifi/get-and-post-requests
title: Inkplate 6 MicroPython - GET and POST requests
sidebar_label: GET and POST requests
id: get-and-post-requests
---

Inkplate 6 can connect to the internet and make HTTP requests.
This example demonstrates how to perform a simple **GET** and **POST** request using the 'urequests' library, with [webhook.site](http://webhook.site) as the test server.

---

## Making a GET request

The example below fetches data from a webhook.site endpoint and prints the response.

<InfoBox>
Webhook.site will generate a unique URL for your personal use. Use `http://` instead of `https://` (many MicroPython builds do not include TLS support).
</InfoBox>

```python
import network
import time
import urequests
from inkplate6 import Inkplate

# Your WiFi credentials
SSID = "YourNetwork"
PASSWORD = "YourPassword"

# Your personal webhook.site URL (use http://, no leading spaces!)
WEBHOOK_URL = "http://webhook.site/your-unique-url"

def connect_wifi():
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        sta_if.active(True)
        sta_if.connect(SSID, PASSWORD)
        start = time.ticks_ms()
        while not sta_if.isconnected():
            if time.ticks_diff(time.ticks_ms(), start) > 10_000:
                print("WiFi connection failed")
                return False
            time.sleep(0.5)
    return True

if connect_wifi():
    print("Connected to WiFi")

    # Perform GET request
    response = urequests.get(WEBHOOK_URL)
    print("GET status:", response.status_code)
    print("GET body:", response.text)
    response.close()
```

<FunctionDocumentation
functionName="urequests.get()"
description="Perform an HTTP GET request to the given URL."
parameters={[
{ type: 'String', name: 'url', description: 'The target URL (must start with http://).' }
]}
returnType="Response"
returnDescription="Response object with .status_code and .text."
/>

<CenteredImage src="/img/inkplate10-micropython/get-output.png" alt="Inkplate 10 running the example code" caption="Example code output." width="1000px" />

---

## Making a POST request

You can also send data to the server. In this examplem we will send **JSON** payload to the webhook URL.

```python

import network
import time
import urequests
import ujson
from inkplate6 import Inkplate

# Your WiFi credentials
SSID = "YourNetwork"
PASSWORD = "YourPassword"

# Your personal webhook.site URL (use http://, no leading spaces!)
WEBHOOK_URL = "http://webhook.site/your-unique-url"

def connect_wifi():
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print("Connecting to WiFi...")
        sta_if.active(True)
        sta_if.connect(SSID, PASSWORD)
        start = time.ticks_ms()
        while not sta_if.isconnected():
            if time.ticks_diff(time.ticks_ms(), start) > 10_000:
                print("WiFi connection failed")
                return False
            time.sleep(0.5)
    print("Connected:", sta_if.ifconfig())
    return True

# Initialize Inkplate display
inkplate = Inkplate(Inkplate.INKPLATE_1BIT)
inkplate.begin()
inkplate.clearDisplay()
inkplate.display()
inkplate.setTextSize(2)
inkplate.setCursor(50, 100)

if connect_wifi():
    # Data to send
    data = {"message": "Hello from Inkplate 10!"}

    # Perform POST request
    try:
        response = urequests.post(WEBHOOK_URL, json=data)
        print("POST status:", response.status_code)
        print("POST body:", response.text)

        inkplate.print("POST OK!")
        inkplate.display()

        response.close()
    except Exception as e:
        print("POST failed:", e)
        inkplate.print("POST failed!")
        inkplate.display()
else:
    inkplate.print("WiFi failed!")
    inkplate.display()

```

<FunctionDocumentation
functionName="urequests.post()"
description="Perform an HTTP POST request to the given URL."
parameters={[
{ type: 'String', name: 'url', description: 'The target URL (must start with http://).' },
{ type: 'Dict', name: 'json', description: 'Dictionary to send as JSON in the request body.' }
]}
returnType="Response"
returnDescription="Response object with .status_code and .text."
/>

<CenteredImage src="/img/inkplate10-micropython/post-output.png" alt="Inkplate 10 running the example code" caption="POST request message on webhook.site." width="800px" />