---
slug: /adc/arduino/examples 
title: Analog Readings (examples)
id: adc-arduino-2 
hide_title: False
---

This page provides various examples for using the ADS1015/ADS1115 analog-to-digital converters (ADC) with Arduino, covering initialization, reading analog inputs, using the comparator, and asynchronous or continuous ADC reads.

---

## Initialization and Gain

This section initializes the ADS1015/ADS1115 sensor, setting up the communication and preparing the ADC for use. It also configures the gain, which adjusts the input voltage range, ensuring optimal resolution and accuracy for the ADC readings based on the expected signal levels.

```cpp
#include "ADS1115-SOLDERED.h"

// Declare your ADC object
ADS1115 ADS;

void setup()
{
    // Initialize the Serial communication
    Serial.begin(115200);
    Serial.println(__FILE__);
    Serial.print("ADS1X15_LIB_VERSION: ");
    Serial.println(ADS1X15_LIB_VERSION);

    // Initialize the ADC
    ADS.begin();
}

void loop()
{
    // Set the gain
    ADS.setGain(0);
}
// ...
```

<FunctionDocumentation
  functionName="ADS.begin()"
  description="Initializes the ADS1115 sensor, setting up I2C communication and configuring the sensor for data acquisition."
  returnDescription="True if initialization is successful, false otherwise."
  parameters={[]}
/>

<FunctionDocumentation
  functionName="ADS.setGain()"
  description="Sets the gain for the ADS1115 to adjust the input voltage range."
  returnDescription="True if the gain is successfully set, false otherwise."
  parameters={[
    { name: "gain", type: "ADSGain", description: "The gain value to be set for the sensor." }
  ]}
/>

---

## Simple ADC Read

This example demonstrates how to read the values from all four analog input channels (AIN0 to AIN3) using the ADS1115.

```cpp
#include "ADS1115-SOLDERED.h"

// Declare your ADC object
ADS1115 ADS;

void setup()
{
    // Initialize the Serial communication
    Serial.begin(115200);
    Serial.println(__FILE__);
    Serial.print("ADS1X15_LIB_VERSION: ");
    Serial.println(ADS1X15_LIB_VERSION);

    // Initialize the ADC
    ADS.begin();
}

void loop()
{
    // Set the gain
    ADS.setGain(0);

    // Read the values from each analog input channel
    int16_t val_0 = ADS.readADC(0);
    int16_t val_1 = ADS.readADC(1);
    int16_t val_2 = ADS.readADC(2);
    int16_t val_3 = ADS.readADC(3);

    // Calculate voltage from raw ADC values
    float f = ADS.toVoltage(1); // Voltage factor

    Serial.print("\tAnalog0: ");
    Serial.print(val_0);
    Serial.print('\t');
    Serial.println(val_0 * f, 3);
    Serial.print("\tAnalog1: ");
    Serial.print(val_1);
    Serial.print('\t');
    Serial.println(val_1 * f, 3);
    Serial.print("\tAnalog2: ");
    Serial.print(val_2);
    Serial.print('\t');
    Serial.println(val_2 * f, 3);
    Serial.print("\tAnalog3: ");
    Serial.print(val_3);
    Serial.print('\t');
    Serial.println(val_3 * f, 3);
    Serial.println();

    delay(1000);
}
```

<FunctionDocumentation
  functionName="ADS.readADC()"
  description="Reads an ADC value from the ADS1115 sensor. It can read either single-ended or differential values depending on the provided input."
  returnDescription="The raw ADC value read from the sensor. The value represents the measured voltage or differential voltage, depending on the mode."
  parameters={[
    { name: "channel1", type: "uint8_t", description: "The first input channel to read from (0 to 3 for single-ended mode or channel pair for differential mode)." },
    { name: "channel2", type: "uint8_t", description: "The second input channel to read from, used only in differential mode (optional)." }
  ]}
/>

---

## ADC Comparator

This example demonstrates how to use the built-in comparator of the ADS1115 to trigger an alert when the input voltage crosses certain thresholds. You can connect an LED to the ALERT pin to visually indicate when the threshold is crossed.

```cpp
#include "ADS1115-SOLDERED.h"

// Declare your ADS1115 instance
ADS1115 ADS;

void setup()
{
    // Initialize the Serial Port
    Serial.begin(115200);
    Serial.println(__FILE__);
    Serial.print("ADS1X15_LIB_VERSION: ");
    Serial.println(ADS1X15_LIB_VERSION);

    // Initialize the ADS1115
    ADS.begin();

    // Set up the comparator mode
    ADS.setComparatorMode(1); // 0 = Traditional, 1 = Window
    ADS.setComparatorPolarity(0); // 0 = Low (default), 1 = High
    ADS.setComparatorLatch(1); // 0 = Non-latch, 1 = Latch
    ADS.setComparatorQueConvert(0); // 0 = trigger after 1 conversion

    // Set comparator thresholds
    float f = ADS.toVoltage(1);                // Voltage factor
    ADS.setComparatorThresholdLow(1.234 / f);  // Convert volts to number
    ADS.setComparatorThresholdHigh(3.142 / f); // Convert volts to number

    Serial.println(ADS.getComparatorThresholdLow());
    Serial.println(ADS.getComparatorThresholdHigh());
}

void loop()
{
    // Set gain of the ADC
    ADS.setGain(0);

    // Read the value from AIN0
    int16_t val_0 = ADS.readADC(0);

    float f = ADS.toVoltage(1); // Voltage factor

    Serial.print("\tAnalog0: ");
    Serial.print(val_0);
    Serial.print('\t');
    Serial.print(val_0 * f, 3);
    Serial.print('\t');
    Serial.print(ADS.getComparatorThresholdLow() * f, 3);
    Serial.print('\t');
    Serial.print(ADS.getComparatorThresholdHigh() * f, 3);
    Serial.println();

    delay(100);
}
```

