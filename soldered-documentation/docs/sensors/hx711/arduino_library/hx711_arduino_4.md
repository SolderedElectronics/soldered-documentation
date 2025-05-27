---
slug: /hx711/arduino/deep-sleep
title: "HX711 Load Cell Amplifier \u2013 Arduino deep sleep"
id: hx711-arduino-4
hide_title: false
---
This page contains a simple example of shutting down the HX711 between readings (deep sleep).

---

In this code snippet, the `loop()` function wakes up the HX711 from deep sleep, takes a raw reading, prints the result to the Serial Monitor, and then puts the HX711 back into deep sleep mode. The program waits for 15 seconds before repeating the process.

<WarningBox>Ensure that the correct pins for `DAT` and `SCK` are defined before initialization. </WarningBox>

```cpp
// Include the library
#include "HX711-SOLDERED.h"

// Define pins used for DAT and SCK here
#define PIN_DAT 4
#define PIN_SCK 3

// Create the HX711 object on the right pins
HX711 hx711(PIN_DAT, PIN_SCK);

void setup()
{
    Serial.begin(115200); // for debugging

    // Initialize HX711
    hx711.begin();

    // Wait a bit until it fully initializes
    delay(200);
}

void loop()
{
    // Wake up the HX711 from deep sleep
    hx711.setDeepSleep(false);

    // Wait a bit until it fully initializes
    delay(200);

    // Make a raw reading and store it in a variable
    long reading = hx711.getRawReading();

    // Print the reading
    Serial.print("HX711 Reading: ");
    Serial.println(reading);

    // Place the HX711 in deep sleep
    hx711.setDeepSleep(true);

    // Wait a long while until the next reading
    delay(15000);
}
```

<FunctionDocumentation functionName="hx711.begin()" description="Initializes the HX711 load-cell amplifier, setting up communication and verifying its presence." returnDescription="None." parameters={[]} />

<FunctionDocumentation 
  functionName="hx711.setDeepSleep()" 
  description="Puts the HX711 load-cell amplifier into deep sleep mode or wakes it up, depending on the input parameter." 
  returnDescription="None."
  parameters={[
    { type: "bool", name: "sleep", description: "True to enable deep sleep mode, false to wake the HX711 from sleep." }
  ]}
/>

<CenteredImage src="/img/hx711/hx711_deepsleep.png" alt="Serial Monitor" caption="HX711 Sensor Serial Monitor output"/>

<QuickLink 
  title="deepSleep.ino" 
  description="Example file for utilizing deep sleep while using the HX711"
  url="https://github.com/SolderedElectronics/Soldered-HX711-ADC-For-Weight-Scales-Arduino-Library/blob/main/examples/deepSleep/deepSleep.ino" 
/>