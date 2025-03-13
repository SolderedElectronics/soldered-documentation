---
slug: /apds-9960/arduino/color-sensor
title: Color Sensor
id: apds-9960-arduino-5
hide_title: False
---

This page contains simple examples of initialization and color detection with the APDS-9960 sensor.

---

In this code snippet, the `loop()` function continuously checks if a color reading is available from the APDS-9960 sensor. The `colorAvailable()` function is used to wait until the color reading is ready. If the reading is not available, the `delay(5)` function is used to pause briefly before checking again.

Once a color reading becomes available, the `readColor()` function is called to retrieve the red, green, and blue (RGB) color intensities. These values are stored in the variables r, g, and b.

The RGB values are then printed to the Serial Monitor to display the current color detected by the sensor. A newline is added after each set of color values for readability.

To prevent continuous querying and to control the reading frequency, a `delay(1000)` function is used to pause for one second before taking another color reading.

```cpp
void loop()
{
    // check if a color reading is available
    while (!APDS.colorAvailable())
    {
        delay(5); //Wait for color reading to be available
    }
    int r, g, b;  //Initialize variables for color intensities

    // read the color
    APDS.readColor(r, g, b);

    // print the values
    Serial.print("r = ");
    Serial.println(r);
    Serial.print("g = ");
    Serial.println(g);
    Serial.print("b = ");
    Serial.println(b);
    Serial.println();

    // wait a bit before reading again
    delay(1000);
}
```

<FunctionDocumentation
  functionName="APDS.colorAvailable()"
  description="Enables the color sensor and verifies the sensor's status."
  returnDescription="An integer: 1 if color data is available, 0 otherwise."
  parameters={[]}
/>

<FunctionDocumentation
  functionName="APDS.readColor()"
  description="Reads color data (clear, red, green, and blue) from the APDS9960 sensor and stores the values in references."
  returnDescription="True if the data is successfully read and false if an error occurs, setting the color values to -1 in case of failure."
  parameters={[]}
/>

---

## Full example

Open the Serial Monitor at 115200 baud to observe the detected color values.

```cpp
// Include the library
#include "APDS9960-SOLDERED.h"

// Create an APDS-9960 object
APDS_9960 APDS;

// Setup function, runs once
void setup()
{
    Serial.begin(115200); //Begin serial communication with PC
    while (!Serial) //Wait until serial becomes active
        ;

    if (!APDS.begin())  //Begin communication with sensor
    {
        Serial.println("Error initializing APDS-9960 sensor!");
      while(1); //Loop forever if sensor is not available
    }

    Serial.println("Sensor initialized.");
}

void loop()
{
    // check if a color reading is available
    while (!APDS.colorAvailable())
    {
        delay(5); //Wait for color reading to be available
    }
    int r, g, b;  //Initialize variables for color intensities

    // read the color
    APDS.readColor(r, g, b);

    // print the values
    Serial.print("r = ");
    Serial.println(r);
    Serial.print("g = ");
    Serial.println(g);
    Serial.print("b = ");
    Serial.println(b);
    Serial.println();

    // wait a bit before reading again
    delay(1000);
}
```

<CenteredImage src="/img/apds-9960/apds9960_color.png" alt="Serial Monitor" caption="Color Sensor Serial Monitor output"/>

<QuickLink 
  title="ColorSensor.ino" 
  description="Example file for using the APDS-9960 sensor with easyC/Qwiic/I2C"
  url="https://github.com/SolderedElectronics/Soldered-APDS9960-Light-Gesture-Color-Sensor-Arduino-Library/blob/main/examples/ColorSensor/ColorSensor.ino" 
/>