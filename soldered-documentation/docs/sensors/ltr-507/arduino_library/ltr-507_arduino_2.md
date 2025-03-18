---
slug: /ltr-507/arduino/init-and-settings
title: Initialization and Settings
id: ltr-507-arduino-2 
hide_title: False
---

This page contains an example how to modify parameters of the LTR-507 light sensor.

## Initialization

To use the LTR-507 sensor, include the required library, create the `light_sensor` object, and initialize the light_sensor in the `setup()` function using `light_sensor.init()`. You can adjust the sensor’s settings, such as **ALS (ambient light sensor) gain**, **measurement rates**, and **IR LED configuration**.



```cpp
// Include needed libraries
#include "LTR-507-Light-And-Proximity-Sensor-SOLDERED.h"

// Create light_sensor object
LTR507 light_sensor;

void setup()
{
    // Begin Serial for debugging purposes
    Serial.begin(115200);

    // Initialize the light_sensor!
    // This function initializes the light_sensor with the default settings
    light_sensor.init();
}
// ...
```

<FunctionDocumentation
  functionName="light_sensor.init()"
  description="Initializes the LTR507 light_sensor by setting up I2C communication and configuring default settings for ALS (ambient light light_sensor) and PS (proximity sensor) modes. This includes configuring gain, measurement rates, LED settings, and proximity light_sensor pulses."
  returnDescription="None"
  parameters={[]}
/>

---

## Different Settings

### Turning the sensor on and off

```cpp
    light_sensor.setALSMode(false);
    light_sensor.setPSMode(false);
    // Setting the parameter to 'true' will turn it back on, this is done by default in init()

```

### Setting the gain of the sensor

```cpp
  light_sensor.setALSGain(LTR507_ALS_GAIN_RANGE1);
```

<FunctionDocumentation
  functionName="light_sensor.setALSGain()"
  description="Sets the gain for the ALS (Ambient Light sensor) to adjust its sensitivity. The 'gain' parameter controls the amplification of the sensor's signal. (See table below)."
  returnDescription="None"
  parameters={[
    { type: 'uint8_t', name: 'gain', description: "The gain level to set for the ALS sensor. Higher values increase sensitivity, while lower values decrease it." }
  ]}
/>

| Gain Range               | Lux Range           | Lux per Count   |
| ------------------------ | ------------------- | --------------- |
| `LTR507_ALS_GAIN_RANGE1` | 1 lux to 64k lux    | 1 lux/count     |
| `LTR507_ALS_GAIN_RANGE2` | 0.5 lux to 32k lux  | 0.5 lux/count   |
| `LTR507_ALS_GAIN_RANGE3` | 0.02 lux to 640 lux | 0.01 lux/count  |
| `LTR507_ALS_GAIN_RANGE4` | 0.01 lux to 320 lux | 0.005 lux/count |


### Setting the automatic measurement rate for ambient lighting

```cpp
  light_sensor.setALSMeasRate(LTR507_ALS_MEASUREMENT_RATE_100MS);
```

<FunctionDocumentation
  functionName="light_sensor.setALSMeasRate()"
  description="Sets the measurement rate for the Ambient Light sensor (ALS). The 'rate' parameter defines how frequently the sensor takes measurements. (See table below)."
  returnDescription="None"
  parameters={[
    { type: 'uint8_t', name: 'rate', description: "The measurement rate to set for the ALS sensor, typically represented in Hz or cycles per second." }
  ]}
/>

| Measurement Rate                     | Description                       |
| ------------------------------------ | --------------------------------- |
| `LTR507_ALS_MEASUREMENT_RATE_100MS`  | Default measurement rate          |
| `LTR507_ALS_MEASUREMENT_RATE_200MS`  | 200 milliseconds per measurement  |
| `LTR507_ALS_MEASUREMENT_RATE_500MS`  | 500 milliseconds per measurement  |
| `LTR507_ALS_MEASUREMENT_RATE_1000MS` | 1000 milliseconds per measurement |
| `LTR507_ALS_MEASUREMENT_RATE_2000MS` | 2000 milliseconds per measurement |



### Setting the automatic measurement rate for proximity

```cpp
  light_sensor.setPSMeasRate(LTR507_PS_MEASUREMENT_RATE_100MS);
```

<FunctionDocumentation
  functionName="light_sensor.setPSMeasRate()"
  description="Sets the measurement rate for the proximity sensor. The 'rate' parameter defines how often the sensor performs measurements. (See table below)."
  returnDescription="None"
  parameters={[
    { type: 'uint8_t', name: 'rate', description: "The measurement rate to set for the proximity sensor, typically represented in Hz or cycles per second." }
  ]}
/>

