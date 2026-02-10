---
slug: /inkplate/13spectra/wifi/wifi-basics
title: Inkplate 13SPECTRA – WiFi basics
sidebar_label: WiFi basics
id: 13spectra-wifi-basics
hide_title: true
---

<SectionTitle title="WiFi basics" backgroundImage="/img/wifi.png" />

On Inkplate 13SPECTRA, WiFi is handled by the onboard ESP32 processor; these pages contain tutorials on how to use this processor to implement WiFi into your projects.

---

## Connecting to WiFi
These are the basic steps to connecting to WiFi, followed by the key function explanations:

```cpp
#include "Inkplate.h"   //Include Inkplate library to the sketch
#include "WiFi.h"       //Include library for WiFi

Inkplate inkplate;
const char ssid[]="your password";  // Your WiFi SSID
const char *password="your password";   // Your WiFi password

void setup(){
    inkplate.begin();   // Init INkplate library (you should call this function ONLY ONCE)
    inkplate.clearDisplay();    // Clear frame buffer of display
    inkplate.setTextColor(INKPLATE_BLACK); //Set the text color to black
    WiFi.begin(ssid, pass);
    inkplate.print("Connecting to WiFi...");
    while(WiFi.status()!=WL_CONNECTED){
        delay(500);
    }
    inkplate.println("\nSuccessfully connected to WiFi");
    inkplate.display();
}
void loop(){}

```

[IMAGE PLACEHOLDER - 13spectra display output]

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

[LINK PLACEHOLDER - 13spectra wifi examples github link]