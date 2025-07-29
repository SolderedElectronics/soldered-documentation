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
| **JP2**    | **NC** (connected)     | Connects `GPIO15` to the microSD Chip Select (CS) line. Needed for SD card communication.                                                                               |
| **JP3**    | **NC** (connected)     | Connects `GPIO39` to the microSD card power enable line or interrupt (depending on routing). May be used for SD power switching or custom IRQ setups.                  |
| **JP4**    | **NO** (not connected) | Connects `GPIO0` to a solderable pad. It is used to manually pull `GPIO0` low, which is often required to enter firmware flashing mode (ESP32 bootloader).          |
| **JP5**    | **NC** (connected)     | Connects `GPIO0` through a capacitor to GND. It provides filtering or a soft pull-down to help stabilize boot mode logic and is typically left connected.             |
| **JP6**    | **NC** (connected)     | Connects `GPIO34` to the interrupt output of the touch controller (`INT B`), which is required for interrupt-driven touch detection.                                  |
| **JP7**    | **NC** (connected)     | Connects the SD card power enable signal to the power MOSFET; if left open, the SD card will not be powered by software control.                                        |
| **JP8**    | **NC** (connected)     | Connects VBAT (battery voltage) to the frontlight MOSFET, controlling whether the frontlight is powered via battery input.                                              |