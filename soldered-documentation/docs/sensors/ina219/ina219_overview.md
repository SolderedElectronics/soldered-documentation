---
slug: /ina219/overview
title: INA219 - Overview
sidebar_label: Overview
id: ina219-overview 
hide_title: False
pagination_prev: null
---

## INA219 Voltage & current sensor

The **INA219** is a digital device that allows the measurement of **current**, **voltage**, and therefore **power**. Simply connect a **Qwiic connector** to this device, and it will provide all the information via **I2C communication** at an address of **0x40**. It is very simple and reliable to use. It has a jumper for changing the I2C address, allowing you to connect more than one INA219 to a single microcontroller.

The maximum measurement current is determined by the shunt resistor on the board, which is 0.1 ohm (± 3.2A). It can **measure power in both directions**! If you want to measure higher currents or smaller currents more precisely, consult the datasheet to select a different resistor. The maximum voltage that can be measured is **26V**.

<CenteredImage src="/img/ina219/333066.jpg" alt="INA219 Voltage & current sensor" caption="INA219 Voltage & current sensor" />

---

## Which product is this documentation for?

<QuickLink 
  title="INA219 Voltage & current sensor" 
  description="333066"
  url="https://soldered.com/product/voltage-current-sensor-ina219-breakout/"
  image="/img/ina219/333066.jpg" 
/>

---

## Key Features

- **Power supply voltage:** 3V-5V  
- **Maximum measuring voltage:** 26V
- **Maximum measuring current:** 3.2A  
- **ADC:** 12-bit
- **Communication:** I2C (address: 0x40, can be changed via jumpers)  
- **Connector:** 2 × **Qwiic (formerly easyC) ports** (plug-and-play, no soldering needed)  
- **Mounting:** **Two mounting holes** for secure attachment  
- **Dimensions:** **38 × 22 mm** (1.5 × 0.9 inch)  

---

## You may also need

<QuickLink 
  title="Qwiic cable" 
  description="Qwiic (formerly easyC) compatible cables with connectors on both ends, available in various lengths."
  url="https://soldered.com/product/easyc-cable/"
  image="/img/333311.webp" 
/>