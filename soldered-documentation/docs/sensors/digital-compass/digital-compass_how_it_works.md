---
slug: /digital-compass/how-it-works 
title: Digital Compass - How it works
sidebar_label: How it works
id: digital-compass-how-it-works 
hide_title: False
---  

The **Digital Compass AK09918C 3-Axis Magnetometer breakout** is an integrated circuit by **Asahi Kasei Microdevices (AKM)**. It is a highly sensitive **3-axis electronic compass IC** that uses advanced **Hall sensor technology** to detect the Earth’s magnetic field along the **X, Y, and Z axes**.

This allows the sensor to precisely determine **heading, orientation, and direction**, making it ideal for digital compasses, robotics, drones, and navigation systems.

<CenteredImage  src="/img/digital-compass/AK09918C_highlighted.JPG" alt="Digital Compass" width="1200px" />

---

## Datasheet

For an in-depth look at technical specifications, refer to the official **AK09918 Electronic Compass** datasheet:

<QuickLink  
  title="AK09918 Electronic Compass Datasheet"  
  description="Detailed technical documentation for the AK09918 Electronic Compass"  
  url="https://www.akm.com/content/dam/documents/products/electronic-compass/ak09918c/ak09918c-en-datasheet.pdf"  
/> 

---

## How the magnetometer works

The **AK09918C** works by measuring the **magnetic flux density** around it using highly sensitive **3-axis Hall effect sensors**.

Inside the IC, there are **three independent Hall sensor elements**, each aligned to one spatial axis:

- **X-axis**
- **Y-axis**
- **Z-axis**

These sensors detect the strength and direction of the surrounding magnetic field, including the **Earth’s magnetic field**, and convert it into **electrical signals**.

The internal signal chain then performs:

- **signal amplification**
- **noise filtering**
- **analog-to-digital conversion (ADC)**
- **digital output formatting**

This results in **16-bit digital magnetic field data** for each axis.

The sensitivity is: **0.15 µT per LSB** which allows for very accurate direction and heading calculations.

---

## Hall sensor principle

The sensor operates using the **Hall effect principle**.

When a magnetic field passes through the Hall sensing element, it creates a small voltage difference proportional to the magnetic field strength.

This voltage is then amplified and converted into readable digital values.

This means:

- stronger magnetic field → larger output value
- weaker magnetic field → smaller output value

By comparing the X, Y, and Z axis values, the microcontroller can calculate:

- **compass heading**
- **tilt-compensated direction**
- **magnetic field intensity**
- **orientation in space**

---

## I2C communication

The **AK09918C** communicates with the microcontroller using the **I2C protocol**.

It supports:

- **Standard mode:** 100 kHz
- **Fast mode:** 400 kHz

The board uses a **fixed I2C address**: **0x0C**.This makes communication simple and ideal for plug-and-play usage with **Qwiic / easyC systems**.

