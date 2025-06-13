---
slug: /inkplate/4tempera/hardware/jumpers
title: Inkplate 4TEMPERA – Jumpers
id: 4tempera-hardware-jumpers
---

Inkplate 4TEMPERA features several **on-board jumpers** that can be used to modify the behavior of certain components. Some jumpers are **connected by default**, while others need to be manually shorted.

See the table below for a detailed explanation of each jumper's function:

---

## Board jumpers

<FlickityCarousel
images={[
  { src: '/img/inkplate_4_tempera/jp1.png', alt: 'Jumper JP1', caption: 'JP1' },
  { src: '/img/inkplate_4_tempera/jp2.png', alt: 'Jumper JP2', caption: 'JP2' },
  { src: '/img/inkplate_4_tempera/jp3.png', alt: 'Jumper JP3', caption: 'JP3' },
  { src: '/img/inkplate_4_tempera/jp4.png', alt: 'Jumper JP4', caption: 'JP4' },
  { src: '/img/inkplate_4_tempera/jp5.png', alt: 'Jumper JP5', caption: 'JP5' },
  { src: '/img/inkplate_4_tempera/jp6.png', alt: 'Jumper JP6', caption: 'JP6' },
]}
/>

| **Jumper** | **Default State**      | **Function**                                                                                                                                                             |
| ---------- | ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **JP1**    | **NO** (not connected) | When shorted, it keeps the microSD card powered at 3.3V at all times. Useful for troubleshooting or logging during deep sleep, though not ideal for low-power use.   |
| **JP2**    | **NC** (connected)     | Connects `GPIO39` to the microSD card power enable line or interrupt (depending on routing). May be used for SD power switching or custom IRQ setups.                  |
| **JP3**    | **NC** (connected)     | Connects `GPIO15` to the microSD Chip Select (CS) line. Needed for SD card communication.                                                                               |
| **JP4**    | **NO** (not connected) | Connects `GPIO0` to a solderable pad. It is used to manually pull `GPIO0` low, which is often required to enter firmware flashing mode (ESP32 bootloader).          |
| **JP5**    | **NC** (connected)     | Connects `GPIO0` through a capacitor to GND. It provides filtering or a soft pull-down to help stabilize boot mode logic and is typically left connected.             |
| **JP6**    | **NC** (connected)     | Connects `GPIO34` to the interrupt output of the touch controller (`INT B`), which is required for interrupt-driven touch detection.                                  |

