---
slug: /slider-potentiometer/initialization-QWIIC-version
title: "Slider Potentiometer \u2013 Initialization QWIIC version"
id: slider-potentiometer-arduino-3
hide_title: false
---
This page contains simple examples illustrating how to take analog slider measurements using the Slider Potentiometer with Qwiic.

---

## Initialization QWIIC version

To start using the **Slider Potentiometer Breakout**, you need to connect it to your microcontroller. The potentiometer acts as a voltage divider, and its output can be read through an analog pin on your microcontroller.

Here’s how you can set it up:

```cpp
#include "Slider-potentiometer-easyC-SOLDERED.h"

// Declare the sensor object
sliderPot slider;

void setup()
{
    // Initialize serial communication via UART
    Serial.begin(115200);

    // Initialize the sensor
    slider.begin();
}
```

---

## Reading slider data

To start reading data obtained by moving the slider, follow the code given below.

```cpp
    Serial.print("Raw value of slider potentiometer: "); // Print information message
    Serial.println(slider.getValue()); // Prints raw value of slider potentiometer

    Serial.print("Minimum value of slider potentiometer: "); // Print information message
    Serial.println(slider.minValue()); // Prints minimum value of potentiometer

    Serial.print("Maximum value of slider potentiometer: "); // Print information message
    Serial.println(slider.maxValue()); // Prints maximum value of potentiometer

    Serial.print("Percent value of slider potentiometer: "); // Print information message
    Serial.println(slider.getPercentage()); // Prints percent value of slider potentiometer
    delay(1000);
```

---

<!-- <CenteredImage src="/img/slider-potentiometer/qwiic_slider.gif" alt="Slider potentiometer example of usage" caption="Slider potentiometer (Qwiic) example of usage" /> -->

<CenteredImage src="/img/slider-potentiometer/result1QWIIC.png" alt="Slider potentiometer(Qwiic) readings 1" caption="Serial Monitor output for position 1" />
<CenteredImage src="/img/slider-potentiometer/result2QWIIC.png" alt="Slider potentiometer(Qwiic) readings 2" caption="Serial Monitor output for position 2" />

---

## Full example

Try all of the above-mentioned functions in this full example which prints out the measured slider potentiometer data over Serial at 115200 baud:

```cpp
#include "Slider-potentiometer-easyC-SOLDERED.h"

// Declare the sensor object
sliderPot slider;

void setup()
{
    // Initialize serial communication via UART
    Serial.begin(115200);

    // Initialize the sensor
    slider.begin();
}

void loop()
{
    Serial.print("Raw value of slider potentiometer: "); // Print information message
    Serial.println(slider.getValue()); // Prints raw value of slider potentiometer

    Serial.print("Minimum value of slider potentiometer: "); // Print information message
    Serial.println(slider.minValue()); // Prints minimum value of potentiometer

    Serial.print("Maximum value of slider potentiometer: "); // Print information message
    Serial.println(slider.maxValue()); // Prints maximum value of potentiometer

    Serial.print("Percent value of slider potentiometer: "); // Print information message
    Serial.println(slider.getPercentage()); // Prints percent value of slider potentiometer
    delay(1000);
}
```