---
slug: /bhi-385-smart-imu-breakout/arduino/game-rotation-vector
title: BHI385 Smart IMU - Game Rotation Vector
sidebar_label: Game Rotation Vector
id: bhi-385-smart-imu-breakout-arduino-4
hide_title: false
---

This page covers reading orientation as a normalized quaternion from the BHI385's Game Rotation Vector virtual sensor.

---

## Game Rotation Vector (quaternion)

The Game Rotation Vector fuses accelerometer and gyroscope data to output a normalized quaternion representing the device's orientation. Pitch and roll are absolute (gravity-referenced); yaw drifts over time because there is no magnetometer.

```cpp
void setup()
{
    // ... begin() and loadFirmware() as above ...

    imu.enableGameRotationVector(100.0f); // 100 Hz
}

void loop()
{
    if (imu.update())
    {
        if (imu.quatUpdated())
        {
            Serial.print("X: "); Serial.print(imu.getQuatX(), 4);
            Serial.print("  Y: "); Serial.print(imu.getQuatY(), 4);
            Serial.print("  Z: "); Serial.print(imu.getQuatZ(), 4);
            Serial.print("  W: "); Serial.println(imu.getQuatW(), 4);
        }
        imu.clearUpdatedFlags();
    }
    delay(20);
}
```

<FunctionDocumentation
  functionName="imu.enableGameRotationVector()"
  description="Enables the Game Rotation Vector virtual sensor, which fuses accelerometer and gyroscope data to produce a normalized quaternion (x, y, z, w). Does not use a magnetometer, so yaw is relative to the device orientation at power-on."
  returnDescription="true if the sensor was configured successfully"
  parameters={[
    { type: 'float', name: 'rateHz', description: 'Output data rate in Hz. Default: 100.0f' },
  ]}
/>

<FunctionDocumentation
  functionName="imu.getQuatX() / getQuatY() / getQuatZ() / getQuatW()"
  description="Returns the specified component of the most recently received normalized quaternion. All four components are in the range -1.0 to +1.0. Valid after update() returns with quatUpdated() true."
  returnDescription="Quaternion component as a float in range [-1, +1]"
  parameters={[]}
/>
