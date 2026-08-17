---
slug: /nula-dual-esp32-c5/arduino
title: NULA Dual ESP32-C5 - Getting started with Arduino
sidebar_label: Getting started with Arduino
id: nula_dual_esp32-c5-arduino-1
hide_title: True
pagination_next: null
---

# Getting started with Arduino

## Arduino board definition

To program your **NULA Dual ESP32-C5**, use the **official Espressif Arduino core for ESP32**.  
Version **3.3.10** and newer include a dedicated **Soldered NULA Dual ESP32C5** board definition, so there's no need to configure a generic ESP32-C5 target.

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

<InfoBox>**No port showing up?** The USB-C port is served by an onboard **CH340K** bridge, so the board appears as a USB serial port rather than a native USB device. Windows and macOS usually have the driver already; if no port appears, install the CH340 driver and reconnect the board.</InfoBox>

<InfoBox>Leave **Tools → USB CDC On Boot** set to **Disabled**. Serial output travels through the CH340K bridge, so enabling USB CDC leaves you with no serial output at all.</InfoBox>

---

## Board settings worth changing

Two defaults are worth adjusting before you start a larger project:

- **Tools → PSRAM → Enabled.** The module carries 8 MB of PSRAM, but it is disabled by default and your sketch cannot use it until you turn it on.
- **Tools → Partition Scheme → 8M with spiffs (3MB APP/1.5MB SPIFFS).** The default scheme only reserves about 1.25 MB for your sketch even though the board has 8 MB of flash. Switch to the 8 MB scheme if you run out of program space.

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

Open the **Serial Monitor** at **115200 baud** - the hello message appears once after each reset, followed by `Running...` once per second.

---

## Onboard RGB LED

The board carries a WS2812B addressable LED on **IO8**, which the board definition exposes as `RGB_BUILTIN`:

```cpp
void setup() {
  // Nothing to set up - rgbLedWrite() handles the pin for you
}

void loop() {
  rgbLedWrite(RGB_BUILTIN, 64, 0, 0);  // red
  delay(500);
  rgbLedWrite(RGB_BUILTIN, 0, 64, 0);  // green
  delay(500);
  rgbLedWrite(RGB_BUILTIN, 0, 0, 64);  // blue
  delay(500);
}
```

<InfoBox>Because the LED sits on **IO8**, anything else you connect to that pin shares it with the LED.</InfoBox>
