---
slug: /nula_dual_esp32-c5/arduino/getting-started
title: NULA Dual ESP32-C5 - Getting started with Arduino
sidebar_label: Getting started with Arduino
id: nula_dual_esp32-c5-arduino-1
hide_title: True
pagination_next: null
---

# Getting started with Arduino

## Arduino board definition

To program your **NULA Dual ESP32-C5**, use the **official Espressif Arduino core for ESP32**.  
This package now includes a dedicated **Soldered NULA Dual ESP32C5** board definition, so there's no need to configure a generic ESP32-C5 target.

<QuickLink
  title="Arduino ESP32 core"
  description="Official Arduino core for all Espressif ESP32 chips, maintained by Espressif."
  url="https://github.com/espressif/arduino-esp32"
/>

<InfoBox>

**New to Arduino?**  
If this is your first time setting up Arduino, follow our beginner's guide for installation, connecting your board, and uploading your first sketch:

<QuickLink
  title="Getting started with Arduino"
  description="Step-by-step guide to installing Arduino and uploading your first program."
  url="/arduino/quick-start-guide"
/>
</InfoBox>

---

## Installing the ESP32 board package

You can install the **ESP32 boards** package directly from the **Arduino Boards Manager**:

1. Open **Arduino IDE**
2. Go to **File → Preferences → Additional Boards Manager URLs** and add:

```
https://espressif.github.io/arduino-esp32/package_esp32_index.json
```

3. Go to **Tools → Board → Boards Manager**
4. Search for **esp32**
5. Find **esp32 by Espressif Systems** and click **Install**

Once installed, select your board from the menu:  
**Tools → Board → esp32 → Soldered NULA Dual ESP32C5**

<InfoBox>The board has an automatic reset/download circuit, so uploading normally just works from a single click of **Upload**. If that ever fails, you can enter download mode manually: hold the **USER** button while pressing **RESET**, then release both.</InfoBox>

---

## Example sketch

Once your board is selected and connected via USB-C, upload this simple test sketch to verify that the module is working:

```cpp
void setup() {
  Serial.begin(115200);
  delay(1000);
  Serial.println("Hello from NULA Dual ESP32-C5!");
}

void loop() {
  delay(1000);
  Serial.println("Running...");
}
```

Open the **Serial Monitor** at **115200 baud** - you should see the hello message printed once per second.
