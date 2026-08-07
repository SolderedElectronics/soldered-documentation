---  
slug: /inkplate/5v2/temperature/read-temperature
title: Inkplate 5V2 - Read Temperature 
sidebar_label: Read Temperature
id: read-temp
hide_title: true
---

<SectionTitle title="Read Temperature" />

Inkplate 5V2 uses the TPS65186 power supply chip to drive the e-paper display. The chip can measure an external NTC (Negative Temperature Coefficient) thermistor, so you can monitor the display panel temperature in the range from -10°C to 85°C. That also gives you an approximate room temperature reading. 

<InfoBox>The readings are meant for onboard temperature monitoring, so treat them as an approximation of room temperature.</InfoBox>

<CenteredImage src="/img/5v2/5v2_tps_highlight.png" alt="TPS highlight image" caption="Onboard TPS chip" />

---

## Read temperature code example

```cpp
#include "Inkplate.h"   // Include Inkplate library to the sketch
#include "tempSymbol.h" // Include .h file that contains byte array for temperature symbol.
Inkplate display(INKPLATE_1BIT); // Create an object on Inkplate library and also set library into 1-bit mode (BW)

void setup()
{
    display.begin();                    // Init Inkplate library (you should call this function ONLY ONCE)
    display.clearDisplay();             // Clear frame buffer of display
    display.display();                  // Put clear image on display
    display.setTextSize(4);             // Scale text to be two times bigger then original (5x7 px)
    display.setTextColor(BLACK, WHITE); // Set text color to black and background color to white
}

void loop()
{
    int temperature = display.readTemperature();            // Read temperature from on-board temperature sensor
    display.clearDisplay();                                 // Clear everything in frame buffer of e-paper display
    display.image.draw(tempSymbol, 100, 100, 38, 79); // Draw temperature symbol at position X=100, Y=100
    display.setCursor(155, 125);
    display.print(temperature, DEC); // Print temperature
    display.print('C');
    display.display(); // Send everything to display (refresh the screen)
    delay(10000);      // Wait 10 seconds before new measurement
}
```

<FunctionDocumentation
  functionName="inkplate.readTemperature()"
  description="Reads the onboard temperature sensor"
  returnType="int8_t"
  returnDescription="Returns the measured temperature in °C"
/>

<QuickLink 
  title="Inkplate5V2_Read_Temperature"
  description="GitHub link with all files" 
  url="https://github.com/SolderedElectronics/Inkplate-Arduino-library/tree/master/examples/Inkplate5V2/Advanced/Other/Inkplate5V2_Read_Temperature" 
/>
