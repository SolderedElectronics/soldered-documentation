---
slug: /nula-deepsleep-esp32-s3/arduino
title: NULA DeepSleep ESP32-S3 - Getting started with Arduino
sidebar_label: Getting started with Arduino
id: deepsleep-esp32-s3_arduino_1
hide_title: True
pagination_next: null
---

# Getting started with Arduino

## Arduino board definition

To program your **NULA DeepSleep ESP32-S3**, use the **official Espressif Arduino core for ESP32**. This package already includes support for the **Soldered NULA DeepSleep ESP32-S3**, so you can select it directly from the board list after installation.

<QuickLink  
  title="Espressif Arduino core for ESP32"  
  description="Official Arduino core by Espressif, supporting ESP32, ESP32-C3, ESP32-S3, and ESP32-C6 boards including the Soldered NULA DeepSleep ESP32-S3."  
  url="https://github.com/espressif/arduino-esp32"  
/>

<InfoBox>

**Are you a first-time Arduino user?**  
For a step-by-step guide on installing Arduino, connecting your board, and uploading your first sketch, see this section of our docs:

<QuickLink  
  title="Getting started with Arduino"  
  description="A comprehensive beginner’s guide to setting up Arduino and uploading your first program."  
  url="/arduino/quick-start-guide"  
/>
</InfoBox>

---

## Installing the ESP32 board package

You can install the **Espressif ESP32 boards** directly from the **Arduino Boards Manager**:

1. Open **Arduino IDE**  
2. Go to **Tools → Board → Boards Manager**  
3. In the search bar, type **ESP32**  
4. Find the entry **ESP32 by Espressif Systems** and click **Install**

Once installed, select your board from the menu:  
**Tools → Board → esp32 → Soldered NULA DeepSleep ESP32-S3**

<InfoBox>If the **Soldered NULA DeepSleep ESP32-S3** does not appear in the list, you can alternatively select:  
**Tools → Board → esp32 → ESP32S3 Dev Module**  
Both options are compatible for uploading and testing sketches.</InfoBox>

---

## Install CH340 driver

The CH340 is an onboard chip that enables serial communication over USB. Without the driver, the board may not show up as a serial port on your computer.

<InfoBox>Linux users can skip this step because the CH340 driver is already installed.</InfoBox>

### Windows

If the driver is not installed, download it from **[this link](https://soldered.com/productdata/2023/02/CH34x_Install_Windows_v3_4.zip)**. Start the installation and follow the instructions.

### Mac

On macOS, the CH340 driver needs to be installed manually. Download it from the official WCH website, open the `.dmg` file, and follow the installation instructions:

<QuickLink 
  title="CH340 driver for macOS" 
  description="Official WCH CH34x serial driver download for macOS"
  url="https://www.wch-ic.com/downloads/CH34XSER_MAC_ZIP.html" 
/>

<InfoBox>After installing, macOS may ask you to allow the driver in **System Settings → Privacy & Security**. Restart your Mac if the board is not detected after installation.</InfoBox>

---

## Example sketch

Once your board is selected and connected via USB-C, try uploading this simple example to verify everything is working:

```cpp
void setup() {
  Serial.begin(115200);
  Serial.println("Hello from NULA DeepSleep ESP32-S3!");
}

void loop() {
  delay(1000);
  Serial.println("Running...");
}
```

<InfoBox>If uploading fails, double-check that the correct board and port are selected, and make sure the **CH340 driver** is installed (see the section above).</InfoBox>