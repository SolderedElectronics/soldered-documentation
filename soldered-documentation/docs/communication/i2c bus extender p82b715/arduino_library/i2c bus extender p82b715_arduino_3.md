---
slug: /i2c-bus-extender-p82b715/arduino/troubleshooting
title: Troubleshooting
id: i2c bus extender p82b715-arduino-3
hide_title: false
pagination_next: null
---

This page contains some tips in case you are having problems using this product.

<ExpandableSection title="I can't find my I²C device after connecting through the extender!">

#### Check wiring

- Confirm the Qwiic cable is properly seated on both the microcontroller and the extender (K1 or K2).
- Check that your remote device is wired correctly to the screw terminal (K4): **SCL**, **SDA**, and **GND**.

#### Check power

Make sure the remote device has its own power supply. The screw terminal doesn't provide power to it.

#### Check pull-ups

Verify a shunt is present on **JP1** and **JP2**, providing pull-up resistors to the local side of the bus. The extended side's pull-ups are fixed and always active.

</ExpandableSection>

<ExpandableSection title="Communication is unreliable or intermittent!">

#### Reduce clock speed

Try reducing the I²C clock speed to **100 kHz** (standard mode). At higher speeds, long cables may cause signal integrity issues.

#### Check cable quality

Check the cable quality and length. While 50 m is theoretically supported, real-world performance depends on cable capacitance and shielding.

#### Check total capacitance

If using multiple devices on the extended bus, verify that their combined capacitance does not exceed **3000 pF**.

</ExpandableSection>

<ExpandableSection title="It works at short distances but fails over a long cable!">

#### Check cable type

The cable itself may have too high a capacitance. Use a lower-capacitance cable type (e.g. twisted-pair).

#### Reduce clock speed

Reduce I²C speed to 100 kHz.

#### Check ground connection

Ensure GND is shared across the entire system (microcontroller, extender, and remote device).

</ExpandableSection>

<ExpandableSection title="There are multiple pull-up resistors on my bus!">

#### Extended side

If your remote device (on the screw terminal side) already includes pull-up resistors, this can conflict with the fixed 5V pull-ups on that side. There's no jumper to disable them.

#### Local side

If your local-side device or microcontroller already provides its own pull-ups, remove the shunt on **JP1** (SDA) and/or **JP2** (SCL) to disable the onboard local-side pull-ups.

Having too many parallel pull-up resistors lowers the effective pull-up resistance and can prevent devices from pulling the line low.

</ExpandableSection>

<ExpandableSection title="The power LED isn't on!">

#### Check JP5

The power LED is on by default, so if it's dark, check that **JP5** hasn't been cut. If it was cut on purpose to disable the LED, this is expected.

#### Check power

Confirm 3.3V power is reaching the board via the Qwiic cable.

</ExpandableSection>

<InfoBox>In case you haven't found the answer to your question, please **Contact us** via [**this**](https://soldered.com/contact/) link, or ask on the [**Soldered community**](https://community.soldered.com), a great place to browse existing questions or post your own.</InfoBox>
