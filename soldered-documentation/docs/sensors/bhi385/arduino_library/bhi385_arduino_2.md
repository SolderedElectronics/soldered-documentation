---
slug: /bhi385/arduino/examples
title: BHI385 – Initialization and basic readings
sidebar_label: Initialization and basic readings
id: bhi385-arduino-2
hide_title: False
---

This page contains examples and function documentation for using the BHI385 Smart IMU with the Soldered Arduino library.

---

## Initialization

To start working with the BHI385, include the library, create a sensor object, and call `begin()` followed by `loadFirmware()` in your `setup()` function.

<InfoBox>

The BHI385 board ships with JP5 bridged to **0x29** (default). Always pass `BHI385_I2C_ADDR_HIGH` to `begin()`. To switch to address **0x28**, move the JP5 solder bridge to the opposite pad and pass `BHI385_I2C_ADDR_LOW` instead.

</InfoBox>

```cpp
// Include the library and the firmware header
// (place BHI385_firmware.h in your sketch folder first — see Getting started)
#include "BHI385-SOLDERED.h"
#include "BHI385_firmware.h"

// Create a BHI385 object
BHI385 imu;

void setup()
{
    Serial.begin(115200);
    while (!Serial)
        delay(10);

    // Set I2C to 400 kHz for faster firmware upload (~1.3 s vs ~5 s at 100 kHz)
    Wire.setClock(400000);

    // Initialize. Pass BHI385_I2C_ADDR_HIGH (0x29) — the Soldered board default.
    if (!imu.begin(BHI385_I2C_ADDR_HIGH))
    {
        Serial.println("Can't initialize BHI385!");
        Serial.println("Check connection and I2C address.");
        while (true)
            ;
    }

    // Upload firmware binary to the BHI385 RAM
    if (!imu.loadFirmware(bhi385Firmware, sizeof(bhi385Firmware)))
    {
        Serial.println("Firmware load failed!");
        while (true)
            ;
    }

    Serial.println("BHI385 initialized successfully.");
}
```

<FunctionDocumentation
  functionName="imu.begin(addr)"
  description="Initializes I2C communication, verifies the BHI385 chip ID, and checks that the host interface is ready. Call this before loadFirmware(). Passing the address is required because the Soldered board default (JP5 open) is 0x29, while the library default parameter is 0x28."
  returnDescription="Returns `true` if the BHI385 is found and the host interface is ready. Returns `false` on wiring error, wrong address, or missing 1.8V supply."
  parameters={[
    { type: "uint8_t", name: "addr", description: "I2C address: BHI385_I2C_ADDR_HIGH (0x29) or BHI385_I2C_ADDR_HIGH (0x28). Default: BHI385_I2C_ADDR_HIGH." },
    { type: "TwoWire&", name: "wire", description: "Wire instance to use. Default: Wire." },
  ]}
/>

<FunctionDocumentation
  functionName="imu.loadFirmware(firmware, fwLen)"
  description="Uploads the Bosch BSX firmware binary to the BHI385 program RAM over I2C and boots it. Must be called after begin() and before enabling any virtual sensors. The firmware header file (BHI385_firmware.h) must be present in your sketch folder."
  returnDescription="Returns `true` if the firmware was uploaded, CRC-verified, and the sensor booted successfully. Returns `false` on upload error or CRC failure."
  parameters={[
    { type: "const uint8_t*", name: "firmware", description: "Pointer to the firmware binary array (from BHI385_firmware.h)." },
    { type: "uint32_t", name: "fwLen", description: "Size of the firmware binary in bytes (use sizeof(bhi385Firmware))." },
  ]}
/>

---

## Accelerometer

### Enabling the accelerometer

```cpp
// Enable accelerometer: 100 Hz output rate, ±8 g full-scale range
if (!imu.enableAccelerometer(100.0f, BHI385_ACCEL_8G))
{
    Serial.println("Failed to enable accelerometer!");
    while (true)
        ;
}
```

<FunctionDocumentation
  functionName="imu.enableAccelerometer(rateHz, range)"
  description="Enables the accelerometer virtual sensor at the specified output data rate and dynamic range."
  returnDescription="Returns `true` on success."
  parameters={[
    { type: "float", name: "rateHz", description: "Output data rate in Hz (e.g. 100.0). Default: 100.0." },
    { type: "bhi385AccelRange", name: "range", description: "Dynamic range: BHI385_ACCEL_4G, BHI385_ACCEL_8G, BHI385_ACCEL_16G, or BHI385_ACCEL_32G. Default: BHI385_ACCEL_8G." },
  ]}
/>

### Reading accelerometer data

Call `update()` in the loop and check `accelUpdated()` before reading the values.

```cpp
void loop()
{
    if (imu.update())
    {
        if (imu.accelUpdated())
        {
            Serial.print("AccelX: "); Serial.print(imu.getAccelX(), 4); Serial.print(" g  ");
            Serial.print("AccelY: "); Serial.print(imu.getAccelY(), 4); Serial.print(" g  ");
            Serial.print("AccelZ: "); Serial.println(imu.getAccelZ(), 4);
        }
        imu.clearUpdatedFlags();
    }
    delay(20);
}
```

