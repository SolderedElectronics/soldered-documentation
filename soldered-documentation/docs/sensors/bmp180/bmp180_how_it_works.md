---
slug: /bmp180/how-it-works
title: "BMP180 Pressure & temperature sensor \u2013 How it works"
id: bmp180-how-it-works
hide_title: false
---
BMP180 is an integrated circuit by **Bosch**. When using our board, you are essentially communicating with the onboard BMP180 directly via **I2C communication**.

<CenteredImage src="/img/bmp180/bmp180_onboard.jpg" alt="BMP180 sensor on board" caption="BMP180 sensor on the board" width="400px" />

---

## Datasheet

For an in-depth look at technical specifications, refer to the official BMP180 Datasheet:  

<QuickLink  
  title="BMP180 Datasheet"  
  description="Detailed technical documentation for the BMP180 sensor"  
  url="https://soldered.com/productdata/2022/03/Soldered_BMP180_datasheet.pdf"  
/>  

---

## How the sensor works 

The BMP180 is a **pressure and temperature sensor** that can also calculate altitude based on pressure.  
The sensor takes measurements by using the piezoresistive effect to gather information.

The **piezoresistive effect** is a change in the electrical resistivity of a material (e.g., semiconductor, metal) when mechanical strain is applied. The electrical resistance change is due to two causes: a change in geometry and a change in conductivity of the material. The change in resistance is much more pronounced for semiconductors than for metals.

Four Si-resistors are diffused into a semiconductor membrane and connected together to form a Wheatstone bridge. Under the influence of pressure, the diaphragm deforms, thereby affecting the electrical resistance of the four Si-resistors. The change in resistance is proportional to the applied pressure.

<CenteredImage src="/img/bmp180/bmp180_piezoresistance.png" alt="Piezoresistor schema" caption="Schematic diagram of the pressure sensor, originally from article [Temperature Compensation Method for Piezoresistive Pressure Sensors Based on Gated Recurrent Unit](https://www.mdpi.com/1424-8220/24/16/5394)" width="600px" />

## I2C communication  

The BMP180 uses the I2C protocol to communicate with a microcontroller. It operates with a fixed I2C address of **0x77** and supports a speed of up to 3.4MHz for rapid data transmission.  

Upon request, the sensor responds with pressure values in a 16 to 19 bit format and temperature values in a 16 bit format.