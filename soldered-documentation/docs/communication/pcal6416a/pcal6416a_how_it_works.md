---
slug: /pcal6416a/how-it-works 
title: PCAL6416A - How it works
sidebar_label: How it works
id: pcal6416a-how-it-works 
hide_title: false
---  

The **PCAL6416A** is a 16-bit I²C GPIO expander from [**NXP Semiconductors**](https://www.nxp.com/products/PCAL6416A). It adds 16 programmable I/O pins over I²C, and the chip itself is capable of voltage-level translation between the I²C bus and the GPIO ports (see [below](#power-supply-and-default-pin-state) for how this specific board uses that feature).

<CenteredImage src="/img/pcal6416a/PCAL6416A_chip.jpg" alt="PCAL6416A chip on board" caption="PCAL6416A chip on board" width="500px" />

---

## Datasheet

For an in-depth look at technical specifications, see the official PCAL6416A Datasheet:  

<QuickLink  
  title="PCAL6416A Datasheet"  
  description="Detailed technical documentation for the PCAL6416A"  
  url="https://www.nxp.com/docs/en/data-sheet/PCAL6416A.pdf"  
/>  
 
---

## GPIO expansion over I2C

The **PCAL6416A GPIO Expander Breakout Board** acts like an extension for your microcontroller's GPIO pins. Instead of directly connecting peripherals to the microcontroller, the **I2C interface** handles communication through the onboard **PCAL6416A chip**. The chip manages all GPIO operations internally and allows each pin to be individually configured as an input or output.

- The **I2C-bus interface** uses only the **SDA** and **SCL** lines for communication with the host microcontroller.

<div align="center">
  <a title="Public domain, via Wikimedia Commons" href="https://commons.wikimedia.org/wiki/File:Iicrp.png">
    <img width="400" alt="I2C bus with pull-up resistors and multiple devices sharing SDA and SCL" src="https://upload.wikimedia.org/wikipedia/commons/2/27/Iicrp.png"/>
  </a>
</div>

Every device on the bus, including the PCAL6416A, connects to the same two shared lines: **SDA** and **SCL**. Each line needs one pull-up resistor (**Rp**) for the whole bus, not one per device, since I2C outputs only pull the line low and rely on the resistor to bring it back high. Devices 1 and 2 in the diagram represent any number of I2C peripherals sharing the bus alongside the expander, each identified by its own I2C address.

- It provides **16 programmable GPIO pins** divided into two 8-bit ports (**Port A: A0-A7** and **Port B: B0-B7**).
- Built-in **voltage-level translation** allows communication between devices operating at different voltages such as **1.8V, 2.5V, 3.3V, and 5V**.
- Each GPIO pin can independently function as either an **input** or an **output** using the configuration registers.
- The board includes an **interrupt output (INT)** that alerts the microcontroller whenever an input state changes.
- Supports programmable **pull-up/pull-down resistors**, **input latching**, **interrupt masking**, and configurable **push-pull or open-drain outputs**.
  
<InfoBox>The PCAL6416A also has ESD protection, programmable drive strength, and 25mA output sink capability for directly driving LEDs.</InfoBox>

---

## Power supply and default pin state

<InfoBox>On this board, VDD(I2C-bus) and VDD(P) are tied together onto a single supply rail, so the chip always runs both sides at the same voltage.</InfoBox>

In NXP's datasheet, the PCAL6416A has two separate power pins, **VDD(I2C-bus)** for the I2C interface and **VDD(P)** for the GPIO ports, that can be wired to different voltages so the chip translates levels between the bus and the ports on its own. This board doesn't use that option: both pins are wired to the same onboard supply, regulated to 3.3V by default (5V if jumper **JP5** bypasses the regulator).

3.3V/5V I2C compatibility is instead handled by a separate level-shifter IC between the chip's native 3.3V bus and the 5V-side pins broken out on the board. The Qwiic connectors carry the native 3.3V bus directly; the standalone SCL/SDA/VCC/GND header carries the level-shifted 5V side.

<WarningBox>At power-on, all GPIO pins are automatically configured as **inputs** for safe startup operation. This prevents accidental output signals during initialization. Make sure to configure each pin direction explicitly in your code before use, as relying on the default state without proper initialization may lead to unexpected behavior.</WarningBox>

---

