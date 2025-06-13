---
slug: /bme680/how-it-works 
title: Bme680 – How it works
id: bme680-how-it-works 
hide_title: False
---  

BME680 is an integrated circuit by [**Bosch**](https://www.bosch-sensortec.com/products/environmental-sensors/gas-sensors/bme680/). When using our board, you are essentially communicating with the onboard BME680 directly via **I2C communication**.

<CenteredImage src="/img/bme680/bme680_onboard.webp" alt="BME280 sensor on board" caption="BME680 sensor on the board" width="400px" />

---

## Datasheet

For an in-depth look at technical specifications, refer to the official BME680 Datasheet:  

<QuickLink  
  title="BME680 Datasheet"  
  description="Detailed technical documentation for the BME680 sensor"  
  url="https://www.bosch-sensortec.com/media/boschsensortec/downloads/datasheets/bst-bme680-ds001.pdf"  
/>

---

## How the sensor works 

The BME680 is an **environmental & air quality sensor with temperature, barometric pressure, humidity, and gas resistance**.

Temperature and humidity sensors work by measuring the capacitance or resistance of air samples. Most of these sensors utilize capacitive measurement to determine the amount of dampness in the air. This sort of measurement relies on two electrical conductors with a non-conductive polymer film laid between them to form an electrical field.

Moisture from the air collects on the film and causes changes in the voltage levels between the two plates. This change is then converted into a computerized measurement of the air’s relative humidity after taking the air temperature into account.

The BME680 also supports a self test on soft reset, as pictured below:

<CenteredImage src="/img/bme680/bme680_selftest.png" alt="BME680 self test diagram" caption="BME680 self test diagram" width="200px" />

The Gas resistance sensor works as follows: Based on the volume and concentration of a gas in an area, the sensor will produce what is called a “corresponding potential difference,” which changes the level of resistance of the material inside the sensor. From this change in the level of resistance comes an electrical signal that is measured as output voltage.

<CenteredImage src="/img/bme680/bme680_resistance.png" alt="BME680 gas resistance depending on pollutants" caption="BME680 gas resistance depending on pollutants" width="600px" />

<InfoBox>To calculate the Air Quality Index (AQI), it is recommended to use the [BSEC Software arduino library by Bosch](https://www.bosch-sensortec.com/software-tools/software/bme680-software-bsec/)</InfoBox>

## I2C communication  

The BME680 uses the I2C protocol to communicate with a microcontroller. It operates with a fixed I2C address of **0x76**.

Upon request, the sensor responds with pressure and temperature values in a 20-bit format and the humidity value as a 16-bit ADC value.

<InfoBox>While the BME680 shares a lot of similarities with the BME280 sensor, the main difference is that the BME680 has an additional gas resistance sensor. [Check out the BME280 here!](../bme280/bme280_overview.md)</InfoBox>