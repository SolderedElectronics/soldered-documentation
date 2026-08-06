---
slug: /inkplate/10/wifi/wifi-basics
title: Inkplate 10 – WiFi basics
sidebar_label: WiFi basics
id: 10-wifi-basics
hide_title: true
---

<SectionTitle title="WiFi basics" />

On Inkplate 10, WiFi is handled by the onboard ESP32, the same chip that runs your sketch. These pages walk through connecting to a network and sending or receiving data.

---

## Connecting to WiFi
These are the basic steps to connecting to WiFi, followed by the key function explanations:
```cpp
#include "Inkplate.h"
#include <WiFi.h>
const char* ssid="yourssid";
const char* pass="yourpassword";
Inkplate display(INKPLATE_1BIT);
void setup(){
  display.begin();
  display.clearDisplay();
  display.display();
  Serial.begin(115200);
  WiFi.begin(ssid, pass);
  display.print("Connecting to WiFi...");
  while(WiFi.status()!=WL_CONNECTED){
    delay(500);
    display.print('.');
    display.partialUpdate(true);
    delay(1000);
  }
  display.println("\nSuccessfully connected to WiFi");
  display.display();
}
void loop(){}
```
<FunctionDocumentation
    functionName="WiFi.begin()"
    description="Starts connecting to a WiFi access point using the specified SSID and password. This is the standard ESP32 Arduino WiFi function, so the connection runs on the same ESP32 that runs your sketch."
    returnType="wl_status_t"
    returnDescription="The connection status at the moment the call returns. Poll WiFi.status() until it reports WL_CONNECTED."
    parameters={[
    { type: "char*", name: "_ssid", description: "Pointer to the SSID (AP name). Must be a valid UTF-8 string." },
    { type: "char*", name: "_pass", description: "Pointer to the AP password. Maximum length is 63 characters." }
  ]}
/>

<FunctionDocumentation
  functionName="WiFi.status()"
  description="Reports the current state of the ESP32 WiFi connection. Compare the result against WL_CONNECTED to check whether the board has joined the access point."
  returnType="wl_status_t"
  returnDescription="A status constant such as WL_IDLE_STATUS, WL_CONNECTED, WL_CONNECT_FAILED or WL_DISCONNECTED."
/>

---

## Full example

To see more details, check out our full examples:
<QuickLink 
  title="Inkplate 10 WiFi examples" 
  description="All the WiFi examples for Inkplate 10 in the Inkplate Arduino library"
  url="https://github.com/SolderedElectronics/Inkplate-Arduino-library/tree/master/examples/Inkplate10/Advanced/WEB_WiFi" 
/>