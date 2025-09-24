---
slug: /inkplate_micropython/inkplate10/wifi/display-image-wifi
title: Inkplate 10 MicroPython - Displaying Image from WiFi
id: display-image-wifi
---

Inkplate 10 can fetch and render images directly from the internet once connected to a WiFi network.  
Supported formats are **JPG, PNG, and BMP**, with optional **inversion** and **dithering** for better grayscale rendering.

<InfoBox>  
Image rendering time depends on the format and dithering option. For example:  
- JPG: ~3 seconds (or ~7s with dithering)  
- PNG: ~10 seconds (or ~14s with dithering)  
- BMP: ~15 seconds (or ~20s with dithering)  
Maximum image file size is around **800 kB**.  
</InfoBox>

<CenteredImage src="/img/inkplate10-micropython/imgweb.jpg" alt="Inkplate 10 running the example code" caption="Inkplate 10 running the example code" width="800px" />
---

## WiFi Image Example

```python
import network
import time
from inkplate10 import Inkplate

SSID = "ENTER_SSID_HERE"
PASSWORD = "ENTER_PASSWORD_HERE"

def do_connect():
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print("Connecting to network...")
        sta_if.active(True)
        sta_if.connect(SSID, PASSWORD)

        timeout = 30
        start = time.ticks_ms()
        while not sta_if.isconnected():
            if time.ticks_diff(time.ticks_ms(), start) > timeout * 1000:
                print("Failed to connect within timeout")
                return False
            time.sleep(0.5)
    print("Network config:", sta_if.ifconfig())
    return True

# Create Inkplate in 2-bit grayscale mode
inkplate = Inkplate(Inkplate.INKPLATE_2BIT)
inkplate.begin()

if not do_connect():
    raise SystemExit("WiFi connection failed")

inkplate.drawImage(
    "https://i.imgur.com/6vMuKxa.jpeg",
    0, 0,
    invert=False,
    dither=True,
    kernel_type=Inkplate.KERNEL_FLOYD_STEINBERG
)

inkplate.display()
```

<FunctionDocumentation
functionName="inkplate.drawImage(path, x0, y0, invert=False, dither=False, kernel_type=Inkplate.KERNEL_FLOYD_STEINBERG)"
description="Draw an image from a local path or URL to the display buffer."
returnDescription="Nothing"
parameters={[
{ type: 'String', name: 'path', description: 'Path or URL to the image (JPG, PNG, BMP).' },
{ type: 'Number', name: 'x0', description: 'X coordinate of the top-left corner.' },
{ type: 'Number', name: 'y0', description: 'Y coordinate of the top-left corner.' },
{ type: 'Boolean', name: 'invert', description: 'If True, invert the image colors (default False).' },
{ type: 'Boolean', name: 'dither', description: 'If True, apply dithering for better grayscale rendering.' },
{ type: 'Const', name: 'kernel_type', description: 'Dithering algorithm to use (e.g., KERNEL_FLOYD_STEINBERG, KERNEL_JJN, KERNEL_STUCKI, KERNEL_BURKES).' }
]}
/>

<FunctionDocumentation
functionName="network.WLAN(interface_id)"
description="Create a WLAN (WiFi) interface object."
returnDescription="WLAN object for managing WiFi connectivity."
parameters={[
{ type: 'Const', name: 'interface_id', description: 'Interface type (usually network.STA_IF for station mode or network.AP_IF for access point mode).' }
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

---

## Full example

<QuickLink title="Inkplate10-displayImageWiFi.py"
description="An example showing how to connect to WiFi and render an image from a URL."
url="https://github.com/SolderedElectronics/Inkplate-micropython/blob/master/Examples/Inkplate10/RTC.py" />