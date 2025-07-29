---
slug: /inkplate/2/wifi/wifi-basics
title: Inkplate 2 – WiFi basics
sidebar_label: WiFi basics
id: 2-wifi-basics
hide_title: true
---

<SectionTitle title="WiFi basics" backgroundImage="/img/wifi.png" />

Inkplate 2 includes an **ESP32 microcontroller** that supports both **WiFi** and **Bluetooth**. This page explains how to use WiFi functionality to connect your Inkplate 2 to a network.

---

## Connecting to WiFi

Below is a basic example of how to connect your Inkplate 2 to a WiFi network. This uses standard ESP32 WiFi functionality:

```cpp
#include "Inkplate.h"
#include <WiFi.h>

const char* ssid = "yourssid";
const char* pass = "yourpassword";

Inkplate inkplate;

void setup() {
  inkplate.begin();
  inkplate.clearDisplay();
  inkplate.display();
  Serial.begin(115200);
  inkplate.setTextColor(INKPLATE2_BLACK);

  WiFi.begin(ssid, pass);
  inkplate.setCursor(10, 10);
  inkplate.print("Connecting to WiFi...");
  inkplate.display();

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    inkplate.print(".");
    inkplate.display();
  }

  inkplate.println("\nConnected!");
  inkplate.display();
}

void loop() {}
```

<FunctionDocumentation
  functionName="WiFi.status()"
  description="Checks the current connection status of the ESP32's WiFi module."
  returnDescription="Returns WL_CONNECTED if the board is connected to a WiFi network."
/>

---

## Full example

To see more details, check out our full examples:
<QuickLink 
  title="Inkplate_2_WiFi_examples" 
  description="Inkpate 10 WiFi examples from Inkplate library"
  url="https://github.com/SolderedElectronics/Inkplate-Arduino-library/tree/dev/examples/Inkplate2/Advanced/WEB_WiFi" 
/>