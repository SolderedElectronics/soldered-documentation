---
slug: /bhi-385-smart-imu-breakout/arduino/accelerometer-gyroscope
title: BHI385 Smart IMU - Accelerometer and Gyroscope
sidebar_label: Accelerometer and Gyroscope
id: bhi-385-smart-imu-breakout-arduino-3
hide_title: false
---

This page covers reading linear acceleration and angular velocity from the BHI385's corrected accelerometer and gyroscope virtual sensors.

---

## Reading accelerometer and gyroscope

After initialization, enable the accelerometer and gyroscope, then call `update()` in your loop. Check `accelUpdated()` or `gyroUpdated()` before reading to confirm that new data arrived in the latest FIFO drain.

```cpp
void setup()
{
    // ... begin() and loadFirmware() as above ...

    imu.enableAccelerometer(100.0f, BHI385_ACCEL_8G);  // 100 Hz, ±8 g
    imu.enableGyroscope(100.0f, BHI385_GYRO_2000DPS);  // 100 Hz, ±2000 deg/s
}

void loop()
{
    if (imu.update())
    {
        if (imu.accelUpdated())
        {
            Serial.print("Accel X: "); Serial.print(imu.getAccelX(), 4); Serial.print(" g  ");
            Serial.print("Y: ");       Serial.print(imu.getAccelY(), 4); Serial.print(" g  ");
            Serial.print("Z: ");       Serial.println(imu.getAccelZ(), 4);
        }
        if (imu.gyroUpdated())
        {
            Serial.print("Gyro  X: "); Serial.print(imu.getGyroX(), 2); Serial.print(" dps  ");
            Serial.print("Y: ");       Serial.print(imu.getGyroY(), 2); Serial.print(" dps  ");
            Serial.print("Z: ");       Serial.println(imu.getGyroZ(), 2);
        }
        imu.clearUpdatedFlags();
    }
    delay(20);
}
```

<FunctionDocumentation
  functionName="imu.enableAccelerometer()"
  description="Enables the corrected accelerometer virtual sensor at the specified output data rate and dynamic range. The firmware applies bias removal and calibration to the raw accelerometer counts before delivering them to the FIFO."
  returnDescription="true if the sensor was configured successfully"
  parameters={[
    { type: 'float', name: 'rateHz', description: 'Output data rate in Hz (e.g. 100.0f). Default: 100.0f' },
    { type: 'bhi385AccelRange', name: 'range', description: 'Dynamic range — BHI385_ACCEL_4G, BHI385_ACCEL_8G (default), BHI385_ACCEL_16G, or BHI385_ACCEL_32G' },
  ]}
/>

<FunctionDocumentation
  functionName="imu.enableGyroscope()"
  description="Enables the corrected gyroscope virtual sensor at the specified output data rate and full-scale range. The firmware applies bias correction before outputting angular velocity."
  returnDescription="true if the sensor was configured successfully"
  parameters={[
    { type: 'float', name: 'rateHz', description: 'Output data rate in Hz. Default: 100.0f' },
    { type: 'bhi385GyroRange', name: 'range', description: 'Full-scale range — BHI385_GYRO_125DPS, BHI385_GYRO_250DPS, BHI385_GYRO_500DPS, BHI385_GYRO_1000DPS, or BHI385_GYRO_2000DPS (default)' },
  ]}
/>

<FunctionDocumentation
  functionName="imu.update()"
  description="Reads and parses all pending data from both the wake-up and non-wake-up FIFOs, updating internal accelerometer, gyroscope, quaternion, step, gesture, and tap fields. Sets the corresponding *Updated flags for any sensor events found. Also drains the STATUS FIFO to prevent overflow. Call this regularly in loop()."
  returnDescription="true if the FIFO read completed (even if no sensor events were present)"
  parameters={[]}
/>

<FunctionDocumentation
  functionName="imu.getAccelX() / getAccelY() / getAccelZ()"
  description="Returns the most recently parsed accelerometer reading for the given axis, in units of g (gravitational acceleration). Values are only valid after update() has returned with accelUpdated() true."
  returnDescription="Acceleration in g as a float"
  parameters={[]}
/>

<FunctionDocumentation
  functionName="imu.getGyroX() / getGyroY() / getGyroZ()"
  description="Returns the most recently parsed gyroscope reading for the given axis, in degrees per second (dps). Values are only valid after update() has returned with gyroUpdated() true."
  returnDescription="Angular velocity in deg/s as a float"
  parameters={[]}
/>

<FunctionDocumentation
  functionName="imu.clearUpdatedFlags()"
  description="Clears all *Updated flags (accelUpdated, gyroUpdated, quatUpdated, stepUpdated, wristGestureUpdated, tapUpdated). Call after processing data from a single update() cycle to avoid acting on stale flags in the next iteration."
  returnDescription="None"
  parameters={[]}
/>
