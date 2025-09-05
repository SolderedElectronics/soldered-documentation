---  
slug: /inkplate/6COLOR/battery/read-voltage  
title: Inkplate 6COLOR - Read Battery Voltage 
sidebar_label: Read Battery Voltage
id: read-bat  
hide_title: true  
---

<SectionTitle title="Read Battery Voltage" backgroundImage="/img/deepsleep.jpg" />

When running your **Inkplate 6COLOR board** on a **Li-ion battery**, it's helpful to know the battery's condition. Inkplate 6COLOR lets you measure the battery voltage directly, giving you an estimate of remaining capacity and help you decide if it's time to recharge.

<WarningBox>Connecting and using the battery correctly is important! Please refer to the battery usage page for guidance before use. </WarningBox> 

---

## Reading voltage example

```cpp
#include "Inkplate.h"   // Include Inkplate library to the sketch
#include "battSymbol.h" // Include .h file that contains byte array for battery symbol.
Inkplate display; // Create an object on Inkplate library

void setup()
{
    display.begin(); // Init Inkplate library (you should call this function ONLY ONCE)
}

void loop()
{
    float voltage = display.readBattery(); // Read battery voltage
    display.clearDisplay();                // Clear everything in frame buffer of e-paper display
    display.drawBitmap(100, 100, battSymbol, battSymbol_w, battSymbol_h,
                       INKPLATE_BLUE); // Draw battery symbol at position X=100 Y=100
    display.setCursor(210, 120);
    display.setTextColor(INKPLATE_BLUE);
    display.setTextSize(3);
    display.print(voltage, 2); // Print battery voltage
    display.print('V');
    display.display(); // Send everything to display (refresh the screen)
    delay(10000);      // Wait 10 seconds before new measurement
}
```

<FunctionDocumentation
  functionName="inkplate.readBattery()"
  description="Reads the current battery voltage when running on battery power"
  returnType="float"
  returnDescription="Returns the measured battery voltage"
/>

<QuickLink 
  title="Inkplate6COLOR_Read_Battery_Voltage"
  description="GitHub link with all files" 
  url="https://github.com/SolderedElectronics/Inkplate-Arduino-library/tree/master/examples/Inkplate6COLOR/Advanced/Other/Inkplate6COLOR_Read_Battery_Voltage"
/>
