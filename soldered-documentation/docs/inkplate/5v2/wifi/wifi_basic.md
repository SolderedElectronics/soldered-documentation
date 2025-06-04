---
slug: /inkplate/5v2/wifi/wifi-basics
title: WiFi basics
id: wifi-basics
hide_title: true
---

<SectionTitle title="WiFi basics" backgroundImage="/img/wifi.png" />

On Inkplate 5V2, WiFi is handled by the onboard ESP32 processor. These pages contain tutorials on how to use this processor to implement WiFi in your projects.

---

## Connecting to WiFi
These are the basic steps to connecting to WiFi, followed by explanations of the key functions:
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
    inkplate.partialUpdate(true);
    delay(1000);
  }
  inkplate.println("\nSuccessfully connected to WiFi");
  inkplate.display();
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
  title="Inkplate 5V2 WiFi examples" 
  description="Inkplate 5V2 WiFi examples from the Inkplate library"
  url="https://github.com/SolderedElectronics/Inkplate-Arduino-library/tree/master/examples/Inkplate5V2/Advanced/WEB_WiFi" 
/>