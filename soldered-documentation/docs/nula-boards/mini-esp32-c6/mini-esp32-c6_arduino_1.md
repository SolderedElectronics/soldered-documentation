---
slug: /nula-mini-esp32-c6/arduino
title: Nula Mini ESP32-C6 - Getting started with Arduino
sidebar_label: Getting started with Arduino
id: mini-esp32-c6-arduino-1
pagination_next: null
hide_title: True
---

# Getting started with Arduino

## Arduino board definition

<div style={{ textAlign: 'justify' }}>

To program your **NULA Mini ESP32-C6**, install the **Soldered ESP32-C6 board definition** for Arduino IDE. This custom definition ensures that all onboard features (such as Qwiic connector, battery management, and power configuration) work optimally.  

<QuickLink  
  title="NULA Mini ESP32-C6 Arduino board definition"  
  description="Official Arduino board definition by Soldered for NULA Mini ESP32-C6."  
  url="https://github.com/SolderedElectronics/Dasduino-Board-Definitions-for-Arduino-IDE"  
/>  

</div>

Alternatively, you can also use the **official Espressif ESP32 board package**, which supports ESP32-C6 devices.

<QuickLink  
  title="Espressif Arduino core for ESP32"  
  description="Official Arduino core for ESP32, ESP32-C3, ESP32-S3, and ESP32-C6 boards."  
  url="https://github.com/espressif/arduino-esp32"  
/>

<InfoBox>

**Are you a first-time Arduino user?**  
For a step-by-step introduction to installing Arduino, connecting your board, and uploading your first sketch, see this section of our docs:

<QuickLink  
  title="Getting started with Arduino"  
  description="A comprehensive beginner’s guide to setting up Arduino and uploading your first program."  
  url="/documentation/arduino/quick-start-guide"  
/>  

</InfoBox>

## Installing the Soldered board definition

You can install the **Soldered ESP32-C6 boards** directly through the **Arduino Boards Manager**:

1. Open Arduino IDE  
2. Go to **File → Preferences**  
3. In the field **Additional Boards Manager URLs**, add this line:

```https://raw.githubusercontent.com/SolderedElectronics/Dasduino-Board-Definitions-for-Arduino-IDE/master/package_Dasduino_Boards_index.json```

4. Click **OK** and open **Tools → Board → Boards Manager**  
5. Search for **Soldered ESP32 Boards** and click **Install**

After installation, select:  
**Tools → Board → Soldered ESP32 Boards → NULA Mini ESP32-C6**

## Using the Espressif definition (alternative)

If you prefer to use the official Espressif package, follow these steps instead:

1. Open **File → Preferences**  
2. Add this URL:

```
https://espressif.github.io/arduino-esp32/package_esp32_index.json
```

3. Go to **Tools → Board → Boards Manager**, search for **ESP32**, and install the package  
4. Select **ESP32C6 Dev Module** under **Tools → Board → esp32**

Both definitions are compatible, but we recommend the **Soldered version** for the best hardware support.


## Example sketch

Once your board is selected and connected via USB-C, you can test it with the example below:

```cpp
void setup() {
  Serial.begin(115200);
  Serial.println("Hello from NULA Mini ESP32-C6!");
}

void loop() {
  delay(1000);
  Serial.println("Running...");
}
```

<InfoBox>If uploading fails, double-check that the correct board and port are selected.  
The NULA Mini ESP32-C6 uses **native USB**, so no external driver is required.</InfoBox>