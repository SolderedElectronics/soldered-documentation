---
slug: /inkplate/6/wifi/image-from-web
title: Inkplate 6 – Draw Image from Web
id: wifi-image-from-web
---

Drawing an image from the web on Inkplate 6 is simple using the `draw` function, which supports multiple image formats.

<InfoBox>Supported formats: JPG, BMP, and PNG.</InfoBox>

<WarningBox>JPG files **without** progressive encoding are supported.</WarningBox>

<InfoBox>If you experience issues displaying an image, try re-saving it with an image editing program. The issue is usually related to the image format.</InfoBox>

---

## Drawing an Image from a URL

Let's draw this image of the Eurodom building in Osijek, Croatia, on Inkplate 6:
<CenteredImage src="/img/6/sample_image.png" alt="Example Image" caption="Example image by Michael Reschke on Wiki Media" />

```cpp
#include "Inkplate.h"            // Include the Inkplate library in the sketch
#include "WiFi.h"                // Include the library for WiFi
Inkplate display(INKPLATE_3BIT); // Create an object for the Inkplate library and set it to 1-bit mode (BW)

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
    if (!display.drawImage("https://upload.wikimedia.org/wikipedia/commons/b/b5/800x600_Wallpaper_Blue_Sky.png", 0, 0, false, false))
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

<CenteredImage src="/img/6/example_image.jpg" alt="Example Image" width="500px" caption="Example image" />


<FunctionDocumentation
    functionName="inkplate.drawImage()"
    description="This function draws an image from a char pointer."
    returnDescription="Returns true if the image was successfully drawn; otherwise, false."
    parameters={[ 
    { type: "const char*", name: "path", description: "Path and filename of the image. It can be a URL (for web images) or a file path (on the microSD card)." },
    { type: "int", name: "x", description: "X-coordinate of the image's upper-left corner in the framebuffer." },
    { type: "int", name: "y", description: "Y-coordinate of the image's upper-left corner in the framebuffer." },
    { type: "uint8_t", name: "dither", description: "Dithering mode: 0 (disabled) or 1 (enabled)." },
    { type: "bool", name: "invert", description: "If true, inverts the colors." },
    ]}
/>

---

## Full Example

<QuickLink 
  title="Inkplate6_Image_From_Web.ino" 
  description="Connect to WiFi and draw an image from the web."
  url="https://github.com/SolderedElectronics/Inkplate-Arduino-library/blob/master/examples/Inkplate6/Advanced/WEB_WiFi/Inkplate6_Show_Pictures_From_Web/Inkplate6_Show_Pictures_From_Web.ino" 
/>