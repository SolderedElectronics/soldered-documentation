---
slug: /apds-9960/how-it-works 
title: How it works
id: apds-9960-how-it-works 
hide_title: False
---  

APDS-9960 is a digital sensor that integrates RGB, ambient light, proximity, and gesture sensing in a single 8-pin package, manufactured by [**Broadcom**](https://www.broadcom.com/products/optical-sensors/integrated-ambient-light-and-proximity-sensors/apds-9960). 

<CenteredImage src="/img/apds-9960/apds9960_onboard.png" alt="APDS-9960 sensor on board" caption="APDS-9960 sensor on board" width="500px" />

---

## Datasheet

For an in-depth look at technical specifications, refer to the official APDS-9960 Datasheet:  

<QuickLink  
  title="APDS-9960 Datasheet"  
  description="Detailed technical documentation for the APDS-9960 sensor"  
  url="https://soldered.com/productdata/2022/03/Soldered_APDS-9960_datasheet.pdf"  
/>  

---

## How the sensor works

The APDS-9960 is a versatile sensor that detects **ambient light, proximity, and gestures**. It integrates a **photodiode, infrared LED, and analog-to-digital converters (ADC)** into a compact module, offering efficient sensing in various applications.

The APDS-9960 operates efficiently with **low power consumption** and **stable performance**, making it ideal for **touchless control** and **smart lighting applications**.

- **Gesture Recognition** - Gesture detection utilizes four directional photodiodes to sense reflected IR energy, converting physical motion information into digital data. The gesture engine accommodates a wide range of gestures, including **up, down, left, right**, and **swipe movements**.

- **Proximity Sensing** - Using a photodiode, the sensor detects reflected IR energy to measure the distance to nearby objects, enabling **proximity detection**.

- **Ambient Light Sensing** - The sensor uses a photodiode to measure ambient light, converting it into a digital signal via an onboard ADC (analog-to-digital converter), providing **precise lux measurements**.

- **Signal Processing and Output** - The sensor processes the data internally, ensuring accurate and stable readings. The results are transmitted via an **I2C** interface for **easy integration with microcontrollers**.

---

## I2C Communication

The APDS-9960 sensor uses **I2C** (Inter-Integrated Circuit) communication to exchange data with a microcontroller. I2C uses two lines: **SDA** for **data transfer** and **SCL** for **clock synchronization**.

As a follower device (a device that accepts or provides a digital message carrying measurement or other data, but only when specifically requested), the APDS-9960 has a unique address that allows a master device to send commands and receive data, enabling features like **gesture recognition, proximity sensing**, and **ambient light measurements**.