| Measurement Rate                    | Description                       |
| ----------------------------------- | --------------------------------- |
| `LTR507_PS_MEASUREMENT_RATE_12_5MS` | 12.5 milliseconds per measurement |
| `LTR507_PS_MEASUREMENT_RATE_50MS  ` | 50 milliseconds per measurement   |
| `LTR507_PS_MEASUREMENT_RATE_70MS  ` | 70 milliseconds per measurement   |
| `LTR507_PS_MEASUREMENT_RATE_100MS ` | Default measurement rate          |
| `LTR507_PS_MEASUREMENT_RATE_200MS ` | 200 milliseconds per measurement  |
| `LTR507_PS_MEASUREMENT_RATE_500MS ` | 500 milliseconds per measurement  |
| `LTR507_PS_MEASUREMENT_RATE_1000MS` | 1000 milliseconds per measurement |
| `LTR507_PS_MEASUREMENT_RATE_2000MS` | 2000 milliseconds per measurement |



### Setting the maximum current supplied to the IR LED

```cpp
  light_sensor.setLEDPeakCurrent(LTR507_LED_PEAK_CURRENT_50MA);
```
<FunctionDocumentation
  functionName="light_sensor.setLEDPeakCurrent()"
  description="Sets the peak current for the IR LED used in proximity sensing. The 'current' parameter controls the maximum current supplied to the LED. (See table below)."
  returnDescription="None"
  parameters={[
    { type: 'uint8_t', name: 'current', description: "The peak current to set for the IR LED, which affects the intensity of the emitted light." }
  ]}
/>

| LED Peak Current               | Description                         |
| ------------------------------ | ----------------------------------- |
| `LTR507_LED_PEAK_CURRENT_5MA ` | 5 milliamps peak current            |
| `LTR507_LED_PEAK_CURRENT_10MA` | 10 milliamps peak current           |
| `LTR507_LED_PEAK_CURRENT_20MA` | 20 milliamps peak current           |
| `LTR507_LED_PEAK_CURRENT_50MA` | Default peak current (50 milliamps) |



### Setting the pulse frequency of the IR LED

```cpp
  light_sensor.setLEDPulseFreq(LTR507_LED_PULSE_FREQ_60KHZ);

  // Set the number of pulses for a proximity measurement
  // You can use any number from 1 to 15, default is 1
  light_sensor.setPSNumPulses(1);
}
// ...

```

<FunctionDocumentation
  functionName="light_sensor.setLEDPulseFreq()"
  description="Sets the pulse frequency for the IR LED used in proximity sensing. The 'freq' parameter controls how often the LED pulses. (See table below)."
  returnDescription="None"
  parameters={[
    { type: 'uint8_t', name: 'freq', description: "The pulse frequency to set for the IR LED, typically represented in Hz or pulses per second." }
  ]}
/>

| LED Pulse Frequency            | Description                      |
| ------------------------------ | -------------------------------- |
| `LTR507_LED_PULSE_FREQ_30KHZ ` | 30 kilohertz pulse frequency     |
| `LTR507_LED_PULSE_FREQ_40KHZ ` | 40 kilohertz pulse frequency     |
| `LTR507_LED_PULSE_FREQ_50KHZ ` | 50 kilohertz pulse frequency     |
| `LTR507_LED_PULSE_FREQ_60KHZ ` | Default pulse frequency (60 kHz) |
| `LTR507_LED_PULSE_FREQ_70KHZ ` | 70 kilohertz pulse frequency     |
| `LTR507_LED_PULSE_FREQ_80KHZ ` | 80 kilohertz pulse frequency     |
| `LTR507_LED_PULSE_FREQ_90KHZ ` | 90 kilohertz pulse frequency     |
| `LTR507_LED_PULSE_FREQ_100KHZ` | 100 kilohertz pulse frequency    |


---

## Full Setup (default settings)

This section outlines the default settings used when initializing the sensor. It can be helpful to refer to these if you wish to modify any of the settings during your project.

```cpp
// Include needed libraries
#include "LTR-507-Light-And-Proximity-Sensor-SOLDERED.h"

// Create light_sensor object
LTR507 light_sensor;

void setup()
{
    // Begin Serial for debugging purposes
    Serial.begin(115200);

    // Initialize the light_sensor!
    light_sensor.init();

    // Set the gain of the light_sensor
    light_sensor.setALSGain(LTR507_ALS_GAIN_RANGE1);

    // Set the automatic measurement rate
    light_sensor.setALSMeasRate(LTR507_ALS_MEASUREMENT_RATE_100MS);

    // Set the auto measurement rate for proximity
    light_sensor.setPSMeasRate(LTR507_PS_MEASUREMENT_RATE_100MS);

    // Set the max current supplied to the IR LED
    light_sensor.setLEDPeakCurrent(LTR507_LED_PEAK_CURRENT_50MA);

    // Set the pulse frequency of the IR LED
    light_sensor.setLEDPulseFreq(LTR507_LED_PULSE_FREQ_60KHZ);

    // Set the number of pulses for a proximity measurement (1-15)
    light_sensor.setPSNumPulses(1);
}
```

<QuickLink 
  title="adjustSettings.ino" 
  description="Example file for adjusting the setting with the LTR-507 sensor"
  url="https://github.com/SolderedElectronics/Soldered-Digital-Light-Sensor-Arduino-Library/blob/main/examples/adjustSettings/adjustSettings.ino" 
/>