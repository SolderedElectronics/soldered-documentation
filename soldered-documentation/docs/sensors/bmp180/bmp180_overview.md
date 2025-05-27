---
slug: /bmp180/overview
title: "BMP180 Pressure & temperature sensor \u2013 Overview"
id: bmp180-overview
hide_title: false
pagination_prev: null
---
## Pressure & temperature sensor BMP180

The **BMP180 Pressure & temperature sensor** is an atmospheric sensor that measures two values: temperature and pressure. The digital sensor on the board precisely measures changes in barometric pressure and temperature. It uses the **piezoresistive effect** to gather information. Since atmospheric pressure varies with altitude, the sensor can also measure altitude. It is simple to use, as it communicates via **I2C communication** with a hardware-defined address of **0x77** and is designed for seamless **Qwiic (formerly easyC) connectivity**. Its very low current consumption and voltage make this sensor suitable for many modern devices.

<CenteredImage src="/img/bmp180/333060.jpg" alt="BMP180 Pressure & temperature sensor" caption="BMP180 Pressure & temperature sensor" />
---

## Which product is this documentation for?

<QuickLink 
  title="Pressure & temperature sensor BMP180 breakout" 
  description="333060"
  url="https://soldered.com/product/pressure-temperature-sensor-bmp180-breakout/"
  image="/img/bme280/333036.webp" 
/>

---

## Key Features

- **Measurement range:**  
  - **Temperature:** -40°C to 85°C, ±2°C accuracy  
  - **Pressure range:** 300hPa to 1100hPa, ±0.02hPa accuracy 
- **Power consumption:**  
  - **Standard current consumption:** 5 µA  
  - **Standby current consumption:** 0.1 µA  
- **Logic voltage level:** 5V on I2C header, 3.3V on easyC  
- **Operating voltage:** 3.3V (onboard regulator for 5V compatibility)  
- **Communication:** I2C (fixed address: 0x77)  
- **Connector:** 2 × **Qwiic (formerly easyC) ports** (plug-and-play, no soldering needed)  
- **Mounting:** **Two mounting holes** for secure attachment  
- **Dimensions:** **22 × 22 mm** (0.9 × 0.9 inch)  

---

## You may also need

<QuickLink 
  title="Qwiic cable" 
  description="Qwiic (formerly easyC) compatible cables with connectors on both ends, available in various lengths."
  url="https://soldered.com/product/easyc-cable/"
  image="/img/333311.webp" 
/>