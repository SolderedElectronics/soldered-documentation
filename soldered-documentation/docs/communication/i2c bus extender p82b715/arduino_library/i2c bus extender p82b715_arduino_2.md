---
slug: /i2c-bus-extender-p82b715/arduino/examples
title: Examples
id: i2c bus extender p82b715-arduino-2
hide_title: false
---

## About the P82B715

Since the P82B715 is a **transparent hardware bus buffer**, it requires no Arduino library. There is no sketch needed to configure the chip — it operates automatically as soon as power is applied.

To use I²C devices through the extender, simply use whatever library you would normally use for those devices. The P82B715 is invisible to your code.

---

## Usage tips

- **Standard-mode (100 kHz)** is recommended for longer cable runs to ensure reliable signal integrity.
- **Fast-mode (400 kHz)** works for shorter runs or well-shielded cables.
- Ensure pull-up resistors are present on both the local and extended sides. The onboard pull-ups (JP1–JP4) handle this by default.
- If you have external pull-up resistors on your I²C bus, cut JP1–JP4 as needed to avoid parallel pull-up conflicts.

---

## Example: I²C device scan

This sketch verifies that a remote I²C device is reachable through the extender:

```cpp
#include <Wire.h>

void setup() {
  Serial.begin(115200);
  Wire.begin();
}

void loop() {
  Serial.println("\nScanning I2C bus...");
  uint8_t found = 0;

  for (uint8_t addr = 1; addr < 127; addr++) {
    Wire.beginTransmission(addr);
    if (Wire.endTransmission() == 0) {
      Serial.print("  Found device at 0x");
      if (addr < 16) Serial.print("0");
      Serial.println(addr, HEX);
      found++;
    }
  }

  if (found == 0) {
    Serial.println("  No I2C devices found.");
  } else {
    Serial.print("  Total devices found: ");
    Serial.println(found);
  }

  delay(5000);
}
```
