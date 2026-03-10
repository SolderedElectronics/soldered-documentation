---
slug: /bmp280/overview
title: Overview
id: bmp280-overview 
hide_title: False
pagination_prev: null
---

## Pressure & altitude sensor BMP280

The **absolute barometric pressure sensor BMP280** is an atmospheric sensor that accurately measures pressure, altitude and temperature. The digital sensor on the board is based on **Bosch's** **piezo-resistive** pressure sensor technology featuring high EMC robustness, high accuracy and linearity and long term stability. Since atmospheric pressure varies with altitude, the sensor can also **measure alititude**. It is simple to use, as it communicates via **I2C communication** with a hardware defined address **0x76** or **0x77** and is designed  for seamless **Qwiic (formerly easyC) connectivity**. Its very low current consumption makes this sensor suitable for many modern devices.

<InfoBox> BMP280 is the successor to the widely adopted **BMP180**. </InfoBox>

<CenteredImage src="/img/bmp280/bmp280_front.JPG" alt="BMP280 image" width="700px"/>

---

## Which product is this documentation for

<QuickLink 
  title="BMP280 Pressure & Altitude sensor" 
  description="333315"
  url="https://soldered.com/products/bmp280-temperature-and-pressure-sensor-breakout"
  image="/img/bmp280/bmp280_front.JPG" 
/>

---

## Key Features

- **Measurement modes:** Pressure and temperature, forced or periodic
- **Measurement range:**
    - **Temperature:** -40°C to 85°C ± 0.01°C resolution
    - **Pressure range:** 300hPa to 1100hPa, ±0.16Pa resolution
- **Current consumption:** 2.7 µA at 1Hz sampling rate
- **Minimum Vdd:** 1.71V
- **Minimum Vddio:** 1.20V
- **Measurement rate:** up to 157Hz
- **Communication:** I2C (default address: 0x76, alternative address: 0x77 by shorting JP2)
- **Connector:** 2 x **Qwiic (formerly easyC) ports** (plug-and-play, no soldering needed)
- **Mounting:** **Four mounting holed** for secure attachment
- **Dimensions:** **22 x 38 mm** (0.87 x 1.5 inch)

---

## You may also need

<QuickLink 
  title="Qwiic cable" 
  description="Qwiic (formerly easyC) compatible cables with connectors on both ends, available in various lengths."
  url="https://soldered.com/product/easyc-cable/"
  image="/img/333311.webp" 
/>