---
slug: /pcal6416a/overview
title: PCAL6416A - Overview
sidebar_label: Overview
id: pcal6416a-overview 
hide_title: false
pagination_prev: null
---

## PCAL6416A I/O Expander

The **PCAL6416A** is a **16-bit I²C GPIO expander** from **NXP Semiconductors**. It adds 16 programmable input/output pins to a microcontroller over two I²C wires, with built-in **interrupt support**, **programmable pull-up/pull-down resistors**, **input latching**, and **voltage-level translation** between different logic levels. The board is **Qwiic compatible**, so it plugs straight into any Qwiic-enabled microcontroller without soldering, or you can wire it up over standard I2C pins instead.

<CenteredImage src="/img/pcal6416a/PCAL6416A_base.jpg" alt="PCAL6416A I/O Expander" caption="PCAL6416A I/O Expander" width="600px"/>

---

## Which product is this documentation for?

<WarningBox>The webstore link for this product is not available yet! We're working on it. In the meantime, please [**contact us**](https://soldered.com/contact/) for more information.</WarningBox>

---

## Key Features

- **16 GPIO Pins**: Provides 16 programmable input/output pins divided into two 8-bit ports.
- **I²C Communication**: Supports **Standard-mode (100 kHz)** and **Fast-mode (400 kHz)**, default address **0x20**.
- **3.3V or 5V Operation**: Runs the PCAL6416A at 3.3V by default through an onboard regulator, or at 5V instead if you bypass the regulator with a jumper.
- **Voltage-Level Translation**: Allows communication between devices operating at different logic voltages.
- **Interrupt Output (INT)**: Open-drain interrupt pin notifies the microcontroller when an input changes state.
- **Configurable Pull-Up/Pull-Down Resistors**: Can be enabled individually for each pin.
- **Low Power Consumption**: Standby current as low as **0.5 µA** typical (rising to **1.5 µA** typical at higher supply voltages); enabling internal pull-ups on every pin raises this to about **1.1 mA** typical.
- **LED Driving Capability**: Each output pin can sink up to **25 mA**, enough to drive LEDs directly.

---

## You may also need

<QuickLink 
  title="Qwiic cable" 
  description="Qwiic (formerly easyC) compatible cables with connectors on both ends, available in various lengths."
  url="https://soldered.com/product/easyc-cable/"
  image="/img/333311.webp" 
  />