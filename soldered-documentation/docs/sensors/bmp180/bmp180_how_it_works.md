---
slug: /bmp180/how-it-works 
title: How it works
id: bmp180-how-it-works 
hide_title: False
---  

BMP180 is an integrated circuit by **Bosch**. When using our board, you are essentially communicating with the onboard BMP180 directly via **I2C communication**.

<CenteredImage src="/img/bmp180/bmp180_onboard.jpg" alt="BMP180 sensor on board" caption="BMP180 sensor on the board" width="400px" />

---

## Datasheet

For an in-depth look at technical specifications, refer to the official BME680 Datasheet:  

<QuickLink  
  title="BMP180 Datasheet"  
  description="Detailed technical documentation for the BMP180 sensor"  
  url="https://soldered.com/productdata/2022/03/Soldered_BMP180_datasheet.pdf"  
/>  

---

## How the sensor works 

The BMP180 is a **Pressure & temperature sensor** that can also calculate the altitude depending on the pressure. 
The sensor takes measurements by using the piezoresistive effect to gather information

The **piezoresistive effect** is a change in the electrical resistivity of a material (e.g. semiconductor, metal) when mechanical strain is applied. The electrical resistance change is due to two causes; geometry change and conductivity change of the material. The change in resistance is much more pronounced for semiconductors than for metals. 

Four Si-resistors are diffused into a semiconductor membrane and connected with another to form a Wheatstone-Bridge. Under the influence of pressure, the diaphragm deforms, thereby affecting the electrical resistance of the four Si-resistors. The change in resistance is proportional to the applied pressure.

<CenteredImage src="/img/bmp180/bmp180_piezoresistance.png" alt="Piezoresistor schema" caption="Schematic diagram of the pressure sensor, originally from article [Temperature Compensation Method for Piezoresistive Pressure Sensors Based on Gated Recurrent Unit](https://www.mdpi.com/1424-8220/24/16/5394)" width="600px" />