<FunctionDocumentation
  functionName="imu.update()"
  description="Reads all pending data from the BHI385 FIFO buffers and parses sensor events. Call this in every loop iteration (or from an interrupt handler). After calling, use the *Updated() flags to check which sensors have new data."
  returnDescription="Returns `true` if at least one new sensor event was available in the FIFO."
  parameters={[]}
/>

<FunctionDocumentation
  functionName="imu.getAccelX() / getAccelY() / getAccelZ()"
  description="Returns the most recently received calibrated accelerometer value along the given axis."
  returnDescription="Returns a float in units of g (gravitational acceleration). Valid after accelUpdated() returns true."
  parameters={[]}
/>

{/* TODO: add serial monitor screenshot for accelerometer example */}

---

## Gyroscope

### Enabling the gyroscope

```cpp
// Enable gyroscope: 100 Hz output rate, ±2000 dps full-scale range
if (!imu.enableGyroscope(100.0f, BHI385_GYRO_2000DPS))
{
    Serial.println("Failed to enable gyroscope!");
    while (true)
        ;
}
```

<FunctionDocumentation
  functionName="imu.enableGyroscope(rateHz, range)"
  description="Enables the gyroscope virtual sensor at the specified output data rate and full-scale range."
  returnDescription="Returns `true` on success."
  parameters={[
    { type: "float", name: "rateHz", description: "Output data rate in Hz (e.g. 100.0). Default: 100.0." },
    { type: "bhi385GyroRange", name: "range", description: "Full-scale range: BHI385_GYRO_125DPS, BHI385_GYRO_250DPS, BHI385_GYRO_500DPS, BHI385_GYRO_1000DPS, or BHI385_GYRO_2000DPS. Default: BHI385_GYRO_2000DPS." },
  ]}
/>

### Reading gyroscope data

```cpp
if (imu.gyroUpdated())
{
    Serial.print("GyroX: "); Serial.print(imu.getGyroX(), 4); Serial.print(" dps  ");
    Serial.print("GyroY: "); Serial.print(imu.getGyroY(), 4); Serial.print(" dps  ");
    Serial.print("GyroZ: "); Serial.println(imu.getGyroZ(), 4);
}
```

<FunctionDocumentation
  functionName="imu.getGyroX() / getGyroY() / getGyroZ()"
  description="Returns the most recently received calibrated gyroscope value along the given axis."
  returnDescription="Returns a float in units of degrees per second (dps). Valid after gyroUpdated() returns true."
  parameters={[]}
/>

{/* TODO: add serial monitor screenshot for gyroscope example */}

---

## Full example — accelerometer & gyroscope

<QuickLink
  title="ReadAccelGyro.ino"
  description="Read accelerometer and gyroscope data from the BHI385 Smart IMU"
  url="https://github.com/SolderedElectronics/Soldered-BHI385-Arduino-Library/blob/main/examples/ReadAccelGyro/ReadAccelGyro.ino"
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

    Serial.println("BHI385 Accelerometer and Gyroscope example");

    // Set I2C to 400 kHz for faster firmware upload (~1.3 s vs ~5 s)
    Wire.setClock(400000);

    if (!imu.begin(BHI385_I2C_ADDR_HIGH))
    {
        Serial.println("ERROR: BHI385 not found! Check wiring, I2C address, and 1.8V supply.");
        while (1)
            delay(100);
    }

    Serial.println("Loading firmware...");
    if (!imu.loadFirmware(bhi385Firmware, sizeof(bhi385Firmware)))
    {
        Serial.println("Firmware load failed.");
        while (1)
            delay(100);
    }
    Serial.println("Firmware loaded successfully.");

    // Enable accelerometer: 100 Hz, ±8 g
    imu.enableAccelerometer(100.0f, BHI385_ACCEL_8G);

    // Enable gyroscope: 100 Hz, ±2000 deg/s
    imu.enableGyroscope(100.0f, BHI385_GYRO_2000DPS);

    Serial.println("AccelX(g)\tAccelY(g)\tAccelZ(g)\tGyroX(dps)\tGyroY(dps)\tGyroZ(dps)");
}

void loop()
{
    if (imu.update())
    {
        if (imu.accelUpdated())
        {
            Serial.print(imu.getAccelX(), 4); Serial.print("\t\t");
            Serial.print(imu.getAccelY(), 4); Serial.print("\t\t");
            Serial.print(imu.getAccelZ(), 4); Serial.print("\t\t");
        }
        if (imu.gyroUpdated())
        {
            Serial.print(imu.getGyroX(), 4); Serial.print("\t\t");
            Serial.print(imu.getGyroY(), 4); Serial.print("\t\t");
            Serial.println(imu.getGyroZ(), 4);
        }
        imu.clearUpdatedFlags();
    }
    delay(20);
}
```

