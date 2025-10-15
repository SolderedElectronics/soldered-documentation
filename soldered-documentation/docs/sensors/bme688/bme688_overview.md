---
slug: /bme688/overview
title: BME688 - Overview
sidebar_label: Overview
id: bme688-overview 
hide_title: False
pagination_prev: null
---

## BME688 Enviromental and air quality sensor breakout

The **BME688** is a digital environmental sensor that integrates temperature, humidity, pressure and AI-based gas classification capabilities. It's the first sensor that has built-in Artificial Intelligence, allowing developers to customize gas detection for specific applications. This board uses **I2C communication protocol** with a default address of **0x76**. It has 2 onboard **Qwiic ports** so it is suitable for a I2C daisychained connection with multiple devices.

<CenteredImage src="/img/bme688/333203.jpg" alt="Enviromental & Air sensor BME688" caption="Enviromental & Air sensor sensor BME688" />

---

## Which products is this documentation for?

<QuickLink
  title="Enviromental & air quality sensor BME688 breakout"
  description="333203"
  url="#"
  image=""
/>

---

## Key Features

- **Digital interface:** I2C (up to 3.4MHz) and SPI (3 and 4 wire, up to 10 MHz)
- **Supply voltage:**
  - 2.1 μA at 1 Hz humidity and temperature
  - 3.1 μA at 1 Hz pressure and temperature
  - 3.7 μA at 1 Hz humidity, presure and temperature
  - 90 μA at ULP mode for p/h/T and air quality
  - 0,9 mA at LP mode for p/h/T and air quality
  - 3,9 mA in standard gas scan mode
  - 0.09 -12 mA for p/h/T/gas in customized operation modes
  - 0.15 μA in sleep mode
- **Operating range**
  - 40 -* 85 °C
  - 0-100% r.H.
  - 300 - 1100 hPa
---

## You may also need

<QuickLink 
  title="Qwiic cable" 
  description="Qwiic (formerly easyC) compatible cables with connectors on both ends, available in various lengths."
  url="https://soldered.com/product/easyc-cable/"
  image="/img/333311.webp" 
/>