---
slug: /pcal6416a/overview
title: PCAL6416AHF - Overview
sidebar_label: Overview
id: gpio expander pcal6416a breakout-overview 
hide_title: false
pagination_prev: null
---

## PCAL6416A I/O Expander

The **PCAL6416A** is a powerful and flexible **16-bit I²C-bus/SMBus GPIO expander** designed for adding extra digital input/output pins to microcontrollers and embedded systems. Developed by **NXP Semiconductors**, this device provides reliable GPIO expansion with advanced features such as **interrupt support**, **programmable pull-up/pull-down resistors**, **input latching**, and **voltage-level translation** between different logic levels. 

The PCAL6416A communicates over the **I²C interface** and is ideal for applications requiring additional GPIOs, LED control, button monitoring, sensors, and other peripheral interfacing while minimizing the number of microcontroller pins used.

<CenteredImage src="/img/pcal6416a/PCAL6416A_base.jpg" alt="PCAL6416AHF I/O Expander" caption="PCAL6416AHF I/O Expander" width="600px"/>
---

## Which product is this documentation for?

<WarningBox>The webstore link for this product is not available yet! We're working on it. In the meantime, please [**contact us**](https://soldered.com/contact/) for more information.</WarningBox>

---

## Key Features

* **16 GPIO Pins**: Provides 16 programmable input/output pins divided into two 8-bit ports. 
* **I²C Communication**: Uses a standard **I²C-bus/SMBus interface** with support for **Fast-mode Plus** up to **1 MHz**. 
* **Default I²C Address**: Base address is **0x20**, configurable to **0x21** by cutting jumper **JP3** and bridging it to VDD.
* **Wide Operating Voltage Range**: Operates from **1.65V to 5.5V**, compatible with both low-voltage and 5V systems. 
* **Voltage-Level Translation**: Allows communication between devices operating at different logic voltages. 
* **Interrupt Output (INT)**: Open-drain interrupt pin notifies the microcontroller when an input changes state. 
* **Configurable Pull-Up/Pull-Down Resistors**: Internal 100 kΩ pull-up or pull-down resistors can be enabled individually for each pin. 
* **Low Power Consumption**: Typical standby current as low as **1 µA to 1.5 µA**. 
* **LED Driving Capability**: Each output pin can sink up to **25 mA**, making it suitable for directly driving LEDs.

---

## You may also need

<QuickLink 
  title="Qwiic cable" 
  description="Qwiic compatible cables with connectors on both ends, available in various lengths."
  url="https://soldered.com/product/easyc-cable/"
  image="/img/333311.webp" 
  />