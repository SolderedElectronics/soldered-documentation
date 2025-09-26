---  
slug: /inkplate/2/micropython/wifi/display-img-web
title: Inkplate 2 – Draw Image from Web
sidebar_label: Draw Image from Web
id: drawing-img-web
hide_title: false  
---

Example showing how to connect to WiFi and render an image fetched from URL using `drawImage`.

<InfoBox>Supported image formats: JPG, BMP, and PNG.</InfoBox>

<WarningBox>JPG files **without** progressive encoding are supported.</WarningBox>

<InfoBox>If you experience issues displaying an image, try re-saving it with an image editing program. The issue is usually related to the image format.</InfoBox>

## Drawing an Image 

<CenteredImage src="/img/inkplate_2/inkplate2-example-img.jpg" alt="Example image" caption="Example image to display on Inkplate" width="212px"/>

```python
from inkplate2 import Inkplate
import network
import time

# WiFi credentials (replace with your own)
SSID = "YOUR_SSID_HERE"
PASSWORD = "YOUR_PASSWORD_HERE"

# Create Inkplate object in 2-bit (grayscale) mode
inkplate = Inkplate()

# Initialize the display, needs to be called only once
inkplate.begin()

# Connect to WiFi (process explained on previous pages)
if not do_connect():
    raise SystemExit("WiFi connection failed")

# Example usage
drawLenght=time.ticks_ms()
inkplate.drawImage(
    "https://i.imgur.com/VSRtgBr.jpeg",  # URL to image
    0, 0,                                # X, Y position
    dither = True						 # Enable/Disable dithering
)

# Show the image from the internal buffer
inkplate.display()
```

<CenteredImage src="/img/inkplate_2/img-web.jpg" alt="Expected output on Inkplate display" caption="Example image displayed on Inkplate with Dithering enabled" />

<CenteredImage src="/img/inkplate_2/img-web-no-dither.jpg" alt="Expected output on Inkplate display" caption="Example image displayed on Inkplate without Dithering" />

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
- JPG: ~3 seconds (or ~5s with dithering)
- PNG: ~4 seconds (or ~6s with dithering)
- BMP: ~6 seconds (or ~7s with dithering)
- Maximum image file size: ~800kB
</InfoBox>