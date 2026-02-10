---
slug: /inkplate/6color/wifi/image-from-web
title: Inkplate 13SPECTRA – Draw Image from Web
sidebar_label: Draw Image from Web
id: wifi-image-from-web
---

Drawing an image from the web on Inkplate 6COLOR is simple using the `draw` function, which supports multiple image formats.

<InfoBox>Supported formats: JPG, BMP, and PNG.</InfoBox>

<WarningBox>JPG files **without** progressive encoding are supported.</WarningBox>

<InfoBox>If you experience issues displaying an image, try re-saving it with an image editing program. The issue is usually related to the image format.</InfoBox>

---

## Draw an Image from a URL

Let's draw this image on Inkplate 13SPECTRA:

```cpp
include "HTTPClient.h" //Include library for HTTPClient
#include "Inkplate.h"   //Include Inkplate library to the sketch
#include "WiFi.h"       //Include library for WiFi
Inkplate inkplate;       // Create an object on Inkplate library and also set library into 1 Bit mode (BW)

const char ssid[] = "Soldered Electronics"; // Your WiFi SSID
const char *password = "dasduino";     // Your WiFi password

void setup()
{
    inkplate.begin();        // Init Inkplate library (you should call this function ONLY ONCE)
    inkplate.clearDisplay(); // Clear frame buffer of display
    inkplate.display();      // Put clear image on display

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

    // Draw the first image from web.
    // Monochromatic bitmap with 1 bit depth. Images like this load quickest.
    // NOTE: Both drawImage methods allow for an optional fifth "invert" parameter. Setting this parameter to true
    // will flip all colors on the image, making black white and white black. This may be necessary when exporting
    // bitmaps from certain softwares. Forth parameter will dither the image. Photo taken by: Roberto Fernandez
    if (!inkplate.image.draw("https://varipass.org/neowise_mono.bmp", 0, 0, true, false))
    {
        // If is something failed (wrong filename or wrong bitmap format), write error message on the screen.
        // REMEMBER! You can only use Windows Bitmap file with color depth of 1, 4, 8 or 24 bits with no compression!
        inkplate.println("Image open error");
        inkplate.display();
    }
    inkplate.display();    
    WiFi.mode(WIFI_OFF);
}

void loop()
{
    // Nothing...
}
```

[IMAGE PLACEHOLDER - 13spectra display output]

<FunctionDocumentation
    functionName="inkplate.image.draw()"
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