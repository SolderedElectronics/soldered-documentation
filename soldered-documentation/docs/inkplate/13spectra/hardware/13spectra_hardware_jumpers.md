---
slug: /inkplate/13spectra/hardware/jumpers
title: Inkplate 13SPECTRA – Jumpers
sidebar_label: Jumpers
id: 13spectra-hardware-jumpers
---

Inkplate 13SPECTRA features several **on-board jumpers**, which can be used to modify the behaviour of certain components. Some jumpers are **connected by default**, while others need to be manually shorted.

See the table below for detailed explanation of each jumper's function:

---

| Jumper 	| Default State 	| Function 	|
|---	|---	|---	|
| **JP1** 	| **NC** (connected) 	| When shorted, it provides a connectoin (on oin IO16) to IO Exapander's INT pin, effectively controlling it 	|
| **JP2** 	| **NO** (not connected) 	| When shorted, it connects RTC clock output to IO2. 	|
| **JP3** 	| **NO** (not connected) 	| When shorted, it keeps the microSD card powered at 3.3V at all times. Useful for troubleshooting, but not ideal for low-power applications. 	|
| **JP4** 	| **NO** (not connected) 	| When shorted, it connects SPI Chip Select line to GPIO15. 	|
| **JP5** 	| **NO** (not connected) 	| When shorted, it connect the pin P1_1 to battery voltage measurement circuit. 	|
| **JP6** 	| **NC** (connected) 	| When shorted, it provides a connection (on pin P1_2) to onboard MOSFET that powers the microSD card. 	|

[FLICKITY CAROUSEL PLACEHOLDER - all jumpers highlighted]