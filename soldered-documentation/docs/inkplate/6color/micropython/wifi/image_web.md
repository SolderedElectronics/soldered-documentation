---  
slug: /inkplate/6color/micropython/wifi/draw_web_image
title: Inkplate 6COLOR – Draw Image from Web
sidebar_label: Draw Image from Web
id: drawing-img-web
hide_title: false  
---

Example showing how to connect to WiFi and render an image fetched from URL using `drawImage`.

<InfoBox>Supported formats: JPG, BMP, and PNG.</InfoBox>

<WarningBox>JPG files **without** progressive encoding are supported.</WarningBox>

<InfoBox>If you experience issues displaying an image, try re-saving it with an image editing program. The issue is usually related to the image format.</InfoBox>

## Drawing an Image 

<CenteredImage src="/img/6color/wifi-img-example-mp.jpg" alt="Example image to show on inkplate" caption="Example image" />

```python
# Include needed libraries
import network
import time
from inkplate6COLOR import Inkplate

# WiFi credentials (replace with your own)
SSID = "YOUR_SSID_HERE"
PASSWORD = "YOUR_PASSWORD_HERE"

# Connects to a WiFi network using given SSID and PASSWORD
def do_connect():
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print("Connecting to network...")
        sta_if.active(True)
        sta_if.connect(SSID, PASSWORD)

        timeout = 30  # seconds
        start = time.ticks_ms()
        while not sta_if.isconnected():
            if time.ticks_diff(time.ticks_ms(), start) > timeout * 1000:
                print("Failed to connect within timeout")
                return False
            time.sleep(0.5)
    print("Network config:", sta_if.ifconfig())
    return True

inkplate = Inkplate()

inkplate.begin()

# Connect to WiFi
if not do_connect():
    raise SystemExit("WiFi connection failed")

# Example usage:
inkplate.drawImage(
    "https://i.imgur.com/nSExTGr.jpeg",  # URL to image
    0, 0,                                # X, Y position
    invert=False,                        # Do not invert colors
    dither=True,                         # Enable dithering
    kernel_type=Inkplate.KERNEL_FLOYD_STEINBERG  # Dithering algorithm
)

# Show the image from the internal buffer
inkplate.display()
```

<CenteredImage src="/img/6color/web-img.jpg" alt="Expected output on Inkplate display" caption="Example image displayed on Inkplate" />

<FunctionDocumentation
    functionName="inkplate.drawImage()"
    description="This function draws an image from the specified char path (either web URL or local file path)"
    returnDescription="None"
    parameters={[ 
        { type: "string", name: "path", description: "Path and filename of the image. Can be a URL (for web images) or a file path (on the microSD card)." },
        { type: "int", name: "x0", description: "X-coordinate of the image's upper-left corner in the framebuffer." },
        { type: "int", name: "y0", description: "Y-coordinate of the image's upper-left corner in the framebuffer." },
        { type: "bool", name: "invert", description: "If true, inverts colors." },
        { type: "bool", name: "dither", description: "Dithering mode: 0 (disabled), 1 (enabled)." },
        { type: "int", name: "kernel_type", description: "Specifies dithering algorithm to use."}
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