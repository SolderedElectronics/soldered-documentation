---
slug: /inkplate/5v2/hardware/jumpers
title: Inkplate 5V2 – Jumpers
sidebar_label: Jumpers
id: hardware-jumpers
---

Inkplate 5V2 has several on-board jumpers that change how certain components behave. Some are connected by default, others you need to short yourself.

The table below explains what each jumper does:

---

## Board jumpers

| **Jumper** | **Default State** | **Function** |
|---|---|---|
| **JP1** 	| NO (not connected) 	| When shorted, keeps the microSD card powered at 3.3v at all times. Useful for troubleshooting, but not ideal for low-power applications. |
| **JP2** | Connected to INT by default | Switch between a digital, open-drain, active low interrupt output and a programmable digital square-wave output that can be used as a system clock. |
| **JP3** | Connected to SPI_CS(IO15) by default | Switch between connecting the CS pin of the microSD card reader to the IO15 pin or the SD0 pin on the ESP32. |
| **JP4** | NO (not connected) | When shorted, bypasses the 330-ohm resistor connected to the buffer, causing the ESP32 to enter bootloader mode. |
| **JP5** | NC (connected) | When shorted, connects the GPIO0 pin to a 100pF capacitor, which gives more stable voltages. |
| **JP6** | Connected to IO34 by default | Switch the INTB pin of the IO expander between the IO34 pin of the ESP32 and a separate solder pad next to the jumper. |
| **JP7** | NC (connected) | Connects pin P1-2 of the IO expander to the MOSFET that powers the microSD card. Cut it and the card stays unpowered, but P1-2 is freed up on the neighbouring solder pad. |
| **JP8** | NC (connected) 	| Connects pin P1-1 of the IO expander to the MOSFET that switches the battery voltage divider on for a measurement. Cut it and `readBattery()` stops working, but P1-1 is freed up on the neighbouring solder pad. |

<FlickityCarousel
images={[
  {src:'/img/5v2/JP1.webp', alt: 'Jumper JP1', caption:'JP1'},
  {src:'/img/5v2/JP2.webp', alt: 'Jumper JP2', caption:'JP2'},
  {src:'/img/5v2/JP3.webp', alt: 'Jumper JP3', caption:'JP3'},
  {src:'/img/5v2/JP4.webp', alt: 'Jumper JP4', caption:'JP4'},
  {src:'/img/5v2/JP5.webp', alt: 'Jumper JP5', caption:'JP5'},
  {src:'/img/5v2/JP6.webp', alt: 'Jumper JP6', caption:'JP6'},
  {src:'/img/5v2/JP7.webp', alt: 'Jumper JP7', caption:'JP7'},
  {src:'/img/5v2/JP8.webp', alt: 'Jumper JP8', caption:'JP8'},
]}
/>