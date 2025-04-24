---
slug: /inkplate/6motion/wifi/wifi-basics
title: WiFi basics
id: 6motion-wifi-basics
hide_title: true
---



<SectionTitle title="WiFi basics" backgroundImage="/img/wifi.png" />

On Inkplate 6MOTION, WiFi is handled by the onboard ESP32 co-processor, these pages contain tutorials on how to use this co-processor to simply connect to WiFi and get and send data.

<InfoBox>The hardware details of the ESP32 co-processor can be found in the **Hardware** section:<QuickLink 
  title="ESP32 co-processor hardware details" 
  description="Hardware details and schematics related to the ESP32 co-processor"
  url="/inkplate/6motion/hardware/esp32" 
/></InfoBox>

---

## Connecting to WiFi

These are the basic steps of connecting to WiFi, followed by the key function explanations:
```cpp
// Include Inkplate Motion library
#include <InkplateMotion.h>
Inkplate inkplate; // Create Inkplate object
// Change WiFi SSID and password here
#define WIFI_SSID "MyNetwork"
#define WIFI_PASS "pass1234"
void setup()
{
    // Initialize Inkplate in black and white mode
    inkplate.begin(INKPLATE_BLACKWHITE);
    
    // Set text options
    inkplate.setCursor(0, 0);
    inkplate.setTextSize(2);
    inkplate.setTextColor(BLACK, WHITE);
    inkplate.setTextWrap(true);

    // Let's initialize the Wi-Fi library:
    WiFi.init();

    // Set mode to Station
    WiFi.setMode(INKPLATE_WIFI_MODE_STA);
    // Connect to WiFi:
    WiFi.begin(WIFI_SSID, WIFI_PASS);

    // Wait until Inkplate is connected connected
    inkplate.print("Connecting to Wi-Fi...");
    while (!WiFi.connected())
    {
        inkplate.print('.');
        inkplate.partialUpdate(true);
        delay(1000);
    }
    inkplate.println("\nSuccessfully connected to Wi-Fi!");
    inkplate.display();
    // Inkplate is now connected to WiFi    
}
void loop()
{
  // Do nothing here
}
```
<FunctionDocumentation
  functionName="WiFi.init()"
  description="Initializes the ESP32-C3 module by powering it up, resetting it to factory settings if required, initializing the ESP32, and disabling the storage of settings in NVM. This function must be called before doing anything else with WiFi."
  returnDescription="Bool, true if initialization is successful, otherwise returns false."
  parameters={[
    { type: 'bool', name: '_resetSettings', description: 'Optional parameter (default: true). If set to true, all stored settings in NVM will be reset to factory defaults. Can be overridden if needed.' },
  ]}
/>
<FunctionDocumentation
  functionName="WiFi.setMode()"
  description="Sets the WiFi mode on the ESP32 module. Available modes include null (modem disabled) or station mode. This function ensures the module is set to the desired mode by sending an AT command."
  returnDescription="Returns true if the mode was successfully set, otherwise returns false."
  parameters={[
    { type: "uint8_t", name: "_wifiMode", description: "WiFi mode to set. Use predefined macros from esp32SpiAtTypedefs.h: INKPLATE_WIFI_MODE_NULL: Null mode (modem disabled), INKPLATE_WIFI_MODE_STA: Station mode." }
  ]}
/>
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
  functionName="WiFi.connected()"
  description="Checks the connection status of the ESP32 WiFi module. Returns whether the module is connected to an access point."
  returnDescription="Returns true if the ESP32 is connected to the AP, otherwise returns false."
/>

<FunctionDocumentation
  functionName="WiFi.disconnect()"
  description="Sends a command to the ESP32 module to disconnect from the currently connected access point."
  returnDescription="Returns true if the command was executed successfully, otherwise returns false."
/>

---
## Full example

To see more details, have a look at the full example:
<QuickLink 
  title="Inkplate_6_Motion_WiFi_Simple.ino" 
  description="Connect to the internet and print the contents of a .txt file"
  url="https://github.com/SolderedElectronics/Inkplate_Motion_Arduino_Library/blob/main/examples/Inkplate6Motion/Advanced/Web_WiFi/Inkplate_6_Motion_WiFi_Simple/Inkplate_6_Motion_WiFi_Simple.ino" 
/>
