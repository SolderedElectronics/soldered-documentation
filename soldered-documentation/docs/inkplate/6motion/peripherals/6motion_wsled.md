---
slug: /inkplate/6motion/peripherals/leds
title: RGB LEDs
id: 6motion-periph-wsled
---


The **Inkplate 6 MOTION** includes **two WS2812 RGB LEDs**, allowing full-color control for notifications, status indicators, or creative lighting effects.

<InfoBox>The **WS2812** implementation in the Inkplate library uses this library from **Adafruit**:<QuickLink 
  title="Adafruit NeoPixel Library" 
  description="The original library which is included in the Inkplate 6 MOTION library"
  url="https://github.com/adafruit/Adafruit_NeoPixel"/></InfoBox>

---

## Configuration

Before using the LEDs, they must be **powered on and initialized**.

<InfoBox>**RGB LEDs** sensor must be powered on via `peripheralState`. See this page for more details: <QuickLink 
  title="Peripheral basics" 
  description="How to power peripherals on and off on Inkplate 6 MOTION"
  url="/inkplate/6motion/peripherals/introduction#powering-on" 
/></InfoBox>

'begin' initializes the NeoPixel library. You can use `setBrightness` as a general setting for the brightness of both of the LEDs:

```cpp
// Power on LEDs
inkplate.peripheralState(INKPLATE_PERIPHERAL_WS_LED, true);

// Initialize LEDs
inkplate.led.begin();

// Set brightness (0-255)
inkplate.led.setBrightness(125);
```

<FunctionDocumentation
  functionName="inkplate.led.begin()"
  description="Configures the NeoPixel LED pin for output. This function must be called before setting LED colors."
  returnDescription="none"
/>

<FunctionDocumentation
  functionName="inkplate.led.setBrightness()"
  description="Adjusts the LED brightness level. The brightness change takes effect on the next `show()` call."
  returnDescription="none"
  parameters={[
    { type: 'uint8_t', name: 'b', description: "Brightness level (0 = off, 255 = brightest)." },
  ]}
/>

---

## Changing Colors

To set a specific color on an LED, use `setPixelColor()`, then call `show()` to apply changes.

```cpp
// Set first LED to red
inkplate.led.setPixelColor(0, 150, 0, 0);
// Set second LED to green
inkplate.led.setPixelColor(1, 0, 150, 0);

// Apply changes
inkplate.led.show();
```


<FunctionDocumentation
  functionName="inkplate.led.setPixelColor()"
  description="Sets an individual LED's color using separate red, green, and blue components."
  returnDescription="none"
  parameters={[
    { type: 'uint16_t', name: 'n', description: "Index of the LED (starting from 0)." },
    { type: 'uint8_t', name: 'r', description: "Red brightness (0-255)." },
    { type: 'uint8_t', name: 'g', description: "Green brightness (0-255)." },
    { type: 'uint8_t', name: 'b', description: "Blue brightness (0-255)." },
  ]}
/>

<FunctionDocumentation
  functionName="inkplate.led.show()"
  description="Sends the color data from RAM to the NeoPixels, applying the changes set by `setPixelColor()`."
  returnDescription="none"
/>

---

## Full Example

For an in-depth example, check out the Inkplate library:

<QuickLink title="Inkplate_6_MOTION_WSLED.ino"
description="Full WS2812 LED example in the Inkplate library"
url="https://github.com/SolderedElectronics/Inkplate_Motion_Arduino_Library/blob/main/examples/Inkplate6Motion/Advanced/Sensors_Other/Inkplate_6_MOTION_WSLED/Inkplate_6_MOTION_WSLED.ino"
/>

