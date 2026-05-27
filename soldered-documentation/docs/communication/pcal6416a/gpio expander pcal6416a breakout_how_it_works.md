---
slug: /pcal6416a/how-it-works 
title: PCAL6416AHF - How it works
sidebar_label: How it works
id: gpio expander pcal6416a breakout-how-it-works 
hide_title: false
---  

The **PCAL6416A** is a low-voltage translating 16-bit I²C-bus/SMBus I/O expander that provides flexible GPIO expansion and voltage-level translation for microcontroller systems in a compact package, manufactured by [**NXP Semiconductors**](https://www.nxp.com/products/PCAL6416A).  

<CenteredImage src="/img/pcal6416a/PCAL6416A_chip.jpg" alt="PCAL6416HF chip on board" caption="PCAL6416HF chip on board" width="500px" />

---

## Datasheet

For an in-depth look at technical specifications, refer to the official PCAL6416A Datasheet:  

<QuickLink  
  title="PCAL6416A Datasheet"  
  description="Detailed technical documentation for the PCAL6416A"  
  url="https://www.nxp.com/docs/en/data-sheet/PCAL6416A.pdf"  
/>  
 
---

## How it works

The **PCAL6416A GPIO Expander Breakout Board** acts like an extension for your microcontroller's GPIO pins. Instead of directly connecting peripherals to the microcontroller, communication is handled through the **I2C interface** using the onboard **PCAL6416A chip**. The chip manages all GPIO operations internally and allows each pin to be individually configured as an input or output. 

Main points:

*   The **I2C-bus interface** uses only the **SDA** and **SCL** lines for communication with the host microcontroller.  
*   It provides **16 programmable GPIO pins** divided into two 8-bit ports (**Port A: A0-A7** and **Port B: B0-B7**).  
*   Built-in **voltage-level translation** allows communication between devices operating at different voltages such as **1.8V, 2.5V, 3.3V, and 5V**.  
*   Each GPIO pin can independently function as either an **input** or an **output** using the configuration registers. 
*   The board includes an **interrupt output (INT)** that alerts the microcontroller whenever an input state changes.  
*   Supports programmable **pull-up/pull-down resistors**, **input latching**, **interrupt masking**, and configurable **push-pull or open-drain outputs**. 
  
<InfoBox>Plus, the PCAL6416A features ESD protection, programmable drive strength, and 25mA output sink capability for directly driving LEDs.</InfoBox>

---

## Enable and Disable

<InfoBox>Device is powered when the VDD(I2C-bus) and VDD(P) pins are connected to valid power sources.</InfoBox>

The PCAL6416A operates whenever stable supply voltages are applied. The chip uses two separate power rails:

*   **VDD(I2C-bus)** powers the I2C communication interface.  
*   **VDD(P)** powers the GPIO port circuitry.  

This dual-supply design enables automatic voltage-level translation between the I2C bus and GPIO pins.

<WarningBox>At power-on, all GPIO pins are automatically configured as **inputs** for safe startup operation. This prevents accidental output signals during initialization. Make sure to configure each pin direction explicitly in your code before use, as relying on the default state without proper initialization may lead to unexpected behavior.</WarningBox>

---

This breakout board is ideal for adding extra GPIO pins to embedded systems, controlling LEDs, reading buttons and sensors, handling interrupts, and interfacing devices operating at different voltage levels.