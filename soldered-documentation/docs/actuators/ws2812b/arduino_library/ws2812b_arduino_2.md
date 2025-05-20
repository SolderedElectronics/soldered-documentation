---
slug: /ws2812b/arduino/init-and-set-colors
title: Ws2812B - Initialization and Setting Colors
id: ws2812b-arduino-2
hide_title: false
---

This page contains an example of initializing the WS2812B LED strip and examples of setting colors for different effects.

---

## Initialization

To use the WS2812B LEDs, include the required [**library**](https://github.com/SolderedElectronics/Soldered-WS2812-Smart-Leds-Arduino-Library/tree/main).

<InfoBox>Our library uses the [**Adafruit Neopixel library**](https://github.com/adafruit/Adafruit_NeoPixel)</InfoBox>

Create the `pixels` object and initialize the LEDs in the `setup()` function using `pixels.begin()`.

```cpp
// Include needed libraries
#include "WS2812-SOLDERED.h"

// Which pin on the Dasduino is connected to the NeoPixels?
#define PIN       6 // If you are using Dasduino Lite, you must specify that pin as PA6
#define NUMPIXELS 10

WS2812 pixels(NUMPIXELS, PIN);

void setup()
{
    pixels.begin(); // INITIALIZE NeoPixel strip object (REQUIRED)
}
```

<FunctionDocumentation
  functionName="pixels.begin()"
  description="Initializes the WS2812 pixels, setting up communication and verifying its presence."
  returnDescription="None."
  parameters={[]}
/>

---

## Setting the LED Colors One by One

To control the colors of the LEDs, use functions such as `clear()` and `show()`, along with the primary function `setPixelColor()`. The `delay()` function can also be used for timing adjustments.

<InfoBox>The first pixel in a strand is #0, the second is #1, and so on.</InfoBox>

```cpp
#define DELAYVAL 500 // Time (in milliseconds) to pause between pixels

void loop()
{
    pixels.clear();

    for (int i = 0; i < NUMPIXELS; i++)
    { // For each pixel...

        // pixels.Color() takes RGB values, from 0,0,0 up to 255,255,255
        // Here we're using a moderately bright green color:
        pixels.setPixelColor(i, pixels.Color(0, 150, 0));

        pixels.show();

        delay(DELAYVAL); // Pause before next pass through loop
    }
}
```

<FunctionDocumentation
  functionName="pixels.clear()"
  description="Sets all pixel colors to 'off'."
  returnDescription="None"
  parameters={[]}
/>

<FunctionDocumentation
  functionName="pixels.show()"
  description="Sends the updated pixel colors to the hardware."
  returnDescription="None"
  parameters={[]}
/>

<FunctionDocumentation functionName="pixels.setPixelColor()" 
                        description="Sets the color of a specific LED in the NeoPixel strip by assigning red, green, and blue values."
                        returnDescription="None"
                        parameters={[
                            { "name": "n", "type": "uint16_t", "description": "Index of the LED to set the color for." },
                            { "name": "r", "type": "uint8_t", "description": "Red component of the color (0-255)." },
                            { "name": "g", "type": "uint8_t", "description": "Green component of the color (0-255)." },
                            { "name": "b", "type": "uint8_t", "description": "Blue component of the color (0-255)." }
                        ]} />


---

## Creating a Rainbow Effect  

To produce a smooth rainbow animation along the entire LED strip, the `rainbow()` function continuously updates pixel colors using the HSV color wheel. It cycles through different hues to create a flowing rainbow effect. The `show()` function updates the strip, while `delay()` controls the animation speed.

<!-- <CenteredImage src="/img/ws2812b/rainboww_vid.gif" alt="wow" width="700px"/> -->

<WarningBox>
Make sure to call the `rainbow()` function with a delay parameter somewhere! Example:
```cpp
void loop()
{
    rainbow(10);
}
```
</WarningBox>

```cpp
void rainbow(int wait)
{
    for (long firstPixelHue = 0; firstPixelHue < 5 * 65536; firstPixelHue += 256)
    {
        for (uint16_t i = 0; i < strip.numPixels(); i++)
        {
            int pixelHue = firstPixelHue + (i * 65536L / strip.numPixels());
            strip.setPixelColor(i, strip.gamma32(strip.ColorHSV(pixelHue)));
        }
        strip.show();
        delay(wait);
    }
}
```

<FunctionDocumentation  
  functionName="pixels.ColorHSV()"  
  description="Generates a color based on the HSV color model, with a hue ranging from 0 to 65535."  
  returnDescription="A 32-bit color value representing the requested hue."  
  parameters={[  
    { "name": "hue", "type": "uint16_t", "description": "Hue value (0-65535)." }  
  ]}  
/>  

<FunctionDocumentation  
  functionName="pixels.gamma32()"  
  description="Applies gamma correction to improve the visual accuracy of colors."  
  returnDescription="A 32-bit color value with gamma correction applied."  
  parameters={[  
    { "name": "color", "type": "uint32_t", "description": "The original 32-bit color value." }  
  ]}  
/>  

<FunctionDocumentation  
  functionName="pixels.setPixelColor()"  
  description="Sets the color of a specific LED in the NeoPixel strip using a 32-bit color value."  
  returnDescription="None"  
  parameters={[  
    { "name": "n", "type": "uint16_t", "description": "Index of the LED to set the color for." },  
    { "name": "color", "type": "uint32_t", "description": "32-bit color value representing the desired color." }  
  ]}  
/>  

---

## Cylon / Knight Rider Effect

A single bright LED moves back and forth, similar to the iconic scanner from *Knight Rider*.

<!-- <CenteredImage src="/img/ws2812b/knight_rider.gif" alt="wow" width="700px"/> -->

```cpp
void cylonEffect()
{
    int maxBrightness = 255;
    
    // Move forward
    for (int i = 0; i < NUMPIXELS; i++)
    {
        pixels.clear();
        pixels.setPixelColor(i, pixels.Color(75, 0, 130));
        pixels.setBrightness(maxBrightness);
        pixels.show();
        delay(50);
    }

    // Move backward
    for (int i = NUMPIXELS - 1; i >= 0; i--)
    {
        pixels.clear();
        pixels.setPixelColor(i, pixels.Color(75, 0, 130));
        pixels.setBrightness(maxBrightness);
        pixels.show();
        delay(50);
    }
}

void loop()
{
    while (true)
    {
        cylonEffect();
    }
}
```

<QuickLink 
  title="Simple.ino" 
  description="Example file for initializing and using the WS2812B LEDs."
  url="https://github.com/SolderedElectronics/Soldered-WS2812-Smart-Leds-Arduino-Library/blob/main/examples/native/Simple/Simple.ino" 
/>

<QuickLink 
  title="Strand_Test.ino" 
  description="Example file for using the WS2812B LEDs to create different color effects."
  url="https://github.com/SolderedElectronics/Soldered-WS2812-Smart-Leds-Arduino-Library/blob/main/examples/native/Strand_Test/Strand_Test.ino" 
/>