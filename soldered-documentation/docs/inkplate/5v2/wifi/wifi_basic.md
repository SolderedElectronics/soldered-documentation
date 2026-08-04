---
slug: /inkplate/5v2/wifi/wifi-basics
title: Inkplate 5V2 – WiFi basics
sidebar_label: WiFi basics
id: wifi-basics
hide_title: true
---

<SectionTitle title="WiFi basics" />

On Inkplate 5V2, WiFi is handled by the onboard ESP32 processor. These pages show you how to use it for WiFi in your own projects.

---

## Connecting to WiFi
Here are the basic steps for connecting to WiFi, with the key functions explained below:
```cpp
#include "Inkplate.h"
#include <WiFi.h>
const char* ssid="yourssid";
const char* pass="yourpassword";
Inkplate inkplate(INKPLATE_1BIT);
void setup(){
  inkplate.begin();
  inkplate.clearDisplay();
  inkplate.display();
  Serial.begin(115200);
  WiFi.begin(ssid, pass);
  inkplate.print("Connecting to WiFi...");
  while(WiFi.status()!=WL_CONNECTED){
    delay(500);
    inkplate.print('.');
    inkplate.partialUpdate();
    delay(1000);
  }
  inkplate.println("\nSuccessfully connected to WiFi");
  inkplate.display();
}
void loop(){}
```
<FunctionDocumentation
    functionName="WiFi.begin()"
    description="Starts connecting to a WiFi access point using the specified SSID and password."
    returnDescription="Returns wl_status_t enum value"
    returnType="wl_status_t"
    parameters={[
    { type: "const char*", name: "ssid", description: "Network SSID (the access point name)." },
    { type: "const char*", name: "passphrase", description: "Network password. Optional, depending on the network's security." }
  ]}
/>

<FunctionDocumentation
  functionName="WiFi.status()"
  description="Returns the current connection status of the ESP32 WiFi radio. Compare it against WL_CONNECTED to check whether the board is online."
  returnDescription="Returns wl_status_t enum value"
  returnType="wl_status_t"
/>

---

## Full example

For more details, have a look at the full examples:
<QuickLink 
  title="Inkplate 5V2 WiFi examples" 
  description="Inkplate 5V2 WiFi examples from the Inkplate library"
  url="https://github.com/SolderedElectronics/Inkplate-Arduino-library/tree/master/examples/Inkplate5V2/Advanced/WEB_WiFi" 
/>