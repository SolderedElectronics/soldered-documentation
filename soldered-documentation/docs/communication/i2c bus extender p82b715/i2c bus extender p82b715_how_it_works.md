---
slug: /i2c-bus-extender-p82b715/how-it-works
title: How it works
sidebar_label: How it works
id: i2c bus extender p82b715-how-it-works
hide_title: false
---

The **P82B715 I2C Bus Extender** breakout board extends the range of standard I²C communication far beyond its usual limits. At its core is the **P82B715** chip by [**NXP/Texas Instruments**](https://www.ti.com/product/P82B715), a bidirectional I²C bus buffer that gives **10× impedance transformation**. That dramatically reduces the effective capacitance seen on each side of the bus, letting I²C signals travel over cable runs of up to **50 metres**.

<WarningBox>Chip photo not yet available. We're working on it!</WarningBox>

---

## Datasheet

For an in-depth look at technical specifications, refer to the official P82B715 datasheet:

<QuickLink 
  title="P82B715 Datasheet (TI)" 
  description="Detailed technical documentation for the P82B715 I²C bus extender chip." 
  url="https://www.ti.com/lit/ds/symlink/p82b715.pdf" 
/>

---

## I²C bus limitations

Standard I²C has a maximum bus capacitance of **400 pF**, which limits usable cable length to only a few metres. As capacitance increases, signal rise times slow down and communication becomes unreliable or fails entirely.

The P82B715 solves this by **isolating the local side from the extended side**. Each side is driven independently, so the capacitive load of the long cable does not affect the microcontroller's I²C bus.

---

## Bidirectional buffering

The P82B715 operates as a transparent, bidirectional buffer:

- **Local side (Sx/Sy):** Connects to the Qwiic ports (K1/K2) through an onboard level shifter, and directly to header K3. Supports up to **400 pF** bus capacitance. Its logic level is **jumper-selectable** (see below): 3.3V or 5V.
- **Extended side (Lx/Ly):** Connects to the screw terminal (K4) for the long cable run. Fixed at **5V**, supports up to **3000 pF** bus capacitance and cable runs of up to **50 m**.

Both sides are driven by the same VCC (5V), but the P82B715's current-mode signaling lets each side sit at a different logic level at the same time. That's what makes the jumper-selectable local side possible without any extra circuitry.

The chip is completely invisible to the I²C protocol. It adds no address, register, or configuration layer, so the microcontroller communicates directly with remote devices using their original I²C addresses.

Both **Standard-mode (100 kHz)** and **Fast-mode (400 kHz)** are supported.

---

## Onboard signal chain

This breakout board adds supporting components around the P82B715:

1. **Boost converter (TPS613222A):** Steps up the 3.3V Qwiic supply to **5V**, powering the P82B715 chip and the fixed 5V pull-ups on the extended side.
2. **Level shifter (dual NMOS):** Sits between the Qwiic connectors (always 3.3V) and the local side (Sx/Sy). If JP1/JP2 select 5V for the local side, this shifter does real level conversion; if they select 3.3V, both sides already match and the shifter just passes the signal through.

Your microcontroller always sees **3.3V I²C** on the Qwiic side, regardless of how the local side is jumpered. The extended side (screw terminal) is always 5V.

---

## Pull-up resistors

I²C's SDA and SCL lines are open-drain: a device can only pull a line low, never drive it high. Pull-up resistors are what bring the line back to a logic high when nothing's pulling it down, as shown below for a typical controller/peripheral pair.

<CenteredImage src="/img/i2c bus extender p82b715/i2c-pullup-schematic.jpg" alt="I2C bus schematic showing pull-up resistors on SDA and SCL" caption="Both I2C lines need a pull-up resistor to the supply voltage" width="500px" attribution_name="SparkFun Learn" attribution_link="https://learn.sparkfun.com/tutorials/i2c/i2c-at-the-hardware-level" />

The resistor value matters: too high and rise times get too slow for reliable communication as bus capacitance increases (exactly the problem the P82B715 is built to work around), too low and it wastes power and can't be pulled fully low by the sinking device. This board provides pull-ups differently on each side:

- **Extended side (Lx/Ly, screw terminal K4):** Fixed 5V pull-ups, always active. There's no jumper for these.
- **Local side (Sx/Sy, header K3 and Qwiic ports):** Selectable pull-ups, set independently per line:
  - **JP1** selects the SDA pull-up source: 5V or 3.3V.
  - **JP2** selects the SCL pull-up source: 5V or 3.3V.

Normally, set JP1 and JP2 to the same voltage so SDA and SCL match. If your I²C bus or remote device already has external pull-up resistors, remove the jumper to avoid driving conflicts caused by parallel pull-ups.
