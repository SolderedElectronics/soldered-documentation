---
slug: /as5600/how-it-works 
title: AS5600 - How it works
sidebar_label: How it works
id: as5600-how-it-works 
hide_title: False
---  

The AS5600 is a magnetic rotary position sensor from [**AMS OSRAM**](https://ams-osram.com/products/sensor-solutions/position-sensors/ams-as5600-position-sensor) that measures the angular position of a rotating magnet without physical contact.

<CenteredImage src="/img/as5600/as5600_onboard.JPG" alt="AS5600 sensor on board" caption="AS5600 sensor on board" width="500px" />

## Datasheet

For an in-depth look at technical specifications, see the official AS5600 Datasheet:  

<QuickLink  
  title="AS5600 Datasheet"  
  description="Detailed technical documentation for the AS5600 sensor"  
  url="https://look.ams-osram.com/m/7059eac7531a86fd/original/AS5600-DS000365.pdf"  
/>  

---

## How the sensor works

The AS5600 uses a **Hall-effect magnetic sensor**, an internal **ADC**, and **digital signal processing** to detect the orientation of a nearby diametric magnet and convert it to an angle value. It reads the magnet's field and tracks its position through a full **360°** of rotation, and the internal ADC resolves that into up to **4096 positions per revolution** (12-bit resolution) for smooth, precise readings. Since nothing physically touches the magnet, there's no mechanical wear over time. The result is available over **I2C**, as an **analog voltage**, or as **PWM**, whichever output your project needs.

---

## I2C Communication

The AS5600 communicates over I2C with a **fixed address of 0x36**. A host microcontroller can request the current angle, raw angle value, and sensor status over the SDA and SCL lines.

Every I2C transaction follows the same pattern shown below: the host pulls SDA low while SCL is high to signal a **start condition (S)**, then SCL toggles once per bit as the data (the register address you're reading, or the angle value coming back) shifts out one bit at a time over SDA, and the transaction ends with a **stop condition (P)**, SDA going high while SCL is high. The AS5600 Arduino library handles all of this for you, `readAngle()` and `rawAngle()` run this exact exchange internally and just hand you back the final number.

<CenteredImage src="/img/as5600/i2c_data_transfer.svg" alt="I2C SDA and SCL signal timing during a data transfer" caption="SDA and SCL signal timing during an I2C data transfer, the same protocol the AS5600 uses to send its readings" width="600px" />

