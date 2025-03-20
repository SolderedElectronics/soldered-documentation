---
slug: /ws2812b/arduino/brightness-control
title: Brightness Control
id: ws2812b-arduino-3 
hide_title: False
---

# Brightness Control  

This page contains examples of **brightness effects** for the WS2812B LED strip. These effects use **variable brightness levels** to create visually appealing animations like breathing, twinkling, and smooth transitions.  

## Adjusting Brightness  

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
        if (random(10) > 7) // 30% chance of twinkling
        {
            pixels.setBrightness(random(50, 255)); // Vary brightness randomly
            pixels.setPixelColor(i, pixels.Color(75, 0, 130)); // Dark purple
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