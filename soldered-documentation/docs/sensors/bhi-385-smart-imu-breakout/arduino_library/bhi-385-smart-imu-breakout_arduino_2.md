---
slug: /bhi-385-smart-imu-breakout/arduino/initialization
title: BHI385 Smart IMU - Initialization
sidebar_label: Initialization
id: bhi-385-smart-imu-breakout-arduino-2
hide_title: false
---

Before any virtual sensor produces data, two steps must complete: `begin()` to verify the chip is reachable, then `loadFirmware()` to upload firmware into program RAM.

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
  functionName="imu.begin()"
  description="Initializes the I2C bus, issues a soft reset to the BHI385, waits for the ROM bootloader to become ready, and verifies the chip ID (expected 0x7C). Must be called before loadFirmware()."
  returnDescription="true if the bootloader is ready and chip identity matches; false on I2C error or wrong chip ID"
  parameters={[
    { type: 'uint8_t', name: 'addr', description: 'I2C address - BHI385_I2C_ADDR_HIGH (0x29) or BHI385_I2C_ADDR_LOW (0x28). The board JP5 jumper defaults to 0x29.' },
    { type: 'TwoWire&', name: 'wire', description: 'Wire instance to use; defaults to the global Wire object' },
  ]}
/>

<FunctionDocumentation
  functionName="imu.loadFirmware()"
  description="Uploads a firmware binary to the BHI385 program RAM in 28-byte I2C chunks, waits for the chip to verify the CRC, sends the boot command, and waits for the firmware to finish booting. This typically takes about 1-5 seconds depending on the I2C clock speed. Must be called after begin() and before enabling any virtual sensors."
  returnDescription="true if the firmware was uploaded, CRC-verified, and booted successfully; false on upload error, CRC mismatch, or timeout"
  parameters={[
    { type: 'const uint8_t*', name: 'firmware', description: 'Pointer to the firmware binary array (from the BHI385_firmware.h header)' },
    { type: 'uint32_t', name: 'fwLen', description: 'Size of the firmware binary in bytes - pass sizeof(bhi385Firmware)' },
  ]}
/>

<FunctionDocumentation
  functionName="imu.enableDebug()"
  description="Enables verbose Serial output that prints every step of the firmware upload and boot process, including byte counts, CRC result, and any I2C error codes. Call before loadFirmware() to get detailed diagnostics."
  returnDescription="None"
  parameters={[]}
/>
