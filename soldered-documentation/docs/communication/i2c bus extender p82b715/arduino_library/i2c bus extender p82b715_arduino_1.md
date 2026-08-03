---
slug: /i2c-bus-extender-p82b715/arduino/getting-started
title: Getting started
id: i2c bus extender p82b715-arduino-1
hide_title: false
---

## Connecting to your microcontroller

The P82B715 I2C Bus Extender is a **transparent I²C buffer**, so no library or driver is needed. Just connect it between your microcontroller and the remote I²C device using the Qwiic connector. Any I²C library that works for your sensor will keep working through the extender.

### Local side: microcontroller to the extender

| **NULA Deepsleep** | **P82B715 I2C Bus Extender** |
|---------------------|-------------------------------|
| Qwiic                | Qwiic (K1 or K2)              |

### Remote side: extender to your I²C device

Connect the remote I²C device to the **screw terminal (K4)** using a long cable (up to 50 m).

| **P82B715 screw terminal (K4)** | **Remote I²C device** |
|-----------------------------------|--------------------------|
| SCL                                | SCL                       |
| SDA                                | SDA                       |
| GND                                | GND                       |

<InfoBox>
The remote device needs its own power supply. The screw terminal only carries SCL, SDA, and GND, not power.
</InfoBox>

<InfoBox>
The P82B715 is completely transparent to I²C. Your microcontroller communicates with the remote device using its original I²C address, and no additional setup is needed. Just wire it up and use your sensor's existing library.
</InfoBox>

---

## Example: Scanning for I²C devices over a long cable

Below is a simple example that demonstrates using the extender. Replace the sensor address and library with your specific device.

```cpp
#include <Wire.h>

void setup() {
  Serial.begin(115200);
  Wire.begin();
  Serial.println("I2C Bus Extender - scanning for devices...");
}

void loop() {
  Serial.println("Scanning I2C bus...");
  for (uint8_t addr = 1; addr < 127; addr++) {
    Wire.beginTransmission(addr);
    if (Wire.endTransmission() == 0) {
      Serial.print("Device found at address 0x");
      Serial.println(addr, HEX);
    }
  }
  delay(3000);
}
```

<InfoBox>
This sketch scans the I²C bus and prints any found device addresses. Run it to verify your remote I²C device is reachable through the extender.
</InfoBox>
