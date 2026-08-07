---  
slug: /inkplate/5v2/battery/read-voltage  
title: Inkplate 5V2 - Read Battery Voltage 
sidebar_label: Read Battery Voltage
id: read-bat  
hide_title: true  
---

<SectionTitle title="Read Battery Voltage" />

When your Inkplate 5V2 runs on a Li-ion battery, it's useful to know how much charge is left. Inkplate 5V2 can measure the battery voltage directly, which gives you an estimate of the remaining capacity and tells you when it's time to recharge.

<WarningBox>Connecting and using the battery correctly matters. Have a look at the <a href="/inkplate/5v2/hardware/battery">battery usage page</a> before you start. </WarningBox> 

---

## Reading voltage example

```cpp
#include "Inkplate.h"   // Include Inkplate library to the sketch
#include "battSymbol.h" // Include .h file that contains byte array for battery symbol.
Inkplate display(INKPLATE_1BIT); // Create an object on Inkplate library and also set library into 1-bit mode (BW)

void setup()
{
    display.begin();                    // Init Inkplate library (you should call this function ONLY ONCE)
    display.clearDisplay();             // Clear frame buffer of display
    display.setTextSize(3);             // Scale text to be three times bigger then original (5x7 px)
    display.setTextColor(BLACK, WHITE); // Set text color to black and background color to white
}

void loop()
{
    float voltage = display.readBattery();                   // Read battery voltage
    display.clearDisplay();                                  // Clear everything in frame buffer of e-paper display
    display.image.draw(battSymbol, 100, 100, 106, 45); // Draw battery symbol at position X=100 Y=100
    display.setCursor(230, 110);
    display.print(voltage, 2); // Print battery voltage
    display.print('V');
    display.display(); // Send everything to display (refresh the screen)
    delay(10000);      // Wait 10 seconds before new measurement
}
```

<FunctionDocumentation
  functionName="inkplate.readBattery()"
  description="Reads the current battery voltage when running on battery power"
  returnType="double"
  returnDescription="Returns the measured battery voltage"
/>

<QuickLink 
  title="Inkplate5V2_Read_Battery_Voltage"
  description="GitHub link with all files" 
  url="https://github.com/SolderedElectronics/Inkplate-Arduino-library/tree/master/examples/Inkplate5V2/Advanced/Other/Inkplate5V2_Read_Battery_Voltage" 
/>
