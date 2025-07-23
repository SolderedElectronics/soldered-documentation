---
slug: /sonar/hardware/laser
title: Sonar Project Kit - Components
sidebar_label: Laser sensor
id: laser
hide_title: false
---

## VL53L1X Laser Sensor
This is a **time-of-flight (ToF)** laser sensor, it works by emitting a tiny infrared laser which is invisible to human eye and measures how long it takes for the light to bounce back to a matching onboard sensor ("flight" time). It uses a very focued laser beam to measure distance directly in front of it with LIDAR-grade precision, avoiding the common angle issues that occur in ultrasonic and IR sensors.

<CenteredImage src="/img/sonar-project/laser-vl53l1x.jpg" alt="Image of laser disance sensor" width="600px"/>

### Key specs
- **Range:** approximately 0.03 - 4m (30mm to 4000mm) 
- **Update rate:** 50Hz (50 measurements per second)
- **Field of View (FOV):** 27° (can be reduced by adjusting sensors ROI size)
- **I²C interface** (standard address: 0x29)
- **Supports 3.3V and 5V logic**

---

## Pin connection
| Pin Marking | Pin Name | Description |
|:---:|:---:|:---:|
| **VCC** | Power | Supply voltage (3V3 or 5V) |
| **GND** | Ground | Common ground for power and signals |
| **SDA** | Data | I²C data line for communication |
| **SCL** | Clock | I²C clock line for communication |

---

## Qwiic (formerly easyC)  

<CenteredImage src="/img/easyc_transparent.png" alt="EasyC/qwiic cable" width="550px" />
 
<InfoBox>This board is fully **Qwiic-compatible**! Just plug it into your board using a **Qwiic/easyC/STEMMA QT cable** and start coding!</InfoBox>

<QuickLink 
  title="Qwiic (formerly easyC) details and specifications" 
  description="Learn about hardware specifications, compatibility, and usage of the Qwiic connector." 
  url="/qwiic" 
/>

---

## Working example

<ReactPlayer src='../../../videos/sonar-project/laser-demo.mp4' width='100%' height='auto' muted='true' autoPlay='true' loop='true'/>

---

### Example code

```cpp
#include "VL53L1X-SOLDERED.h"

VL53_L1X sensor;

void setup()
{
    Serial.begin(115200);
    Serial.println("Serial Initialised");

    sensor.setTimeout(500);
    sensor.begin();

    // Use long distance mode and allow up to 50000 us (50 ms) for a measurement
    // The minimum timing budget is 20 ms for short distance mode and 33 ms for
    // medium and long distance modes
    sensor.setDistanceMode(VL53L1X::Long);
    sensor.setMeasurementTimingBudget(50000);

    // Start continuous readings at a rate of one measurement every 50 ms (the
    // inter-measurement period). This period should be at least as long as the
    // timing budget.
    sensor.startContinuous(50);
}

void loop()
{
    Serial.print(String(sensor.read()) + "mm");
    if (sensor.timeoutOccurred()) // Check if sensor has been measuring longer than timeout period
    {
        Serial.print(" TIMEOUT");
    }

    Serial.println();
}
```
