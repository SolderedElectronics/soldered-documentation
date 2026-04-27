---
slug: /iis2dulpx/arduino/examples 
title: IIS2DULPX – Measuring acceleration
sidebar_label: Measuring acceleration
id: iis2dulpx-arduino-2 
hide_title: False
---

This page contains examples with function documentation on how to use the **IIS2DULPX Accelerometer breakout** with Arduino.

---

## Initialization

To start working with the **IIS2DULPX Accelerometer Breakout**, include the library, create a sensor object, and initialize it in `setup()`. The return value of `begin()` tells you whether the sensor was found and configured successfully:

```cpp
#include <Soldered-IIS2DULPX.h>

// Create an instance of the IIS2DULPX sensor (I2C address 0x18)
Soldered_IIS2DULPX sensor;

void setup()
{
    Serial.begin(115200);

    // Initialize I2C bus
    Wire.begin();

    // Initialize the sensor
    if (sensor.begin() != IIS2DULPX_OK) {
        Serial.println("Failed to initialize IIS2DULPX sensor!");
        while (1);
    }

    // Enable the accelerometer
    if (sensor.Enable_X() != IIS2DULPX_OK) {
        Serial.println("Failed to enable accelerometer!");
        while (1);
    }

    Serial.println("IIS2DULPX initialized successfully.");
}
```

<FunctionDocumentation
  functionName="sensor.begin()"
  description="Initializes the IIS2DULPX sensor over I2C. Disables I3C, enables block data update (BDU), configures FIFO to bypass mode, and sets default ODR (100 Hz) and full scale (±2g) in High Performance mode."
  returnDescription="Returns `IIS2DULPX_OK` (0) on success, `IIS2DULPX_ERROR` (-1) on failure."
  parameters={[]}
/>

<FunctionDocumentation
  functionName="sensor.Enable_X()"
  description="Powers on the accelerometer and begins acquiring data at the configured ODR and full scale."
  returnDescription="Returns `IIS2DULPX_OK` (0) on success, `IIS2DULPX_ERROR` (-1) on failure."
  parameters={[]}
/>

---

## Reading acceleration data

Once the accelerometer is enabled, call `Get_X_Axes()` to retrieve the current acceleration along all three axes in **mg** (milli-g):

```cpp
void loop()
{
    IIS2DULPX_Axes_t accel;

    if (sensor.Get_X_Axes(&accel) == IIS2DULPX_OK) {
        Serial.print("Accel-X [mg]: ");
        Serial.print(accel.x);
        Serial.print(", Accel-Y [mg]: ");
        Serial.print(accel.y);
        Serial.print(", Accel-Z [mg]: ");
        Serial.println(accel.z);
    } else {
        Serial.println("Failed to read acceleration data!");
    }

    delay(100);
}
```

<FunctionDocumentation
  functionName="sensor.Get_X_Axes(&accel)"
  description="Reads the acceleration along all three axes and stores the results in the provided `IIS2DULPX_Axes_t` structure. Values are in mg (milli-g), computed using the currently configured full-scale sensitivity."
  returnDescription="Returns `IIS2DULPX_OK` (0) on success, `IIS2DULPX_ERROR` (-1) on failure."
  parameters={[
    { name: "accel", type: "IIS2DULPX_Axes_t *", description: "Pointer to a structure that will hold the X, Y, Z acceleration values in mg." }
  ]}
/>

---

## Configuring full scale and ODR

You can change the full-scale range and output data rate to suit your application:

```cpp
// Set full scale to ±8g
sensor.Set_X_FullScale(8);

// Set ODR to 200 Hz in High Performance mode
sensor.Set_X_OutputDataRate_With_Mode(200.0f, IIS2DULPX_HIGH_PERFORMANCE);
```

<FunctionDocumentation
  functionName="sensor.Set_X_FullScale(fullScale)"
  description="Configures the accelerometer full-scale range."
  returnDescription="Returns `IIS2DULPX_OK` (0) on success, `IIS2DULPX_ERROR` (-1) on failure."
  parameters={[
    { name: "fullScale", type: "int32_t", description: "Full-scale range in g. Accepted values: 2, 4, 8, 16." }
  ]}
/>

<FunctionDocumentation
  functionName="sensor.Set_X_OutputDataRate_With_Mode(odr, powerMode)"
  description="Configures the accelerometer output data rate and power mode simultaneously."
  returnDescription="Returns `IIS2DULPX_OK` (0) on success, `IIS2DULPX_ERROR` (-1) on failure."
  parameters={[
    { name: "odr", type: "float", description: "Desired output data rate in Hz (e.g. 1.6, 6.0, 12.5, 25.0, 50.0, 100.0, 200.0, 400.0, 800.0)." },
    { name: "powerMode", type: "IIS2DULPX_Power_Mode_t", description: "Power mode: IIS2DULPX_ULTRA_LOW_POWER, IIS2DULPX_LOW_POWER, or IIS2DULPX_HIGH_PERFORMANCE." }
  ]}
