---
slug: /inkplate/6color/hardware/power-switch
title: Inkplate 6COLOR – Bypass power switch
sidebar_label: Bypass power switch
id: hardware-power-switch
---

The Inkplate 6COLOR can be configured to power on automatically when current is present, bypassing the power switch.

To bypass the power switch, short the **R16** pads with a small amount of solder, or fit a 0 ohm resistor. R16 is left unpopulated from the factory and sits directly across the switch, between `SW_IN` and `VIN`. The location of these pads is shown below:

<CenteredImage src="/img/6color/pwr_sw_bypass.webp" alt="Power switch location on Inkplate 6COLOR" caption="R16 connection highlighted" />

