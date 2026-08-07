---
slug: /inkplate/6color/wifi/image-from-web
title: Inkplate 6COLOR – Draw Image from Web
sidebar_label: Draw Image from Web
id: wifi-image-from-web
---

Drawing an image from the web on Inkplate 6COLOR is simple using the `draw` function, which supports multiple image formats.

<InfoBox>Supported formats: JPG, BMP, and PNG.</InfoBox>

<WarningBox>JPG files **without** progressive encoding are supported.</WarningBox>

<InfoBox>If you experience issues displaying an image, try re-saving it with an image editing program. The issue is usually related to the image format.</InfoBox>

---

## Drawing an image from a URL

Let's draw this image on Inkplate 6COLOR:
<CenteredImage src="/img/6color/splash.jpg" alt="Example Image" caption="Example image" width="800px" />

```cpp
#include "HTTPClient.h" //Include library for HTTPClient
#include "Inkplate.h"   //Include Inkplate library to the sketch
#include "WiFi.h"       //Include library for WiFi
Inkplate display;       // Create an object on Inkplate library

const char ssid[] = ""; // Your WiFi SSID
const char *password = "";     // Your WiFi password

void setup()
{
    display.begin();        // Init Inkplate library (you should call this function ONLY ONCE)
    display.clearDisplay(); // Clear frame buffer of display
    display.display();      // Put clear image on display

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
    if (!display.image.draw("https://varipass.org/neowise_mono.bmp", 0, 0, true, false))
    {
        // If is something failed (wrong filename or wrong bitmap format), write error message on the screen.
        // REMEMBER! You can only use Windows Bitmap file with color depth of 1, 4, 8 or 24 bits with no compression!
        display.println("Image open error");
        display.display();
    }
    display.display();

    if (!display.image.draw("https://varipass.org/neowise.bmp", 0, 0, true, false))
    {
        // If is something failed (wrong filename or wrong bitmap format), write error message on the screen.
        // REMEMBER! You can only use Windows Bitmap file with color depth of 1, 4, 8 or 24 bits with no compression!
        display.println("Image open error");
        display.display();
    }
    display.display();

    display.clearDisplay();
    delay(3000);

    // Try to load image and display it on e-paper at position X=0, Y=100
    // NOTE: Both drawJpegFromWeb methods allow for an optional fifth "invert" parameter. Setting this parameter to
    // true will flip all colors on the image, making black white and white black. forth parameter will dither the
    // image.
    if (!display.image.draw("https://varipass.org/destination.jpg", 0, 25, true, false))
    {
        // If is something failed (wrong filename or format), write error message on the screen.
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
    functionName="display.image.draw()"
    description="This function draws an image from the specified char path."
    returnDescription="Returns true if the image was successfully drawn, otherwise false."
    parameters={[ 
        { type: "const char*", name: "path", description: "Path and filename of the image. Can be a URL (for web images) or a file path (on the microSD card)." },
        { type: "int", name: "x", description: "X-coordinate of the image's upper-left corner in the framebuffer." },
        { type: "int", name: "y", description: "Y-coordinate of the image's upper-left corner in the framebuffer." },
        { type: "bool", name: "dither", description: "Dithering mode: false (disabled), true (enabled). Defaults to true." },
        { type: "bool", name: "invert", description: "If true, inverts colors." },
    ]}
/>

---

## Full example

<QuickLink 
  title="Inkplate6COLOR_Show_Pictures_From_Web.ino" 
  description="Connect to WiFi and draw an image from the web." 
  url="https://github.com/SolderedElectronics/Inkplate-Arduino-library/blob/master/examples/Inkplate6COLOR/Advanced/WEB_WiFi/Inkplate6COLOR_Show_Pictures_From_Web/Inkplate6COLOR_Show_Pictures_From_Web.ino" 
/>
