---
slug: /bme688/how-it-works 
title: BME688 - How it works
sidebar_label: How it works
id: bme688-how-it-works 
hide_title: False
---  

BME688 is an integrated circuit by [**Bosch**](https://www.bosch-sensortec.com/products/environmental-sensors/gas-sensors/bme688/). When using our board, you are essentially communicationg with the onboard BME688 directly via **I2C communication**.

<CenteredImage src="/img/bme688/bme688_onboard.jpg" alt="BME688 sensor on board" caption="BME688 sensor on the board" width="400px"/>

---

## Datasheet

For an in-depth look at technical specifications, refer to the official BME688 Datasheet

<QuickLink
    title="BME688 Datasheet"
    description="Detailed technical documentation for the BME688 sensor"
    url="https://www.bosch-sensortec.com/media/boschsensortec/downloads/datasheets/bst-bme688-ds000.pdf"
/>

---

## How the sensor works

The Bosch BME688 is a compact enviromental sensor that combines gas, pressure, temperature and humidity sensing in one device. Its gas sensor uses a heated **metal-oxide** layer that changes electrical resistance when exposed to volatile organic compounds (VOCs) and other gases. By cycling the heater through different temperature steps, the sensor creates a "fingerprint" of gas responses, which allows it to distinguish between different gas mixtures. The raw resistance values are processed by Bosch's **BSEC** software, which applies compensation for humidity and temperature effects, then converts them into meaningful outputs such as an **Index of Air Quality** (IAQ), estimated **CO2** levels, and **breath-VOC** equivalents. The BME688 continuously calibrates itself to typical indoor environments and can be customized with **AI-based** tools to recognize specific gas patterns for applications like air quality monitoring, food spoilage detection, or smart home devices.

<InfoBox> To calculate the Air Quality Index (AQI), it is recommended to use the [BSEC Software arduino library by Bosch](https://www.bosch-sensortec.com/software-tools/software/bme688-and-bme690-software/)</InfoBox>

---

## I2C communication

The BME688 breakout board uses the I2C protocol to communicate with the microcontroller. It operates with a default I2C addres of **0x76** (or 0x77 if the **SDO** pin is pulled high). Upon request, the sensor responds with pressure and tepmerature values in a 20-bit format and the humidity value as a 16-bit ADC value.

