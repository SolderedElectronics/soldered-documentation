---
slug: /bhi-385-smart-imu-breakout/arduino/troubleshooting
title: BHI385 Smart IMU - Troubleshooting
sidebar_label: Troubleshooting
id: bhi-385-smart-imu-breakout-arduino-7
hide_title: false
pagination_next: null
---

<ExpandableSection title="begin() returns false - sensor not found">

The most common reason `begin()` fails is that the BHI385 is not reachable on the I2C bus.

#### Check your wiring
Make sure the Qwiic/easyC cable is fully seated on both ends. Try a different cable, or wiggle the connector gently. A loose fit is a frequent culprit. If you are wiring manually, confirm that SDA and SCL are not swapped.

#### Check the I2C pins on your board
Different microcontrollers assign I2C to different pin numbers. Consult your board's pinout diagram and make sure you are using the correct SDA and SCL pins. On Dasduino boards, the Qwiic port handles this automatically.

#### Scan the I2C bus
Upload the [**I2C scanner sketch**](https://github.com/SolderedElectronics/Soldered-Hacky-Codes/tree/main/I2C_Scanner) to confirm the BHI385 appears on the bus. It will show up at **0x28** or **0x29** depending on the state of the ADDR solder jumper on the breakout.

#### Verify the I2C address in your code
The library defaults to **0x29** (`BHI385_I2C_ADDR_HIGH`). If the ADDR jumper on your breakout is set to the low position, pass `BHI385_I2C_ADDR_LOW` (0x28) as the first argument to `begin()`:

```cpp
imu.begin(BHI385_I2C_ADDR_LOW);
```

#### Power the board at 3.3 V
The BHI385 operates at 3.3 V. Driving it from a 5 V supply without level shifting may prevent the chip from responding or damage it. The on-board regulator handles conversion when powered through the Qwiic connector.

</ExpandableSection>

<ExpandableSection title="loadFirmware() fails or hangs">

The BHI385 has no internal flash. Firmware must be uploaded into program RAM on every power-on. Several things can cause this step to fail.

#### Make sure the firmware header is in your sketch folder
The firmware binary is distributed by Bosch Sensortec as part of their **BHI385 SensorAPI** package and is **not** included in the Soldered library. Download it from [Bosch Sensortec's GitHub](https://github.com/boschsensortec/BHI385_SensorAPI), locate the `BHI385_firmware.h` file inside the `firmware/` folder, and copy it into the same folder as your `.ino` file. Include it with:

```cpp
#include "BHI385_firmware.h"
```

Without this file, `loadFirmware()` cannot be called at all and will not compile.

#### Enable debug output to see what fails
Call `imu.enableDebug()` before `loadFirmware()` and open the Serial Monitor at 115200 baud. The library will print every stage of the upload (byte count, CRC check result, and boot status) so you can pinpoint exactly where it stops.

#### Increase the I2C clock speed
The firmware binary is large and is sent over I2C in 28-byte chunks. At the default 100 kHz clock speed this can take many seconds and occasionally causes a timeout. Setting the clock to 400 kHz before calling `begin()` speeds up the upload significantly and reduces the chance of a timeout:

```cpp
Wire.setClock(400000);
imu.begin(BHI385_I2C_ADDR_HIGH);
```

#### Note on ESP32-based boards and RAM
On ESP32-based boards (including NULA DeepSleep), the library copies the firmware to a RAM staging buffer before uploading it over I2C, because the ESP32's Wire DMA cannot read directly from flash. This means the firmware binary must fit in available heap. If you see a crash immediately after calling `loadFirmware()` on an ESP32, check your heap with `ESP.getFreeHeap()` before the call. You need enough free heap for the firmware array plus the rest of your sketch.

</ExpandableSection>

<ExpandableSection title="Virtual sensors enabled but update() never delivers new data">

If `begin()` and `loadFirmware()` both succeed, but your loop never gets new readings, the issue is usually in how sensors are enabled or how `update()` results are checked.

#### Make sure you call the correct enable function before loop()
Each virtual sensor must be explicitly enabled in `setup()` after firmware is loaded. If you skip this step, the FIFO will never carry events for that sensor type:

```cpp
imu.enableAccelerometer(100.0f, BHI385_ACCEL_8G);
imu.enableGyroscope(100.0f, BHI385_GYRO_2000DPS);
```

#### Check *Updated() flags after every update() call
`update()` returns `true` even when the FIFO contained no new events for a particular sensor. Always gate your reads behind the corresponding flag:

```cpp
if (imu.update())
{
    if (imu.accelUpdated())
    {
        // safe to call getAccelX() etc. here
    }
}
```

If you call `getAccelX()` without checking `accelUpdated()`, you will read the last known value, which may be zero if no data has arrived yet.

#### Do not block between update() calls
Any `delay()` longer than one FIFO drain interval can cause the FIFO to overflow and drop events. Keep the main loop tight, or reduce the sensor output data rate to match your loop timing.

</ExpandableSection>

<ExpandableSection title="Readings are always zero or repeat the same value">

If you get readings, but they never change or are always exactly zero, the likely cause is stale flags.

#### Call clearUpdatedFlags() at the end of each loop iteration
After processing data from a single `update()` cycle, call `imu.clearUpdatedFlags()`. Without this, the `*Updated` flags from the previous cycle remain set, and your code will act on stale data instead of waiting for fresh events:

```cpp
void loop()
{
    if (imu.update())
    {
        if (imu.accelUpdated())
        {
            Serial.println(imu.getAccelX());
        }
        imu.clearUpdatedFlags(); // must be here
    }
}
```

#### Verify that the correct sensor is enabled
Double-check that the `enable*()` call in `setup()` matches the getter you are calling in `loop()`. For example, enabling only `enableStepCounter()` and then calling `getAccelX()` will always return zero because the accelerometer virtual sensor was never started.

</ExpandableSection>

<ExpandableSection title="Gyroscope drifts or accelerometer readings are inaccurate">

Some variation in raw readings is expected, but unusually high drift or offset usually has a physical or configuration cause.

#### Keep the board still during the first few seconds after power-on
The BHI385 firmware runs an automatic bias-calibration routine when it first boots. Moving the board during this window can corrupt the initial calibration and cause persistent drift. Let the board sit flat and motionless for 2-3 seconds after `loadFirmware()` returns before collecting data.

#### Reduce the full-scale range if your application does not need the maximum
Choosing a wider range (e.g. `BHI385_GYRO_2000DPS`) reduces resolution at low angular velocities. If your project measures gentle motion, switch to a narrower range:

```cpp
imu.enableGyroscope(100.0f, BHI385_GYRO_125DPS);
```

Similarly for the accelerometer, prefer `BHI385_ACCEL_4G` over `BHI385_ACCEL_32G` if you do not expect large accelerations.

#### Check for mechanical vibration from nearby components
The BHI385 is sensitive to vibration. If the breakout is mounted near a motor, fan, or buzzer, structural vibration will appear as noise on both the accelerometer and gyroscope. Mount the board on a vibration-isolated surface or add low-pass filtering in software.

</ExpandableSection>

<InfoBox>In case you haven't found the answer to your question, please **contact us** via [**this**](https://soldered.com/contact/) link.</InfoBox>
