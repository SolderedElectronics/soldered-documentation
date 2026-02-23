---
slug: /inkplate/13spectra/micropython/wifi/get-and-post-requests
title: Inkplate 13SPECTRA MicroPython - GET and POST requests
sidebar_label: GET and POST requests
id: 13spectra-get-and-post-requests
---

Inkplate 13SPECTRA can connect to the internet and make HTTP requests.
This example demonstrates how to perform a simple **GET** and **POST** request using the 'urequests' library, with [webhook.site](http://webhook.site) as the test server.

---

## Making a GET request

This example below fetches data from a webhook.site endpoint and prints the response.

<InfoBox>webhook.site will generate a unique URL for your personal use. Use `http://` instead of `https://` (many MicroPython build do not include TLS support). </InfoBox>

```python
# Include needed libraries
import network
import time
import urequests
from inkplate13SPECTRA import Inkplate

# Enter your WiFi credentials here
ssid = "your ssid"
password = "your password"

#Your personal webhook.site URL (use http://, no leading spaces!)
WEBHOOK_URL ="yout webhook id"
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
    response=urequests.get(WEBHOOK_URL)
    print("GET status:", response.status_code)
    print("GET body",response.text)
    response.close()

else:
    inkplate.print("Wifi failed")

inkplate.display()
```

<CenteredImage src="/img/13spectra/micropython_get_example.png" alt="Example output displayed in console" caption="Example output displayed in console" width="1200px" />

<FunctionDocumentation
functionName="urequests.get()"
description="Perform an HTTP GET request to the given URL."
parameters={[
{ type: 'String', name: 'url', description: 'The target URL (must start with http://).' }
]}
returnType="Response"
returnDescription="Response object with .status_code and .text."
/>

---

## Making a POST request

You can also send data to the server. In this example we will send **JSON** payload to the webhook URL.

```python
import network
import time
import urequests
import ujson
from inkplate13SPECTRA import Inkplate

# Enter your WiFi credentials here
ssid = ""
password = ""

#Your personal webhook.site URL (use http://, no leading spaces!)
WEBHOOK_URL =""
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
    data = {"message": "Hello from Inkplate 13Spectra!"}

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
    inkplate.print("Wifi failed")
    inkplate.display()
```

<CenteredImage src="/img/13spectra/micropython_post_example.png" alt="POST request logged on webhook.site" caption="POST request logged on webhook.site" width="1200px" />

<CenteredImage src="/img/13spectra/DSC00717.jpg" alt="Example output displayed on e-paper display" caption="Example output displayed on e-paper display" width="1200px" />

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

