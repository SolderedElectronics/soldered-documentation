---  
slug: /bmp388/how-it-works  
title: BMP388 Pressure & Temperature Sensor - How it Works  
id: bmp388-how-it-works  
sidebar_label: How it works  
hide_title: False  
---  

The **BMP388** is an integrated circuit by [**Bosch**](https://www.bosch-sensortec.com/media/boschsensortec/downloads/product_flyer/bst-bmp388-fl000.pdf). When using our board, you are essentially communicating directly with the onboard BME280 via **I2C communication**.

<CenteredImage src="/img/bmp388/bmp_sensor_onboard.png" alt="BMP388 sensor on board" caption="Onboard BMP388 sensor" width="600px" />

---

## Datasheet

For an in-depth look at technical specifications, refer to the official BMP388 Datasheet:  

<QuickLink  
  title="BMP388 Datasheet"  
  description="Detailed technical documentation for the BMP388 sensor"  
  url="https://www.bosch-sensortec.com/media/boschsensortec/downloads/datasheets/bst-bmp388-ds001.pdf"  
/>

---

## How the sensor works

The BMP388 is a **sensor with temperature and barometric pressure** measurement capability. The basic working principle is that the sensor performs temperature and pressure measurements; after the measurement period, the selected temperature and pressure data pass through a low-pass IIR filter that removes noise caused by short-term pressure fluctuations, such as those from wind blowing directly into the sensor, door impacts, car acceleration, etc.

<CenteredImage src="/img/bmp388/diagram.png" alt="BMP388 simplified block diagram" caption="BMP388 simplified block diagram" width="600px" />

Temperature sensors work by measuring the capacitance or resistance of air samples.

A barometric pressure sensor works by using a flexible diaphragm that deforms under atmospheric pressure, converting this physical change into a measurable electrical signal.

<CenteredImage src="/img/bmp388/flow_chart.png" alt="BMP388 measurement flow chart" caption="BMP388 measurement flow chart" width="600px" />

It has three operating modes:
- **Sleep**: Lowest power consumption mode; no measurements are performed, and all registers are accessible.
- **Forced**: Suitable for situations that do not require frequent measurements, such as when reading weather conditions. One measurement is performed, the data is saved to registers, and the sensor returns to sleep mode. This method reduces power consumption.
- **Normal**: Constantly performs measurements with an adjustable delay (i.e., inactive time).

---

## I2C communication

The BMP388 uses the I2C protocol to communicate with a microcontroller. It operates with a fixed I2C address of **0x76**.

Upon request, the sensor responds with pressure and temperature values in an unsigned 24-bit format.