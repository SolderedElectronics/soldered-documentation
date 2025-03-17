---
slug: /ltr-507/arduino/settings
title: Adjusting the Settings
id: ltr-507-arduino-2 
hide_title: False
---

This page contains an example how to modify parameters of the LTR-507 light sensor.

## Initialization

To use the LTR-507 sensor, include the required library, create the sensor object, and initialize the sensor in the `setup()` function using `sensor.init()`. You can adjust the sensor’s settings, such as **ALS (ambient light sensor) gain**, **measurement rates**, and **IR LED configuration**.



```cpp
// Include needed libraries
#include "LTR-507-Light-And-Proximity-Sensor-SOLDERED.h"

// Create sensor object
LTR507 sensor;

void setup()
{
    // Begin Serial for debugging purposes
    Serial.begin(115200);

    // Initialize the sensor!
    // This function initializes the sensor with the default settings
    sensor.init();
}
// ...
```

---

## Different Settings

### Turning the sensor on and off

```cpp

    // This turns off the ambient light sensor (ALS) and proximity sensor
    sensor.setALSMode(false);
    sensor.setPSMode(false);
    // Setting the parameter to 'true' will turn it back on, this is done by default in init()

```

### Setting the gain of the sensor

```cpp

    // Set the gain of the sensor
    // This way you can get more or less sensitivity
    // From the datasheet:
    //      -LTR507_ALS_GAIN_RANGE1: 1 lux to 64k lux (1 lux/count) (default)
    //      -LTR507_ALS_GAIN_RANGE2: 0.5 lux to 32k lux (0.5 lux/count)
    //      -LTR507_ALS_GAIN_RANGE3: 0.02 lux to 640 lux (0.01 lux/count)
    //      -LTR507_ALS_GAIN_RANGE4: 0.01 lux to 320 lux (0.005 lux/count)
    sensor.setALSGain(LTR507_ALS_GAIN_RANGE1);
```

<FunctionDocumentation
functionName="sensor.setALSGain(uint8_t gain)"
description="Sets the gain for the ALS sensor to adjust its sensitivity."
returnDescription="None"
/>

### Setting the automatic measurement rate for ambient lighting

```cpp

    // You can use:
    //      -LTR507_ALS_MEASUREMENT_RATE_100MS (default)
    //      -LTR507_ALS_MEASUREMENT_RATE_200MS
    //      -LTR507_ALS_MEASUREMENT_RATE_500MS
    //      -LTR507_ALS_MEASUREMENT_RATE_1000MS
    //      -LTR507_ALS_MEASUREMENT_RATE_2000MS
    sensor.setALSMeasRate(LTR507_ALS_MEASUREMENT_RATE_100MS);

    // Set the bit width of the ALS measurement
    // This changes the time required to complete a single measurement
    // So, it's reccomended to leave it as default
    // sensor.setALSBitWidth(LTR507_ALS_ADC_BIT_WIDTH_16BIT);

```

<FunctionDocumentation
functionName="sensor.setALSMeasRate(uint8_t rate)"
description="Sets the measurement rate for the ambient light sensor."
returnDescription="None"
/>

### Setting the automatic measurement rate for proximity

```cpp

    // You can use:
    //      -LTR507_PS_MEASUREMENT_RATE_12_5MS
    //      -LTR507_PS_MEASUREMENT_RATE_50MS
    //      -LTR507_PS_MEASUREMENT_RATE_70MS
    //      -LTR507_PS_MEASUREMENT_RATE_100MS (default)
    //      -LTR507_PS_MEASUREMENT_RATE_200MS
    //      -LTR507_PS_MEASUREMENT_RATE_500MS
    //      -LTR507_PS_MEASUREMENT_RATE_1000MS
    //      -LTR507_PS_MEASUREMENT_RATE_2000MS
    sensor.setPSMeasRate(LTR507_PS_MEASUREMENT_RATE_100MS);
```

<FunctionDocumentation
functionName="sensor.setPSMeasRate(uint8_t rate)"
description="Sets the measurement rate for the proximity sensor."
returnDescription="None"
/>

### Setting the maximum current supplied to the IR LED

```cpp

    // You can use:
    //      -LTR507_LED_PEAK_CURRENT_5MA
    //      -LTR507_LED_PEAK_CURRENT_10MA
    //      -LTR507_LED_PEAK_CURRENT_20MA
    //      -LTR507_LED_PEAK_CURRENT_50MA (default)
    sensor.setLEDPeakCurrent(LTR507_LED_PEAK_CURRENT_50MA);
```
<FunctionDocumentation
functionName="sensor.setLEDPeakCurrent(uint8_t current)"
description="Sets the peak current for the IR LED used in proximity sensing."
returnDescription="None"
/>

### Setting the pulse frequency of the IR LED

```cpp
    // You can use:
    //      -LTR507_LED_PULSE_FREQ_30KHZ
    //      -LTR507_LED_PULSE_FREQ_40KHZ
    //      -LTR507_LED_PULSE_FREQ_50KHZ
    //      -LTR507_LED_PULSE_FREQ_60KHZ (default)
    //      -LTR507_LED_PULSE_FREQ_70KHZ
    //      -LTR507_LED_PULSE_FREQ_80KHZ
    //      -LTR507_LED_PULSE_FREQ_90KHZ
    //      -LTR507_LED_PULSE_FREQ_100KHZ
    sensor.setLEDPulseFreq(LTR507_LED_PULSE_FREQ_60KHZ);

    // Set the number of pulses for a proximity measurement
    // You can use any number from 1 to 15, default is 1
    sensor.setPSNumPulses(1);
}
// ...

```

<FunctionDocumentation
functionName="sensor.setLEDPulseFreq(uint8_t freq)"
description="Sets the pulse frequency for the IR LED used in proximity sensing."
returnDescription="None"
/>

---

## Full Setup (default settings)

```cpp

// Include needed libraries
#include "LTR-507-Light-And-Proximity-Sensor-SOLDERED.h"

// Create sensor object
LTR507 sensor;

void setup()
{
    // Begin Serial for debugging purposes
    Serial.begin(115200);

    // Initialize the sensor!
    sensor.init();

    // Set the gain of the sensor
    sensor.setALSGain(LTR507_ALS_GAIN_RANGE1);

    // Set the automatic measurement rate
    sensor.setALSMeasRate(LTR507_ALS_MEASUREMENT_RATE_100MS);

    // Set the auto measurement rate for proximity
    sensor.setPSMeasRate(LTR507_PS_MEASUREMENT_RATE_100MS);

    // Set the max current supplied to the IR LED
    sensor.setLEDPeakCurrent(LTR507_LED_PEAK_CURRENT_50MA);

    // Set the pulse frequency of the IR LED
    sensor.setLEDPulseFreq(LTR507_LED_PULSE_FREQ_60KHZ);

    // Set the number of pulses for a proximity measurement (1-15)
    sensor.setPSNumPulses(1);
}
```

<QuickLink 
  title="adjustSettings.ino" 
  description="Example file for adjusting the setting with the LTR-507 sensor"
  url="https://github.com/SolderedElectronics/Soldered-Digital-Light-Sensor-Arduino-Library/blob/main/examples/adjustSettings/adjustSettings.ino" 
/>