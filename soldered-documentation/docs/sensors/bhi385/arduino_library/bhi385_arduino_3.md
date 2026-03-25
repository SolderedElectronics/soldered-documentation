---
slug: /bhi385/arduino/more-examples
title: BHI385 – Virtual sensor examples
sidebar_label: Virtual sensor examples
id: bhi385-arduino-3
hide_title: False
---

This page contains additional examples for the BHI385 virtual sensors beyond basic accelerometer and gyroscope reading.

---

## Game Rotation Vector (orientation quaternion)

The **Game Rotation Vector** virtual sensor fuses accelerometer and gyroscope data to produce a normalized orientation **quaternion** (x, y, z, w). It does not use a magnetometer, so yaw is relative to the sensor orientation at power-on. Pitch and roll are absolute (gravity-referenced).

<QuickLink
  title="GameRotationVector.ino"
  description="Read a normalized orientation quaternion from the BHI385"
  url="https://github.com/SolderedElectronics/Soldered-BHI385-Arduino-Library/blob/main/examples/GameRotationVector/GameRotationVector.ino"
/>

```cpp
#include "BHI385-SOLDERED.h"
#include "BHI385_firmware.h"

BHI385 imu;

void setup()
{
    Serial.begin(115200);
    while (!Serial)
        delay(10);

    Wire.setClock(400000);
    imu.begin(BHI385_I2C_ADDR_HIGH);
    imu.loadFirmware(bhi385Firmware, sizeof(bhi385Firmware));

    imu.enableGameRotationVector(100.0f);

    Serial.println("Quat X\t\tQuat Y\t\tQuat Z\t\tQuat W");
}

void loop()
{
    if (imu.update() && imu.quatUpdated())
    {
        Serial.print(imu.getQuatX(), 4); Serial.print("\t\t");
        Serial.print(imu.getQuatY(), 4); Serial.print("\t\t");
        Serial.print(imu.getQuatZ(), 4); Serial.print("\t\t");
        Serial.println(imu.getQuatW(), 4);
        imu.clearUpdatedFlags();
    }
    delay(20);
}
```

<FunctionDocumentation
  functionName="imu.enableGameRotationVector(rateHz)"
  description="Enables the Game Rotation Vector virtual sensor, which fuses accelerometer and gyroscope data to output a normalized quaternion. No magnetometer is used, so absolute heading (yaw) is not available — yaw is relative to the orientation at power-on."
  returnDescription="Returns `true` on success."
  parameters={[
    { type: "float", name: "rateHz", description: "Output data rate in Hz. Default: 100.0." },
  ]}
/>

<CenteredImage src="/img/bhi385/game.png" alt="GameRotationVector serial monitor output" caption="GameRotationVector serial monitor output" width="800px" />

---

## Step Counter

The **Step Counter** virtual sensor counts cumulative footsteps detected while walking or running. The count persists across sensor enable/disable cycles but resets on power-off.

<QuickLink
  title="StepCounter.ino"
  description="Count footsteps using the BHI385 step counter virtual sensor"
  url="https://github.com/SolderedElectronics/Soldered-BHI385-Arduino-Library/blob/main/examples/StepCounter/StepCounter.ino"
/>

```cpp
#include "BHI385-SOLDERED.h"
#include "BHI385_firmware.h"

BHI385 imu;

void setup()
{
    Serial.begin(115200);
    while (!Serial)
        delay(10);

    Wire.setClock(400000);
    imu.begin(BHI385_I2C_ADDR_HIGH);
    imu.loadFirmware(bhi385Firmware, sizeof(bhi385Firmware));

    imu.enableStepCounter(100.0f);

    Serial.println("Walk around to count steps.");
    Serial.println("Steps");
}

void loop()
{
    if (imu.update() && imu.stepUpdated())
    {
        Serial.println(imu.getStepCount());
        imu.clearUpdatedFlags();
    }
    delay(100);
}
```

<FunctionDocumentation
  functionName="imu.enableStepCounter(rateHz)"
  description="Enables the step counter virtual sensor. Outputs a cumulative step count (uint32) that increments as walking or running is detected. The count resets on power-off."
  returnDescription="Returns `true` on success."
  parameters={[
    { type: "float", name: "rateHz", description: "Update rate in Hz. Default: 100.0." },
  ]}
/>

<CenteredImage src="/img/bhi385/steps.png" alt="StepCounter serial monitor output" caption="StepCounter serial monitor output" width="800px" />

---

## Tap detection

The **multi-tap sensor** detects single, double, or triple taps on the board. Use `BHI385_TAP_SINGLE` or `BHI385_TAP_DOUBLE` to configure which tap types to detect.

<QuickLink
  title="SingleTap.ino"
  description="Detect single taps using the BHI385 multi-tap virtual sensor"
  url="https://github.com/SolderedElectronics/Soldered-BHI385-Arduino-Library/blob/main/examples/SingleTap/SingleTap.ino"
