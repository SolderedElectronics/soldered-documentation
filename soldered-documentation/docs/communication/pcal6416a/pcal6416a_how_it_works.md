---
slug: /pcal6416a/how-it-works 
title: PCAL6416A - How it works
sidebar_label: How it works
id: pcal6416a-how-it-works 
hide_title: false
---  

The **PCAL6416A** is a 16-bit I²C GPIO expander from [**NXP Semiconductors**](https://www.nxp.com/products/PCAL6416A). It adds 16 programmable I/O pins over I²C and handles voltage-level translation between different logic levels.

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

