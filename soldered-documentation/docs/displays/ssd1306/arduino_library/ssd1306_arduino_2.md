---
slug: /ssd1306/arduino/initializing-the-screen
title: Initializing the screen
id: ssd1306-arduino-2 
hide_title: False
---

To use the SSD1306 OLED Display, first, include the required library, create the display object and initialize the sensor in the `setup()` function.

```cpp
//Include the library
#include "OLED-Display-SOLDERED.h"

//Create an instance of the OLED display
OLED_Display display;

void setup() {
  //Initialize serial communication
  Serial.begin(115200);

  //Initialize the display
  if(display.begin())
  {
    //If the display initialized successfully, print a message and show logo on display
    Serial.println("OLED display initialized successfully!");
    display.display();
  }
  else
  {
    Serial.println("OLED failed to initialize, check connection");
  }
}
```
<InfoBox>If you did everything correctly, you should be greeted with the **Soldered logo!**</InfoBox>

<FunctionDocumentation
  functionName="display.begin()"
  description="Initializes the OLED Display, setting up communication over I2C and setting resolution to 128x64"
  returnDescription="Boolean value, returns true if display was successfully initialized, false if not"
  parameters={[]}
/>

<FunctionDocumentation
  functionName="display.display()"
  description="Displays what we had defined to be drawn previously"
  returnDescription="None"
  parameters={[]}
/>

<WarningBox>The display is only updated when the display() function is called!</WarningBox>
