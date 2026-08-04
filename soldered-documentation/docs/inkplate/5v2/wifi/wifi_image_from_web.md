---
slug: /inkplate/5v2/wifi/image-from-web
title: Inkplate 5V2 – Draw Image from Web
sidebar_label: Draw Image from Web
id: wifi-image-from-web
---

You can draw an image from the web on Inkplate 5V2 with the `draw` function, which supports several image formats.

<InfoBox>Supported formats: JPG, BMP, and PNG.</InfoBox>

<WarningBox>JPG files **without** progressive encoding are supported.</WarningBox>

<InfoBox>If an image won't display, try re-saving it in an image editor. It's usually a format issue.</InfoBox>

---

## Drawing an image from a URL

Let's draw this image on Inkplate 5V2:
<CenteredImage src="/img/5v2/sample_image.jpg" alt="Example Image" caption="Example image by @alexisg on Wallpaper Safari" />

```cpp
#include "Inkplate.h"            // Include the Inkplate library in the sketch
#include "WiFi.h"                // Include the library for WiFi
Inkplate display(INKPLATE_3BIT); // Create an object for the Inkplate library and set it to 3-bit mode (grayscale)

const char ssid[] = "";    // Your WiFi SSID
const char *password = ""; // Your WiFi password

void setup()
{
    display.begin();        // Initialize the Inkplate library (you should call this function ONLY ONCE)
    display.clearDisplay(); // Clear the display's frame buffer
    display.display();      // Show a clear image on the display

    display.print("Connecting to WiFi...");
    display.display();

    // Connect to the WiFi network.
    WiFi.mode(WIFI_MODE_STA);
    WiFi.begin(ssid, password);
    while (WiFi.status() != WL_CONNECTED)
    {
        delay(500);
        display.print(".");
        display.display();
    }
    display.println("\nWiFi OK! Downloading...");
    display.display();
    if (!display.image.draw("https://varipass.org/destination.jpg", 0, 0, true, false))
    {
        // If something fails (for example, a wrong filename or incorrect bitmap format), write an error message on the screen.
        // REMEMBER! You can only use Windows Bitmap files with a color depth of 1, 4, 8, or 24 bits with no compression!
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
<CenteredImage src="/img/5v2/webimage.jpg" alt="Example Image" width="500px" caption="Example image" />

<FunctionDocumentation
    functionName="display.image.draw()"
    description="Draws an image from a char path."
    returnDescription="Returns true if the image was successfully drawn, otherwise false."
    parameters={[ 
    { type: "const char*", name: "path", description: "Path and filename of the image. Can be a URL (for web images) or a file path (on the microSD card)." },
    { type: "int", name: "x", description: "X-coordinate of the image's upper-left corner in the framebuffer." },
    { type: "int", name: "y", description: "Y-coordinate of the image's upper-left corner in the framebuffer." },
    { type: "uint8_t", name: "dither", description: "Dithering mode: 0 (disabled), 1 (enabled)." },
    { type: "bool", name: "invert", description: "If true, inverts colors." },
    ]}
/>

---

## Full example

<QuickLink 
  title="Inkplate5V2_Show_Pictures_From_Web.ino" 
  description="Connect to WiFi and draw an image from the web."
  url="https://github.com/SolderedElectronics/Inkplate-Arduino-library/blob/master/examples/Inkplate5V2/Advanced/WEB_WiFi/Inkplate5V2_Show_Pictures_From_Web/Inkplate5V2_Show_Pictures_From_Web.ino" 
/>