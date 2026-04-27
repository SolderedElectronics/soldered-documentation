---
slug: /iis2dulpx/arduino/troubleshooting 
title: Troubleshooting
id: iis2dulpx-arduino-3 
hide_title: False
pagination_next: null
---

## Sensor not detected / `begin()` returns error

**Symptoms:** Serial monitor prints `"Failed to initialize IIS2DULPX sensor!"` and the sketch halts.

**Possible causes and fixes:**

- **Incorrect wiring** — Double-check that SDA and SCL are connected to the correct pins on your microcontroller. On Dasduino CONNECTPLUS, these are IO21 (SDA) and IO22 (SCL). Refer to your board's pinout diagram.
- **Missing `Wire.begin()`** — Make sure you call `Wire.begin()` before `sensor.begin()` in `setup()`.
- **Wrong I2C address** — The board's I2C address is fixed at **0x18**. Verify this matches what your I2C scanner reports.
- **Power supply issue** — Make sure VCC is connected and the board is receiving power. The onboard LED (if present) should be lit.
- **I2C bus conflict** — If multiple I2C devices are on the bus, check for address conflicts. Use an I2C scanner sketch to list all detected devices.

---

## Acceleration readings are always zero or invalid

**Symptoms:** `Get_X_Axes()` returns `IIS2DULPX_OK` but all values are 0 or constant.

**Possible causes and fixes:**

- **Accelerometer not enabled** — Ensure you called `sensor.Enable_X()` after `sensor.begin()`.
- **Full scale or ODR misconfigured** — Make sure `Set_X_FullScale()` is called with a valid value (2, 4, 8, or 16) and `Set_X_OutputDataRate()` is set to a non-zero rate.
- **Reading too fast** — If you are reading faster than the configured ODR, the data register may not have updated yet. Add a delay or poll the data-ready status with `Get_X_DRDY_Status()`.

---

## Interrupt not triggering

**Symptoms:** The ISR attached to INT1/INT2 is never called even when the board is moved.

**Possible causes and fixes:**

- **INT pin not connected** — Make sure the INT1 (or INT2) pin of the breakout is wired to a digital input pin on your microcontroller that supports interrupts.
- **`attachInterrupt` using wrong pin number** — On ESP32-based boards (like Dasduino CONNECTPLUS), pass the GPIO number directly. On AVR-based boards (like Uno), use `digitalPinToInterrupt(pin)`.
- **Wake-up threshold too high** — Lower the threshold with `sensor.Set_Wake_Up_Threshold(value)`. Start with a small value and increase it as needed.
- **Wrong interrupt pin specified** — Ensure the pin passed to `Enable_Wake_Up_Detection()` matches the physical pin you wired:
  ```cpp
  sensor.Enable_Wake_Up_Detection(IIS2DULPX_INT1_PIN); // routes to INT1
  ```

---

## Library not found / compilation error

**Symptoms:** Arduino IDE reports `"No such file or directory"` for `Soldered-IIS2DULPX.h`.

**Fix:** Install the library via Arduino Library Manager by searching for **"Soldered IIS2DULPXTR Accelerometer"**, or download and install it manually from the [GitHub repository](https://github.com/SolderedElectronics/Soldered-IIS2DULPXTR-Accelerometer-Arduino-Library).

---

## Still having issues?

If none of the above resolved your problem, reach out to the Soldered community or support team:

<QuickLink
  title="Soldered Community & Technical Support"
  description="Get help from the Soldered team and community forum."
  url="https://soldered.com/community"
/>