/>

<QuickLink
  title="DoubleTap.ino"
  description="Detect double taps using the BHI385 multi-tap virtual sensor"
  url="https://github.com/SolderedElectronics/Soldered-BHI385-Arduino-Library/blob/main/examples/DoubleTap/DoubleTap.ino"
/>

```cpp
#include "BHI385-SOLDERED.h"
#include "BHI385_firmware.h"

BHI385 imu;
uint32_t tapCount = 0;

void setup()
{
    Serial.begin(115200);
    while (!Serial)
        delay(10);

    Wire.setClock(400000);
    imu.begin(BHI385_I2C_ADDR_HIGH);
    imu.loadFirmware(bhi385Firmware, sizeof(bhi385Firmware));

    // Detect single taps only (use BHI385_TAP_DOUBLE for double taps)
    imu.enableMultiTapDetect(BHI385_TAP_SINGLE, 100.0f);

    Serial.println("Tap the sensor once to detect a single tap.");
}

void loop()
{
    if (imu.update() && imu.tapUpdated())
    {
        if (imu.getTapType() == BHI385_TAP_SINGLE)
        {
            tapCount++;
            Serial.print("Single tap #"); Serial.println(tapCount);
        }
        imu.clearUpdatedFlags();
    }
}
```

<FunctionDocumentation
  functionName="imu.enableMultiTapDetect(tapMask, rateHz)"
  description="Enables the multi-tap virtual sensor. Configure which tap types to detect by passing a bitmask of bhi385TapType values."
  returnDescription="Returns `true` on success."
  parameters={[
    { type: "uint8_t", name: "tapMask", description: "Bitmask of tap types: BHI385_TAP_SINGLE (1), BHI385_TAP_DOUBLE (2), BHI385_TAP_ALL (7), etc. Default: BHI385_TAP_ALL." },
    { type: "float", name: "rateHz", description: "Sensor update rate in Hz. Default: 100.0." },
  ]}
/>

<CenteredImage src="/img/bhi385/singletap.png" alt="SingleTap serial monitor output" caption="SingleTap serial monitor output" width="600px" />

---

## Wrist gesture detection

The **Wrist Gesture Detect** virtual sensor recognizes three wrist motions: wrist shake/jiggle, arm flick in, and arm flick out. Configure for the correct wrist using `BHI385_WRIST_LEFT` or `BHI385_WRIST_RIGHT`.

<QuickLink
  title="WristGestureDetect.ino"
  description="Detect wrist gestures using the BHI385 wrist gesture virtual sensor"
  url="https://github.com/SolderedElectronics/Soldered-BHI385-Arduino-Library/blob/main/examples/WristGestureDetect/WristGestureDetect.ino"
/>

```cpp
#include "BHI385-SOLDERED.h"
#include "BHI385_firmware.h"

BHI385 imu;

const char *gestureName(uint8_t gesture)
{
    switch (gesture)
    {
    case BHI385_WRIST_GEST_SHAKE_JIGGLE: return "Wrist shake/jiggle";
    case BHI385_WRIST_GEST_FLICK_IN:     return "Arm flick in";
    case BHI385_WRIST_GEST_FLICK_OUT:    return "Arm flick out";
    default:                              return "No gesture";
    }
}

void setup()
{
    Serial.begin(115200);
    while (!Serial)
        delay(10);

    Wire.setClock(400000);
    imu.begin(BHI385_I2C_ADDR_HIGH);
    imu.loadFirmware(bhi385Firmware, sizeof(bhi385Firmware));

    // Pass BHI385_WRIST_RIGHT if the device is on the right wrist
    imu.enableWristGestureDetect(100.0f, BHI385_WRIST_LEFT);

    Serial.println("Perform a wrist gesture to detect it.");
}

void loop()
{
    if (imu.update() && imu.wristGestureUpdated())
    {
        uint8_t gesture = imu.getWristGesture();
        Serial.println(gestureName(gesture));
        imu.clearUpdatedFlags();
    }
}
```

<FunctionDocumentation
  functionName="imu.enableWristGestureDetect(rateHz, hand)"
  description="Enables the wrist gesture detect virtual sensor. The firmware uses gravity-bound checks that are mirrored between left and right wrist orientations, so passing the correct hand is important for accurate detection."
  returnDescription="Returns `true` on success."
  parameters={[
    { type: "float", name: "rateHz", description: "Output rate in Hz. Default: 100.0." },
    { type: "bhi385WristHand", name: "hand", description: "BHI385_WRIST_LEFT (0) for left wrist, BHI385_WRIST_RIGHT (1) for right wrist. Default: BHI385_WRIST_LEFT." },
  ]}
/>

<CenteredImage src="/img/bhi385/gesture.png" alt="WristGestureDetect serial monitor output" caption="WristGestureDetect serial monitor output" width="800px" />
