---
slug: /inkplate_micropython/inkplate10/wifi/network-example
title: Inkplate 10 MicroPython - Basic Network Usage 
id: network-example
---

Inkplate 10 can connect to **WiFi** and communicate with the internet using standard MicroPython networking libraries.  
This example shows how to connect to a network and perform an **HTTP GET** request.

<InfoBox>  
Before running this example, make sure to enter your own WiFi credentials (`ssid` and `password`).  
</InfoBox>

<CenteredImage src="/img/inkplate10-micropython/examplenetwork.jpg" alt="Inkplate 10 running the example code" caption="Inkplate 10 running the example code" width="800px" />

---

## Network Example

```python
import network
import time
from inkplate10 import Inkplate

ssid = "ENTER_SSID_HERE"
password = "ENTER_PASSWORD_HERE"

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

def http_get(url):
    import socket
    res = ""
    _, _, host, path = url.split("/", 3)
    addr = socket.getaddrinfo(host, 80)[0][-1]
    s = socket.socket()
    s.connect(addr)
    s.send(bytes("GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n" % (path, host), "utf8"))
    while True:
        data = s.recv(100)
        if data:
            res += str(data, "utf8")
        else:
            break
    s.close()
    return res

# First, connect
do_connect()

# Do a GET request
response = http_get("http://micropython.org/ks/test.html")

# Create and initialize Inkplate
inkplate = Inkplate(Inkplate.INKPLATE_1BIT)
inkplate.begin()
inkplate.setTextSize(1)

# Print response
inkplate.print(response)
inkplate.display()
```

<FunctionDocumentation
functionName="network.WLAN(interface_id)"
description="Create a WLAN (WiFi) interface object."
returnDescription="WLAN object used for managing WiFi connectivity."
parameters={[
{ type: 'Const', name: 'interface_id', description: 'network.STA_IF for station mode (connect to an AP), or network.AP_IF for access point mode.' }
]}
/>

<FunctionDocumentation
functionName="sta_if.connect(ssid, password)"
description="Connect the WLAN interface to a WiFi network."
returnDescription="Nothing (raises OSError on failure)."
parameters={[
{ type: 'String', name: 'ssid', description: 'WiFi SSID (network name).' },
{ type: 'String', name: 'password', description: 'WiFi password.' }
]}
/>

<FunctionDocumentation functionName="sta_if.isconnected()" description="Check if the WLAN interface is currently connected to a network." returnDescription="Boolean (`True` if connected, `False` otherwise)." parameters={[]} />

<FunctionDocumentation functionName="sta_if.ifconfig()" description="Get the IP configuration of the WLAN interface." returnDescription="Tuple containing `(ip, subnet_mask, gateway, dns)`." parameters={[]} />

<FunctionDocumentation
functionName="http_get(url)"
description="Perform a simple HTTP GET request over TCP."
returnDescription="String containing the full server response body and headers."
parameters={[
{ type: 'String', name: 'url', description: 'Full HTTP URL (must start with http://).' }
]}
/>

---

## Full example

<QuickLink title="Inkplate10-exampleNetwork.py" 
description="An example showing how to connect to WiFi and fetch data from the internet using HTTP GET." 
url="https://github.com/SolderedElectronics/Inkplate-micropython/blob/micropython-library-revamp/Examples/Inkplate10/exampleNetwork.py" />