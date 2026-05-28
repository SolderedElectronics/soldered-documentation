---
slug: /i2c-bus-extender-p82b715/how-it-works
title: How it works
sidebar_label: How it works
id: i2c bus extender p82b715-how-it-works
hide_title: false
---

The **P82B715 I2C Bus Extender** breakout board extends the range of standard I²C communication far beyond its usual limits. At its core is the **P82B715** chip by [**NXP/Texas Instruments**](https://www.ti.com/product/P82B715) — a bidirectional I²C bus buffer that provides **10× impedance transformation**, dramatically reducing the effective capacitance seen on each side of the bus and allowing I²C signals to travel over cable runs of up to **30 metres**.

---

## Datasheet

For an in-depth look at technical specifications, refer to the official P82B715 datasheet:

<QuickLink 
  title="P82B715 Datasheet (TI)" 
  description="Detailed technical documentation for the P82B715 I²C bus extender chip." 
  url="https://www.ti.com/lit/ds/symlink/p82b715.pdf" 
/>

---

## I²C Bus Limitations

Standard I²C has a maximum bus capacitance of **400 pF**, which limits usable cable length to only a few metres. As capacitance increases, signal rise times slow down and communication becomes unreliable or fails entirely.

The P82B715 solves this by **isolating the local side from the extended side**. Each side is driven independently, so the capacitive load of the long cable does not affect the microcontroller's I²C bus.

---

## Bidirectional Buffering

The P82B715 operates as a transparent, bidirectional buffer:

- **Local side (Sx/Sy):** Standard 3.3V I²C — supports up to **400 pF** bus capacitance
- **Extended side (Lx/Ly):** Buffered 5V I²C — supports up to **3000 pF** bus capacitance, enabling cable runs of up to **30 m**

The chip is completely invisible to the I²C protocol. It adds no address, register, or configuration layer — the microcontroller communicates directly with remote devices using their original I²C addresses.

Both **Standard-mode (100 kHz)** and **Fast-mode (400 kHz)** are supported.

---

## Onboard Signal Chain

This breakout board adds two supporting components around the P82B715:

1. **Boost converter (TPS613222A):** Steps up the 3.3V Qwiic supply to **5V**, powering the P82B715 chip and the extended bus pull-up resistors.
2. **Level shifter (dual NMOS):** Bridges the 3.3V local side and the 5V extended side transparently, ensuring correct logic levels in both directions.

Your microcontroller always sees **3.3V I²C** on the Qwiic side. The voltage conversion to 5V for the cable side happens automatically — no configuration needed.

---

## Pull-up Resistors

I²C requires pull-up resistors on both SDA and SCL. This board includes onboard pull-ups on both sides, all active by default:

- **JP1 (NC):** Pull-up resistors on the 5V extended side
- **JP2 (NC):** Pull-up resistors on the 3.3V local side
- **JP3 (NC):** SDA pull-up connection on the local side
- **JP4 (NC):** SCL pull-up connection on the local side

If your I²C bus or remote device already has external pull-up resistors, cut the relevant jumpers to avoid driving conflicts caused by parallel pull-ups.
