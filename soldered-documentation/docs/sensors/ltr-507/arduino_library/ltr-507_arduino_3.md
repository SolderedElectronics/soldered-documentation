---
slug: /ltr-507/arduino/light-and-proximity
title: Ltr 507 - Reading Light and Proximity
sidebar_label: Reading Light and Proximity
id: ltr-507-arduino-3
hide_title: false
---

This page contains simple examples with function documentation on how to use the **LTR-507 sensor** to read **ambient light** levels and **proximity**.

---

## Reading Light

```cpp
// Include needed libraries
#include "LTR-507-Light-And-Proximity-Sensor-SOLDERED.h"

// Create light_sensor object
LTR507 light_sensor;

void setup()
{
    // Begin Serial for debugging purposes
    Serial.begin(115200);

    // Initialize the light_sensor!
    light_sensor.init();
}

void loop()
{
    // Create a local variable for the light reading
    uint16_t lightReading;

    // Obtain the reading!
    lightReading = light_sensor.getLightIntensity();
    
    // Print the reading
    Serial.print("Light sensor reading: ");
    Serial.println(lightReading);

    // Wait a bit before taking the next reading so that the output isn't too fast
    delay(1000);
}
```

<FunctionDocumentation functionName="light_sensor.getLightIntensity()" description="Reads the ambient light intensity in lux from the LTR-507 sensor." returnDescription="A 16-bit integer (lux)." parameters={[]} />

<InfoBox> The higher the lux value, the brighter the environment. A lower lux value means a darker setting. This can be useful for automatic brightness adjustment, environment monitoring, and smart lighting applications. </InfoBox>

<CenteredImage src="/img/ltr-507/light_noo_hand.png" alt="Serial Monitor" caption="Sensor with a connected IR LED in open air" width="700px"/>
<CenteredImage src="/img/ltr-507/serial_light_no_hand.png" alt="Serial Monitor" caption="Serial Monitor output" width="700px"/>

<CenteredImage src="/img/ltr-507/light_with_hand.png" alt="Serial Monitor" caption="Sensor covered by a hand" width="700px"/>
<CenteredImage src="/img/ltr-507/serial_light_with_hand.png" alt="Serial Monitor" caption="LTR-507 Light Sensor Serial Monitor output" width="700px"/>

<QuickLink title="readLight.ino" description="Example file for reading the light sensor value using the LTR-507" url="https://github.com/SolderedElectronics/Soldered-Digital-Light-Sensor-Arduino-Library/blob/main/examples/readLight/readLight.ino" />

---

## Reading Proximity

The LTR-507 measures the **infrared reflection** from nearby objects to determine their **proximity**. This is useful for **gesture detection**, **object detection**, and **automatic triggering systems**.

<WarningBox>**An IR LED must be connected!**</WarningBox>

```cpp
// Include the library
#include "LTR-507-Light-And-Proximity-Sensor-SOLDERED.h"

LTR507 light_sensor; // Create light_sensor object

void setup()
{
    Serial.begin(115200); // Initialize Serial Monitor
    light_sensor.init();  // Initialize the light_sensor
}

void loop()
{
    uint16_t proximityReading = light_sensor.getProximity(); // Read proximity value

    Serial.print("Proximity reading: ");
    Serial.println(proximityReading); // Print proximity value to Serial Monitor

    delay(1000); // Wait before the next reading
}
```

<FunctionDocumentation functionName="light_sensor.getProximity()" description="Reads the proximity value based on infrared reflection from nearby objects." returnDescription="A 16-bit integer." parameters={[]} />

<CenteredImage src="/img/ltr-507/proximity_no_hand.png" alt="Serial Monitor" caption="Sensor with a connected IR LED in open air" width="700px"/>
<CenteredImage src="/img/ltr-507/serial_distance_to_camera.png" alt="Serial Monitor" caption="Serial Monitor output" width="700px"/>

<CenteredImage src="/img/ltr-507/proximity_with_hand.png" alt="Serial Monitor" caption="Sensor covered by a hand" width="700px"/>
<CenteredImage src="/img/ltr-507/serial_distance_to_hand.png" alt="Serial Monitor" caption="LTR-507 Light Sensor Serial Monitor output" width="700px"/>

<QuickLink title="readProximity.ino" description="Example file for reading the proximity sensor value using the LTR-507" url="https://github.com/SolderedElectronics/Soldered-Digital-Light-Sensor-Arduino-Library/blob/main/examples/readProximity/readProximity.ino" />