---
slug: /inkplate/6color/wifi/image-from-web
title: Draw Image from Web
id: wifi-image-from-web
---

Drawing an image from the web on Inkplate 6COLOR is simple using the `draw` function, which supports multiple image formats.

<InfoBox>Supported formats: JPG, BMP, and PNG.</InfoBox>

<WarningBox>JPG files **without** progressive encoding are supported.</WarningBox>

<InfoBox>If you experience issues displaying an image, try re-saving it with an image editing program. The issue is usually related to the image format.</InfoBox>

---

## Drawing an Image from a URL

Let's draw this image on Inkplate 6COLOR:
<CenteredImage src="/img/6color/splash.jpg" alt="Example Image" caption="Example image" width="800px" />

```cpp
#include "Inkplate.h"            // Include the Inkplate library in the sketch
#include "WiFi.h"                // Include the WiFi library
Inkplate display; // Create an Inkplate object and set the library to 1-bit mode (BW)

const char ssid[] = "";    // Your WiFi SSID
const char *password = ""; // Your WiFi password

void setup()
{
  Serial.begin(115200);
    display.begin();        // Initialize the Inkplate library (you should call this function ONLY ONCE)
    display.clearDisplay(); // Clear the display's frame buffer
    display.display();

    Serial.print("Connecting to WiFi...");

    // Connect to the WiFi network.
    WiFi.mode(WIFI_MODE_STA);
    WiFi.begin(ssid, password);
    while (WiFi.status() != WL_CONNECTED)
    {
        delay(500);
        Serial.print(".");
    }
    Serial.println("\nWiFi OK! Downloading...");
    if (!display.drawImage("https://i.imgur.com/EjIOxx7.jpeg", 0, 0, false, false))
    {
        // If something fails (wrong filename or incorrect bitmap format), write an error message on the screen.
        // REMEMBER! You can only use a Windows Bitmap file with a color depth of 1, 4, 8, or 24 bits with no compression!
        display.println("Image open error");
        display.display();
    }
    display.display();
    WiFi.mode(WIFI_OFF);
}

void loop()
{
    // Nothing...
}
```

<CenteredImage src="/img/6color/example_image.jpg" alt="Example Image" width="500px" caption="Example image" />

<FunctionDocumentation
    functionName="inkplate.drawImage()"
    description="This function draws an image from the specified char path."
    returnDescription="Returns true if the image was successfully drawn, otherwise false."
    parameters={[ 
        { type: "const char*", name: "path", description: "Path and filename of the image. Can be a URL (for web images) or a file path (on the microSD card)." },
        { type: "int", name: "x", description: "X-coordinate of the image's upper-left corner in the framebuffer." },
        { type: "int", name: "y", description: "Y-coordinate of the image's upper-left corner in the framebuffer." },
        { type: "uint8_t", name: "dither", description: "Dithering mode: 0 (disabled), 1 (enabled)." },
        { type: "bool", name: "invert", description: "If true, inverts colors." },
    ]}
/>