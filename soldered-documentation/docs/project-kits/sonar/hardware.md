---
slug: /sonar/hardware
title: Sonar Project Kit - Components
sidebar_label: Hardware
id: sonar-hardware
hide_title: false
pagination_prev: null
---

In the following pages, we will go through each component used in the project to gain a better understanding of how they work individually and how they all work together.

---

## VL53L1X Laser Sensor
This is a **time-of-flight (ToF)** laser sensor, it works by emitting a tiny infrared laser which is invisible to human eye and measures how long it takes for the light to bounce back to a matching onboard sensor ("flight" time). It uses a very focued laser beam to measure distance directly in front of it with LIDAR-grade precision, avoiding the common angle issues that occur in ultrasonic and IR sensors.

<CenteredImage src="/img/under_construction.png" alt="Image of laser disance sensor" width="600px"/>

### Key specs
- **Range:** approximately 0.03 - 4m (30mm to 4000mm) 
- **Update rate:** 50Hz (50 measurements per second)
- **Field of View (FOV):** 27° (can be reduced by adjusting sensors ROI size)
- **I²C interface** (standard address: 0x29)
- **Supports 3.3V and 5V logic**

---

## Working example

<CenteredImage src="/img/under_construction.png" alt="Image of laser disance sensor" caption="Video of working example" width="600px"/>

```cpp
#include "VL53L1X-SOLDERED.h"

VL53_L1X sensor;

void setup()
{
    Serial.begin(115200);
    Serial.println("Serial Initialised");

    sensor.setTimeout(500);
    sensor.begin();

    sensor.setDistanceMode(VL53L1X::Long);
    sensor.setMeasurementTimingBudget(50000);

    sensor.startContinuous(50);
}

void loop()
{
    Serial.print(String(sensor.read()) + "mm");
    if (sensor.timeoutOccurred()) 
    {
        Serial.print(" TIMEOUT");
    }

    Serial.println();
}
```