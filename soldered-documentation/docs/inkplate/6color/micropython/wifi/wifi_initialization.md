---
slug: /inkplate/6color/micropython/wifi/wifi_initialization
title: Inkplate 6COLOR – WiFi Initialization
sidebar_label: WiFi Initialization
id: wifi-init
hide_title: true
---

<SectionTitle title="WiFi Basics" backgroundImage="img/arduino_bg.jpg" />

Inkplate 6COLOR uses ESP32 to handle WiFi connections. This page demonstrates how to connect your Inkplate board to existing WiFi network.

---

## WiFi Connection Example

```python
from inkplate6COLOR import Inkplate
import network
import time

# WiFi credentials
SSID = "YOUR_SSID_HERE"
PASSWORD = "YOUR_PASSWORD_HERE"

inkplate = Inkplate()

inkplate.begin()

# Connect to a WiFi network using given SSID and PASSWORD.
sta_if = network.WLAN(network.STA_IF)

connected = False

if not sta_if.isconnected():
    inkplate.println("Connecting to network...")
    sta_if.active(True)
    try:
        sta_if.connect(SSID, PASSWORD)
    except Exception as e:
        inkplate.println(f"Wi-Fi connect error: {e}")
        inkplate.print("Check your credentials!")
    else:
        timeout = 30  # seconds
        start = time.ticks_ms()

        while not sta_if.isconnected():
            if time.ticks_diff(time.ticks_ms(), start) > timeout * 1000:
                print("Failed to connect within timeout")
                break
            time.sleep(0.5)
        else:
            connected = True
else:
    connected = True

if connected:
    inkplate.print(f"CONNECTED: \n{sta_if.ifconfig()}")
    
inkplate.display()
```

<FunctionDocumentation
    functionName="network.WLAN()"
    description="Create a WLAN network interface object and connect to WiFi access point"
    parameters={[  
    { type: "int", name: "interface_id", description: "Set to network.STA_IF for connecting to access point, or network.STA_AP to allow other WiFi clients to connect" }
  ]}
/>

<FunctionDocumentation
    functionName="WLAN.active()"
    description="Create a WLAN network interface object and connect to WiFi access point"
    returnDescription="Returns current state if no argument is provided"
    parameters={[  
    { type: "bool", name: "is_active", description: "Activate/Deactivate network interface if arguments is passed" }
  ]}
/>

<FunctionDocumentation
    functionName="WLAN.connect()"
    description="Connect to the specified wireless network, using the specified key (only works in STA interface)"
    returnDescription=""
    parameters={[  
    { type: "string", name: "ssid", description: "Network SSID" },
    { type: "string", name: "key", description: "Network password" }
  ]}
/>

<FunctionDocumentation
    functionName="WLAN.isconnected()"
    description="Check the connection status"
    returnDescription="Returns True if connected to a WiFi access point and has a valid IP address. In AP mode returns True when a station is connected, otherwise False"
    returnType="Bool"
    parameters={[
  ]}
/>

<FunctionDocumentation
    functionName="WLAN.ifconfig()"
    description="Get/Set network interface parameters: IP address, subnet mask, gateway and DNS server"
    returnDescription="When called with no arguments, returns a 4-tuple with the above information"
    returnType="Tuple"
    parameters={[
        { type: "Tuple", name: "(ip, subnet, gateway, dns)", description: "Network parameters" }
  ]}
/>
