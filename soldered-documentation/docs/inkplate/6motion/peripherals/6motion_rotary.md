---
slug: /inkplate/6motion/peripherals/rotary-encoder
title: Rotary Encoder
id: 6motion-periph-rotary
---

The **Inkplate 6 MOTION** includes a **AS5600 magnetic rotary encoder**, which allows precise rotation tracking. It is ideal for navigating menus or fine tuning numerical input values. 

<InfoBox>This peripheral IC is mostly relevant to you only if you have the Inkplate 6 MOTION with **enclosure**, as it cointains the perfectly-placed **dial** with magnet to interface with the rotary encoder IC.</InfoBox>

<CenteredImage src="/img/inkplate_6_motion/6motion_rotary.jpg" alt="Inkplate 6 MOTION Rotary Encoder" caption="Rotary encoder on the Inkplate 6 MOTION enclosure" width="600px" />

The dial made to interface with the rotary encoder is **transparent**! It's made this way so that the **first** onboard [**RGB LED**](/inkplate/6motion/peripherals/leds/) can change it's color when it lights up!

<InfoBox>The **AS5600** implementation in the Inkplate library uses this library from **Rob Tillaart**:<QuickLink 
  title="AS5600" 
  description="Arduino library for AS5600 and AS5600L magnetic rotation meter"
  url="https://github.com/RobTillaart/AS5600"/></InfoBox>

---

## Initializaiton

Before using the rotary encoder, it must be **powered on and initialized**.

```cpp
// Enable power to the rotary encoder
inkplate.peripheralState(INKPLATE_PERIPHERAL_ROTARY_ENCODER, true);
delay(100);

// Initialize rotary encoder
inkplate.rotaryEncoder.begin();
```
<FunctionDocumentation
  functionName="inkplate.rotaryEncoder.begin()"
  description="Initializes the rotary encoder sensor for use. This function must be called before retrieving values."
  returnDescription="Returns true if initialization was successful, otherwise false."
/>

---

## Reading the rotation angle

To get the current angle of the rotary encoder in degrees:

```cpp
int currentValue = (int)(inkplate.rotaryEncoder.rawAngle() * AS5600_RAW_TO_DEGREES);
```

This will return the current rotational position of the encoder.

<FunctionDocumentation
  functionName="inkplate.rotaryEncoder.rawAngle()"
  description="Gets the raw angle value from the rotary encoder, which can be converted to degrees or radians."
  returnDescription="Returns the raw angle as a 12-bit integer (0-4095)."
/>

You can use the following factors for conversion:
| Conversion | Constant | Value |
|------------|--------------------------|---------------------------|
| **Raw to Degrees** | `AS5600_RAW_TO_DEGREES` | `360.0 / 4096` (`0.087890625`) |
| **Raw to Radians** | `AS5600_RAW_TO_RADIANS` | `PI * 2.0 / 4096` (`0.00153398079`) |


---

## Full Example

This example tracks the rotary encoder's angle and updates the display when the angle changes by 2 degrees:
<QuickLink title="Inkplate_6_MOTION_Rotary_Encoder.ino"
description="Full rotary encoder example in the Inkplate library"
url="https://github.com/SolderedElectronics/Inkplate_Motion_Arduino_Library/blob/main/examples/Inkplate6Motion/Advanced/Sensors_Other/Inkplate_6_MOTION_Rotary_Encoder/Inkplate_6_MOTION_Rotary_Encoder.ino"
/>

