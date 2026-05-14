---
slug: /as5600/how-it-works 
title: As5600 - How it works
sidebar_label: How it works
id: as5600-how-it-works 
hide_title: False
---  

The AS5600 is a magnetic rotary position sensor that provides high-resolution angle measurement and contactless rotational sensing in a compact package, manufactured by [**AMS OSRAM**](https://ams-osram.com/products/sensor-solutions/position-sensors/ams-as5600-position-sensor).

<CenteredImage src="/img/as5600/as5600_onboard.JPG" alt="AS-5600 sensor on board" caption="AS-5600 sensor on board" width="500px" />

## Datasheet

For an in-depth look at technical specifications, refer to the official APDS-9960 Datasheet:  

<QuickLink  
  title="AS-5600 Datasheet"  
  description="Detailed technical documentation for the AS-5600 sensor"  
  url="https://look.ams-osram.com/m/7059eac7531a86fd/original/AS5600-DS000365.pdf"  
/>  

---

## How the sensor works

The AS5600 is a magnetic rotary position sensor designed for **accurate contactless angle measurement**. It integrates a **Hall-effect magnetic sensor, analog-to-digital converter (ADC), and digital signal processing** into a compact module, enabling precise rotational position tracking in various applications.

The AS5600 operates with **low power consumption** and **high measurement accuracy**, making it ideal for **motor control, robotics, rotary knobs, and position sensing systems**.

- **Magnetic Angle Sensing** - The sensor detects the magnetic field orientation of a nearby diametric magnet and converts it into precise angular position data with **360° rotational tracking**.

- **High-Resolution Measurement** - The integrated **12-bit ADC** provides up to **4096 positions per revolution**, enabling smooth and accurate angle measurements.

- **Contactless Operation** - Using Hall-effect sensing technology, the AS5600 measures rotation without physical contact, reducing **mechanical wear** and improving long-term reliability.

- **Signal Processing and Output** - The sensor processes position data internally and provides output through **I2C, analog voltage, or PWM interfaces**, allowing **easy integration with microcontrollers and embedded systems**.
---

## I2C Communication

The AS5600 sensor uses **I2C** (Inter-Integrated Circuit) communication to exchange data with a microcontroller. I2C uses two lines: **SDA** for **data transfer** and **SCL** for **clock synchronization**.

As a follower device (a device that accepts or provides a digital message carrying measurement or other data, but only when specifically requested), the AS5600 has a fixed I2C address that allows a master device to read precise **rotational position and angle measurements**.

The sensor continuously monitors the orientation of a nearby magnet and converts it into digital position data, enabling applications such as **motor control, rotary encoders, robotics**, and **position tracking systems**.