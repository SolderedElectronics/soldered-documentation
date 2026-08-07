---
slug: /inkplate/6motion/hardware/jumpers
title: Inkplate 6MOTION - Jumpers
sidebar_label: Jumpers
id: 6motion-hardware-jumpers
---

Inkplate 6MOTION features several **on-board jumpers**, which can be used to modify the behavior of certain components. Some jumpers are **connected by default**, while others need to be manually shorted.

See the table below for a detailed explanation of each jumper's function:  

---

## Inkplate board jumpers

<FlickityCarousel
images={[
  { src: '/img/inkplate_6_motion/JP1.jpg', alt: 'Jumper JP1', caption: 'JP1' },
  { src: '/img/inkplate_6_motion/JP2.jpg', alt: 'Jumper JP2', caption: 'JP2' },
  { src: '/img/inkplate_6_motion/JP3.jpg', alt: 'Jumper JP3', caption: 'JP3' },
  { src: '/img/inkplate_6_motion/JP4.jpg', alt: 'Jumper JP4', caption: 'JP4' },
]}
/>

| Jumper  | Default State | Function |
|---------|--------------|----------|
| **JP1** | **Open** (not connected) | When shorted, it **keeps the microSD card powered at 3.3V** at all times. Useful for troubleshooting, but not ideal for low-power applications. |
| **JP2** | **Connected by default** | Bridges the **WAKE button** with **PC13**, allowing the board to wake from deep sleep via button press. |
| **JP3** | **Connected by default** | Bridges the **USER1 button** with **PG6**, enabling button input functionality. |
| **JP4** | **Connected by default** | Bridges the **USER2 button** with **PA0**, allowing interaction with USER2. |

## STM board jumpers

These two jumpers are on the **STM board**, the daughterboard that carries the STM32H743 and the SDRAM. You'll find both just right of the STM32, inside the `INKPLATE 6 MOTION STM BOARD` silkscreen.

<FlickityCarousel
images={[
  { src: '/img/inkplate_6_motion/stm_JP1.jpg', alt: 'STM board jumper JP1', caption: 'JP1' },
  { src: '/img/inkplate_6_motion/stm_JP2.jpg', alt: 'STM board jumper JP2', caption: 'JP2' },
]}
/>

| Jumper  | Default State | Function |
|---------|--------------|----------|
| **JP1** | **Connected by default** | Connects **3V3A** to **VREF**. If a separate voltage reference for **VREF** is not needed, this jumper keeps it tied to **3V3-A**. It is connected by default to ensure STM32 operates correctly. Advanced users who require a dedicated voltage reference can **cut this jumper** and supply an external voltage to the **VREF** pin on the Inkplate board. |
| **JP2** | **Connected by default** | Connects **GND** to **AGND**. **AGND** is the reference for the STM32's analog section. If higher precision analog measurements are needed, this jumper can be **cut** to separate AGND from GND and apply additional filtering. Users can then supply a reference voltage via the **AREF** pin on the Inkplate board. |