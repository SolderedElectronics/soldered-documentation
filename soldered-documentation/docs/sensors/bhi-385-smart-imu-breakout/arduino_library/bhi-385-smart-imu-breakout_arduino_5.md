---
slug: /bhi-385-smart-imu-breakout/arduino/step-counter-tap-detection
title: BHI385 Smart IMU - Step Counter and Multi-Tap Detection
sidebar_label: Step Counter and Multi-Tap
id: bhi-385-smart-imu-breakout-arduino-5
hide_title: false
---

This page covers the BHI385's activity recognition sensors: the cumulative step counter and the multi-tap gesture detector.

---

## Step counter

The step counter virtual sensor uses an adaptive pedometer algorithm in the firmware to count footsteps cumulatively. The count increments automatically as the sensor detects walking or running patterns; it resets to zero on power-off.

```cpp
void setup()
{
    // ... begin() and loadFirmware() as above ...

    imu.enableStepCounter(100.0f);
}

void loop()
{
    if (imu.update())
    {
        if (imu.stepUpdated())
        {
            Serial.print("Steps: ");
            Serial.println(imu.getStepCount());
        }
        imu.clearUpdatedFlags();
    }
    delay(100);
}
```

<FunctionDocumentation
  functionName="imu.enableStepCounter()"
  description="Enables the low-power step counter virtual sensor. The firmware increments the cumulative step count each time a footstep-like acceleration signature is detected. The count persists across enable/disable cycles but resets on power-off."
  returnDescription="true if the sensor was configured successfully"
  parameters={[
    { type: 'float', name: 'rateHz', description: 'Sensor update rate in Hz. Default: 100.0f' },
  ]}
/>

<FunctionDocumentation
  functionName="imu.getStepCount()"
  description="Returns the current cumulative step count as reported by the firmware step counter. Valid after update() returns with stepUpdated() true."
  returnDescription="Cumulative step count as uint32_t"
  parameters={[]}
/>

---

## Multi-tap detection

The multi-tap sensor detects sharp, brief acceleration impulses and classifies them as single, double, or triple taps. You configure which tap types to detect via a bitmask before enabling the sensor.

```cpp
void setup()
{
    // ... begin() and loadFirmware() as above ...

    // Detect double taps only
    imu.enableMultiTapDetect(BHI385_TAP_DOUBLE, 100.0f);
}

void loop()
{
    if (imu.update())
    {
        if (imu.tapUpdated())
        {
            if (imu.getTapType() == BHI385_TAP_SINGLE)  Serial.println("Single tap!");
            if (imu.getTapType() == BHI385_TAP_DOUBLE)  Serial.println("Double tap!");
            if (imu.getTapType() == BHI385_TAP_TRIPLE)  Serial.println("Triple tap!");
        }
        imu.clearUpdatedFlags();
    }
}
```

<FunctionDocumentation
  functionName="imu.enableMultiTapDetect()"
  description="Enables the multi-tap detection virtual sensor. Writes the tap-type bitmask to the firmware parameter page before activating the sensor, so only the requested tap types generate events. Use BHI385_TAP_ALL to detect single, double, and triple taps simultaneously."
  returnDescription="true if the parameter write and sensor configuration both succeeded"
  parameters={[
    { type: 'uint8_t', name: 'tapMask', description: 'OR-combined bitmask of tap types to detect: BHI385_TAP_SINGLE (1), BHI385_TAP_DOUBLE (2), BHI385_TAP_TRIPLE (4), or BHI385_TAP_ALL (7). Default: BHI385_TAP_ALL' },
    { type: 'float', name: 'rateHz', description: 'Sensor update rate in Hz. Default: 100.0f' },
  ]}
/>

<FunctionDocumentation
  functionName="imu.getTapType()"
  description="Returns the tap type reported in the most recent multi-tap event. Matches one of the bhi385TapType enum values: BHI385_TAP_SINGLE, BHI385_TAP_DOUBLE, or BHI385_TAP_TRIPLE. Valid after update() returns with tapUpdated() true."
  returnDescription="Tap type as uint8_t (bhi385TapType enum value)"
  parameters={[]}
/>
