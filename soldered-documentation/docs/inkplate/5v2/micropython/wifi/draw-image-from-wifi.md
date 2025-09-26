---
slug: /inkplate/5v2/micropython/wifi/draw-image-from-wifi
title: Inkplate 5v2 MicroPython - Draw Image from WiFi
sidebar_label: Draw Image from WiFi
id: draw-image-from-wifi
---

Inkplate 5v2 can connect to WiFi and fetch images directly from the internet. This example demonstrates downloading a JPEG file from a URL and rendering it on e-paper display.

---

## Downloading and displaying an image

Below is a complere example that connects to WiFi and loads an image from the web. Make sure to replace the **SSID** and **password** with your own WiFi credentials.

```python
import network
import time
from inkplate5v2 import Inkplate

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
functionName="inkplate.drawImage()"
description="Download and draw an image from a URL or local file path onto the display buffer."
parameters={[
{ type: 'String', name: 'path', description: 'Image URL or local file path.' },
{ type: 'Number', name: 'x', description: 'X coordinate of top-left corner where image will be placed.' },
{ type: 'Number', name: 'y', description: 'Y coordinate of top-left corner where image will be placed.' },
{ type: 'Boolean', name: 'invert', description: 'If True, invert black and white colors.' },
{ type: 'Boolean', name: 'dither', description: 'Enable or disable dithering for grayscale images.' },
{ type: 'Constant', name: 'kernel_type', description: 'Dithering algorithm to use (e.g., Inkplate.KERNEL_FLOYD_STEINBERG).' }
]}
/>

<InfoBox>
Available options for **dithering** algorithm:

| **Algorithm**  | **Value** |
| --------------------- | ------------------------ |
| `Inkplate.KERNEL_FLOYD_STEINBERG` | 0 |
| `Inkplate.KERNEL_JJN` | 1 |
| `Inkplate.KERNEL_STUCKI` | 2 |
| `Inkplate.KERNEL_BURKES `| 3 |

**Performance Notes**
- JPG: ~3 seconds (or ~14s with dithering)
- PNG: ~9 seconds (or ~19s with dithering)
- BMP: ~20 seconds (or ~40s with dithering)
- Maximum image file size: ~800kB

</InfoBox>

<CenteredImage src="/img/inkplate5v2-micropython/imgweb.jpg" alt="Inkplate 5v2 running the example code" caption="Displaying an image from web." width="1000px" />