<FunctionDocumentation
  functionName="ADS.toVoltage()"
  description="Converts the raw ADC value to voltage using the specified conversion factor."
  returnDescription="The voltage equivalent of the raw ADC value."
  parameters={[ 
    { name: "factor", type: "float", description: "The conversion factor to scale the raw ADC value to voltage." }
  ]}
/>

| Function                             | Return Type | Description                                                                      |
| ------------------------------------ | ----------- | -------------------------------------------------------------------------------- |
| `ADS.setComparatorMode(1)`           | `void`      | Sets the comparator mode for the ADS1115. Mode `0` is traditional, `1` is window. |
| `ADS.setComparatorPolarity(0)`       | `void`      | Sets the comparator polarity. Mode `0` is low (default), `1` is high.            |
| `ADS.setComparatorLatch(1)`          | `void`      | Sets the comparator latch. Mode `0` is non-latch, `1` is latch.                  |
| `ADS.setComparatorQueConvert(0)`     | `void`      | Sets the comparator to trigger after 1 conversion.                               |
| `ADS.setComparatorThresholdLow(1.234 / f)` | `void`      | Sets the low threshold for the comparator. The value is in voltage and converted to a number. |
| `ADS.setComparatorThresholdHigh(3.142 / f)`| `void`      | Sets the high threshold for the comparator. The value is in voltage and converted to a number. |
| `ADS.getComparatorThresholdLow()`    | `float`     | Retrieves the low comparator threshold value in raw ADC counts.                 |
| `ADS.getComparatorThresholdHigh()`   | `float`     | Retrieves the high comparator threshold value in raw ADC counts.                |

---

## Asynchronous ADC Read

This example demonstrates how to asynchronously read the ADC values without blocking the program flow. The ADS1115 allows you to request ADC values and read them later once they are ready.

```cpp
#include "ADS1115-SOLDERED.h"

// Declare your ADS1115 instance:
ADS1115 ADS;
float f = 0;

void setup()
{
    // Initialize the Serial communication
    Serial.begin(115200);
    Serial.println(__FILE__);
    Serial.print("ADS1X15_LIB_VERSION: ");
    Serial.println(ADS1X15_LIB_VERSION);

    // Setup the ADS1115
    ADS.begin();
    ADS.setGain(0);
    f = ADS.toVoltage(); // Voltage factor
    ADS.requestADC(0);
}

void loop()
{
    // Read the ADC value if available
    if (ADS.isBusy() == false)
    {
        int16_t val_0 = ADS.getValue();
        ADS.requestADC(0); // Request a new reading
        Serial.print("\tAnalog0: ");
        Serial.print(val_0);
        Serial.print('\t');
        Serial.println(val_0 * f, 3);
    }
    // Simulate other tasks...
    delay(2000);
}
```

---

## Continuous ADS Read

This example demonstrates how to continuously read the ADC values from the ADS1015 without needing to manually trigger each read. In continuous mode, the ADS1015 automatically samples the analog input at the specified data rate, allowing for real-time monitoring of the signal as long as the system is powered on.

```cpp
#include "ADS1015-SOLDERED.h"

// Declare an ADS1015 class instance.
ADS1015 ADS;

void setup()
{
    // Setup Serial
    Serial.begin(115200);
    Serial.println(__FILE__);
    Serial.print("ADS1X15_LIB_VERSION: ");
    Serial.println(ADS1X15_LIB_VERSION);

    // setup ADS1015
    ADS.begin();
    ADS.setGain(0);     // 6.144 volt
    ADS.setDataRate(7); // fast
    ADS.setMode(0);     // continuous mode
    ADS.readADC(0);     // first read to trigger
}

void loop()
{
    // read ADC
    Serial.println(ADS.getValue());
}
```

<FunctionDocumentation
  functionName="ADS.setMode()"
  description="Sets the operating mode of the ADS1015/ADS1115. In continuous mode, the ADC continuously converts data, while in single-shot mode, it only converts once per request."
  returnDescription="None"
  parameters={[
    { name: "mode", type: "int", description: "The mode to set: 0 for continuous mode, 1 for single-shot mode." }
  ]}
/>

<QuickLink 
  title="Reading Examples" 
  description="Example files for using the ADC ADS1x15 sensors."
  url="https://github.com/SolderedElectronics/Soldered-ADS1015-ADS1115-ADC-Arduino-Library/tree/main/examples" 
/>
