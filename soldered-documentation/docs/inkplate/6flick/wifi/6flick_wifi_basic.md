---
slug: /inkplate/6flick/wifi/wifi-basics
title: Inkplate 6FLICK – WiFi basics
sidebar_label: WiFi basics
id: 6flick-wifi-basics
hide_title: true
---

<SectionTitle title="WiFi basics" />

On Inkplate 6FLICK, WiFi is handled by the onboard ESP32 processor. These pages contain tutorials on how to use this processor to implement WiFi in your projects.

---

## Connecting to WiFi
These are the basic steps for connecting to WiFi, followed by the key function explanations:
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
    description="Connects to a WiFi access point using the specified SSID and password. Sends an AT command to establish the connection. Avoid using the following characters in SSID and password: , {, }, \\"
    returnDescription="Returns true if the command execution was successful, otherwise returns false."
    parameters={[ 
    { type: "char*", name: "_ssid", description: "Pointer to the SSID (AP name). Must be a valid UTF-8 string." },
    { type: "char*", name: "_pass", description: "Pointer to the AP password. Maximum length is 63 characters." }
  ]}
/>

<FunctionDocumentation
  functionName="WiFi.status()"
  description="Checks the connection status of the ESP32 WiFi module. Returns whether the module is connected to an access point."
  returnDescription="Returns true if the ESP32 is connected to the AP, otherwise returns false."
/>

---

## Full example

To see more details, check out our full examples:
<QuickLink 
  title="Inkplate 6FLICK WiFi examples" 
  description="Inkplate 6FLICK WiFi examples from Inkplate library"
  url="https://github.com/SolderedElectronics/Inkplate-Arduino-library/tree/master/examples/Inkplate6FLICK/Advanced/WEB_WiFi" 
/>