/>

---

## Full example — Serial Plotter

This example continuously reads X/Y/Z acceleration and prints the values in a format compatible with the Arduino Serial Plotter:

```cpp
#include <Soldered-IIS2DULPX.h>

Soldered_IIS2DULPX sensor;

void setup()
{
    Serial.begin(115200);
    Wire.begin();

    if (sensor.begin() != IIS2DULPX_OK) {
        Serial.println("Failed to initialize IIS2DULPX sensor!");
        while (1);
    }

    if (sensor.Enable_X() != IIS2DULPX_OK) {
        Serial.println("Failed to enable accelerometer!");
        while (1);
    }

    Serial.println("IIS2DULPX sensor initialized and accelerometer enabled.");
}

void loop()
{
    IIS2DULPX_Axes_t accel;

    if (sensor.Get_X_Axes(&accel) == IIS2DULPX_OK) {
        Serial.print("Accel-X [mg]:");
        Serial.print(accel.x);
        Serial.print(",Accel-Y[mg]:");
        Serial.print(accel.y);
        Serial.print(",Accel-Z[mg]:");
        Serial.println(accel.z);
    } else {
        Serial.println("Failed to read acceleration data!");
    }
}
```

<QuickLink
  title="serialPlotter.ino"
  description="Continuously polls X/Y/Z acceleration and outputs it to the Arduino Serial Plotter."
  url="https://github.com/SolderedElectronics/Soldered-IIS2DULPXTR-Accelerometer-Arduino-Library/blob/main/examples/serialPlotter/serialPlotter.ino"
/>

---

## Interrupt-based wake-up detection

The IIS2DULPX can generate an interrupt on **INT1** or **INT2** when motion above a threshold is detected. This allows the microcontroller to sleep and only wake up when movement occurs:

```cpp
#include <Soldered-IIS2DULPX.h>

#define INT1_PIN   5   // Connect INT1 of the breakout to this pin
#define BUZZER_PIN 23  // Optional buzzer for feedback

Soldered_IIS2DULPX sensor;
volatile int mems_event = 0;

void INT1Event_cb()
{
    mems_event = 1;
}

void setup()
{
    Serial.begin(115200);
    Wire.begin();

    attachInterrupt(INT1_PIN, INT1Event_cb, RISING);

    sensor.begin();
    sensor.Enable_X();

    // Enable wake-up detection on INT1
    sensor.Enable_Wake_Up_Detection(IIS2DULPX_INT1_PIN);
}

void loop()
{
    if (mems_event) {
        mems_event = 0;

        IIS2DULPX_Event_Status_t status;
        sensor.Get_X_Event_Status(&status);

        if (status.WakeUpStatus) {
            Serial.println("Wake-up detected!");
            tone(BUZZER_PIN, 200, 200);
        }
    }
}
```

<FunctionDocumentation
  functionName="sensor.Enable_Wake_Up_Detection(intPin)"
  description="Enables wake-up detection. An interrupt is generated on the specified pin when the accelerometer detects motion exceeding the wake-up threshold."
  returnDescription="Returns `IIS2DULPX_OK` (0) on success, `IIS2DULPX_ERROR` (-1) on failure."
  parameters={[
    { name: "intPin", type: "IIS2DULPX_SensorIntPin_t", description: "Interrupt pin to route the event to: IIS2DULPX_INT1_PIN or IIS2DULPX_INT2_PIN." }
  ]}
/>

<FunctionDocumentation
  functionName="sensor.Get_X_Event_Status(&status)"
  description="Reads the current event status register and populates the provided structure with flags for all detected events (wake-up, free-fall, tap, tilt, orientation, step, sleep)."
  returnDescription="Returns `IIS2DULPX_OK` (0) on success, `IIS2DULPX_ERROR` (-1) on failure."
  parameters={[
    { name: "status", type: "IIS2DULPX_Event_Status_t *", description: "Pointer to a structure that will be populated with event flags." }
  ]}
/>

<FunctionDocumentation
  functionName="sensor.Set_Wake_Up_Threshold(threshold)"
  description="Sets the wake-up detection threshold. The threshold is expressed in LSB units relative to the configured full scale."
  returnDescription="Returns `IIS2DULPX_OK` (0) on success, `IIS2DULPX_ERROR` (-1) on failure."
  parameters={[
    { name: "threshold", type: "uint32_t", description: "Wake-up threshold value in LSB." }
  ]}
/>

<QuickLink
  title="interruptWakeup.ino"
  description="Uses INT1 to detect motion and trigger a buzzer tone on wake-up."
  url="https://github.com/SolderedElectronics/Soldered-IIS2DULPXTR-Accelerometer-Arduino-Library/blob/main/examples/interruptWakeup/interruptWakeup.ino"
/>
