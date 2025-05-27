---
slug: /hx711/arduino/simple-read
title: "HX711 Load Cell Amplifier \u2013 Arduino simple read"
id: hx711-arduino-2
hide_title: false
---
This page contains an example of initializing the HX711 load-cell amplifier and a simple **reading example** using both the **regular** and **easyC versions**.

---

To use the HX711 sensor, first include the required [**library**](https://github.com/SolderedElectronics/Soldered-HX711-ADC-For-Weight-Scales-Arduino-Library/tree/main), create the sensor object, and initialize the sensor in the `setup()` function.

<WarningBox>Ensure that the correct pins for `DAT` and `SCK` are defined before initialization.</WarningBox>

<InfoBox>

If you're using the easyC version, there is **no need to define the DAT and SCK pins**, and the HX711 object is created as follows:

```cpp
// Create the easyC variant of the HX711 object
HX711 hx711;
```

</InfoBox>

```cpp
// Include the library
#include "HX711-SOLDERED.h"

// Define pins used for DAT and SCK here
#define PIN_DAT 4
#define PIN_SCK 3

// Create the HX711 object on the right pins
HX711 hx711(PIN_DAT, PIN_SCK);

void setup()
{
    Serial.begin(115200); // Start serial communication
    
    // Initialize the HX711 sensor
    hx711.begin();
    
    // Wait a bit until it initializes fully
    delay(200);
}

void loop()
{
    // Make raw reading and store in variable
    long reading = hx711.getRawReading();
    
    // Print the reading
    Serial.print("HX711 Reading: ");
    Serial.println(reading);
    
    // Wait a short while until the next reading
    delay(200);
}
```

<FunctionDocumentation functionName="hx711.begin()" description="Initializes the HX711 load-cell amplifier, setting up communication and verifying its presence." returnDescription="None." parameters={[]} />

<FunctionDocumentation functionName="hx711.getRawReading()" 
                        description="Reads raw data from the HX711 load-cell amplifier and returns the raw 32-bit value, representing the weight or force applied to the load cell. It handles both native communication and easyC communication methods."
                        returnDescription="A 32-bit signed long representing the raw reading from the load cell."
                        parameters={[]} />

<!-- <CenteredImage src="/img/hx711/load_cell_hx711_vid.gif" alt="Serial Monitor" caption="Placing weight on the load cell" width="700px"/> -->
<CenteredImage src="/img/hx711/hx711_simpleread.png" alt="Serial Monitor" caption="HX711 Sensor Serial Monitor output" width="700px"/>

<QuickLink 
  title="simpleRead.ino" 
  description="Example file for using the HX711 Sensor"
  url="https://github.com/SolderedElectronics/Soldered-HX711-ADC-For-Weight-Scales-Arduino-Library/blob/main/examples/simpleRead/simpleRead.ino" 
/>

<QuickLink 
  title="easyCExample.ino" 
  description="Example file for using the easyC HX711 Sensor"
  url="https://github.com/SolderedElectronics/Soldered-HX711-ADC-For-Weight-Scales-Arduino-Library/blob/main/examples/easyCExample/easyCExample.ino" 
/>