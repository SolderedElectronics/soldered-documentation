---
slug: /nula-max-rp2350/arduino
title: NULA Max RP2350 - Getting started with Arduino
sidebar_label: Getting started with Arduino
id: max-rp2350_arduino_1
hide_title: True
pagination_next: null
---

# Getting started with Arduino

## Arduino board definition

To program your **NULA Max RP2350**, use the **official Raspberry Pi core for Arduino** maintained by **Earle Philhower**.  
This package already includes the **Soldered Electronics NULA RP2350** as a defined board variant, so you can select it directly from the Arduino board list after installation.

<QuickLink  
  title="RP2350 Arduino core"  
  description="Official Arduino core for Raspberry Pi RP2040 and RP2350 chips, including the Soldered Electronics NULA RP2350 board definition."  
  url="https://github.com/earlephilhower/arduino-pico"  
/>

<InfoBox>

**New to Arduino?**  
If this is your first time setting up Arduino, follow our beginner’s guide for installation, connecting your board, and uploading your first sketch:

<QuickLink  
  title="Getting started with Arduino"  
  description="Step-by-step guide to installing Arduino and uploading your first program."  
  url="/documentation/arduino/quick-start-guide"  
/>
</InfoBox>

---

## Installing the RP2040/RP2350 board package

You can install the **Raspberry Pi RP2040/RP2350 boards** package directly from the **Arduino Boards Manager**:

1. Open **Arduino IDE**  
2. Go to **Tools → Board → Boards Manager**  
3. In the search bar, type **rp2350**  or **Earle**
4. Find **Raspberry Pi Pico/RP2040/RP2350 Boards by Earle Philhower** and click **Install**

Alternatively, you can install it manually by adding the package URL:

```https://github.com/earlephilhower/arduino-pico/releases/download/global/package_rp2040_index.json```


Then go to **File → Preferences → Additional Boards Manager URLs**, paste the link above, and reopen the **Boards Manager**.

Once installed, select your board from the menu:  
**Tools → Board → Soldered Electronics NULA RP2350**

<InfoBox>If the **Soldered Electronics NULA RP2350** does not appear in the list, you can alternatively select:  
**Tools → Board → Generic RP2350**  
Both options are compatible for uploading and testing basic sketches.</InfoBox>

---

## Example sketch

Once your board is selected and connected via USB-C, you can upload this simple test sketch to verify communication:

```cpp
void setup() {
  Serial.begin(115200);
  Serial.println("Hello from NULA Max RP2350!");
}

void loop() {
  delay(1000);
  Serial.println("Running...");
}
```

<InfoBox> If the upload fails, make sure the correct board and port are selected in **Tools → Port**. The NULA Max RP2350 uses native USB and does not require external drivers on most systems. If necessary, enter **BOOTSEL mode** by holding the **FLASH** button while connecting the USB-C cable, then release it once detected. </InfoBox>