---  
slug: /inkplate/6FLICK/battery/read-voltage  
title: Inkplate 6FLICK - Read Battery Voltage 
sidebar_label: Read Battery Voltage
id: read-bat  
hide_title: true  
---

<SectionTitle title="Read Battery Voltage" backgroundImage="/img/deepsleep.jpg" />

When running your **Inkplate 6FLICK board** on a **Li-ion battery**, it's helpful to know the battery's condition. Inkplate 6FLICK lets you measure the battery voltage directly, giving you an estimate of remaining capacity and help you decide if it's time to recharge.

<WarningBox>Connecting and using the battery correctly is important! Please refer to the battery usage page for guidance before use. </WarningBox> 

---

## Reading voltage example

```cpp
#include "Inkplate.h"   // Include Inkplate library to the sketch
#include "battSymbol.h" // Include .h file that contains byte array for battery symbol.
Inkplate display(INKPLATE_1BIT); // Create an object on Inkplate library and also set library into 1-bit mode (BW)

void setup()
{
    display.begin();                    // Init Inkplate library (you should call this function ONLY ONCE)
    display.setTextSize(2);             // Scale text to be two times bigger then original (5x7 px)
    display.setTextColor(BLACK, WHITE); // Set text color to black and background color to white
}

void loop()
{
    float voltage = display.readBattery();                   // Read battery voltage
    display.clearDisplay();                                  // Clear everything in frame buffer of e-paper display
    display.drawImage(battSymbol, 100, 100, 106, 45, BLACK); // Draw battery symbol at position X=100 Y=100
    display.setCursor(210, 120);
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
  title="Inkplate6FLICK_Read_Battery_Voltage"
  description="GitHub link with all files" 
  url="https://github.com/SolderedElectronics/Inkplate-Arduino-library/tree/master/examples/Inkplate6FLICK/Advanced/Other/Inkplate6FLICK_Read_Battery_Voltage"
/>
