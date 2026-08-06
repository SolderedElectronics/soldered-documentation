---
slug: /inkplate/6flick/hardware/jumpers
title: Inkplate 6FLICK – Jumpers
sidebar_label: Jumpers
id: 6flick-hardware-jumpers
---

Inkplate 6FLICK features several **on-board jumpers** that can be used to modify the behavior of certain components. Some jumpers are **connected by default**, while others need to be manually shorted.

See the table below for a detailed explanation of each jumper's function:

---

## Board jumpers

<FlickityCarousel
images={[
  { src: '/img/inkplate_6_flick/jp1.png', alt: 'Jumper JP1', caption: 'JP1' },
  { src: '/img/inkplate_6_flick/jp2.png', alt: 'Jumper JP2', caption: 'JP2' },
  { src: '/img/inkplate_6_flick/jp3.png', alt: 'Jumper JP3', caption: 'JP3' },
  { src: '/img/inkplate_6_flick/jp4.png', alt: 'Jumper JP4', caption: 'JP4' },
  { src: '/img/inkplate_6_flick/jp5.png', alt: 'Jumper JP5', caption: 'JP5' },
  { src: '/img/inkplate_6_flick/jp6.png', alt: 'Jumper JP6', caption: 'JP6' },
  { src: '/img/inkplate_6_flick/jp7.png', alt: 'Jumper JP7', caption: 'JP7' },
  { src: '/img/inkplate_6_flick/jp8.png', alt: 'Jumper JP8', caption: 'JP8' },
]}
/>

| **Jumper** | **Default State**      | **Function**                                                                                                                                                             |
| ---------- | ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **JP1**    | **NO** (not connected) | When shorted, it keeps the microSD card powered at 3.3V at all times. Useful for troubleshooting or logging during deep sleep, though not ideal for low-power use.   |
| **JP2**    | **NC** (connected)     | Connects the microSD Chip Select line to `IO15` (`SPI_CS`) on the ESP32. Cut it to drive the card's CS from the `GPIO15` breakout pad instead.                       |
| **JP3**    | **NC** (connected)     | Selects what the RTC drives on `IO39`: its interrupt output, or the `CLKOUT` square-wave output. Nothing to do with the microSD card.                                |
| **JP4**    | **NO** (not connected) | Shorts out `R58`, the 47 Ω series resistor on the `GPIO0` to `EPD_CL` clock line. Only for signal-integrity experiments on the e-paper clock.                        |
| **JP5**    | **NC** (connected)     | Connects `C61`, a 100 pF filter capacitor, to that same `EPD_CL` clock line. Leave it connected unless you are deliberately tuning the clock edge.                   |
| **JP6**    | **NC** (connected)     | Connects `IO34` to `INTB`, the interrupt output of **IO expander 1**. Cut it to free `IO34` for your own use.                                                        |
| **JP7**    | **NC** (connected)     | Connects `SD_ENABLE` to pin P1-5 of IO expander 1, letting the library switch microSD card power on and off.                                                          |
| **JP8**    | **NC** (connected)     | Connects `V_BAT_MOS` to pin P1-1 of IO expander 1. This enables the battery voltage divider, so battery voltage is only measured when requested.                      |