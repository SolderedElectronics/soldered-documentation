---
slug: /ltr-507/how-it-works 
title: Ltr 507 – How it works
sidebar_label: How it works
id: ltr-507-how-it-works 
hide_title: False
---  

The LTR-507ALS-01 is an integrated I2C digital light sensor (ALS) and proximity sensor (PS) with a built-in LED driver manufactured by [**Lite-On**](https://optoelectronics.liteon.com/en-global/led/LED-Component).

<CenteredImage src="/img/ltr-507/ltr-507onboard.png" alt="ltr-507 sensor on board" caption="LTR-507 sensor on board" width="500px" />

---

## Datasheet

For an in-depth look at the technical specifications, refer to the official LTR-507 Datasheet:

<QuickLink  
  title="LTR-507 Datasheet"  
  description="Detailed technical documentation for the LTR-507 sensor"  
  url="https://soldered.com/productdata/2022/03/Soldered_LTR-507ALS_datasheet.pdf"  
/>

---

## How the Sensor Works

The LTR-507 is a highly efficient **ambient light** and **proximity sensor** designed for **low power consumption** and **precise measurements** in a compact form factor. It integrates a **photodiode**, an **analog-to-digital converter (ADC)**, and a **digital output interface**, making it ideal for applications in energy-efficient systems, smart lighting, and proximity sensing.

- **Ambient Light Sensing** – The LTR-507 features a **photodiode** that measures the **intensity of ambient light**. The sensor then converts this **analog signal** into a **digital output** using its onboard **ADC**, delivering precise lux measurements ranging from 0 to 65,535 lux. This makes the sensor perfect for applications requiring **dynamic light adjustments** based on environmental lighting conditions.
  
- **Proximity Sensing** – The LTR-507 uses **infrared (IR)** light to detect objects within its proximity range (up to 20 cm). The sensor emits IR light, and the photodiode measures the amount of reflected light to calculate the distance to nearby objects, providing accurate proximity sensing for various applications.

- **Signal Processing and Output** – After collecting data, the LTR-507 processes the light and proximity readings internally. The sensor provides the processed data through the **I2C interface**, ensuring easy integration with microcontrollers like **Arduino** or **Raspberry Pi**.

---

## I2C Communication

The LTR-507ALS-01 sensor utilizes **I2C** (Inter-Integrated Circuit) communication to transmit data between the sensor and a microcontroller. I2C operates with two main lines: **SDA** for **data transfer** and **SCL** for **clock synchronization**.

<InfoBox>The I2C address can be changed! [**Address selection**](/ltr-507/hardware#address-selection)</InfoBox>

As a follower device, the LTR-507 responds to commands sent from the leader device. It has a configurable I2C address, allowing for easy communication. The leader device can request **ambient light** and **proximity data**, enabling the sensor to provide measurements of **lux levels** and the **distance to nearby objects**.