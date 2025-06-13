---
slug: /inkplate/10/hardware/jumpers
title: Inkplate 10 – Jumpers
id: 10-hardware-jumpers
---

Inkplate 10 features several **on-board jumpers**, which can be used to modify the behavior of certain components. Some jumpers are **connected by default**, while others need to be manually shorted.

See the table below for a detailed explanation of each jumper's function:

---

## Board jumpers

| **Jumper** 	| **Default State** 	| **Function** 	|
|---	|---	|---	|
| **JP1** 	| **NO**(not connected) 	| When shorted, it keeps the microSD card powered at 3.3v at all times. Useful for troubleshooting, but not ideal for low-power applications. 	|
| **JP2** 	| **Connected to INT by default** 	| Switch between a digital, open-drain, active low interrupt output and a programmable digital quare-wavee output that can be used as a system clock. 	|
| **JP3** 	| **NC** (connected) 	| When shorted, enables Chip Select function for communication with microSD card. 	|
| **JP4** 	| **NC** (connected) 	| When shorted, it enables interupt pin on PCAL6416A	|
| **JP5** 	| **NC** (connected) 	| When shorted, it provides a connection to onboard MOSFET that powers the microSD card. 
| **JP6** 	| **NC** (connected) 	| When shorted, it connects the battery terminal to MCP73831 	|
<FlickityCarousel
images={[
{src:'/img/inkplate10/jp1.webp', alt: 'Jumper JP1', caption:'JP1'},
{src:'/img/inkplate10/jp2.webp', alt: 'Jumper JP2', caption:'JP2'},
{src:'/img/inkplate10/jp3.webp', alt: 'Jumper JP3', caption:'JP3'},
{src:'/img/inkplate10/jp4.webp', alt: 'Jumper JP4', caption:'JP4'},
{src:'/img/inkplate10/jp5.webp', alt: 'Jumper JP5', caption:'JP5'},
{src:'/img/inkplate10/jp6.webp', alt: 'Jumper JP6', caption:'JP6'},
]}
/>