---
slug: /ws2812b/arduino/brightness-control
title: Brightness Control and Effects
id: ws2812b-arduino-3 
hide_title: False
---

This page contains examples of **brightness effects** for the WS2812B LED strip. These effects use **variable brightness levels** to create visually appealing animations like breathing, twinkling, and smooth transitions.  

## Adjusting Brightness

To use the WS2812B LEDs, include the required [**library**](https://github.com/SolderedElectronics/Soldered-WS2812-Smart-Leds-Arduino-Library/tree/main).

<InfoBox>Our library is using the [**Adafruit Neopixel library**](https://github.com/adafruit/Adafruit_NeoPixel)</InfoBox>

To modify the brightness of the LEDs, use the `setBrightness()` function before calling `show()`.  

<InfoBox>Brightness values range from 0 (off) to 255 (maximum brightness).</InfoBox>  

```cpp
// Set brightness to 50%
pixels.setBrightness(128);
pixels.show();
```

<FunctionDocumentation
functionName="pixels.setBrightness()"
description="Adjusts the brightness of all LEDs in the strip."
returnDescription="None"
parameters={[
{ "name": "brightness", "type": "uint8_t", "description": "Brightness level (0-255)." }
]}
/>

## Other functions used in the examples

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

## Rainbow Fade Effect

A smooth brightness-controlled rainbow animation cycles across the LED strip. 

```cpp
void rainbowFade(int wait)
{
    for (long firstPixelHue = 0; firstPixelHue < 5 * 65536; firstPixelHue += 256)
    {
        for (uint16_t i = 0; i < pixels.numPixels(); i++)
        {
            int pixelHue = firstPixelHue + (i * 65536L / pixels.numPixels());
            pixels.setPixelColor(i, pixels.gamma32(pixels.ColorHSV(pixelHue)));
        }
        pixels.setBrightness(abs(255 - (firstPixelHue / 256) % 256)); // Create a brightness fade
        pixels.show();
        delay(wait);
    }
}

void loop()
{
    while (true)
    {
        rainbowFade(10);
    }
}
```

---

## Breathing Effect

This effect gradually fades LEDs in and out in a smooth, pulsating motion.

```cpp
void breathingEffect()
{
    float brightness;
    for (float t = 0; t < 3.14; t += 0.05) // Use a sine wave for smooth breathing effect
    {
        brightness = (exp(sin(t)) - 0.36787944) * 108.0; // Adjusted sine wave for smooth brightness
        pixels.setBrightness((int)brightness);
        for (int i = 0; i < NUMPIXELS; i++)
        {
            pixels.setPixelColor(i, pixels.Color(75, 0, 130)); // Dark purple
        }
        pixels.show();
        delay(20);
    }
}

void loop()
{
    while (true)
    {
        breathingEffect();
    }
}
```

---

## Twinkling Stars Effect

This effect randomly selects LEDs t o twinkle with varying brightness, simulating a starry sky.

```cpp
void twinklingStars()
{
    pixels.clear();
    for (int i = 0; i < NUMPIXELS; i++)
    {
        int randomBrightness = random(0, MAX_BRIGHTNESS); // Random brightness value
        if (random(0, 10) > 3) // Random chance of turning on the LED
        {
            pixels.setPixelColor(i, pixels.Color(75, 0, 130)); // Dark purple color
            pixels.setBrightness(randomBrightness); // Set random brightness
        }
        else
        {
            pixels.setPixelColor(i, pixels.Color(0, 0, 0)); // Turn off LED
        }
    }
    pixels.show();
    delay(100);
}

void loop()
{
    while (true)
    {
        twinklingStars();
    }
}
```

---

## Full example

```cpp
// Include the library
#include "WS2812-SOLDERED.h"

// Pin connected to the NeoPixels
#define PIN       25
#define NUMPIXELS 10

WS2812 pixels(NUMPIXELS, PIN);

#define DELAYVAL 100   // Speed of twinkling (smaller = faster)
#define MAX_BRIGHTNESS 255 // Maximum brightness level

// Function to create a rainbow fade effect
void rainbowFade(int wait)
{
    for (long firstPixelHue = 0; firstPixelHue < 5 * 65536; firstPixelHue += 256)
    {
        for (uint16_t i = 0; i < pixels.numPixels(); i++)
        {
            int pixelHue = firstPixelHue + (i * 65536L / pixels.numPixels());
            pixels.setPixelColor(i, pixels.gamma32(pixels.ColorHSV(pixelHue)));
        }
        pixels.setBrightness(abs(255 - (firstPixelHue / 256) % 256)); // Create a brightness fade
        pixels.show();
        delay(wait);
    }
}

// Function to create a breathing effect
void breathingEffect()
{
    float brightness;
    for (float t = 0; t < 3.14; t += 0.05) // Use a sine wave for smooth breathing effect
    {
        brightness = (exp(sin(t)) - 0.36787944) * 108.0; // Adjusted sine wave for smooth brightness
        pixels.setBrightness((int)brightness);
        for (int i = 0; i < NUMPIXELS; i++)
        {
            pixels.setPixelColor(i, pixels.Color(75, 0, 130)); // Dark purple
        }
        pixels.show();
        delay(20);
    }
}

// Function to create twinkling star effect
void twinklingStars()
{
    // Randomly turn on and off LEDs
    for (int i = 0; i < NUMPIXELS; i++)
    {
        int randomBrightness = random(0, MAX_BRIGHTNESS); // Random brightness value
        if (random(0, 10) > 3) // Random chance of turning on the LED
        {
            pixels.setPixelColor(i, pixels.Color(75, 0, 130)); // Dark purple color
            pixels.setBrightness(randomBrightness); // Set random brightness
        }
        else
        {
            pixels.setPixelColor(i, pixels.Color(0, 0, 0)); // Turn off LED
        }
    }
    pixels.show();
    delay(DELAYVAL); // Delay for twinkling effect speed
}

void setup()
{
    pixels.begin(); // Initialize NeoPixel strip object (REQUIRED)
}

void loop()
{
    // Choose the effect to run
    rainbowFade(10);           // Rainbow effect with a 10ms delay between color changes
    breathingEffect();         // Breathing effect with dark purple color
    twinklingStars();           // Twinkling stars effect
}
```