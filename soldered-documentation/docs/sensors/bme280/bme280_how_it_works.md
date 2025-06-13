---
slug: /bme280/how-it-works 
title: Bme280 – How it works
id: bme280-how-it-works 
hide_title: False
---  

BME280 is an integrated circuit by [**Bosch**](https://www.bosch-sensortec.com/products/environmental-sensors/humidity-sensors-bme280/). When using our board, you are essentially communicating directly with the onboard BME280 via **I2C communication**.

<CenteredImage src="/img/bme280/bme280_onboard.webp" alt="BME280 sensor on board" caption="BME280 sensor on the board" width="400px" />

---

## Datasheet

For an in-depth look at technical specifications, refer to the official BME280 Datasheet:  

<QuickLink  
  title="BME280 Datasheet"  
  description="Detailed technical documentation for the BME280 sensor"  
  url="https://www.bosch-sensortec.com/media/boschsensortec/downloads/datasheets/bst-bme280-ds002.pdf"  
/>

---

## How the sensor works  

The BME280 is an **environmental sensor with temperature, barometric pressure, and humidity** measurement capabilities. The basic working principle is that the sensor performs temperature, pressure, and humidity measurements; after the measurement period, the selected temperature and pressure data pass through a low-pass IIR filter that removes the noise caused by short-term pressure fluctuations, such as those from wind blowing directly into the sensor, door impacts, car acceleration, etc.

<CenteredImage src="/img/bme280/bme280_diagram.png" alt="BME280 simplified block diagram" caption="BME280 simplified block diagram" width="600px" />

Temperature and humidity sensors work by measuring the capacitance or resistance of air samples. Most of these sensors utilize capacitive measurement to determine the amount of moisture in the air. This method relies on two electrical conductors with a non-conductive polymer film lying between them to form an electrical field.

Moisture from the air collects on the film and causes changes in the voltage levels between the two plates. This change is then converted into a computerized measurement of the air’s relative humidity after taking the air temperature into account.

<CenteredImage src="/img/bme280/bme280_flowchart.png" alt="BME280 measurement cycle" caption="BME280 measurement cycle" width="600px" />

It has three operating modes:
- **Sleep**: Lowest power consumption mode; no measurements are performed, and all registers are accessible.
- **Forced**: Suitable for situations that do not require frequent measurements, such as when reading weather conditions. One measurement is performed, the data is saved to registers, and the sensor returns to sleep mode. This method reduces power consumption.
- **Normal**: Constantly performs measurements with an adjustable delay (i.e., inactive time).

---

## I2C communication  

The BME280 uses the I2C protocol to communicate with a microcontroller. It operates with a fixed I2C address of **0x76**.

Upon request, the sensor responds with pressure and temperature values in a 20-bit format and the humidity value as a 16-bit ADC value.

<InfoBox>While the BME280 shares many similarities with the BME680 sensor, the main difference is that the BME680 includes an additional gas resistance sensor. [Check out the BME680 here!](../bme680/bme680_overview.md)</InfoBox>