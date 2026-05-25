---
slug: /bhi-385-smart-imu-breakout/arduino/examples
title: BHI385 Smart IMU - Examples
sidebar_label: Examples
id: bhi-385-smart-imu-breakout-arduino-2
hide_title: false
---

This page covers how to initialize the BHI385, upload its firmware, and use the key virtual sensors — accelerometer, gyroscope, Game Rotation Vector, step counter, and multi-tap detection.

---

## Connections for this example

<!-- <CenteredImage src="/img/bhi-385-smart-imu-breakout/connections.png" alt="BHI385 connections" /> -->

---

## Initialization and firmware loading

The BHI385 requires two steps before any sensor data is available: `begin()` initializes the I2C interface and verifies the chip ID, then `loadFirmware()` uploads the firmware binary into the chip's program RAM and boots the internal processor. Both steps must succeed before calling any `enable*()` function.

```cpp
#include "BHI385-SOLDERED.h"
#include "BHI385_firmware.h"  // Firmware header from Bosch Sensortec SensorAPI

BHI385 imu;

void setup()
{
    Serial.begin(115200);
    Wire.setClock(400000); // 400 kHz speeds up firmware upload significantly

    if (!imu.begin(BHI385_I2C_ADDR_HIGH)) // Use BHI385_I2C_ADDR_LOW for 0x28
    {
        Serial.println("BHI385 not found! Check connections.");
        while (1) delay(100);
    }

    imu.enableDebug(); // Prints step-by-step firmware load progress to Serial

    if (!imu.loadFirmware(bhi385Firmware, sizeof(bhi385Firmware)))
    {
        Serial.println("Firmware load failed!");
        while (1) delay(100);
    }

    Serial.println("Ready.");
}
```

<FunctionDocumentation
  functionName="imu.begin(addr, wire)"
  description="Initializes the I2C bus, issues a soft reset to the BHI385, waits for the ROM bootloader to become ready, and verifies the chip ID (expected 0x7C). Must be called before loadFirmware()."
  returnDescription="true if the bootloader is ready and chip identity matches; false on I2C error or wrong chip ID"
  parameters={[
    { type: 'uint8_t', name: 'addr', description: 'I2C address — BHI385_I2C_ADDR_HIGH (0x29, default) or BHI385_I2C_ADDR_LOW (0x28)' },
    { type: 'TwoWire&', name: 'wire', description: 'Wire instance to use; defaults to the global Wire object' },
  ]}
/>

<FunctionDocumentation
  functionName="imu.loadFirmware(firmware, fwLen)"
  description="Uploads a firmware binary to the BHI385 program RAM in 28-byte I2C chunks, waits for the chip to verify the CRC, sends the boot command, and waits for the firmware to finish booting. This typically takes about 1–5 seconds depending on the I2C clock speed. Must be called after begin() and before enabling any virtual sensors."
  returnDescription="true if the firmware was uploaded, CRC-verified, and booted successfully; false on upload error, CRC mismatch, or timeout"
  parameters={[
    { type: 'const uint8_t*', name: 'firmware', description: 'Pointer to the firmware binary array (from the BHI385_firmware.h header)' },
    { type: 'uint32_t', name: 'fwLen', description: 'Size of the firmware binary in bytes — pass sizeof(bhi385Firmware)' },
  ]}
/>

<FunctionDocumentation
  functionName="imu.enableDebug()"
  description="Enables verbose Serial output that prints every step of the firmware upload and boot process, including byte counts, CRC result, and any I2C error codes. Call before loadFirmware() to get detailed diagnostics."
  returnDescription="None"
  parameters={[]}
/>

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
  functionName="imu.enableAccelerometer(rateHz, range)"
  description="Enables the corrected accelerometer virtual sensor at the specified output data rate and dynamic range. The firmware applies bias removal and calibration to the raw accelerometer counts before delivering them to the FIFO."
  returnDescription="true if the sensor was configured successfully"
  parameters={[
    { type: 'float', name: 'rateHz', description: 'Output data rate in Hz (e.g. 100.0f). Default: 100.0f' },
    { type: 'bhi385AccelRange', name: 'range', description: 'Dynamic range — BHI385_ACCEL_4G, BHI385_ACCEL_8G (default), BHI385_ACCEL_16G, or BHI385_ACCEL_32G' },
  ]}
/>

<FunctionDocumentation
  functionName="imu.enableGyroscope(rateHz, range)"
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
  functionName="imu.enableGameRotationVector(rateHz)"
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
  functionName="imu.enableStepCounter(rateHz)"
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
  functionName="imu.enableMultiTapDetect(tapMask, rateHz)"
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
