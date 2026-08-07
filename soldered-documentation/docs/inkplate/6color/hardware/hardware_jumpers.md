---
slug: /inkplate/6color/hardware/jumpers
title: Inkplate 6COLOR – Jumpers
sidebar_label: Jumpers
id: hardware-jumpers
---

Inkplate 6COLOR features several **on-board jumpers**, which can be used to modify the behavior of certain components. Some jumpers are **connected by default**, while others need to be manually shorted.

See the table below for a detailed explanation of each jumper's function:

---

## Board jumpers

| **Jumper** | **Default State** | **Function** |
|---|---|---|
| **JP1** | **Connected to IO34 by default** | Switch between connecting the Interrupt pin of the IO expander to the IO34 pin on the ESP32 or the K1 output header on the board |
| **JP2** | **Connected to P1_2 by default** | Switch between connecting the SD_ENABLE pin of the microSD card reader to pin 12 on the IO expander or the K20 output header on the board |
| **JP3** | **Connected to P1_1 by default** | Switch between connecting V_BAT_MOS, which enables the battery voltage divider, to pin 11 on the IO expander or the K26 output header on the board |
| **JP4** | **NO** (not connected) | When shorted, it keeps the microSD card powered at 3.3V at all times. Useful for troubleshooting, but not ideal for low-power applications. |
| **JP5** | **Connected to GPIO39 by default** | Selects what the RTC drives on GPIO39: the interrupt output, or the CLKOUT square-wave output |
| **JP6** | **Connected to SPI_CS(IO15) by default** | Switch between connecting the CS pin of the microSD card reader to IO15 or to the GPIO15 breakout pad |

<FlickityCarousel
images={[
  {src:'/img/6color/JP1.webp', alt: 'Jumper JP1', caption:'JP1'},
  {src:'/img/6color/JP2.webp', alt: 'Jumper JP2', caption:'JP2'},
  {src:'/img/6color/JP3.webp', alt: 'Jumper JP3', caption:'JP3'},
  {src:'/img/6color/JP4.webp', alt: 'Jumper JP4', caption:'JP4'},
  {src:'/img/6color/JP5.webp', alt: 'Jumper JP5', caption:'JP5'},
  {src:'/img/6color/JP6.webp', alt: 'Jumper JP6', caption:'JP6'},
]}
/>