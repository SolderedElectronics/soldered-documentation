---
slug: /inkplate/5v2/micropython/wifi/draw-image-from-wifi
title: Inkplate 5v2 MicroPython - Draw image from WiFi
sidebar_label: Draw image from WiFi
id: draw-image-from-wifi
---

Inkplate 5v2 can connect to WiFi and fetch images directly from the internet. This example downloads a JPEG file from a URL and renders it on the e-paper display.

---

## Downloading and displaying an image

Here is a complete example that connects to WiFi and loads an image from the web. Replace the SSID and password with your own WiFi credentials.

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

inkplate.draw_image(
    "https://i.imgur.com/8yvGmvs.jpeg",
    0, 0,
    invert=False,
    dither=True,
    kernel_type=Inkplate.KERNEL_FLOYD_STEINBERG
)

inkplate.display()

```

<FunctionDocumentation
functionName="inkplate.draw_image()"
description="Download and draw an image from a URL or local file path onto the display buffer."
parameters={[
{ type: 'String', name: 'path', description: 'Image URL or local file path.' },
{ type: 'Number', name: 'x0', description: 'X coordinate of top-left corner where image will be placed.' },
{ type: 'Number', name: 'y0', description: 'Y coordinate of top-left corner where image will be placed.' },
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
| `Inkplate.KERNEL_BURKES` | 3 |

**Performance notes**
- JPG: ~3 seconds (or ~7s with dithering)
- PNG: ~10 seconds (or ~14s with dithering)
- BMP: ~15 seconds (or ~20s with dithering)
- Maximum image file size: ~800kB

</InfoBox>

<CenteredImage src="/img/inkplate5v2-micropython/imgweb.jpg" alt="Inkplate 5v2 running the example code" caption="Displaying an image from web." width="1000px" />

---

## Full example

<QuickLink title="display_image_web.py" 
description="Connect to WiFi and render an image from a URL." 
url="https://github.com/SolderedElectronics/Inkplate-micropython/blob/master/examples/inkplate5v2/display_image_web.py" />
