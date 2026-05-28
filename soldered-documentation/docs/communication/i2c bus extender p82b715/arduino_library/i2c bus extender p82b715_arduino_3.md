---
slug: /i2c-bus-extender-p82b715/arduino/troubleshooting
title: Troubleshooting
id: i2c bus extender p82b715-arduino-3
hide_title: false
pagination_next: null
---

## I²C device not found after connecting through the extender

- Confirm the Qwiic cable is properly seated on both the microcontroller and the extender (K1 or K2).
- Check that your remote device is wired correctly to the screw terminal (K4): **SCL**, **SDA**, and **GND**.
- Make sure the remote device has its own power supply — the screw terminal does not provide power to the remote device.
- Verify that the jumpers JP1–JP4 are intact (NC by default), providing pull-up resistors to both sides of the bus.

---

## I²C communication is unreliable or intermittent

- Try reducing the I²C clock speed to **100 kHz** (standard mode). At higher speeds, long cables may cause signal integrity issues.
- Check the cable quality and length. While 30 m is theoretically supported, real-world performance depends on cable capacitance and shielding.
- If using multiple devices on the extended bus, verify that their combined capacitance does not exceed **3000 pF**.

---

## Device works at short distances but fails over a long cable

- The cable itself may have too high a capacitance. Use a lower-capacitance cable type (e.g. twisted-pair).
- Reduce I²C speed to 100 kHz.
- Ensure GND is shared across the entire system (microcontroller, extender, and remote device).

---

## Multiple pull-up resistors on the bus

- If your remote I²C device already includes pull-up resistors, cut **JP1** (extended side) to disable the onboard 5V pull-ups.
- If your microcontroller already provides 3.3V pull-ups, cut **JP2**, **JP3**, and/or **JP4** to disable the onboard 3.3V pull-ups.
- Having too many parallel pull-up resistors lowers the effective pull-up resistance and can prevent devices from pulling the line low.

---

## Power LED is not on

- The power LED is disabled by default. Bridge **JP5** to enable it.
- Confirm 3.3V power is reaching the board via the Qwiic cable.
