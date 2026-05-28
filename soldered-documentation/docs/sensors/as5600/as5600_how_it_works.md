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

For an in-depth look at technical specifications, refer to the official AS5600 Datasheet:  

<QuickLink  
  title="AS5600 Datasheet"  
  description="Detailed technical documentation for the AS5600 sensor"  
  url="https://look.ams-osram.com/m/7059eac7531a86fd/original/AS5600-DS000365.pdf"  
/>  

---

## How the sensor works

The AS5600 uses a **Hall-effect magnetic sensor**, an internal **ADC**, and **digital signal processing** to detect the orientation of a nearby diametric magnet and convert it to an angle value.

- **Magnetic angle sensing** - The sensor reads the magnetic field of a diametrically magnetised magnet placed above it and outputs its angular position with **360° tracking**.

- **12-bit resolution** - The internal ADC provides up to **4096 positions per revolution**, giving smooth and precise readings.

- **Contactless operation** - No physical contact means no mechanical wear over time.

- **Multiple output options** - Angle data is available via **I2C**, **analog voltage output**, or **PWM**, depending on what your application needs.

---

## I2C Communication

The AS5600 communicates over I2C with a **fixed address of 0x36**. A host microcontroller can request the current angle, raw angle value, and sensor status over the SDA and SCL lines.


