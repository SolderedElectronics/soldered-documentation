---
slug: /inkplate/6/hardware/jumpers
title: Inkplate 6 – Jumpers
sidebar_label: Jumpers
id: hardware-jumpers
---

Inkplate 6 features several **on-board jumpers**, which can be used to modify the behavior of certain components. Some jumpers are **connected by default**, while others need to be manually shorted.

See the table below for a detailed explanation of each jumper's function:

---

## Board jumpers

| **Jumper** | **Default State** | **Function** |
|---|---|---|
| **JP1** 	| **NO** (not connected) 	| When shorted, it keeps the microSD card powered at 3.3v at all times. Useful for troubleshooting, but not ideal for low-power applications. |
| **JP2** |  **Connected to IO34 by default** | Switch between connecting the INTB pin of the IO expander to the IO34 pin of the ESP32 or make that pin user-accessible. |
| **JP3** |  **NC** (connected) 	| Connects pin P1-2 of IO expander 1 to the gate of the MOSFET that powers the microSD card, letting the library switch the card on and off. |
| **JP4** |  **NC** (connected) 	| Connects the Chip Select pin of the microSD card slot to IO15 of the ESP32. Cut it to drive the card's CS from the GPIO15 breakout pad instead. 	|
| **JP5** | **Connected to INT by default** 	| Selects what the RTC drives on IO39: a digital, open-drain, active low interrupt output, or a programmable digital square-wave output that can be used as a system clock. 	|
| **JP6** | **NC** (connected) 	| Connects pin P1-1 of IO expander 1 to the MOSFET that enables the battery voltage divider, so battery voltage is only measured when requested. |

<FlickityCarousel
images={[
  {src:'/img/6/JP1.webp', alt: 'Jumper JP1', caption:'JP1'},
  {src:'/img/6/JP2.webp', alt: 'Jumper JP2', caption:'JP2'},
  {src:'/img/6/JP3.webp', alt: 'Jumper JP3', caption:'JP3'},
  {src:'/img/6/JP4.webp', alt: 'Jumper JP4', caption:'JP4'},
  {src:'/img/6/JP5.webp', alt: 'Jumper JP5', caption:'JP5'},
  {src:'/img/6/JP6.webp', alt: 'Jumper JP6', caption:'JP6'},
]}
/>