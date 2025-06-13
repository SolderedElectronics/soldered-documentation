---
slug: /shtc3/how-it-works 
title: Shtc3 - How it works
sidebar_label: How it works
id: shtc3-how-it-works 
hide_title: False
---  

SHTC3 is an integrated circuit by [**Sensirion**](https://sensirion.com/products/catalog/SHTC3). When using our board, you are essentially communicating with the onboard SHTC3 directly via **I2C communication**.

<CenteredImage src="/img/shtc3/shtc3_onboard.png" alt="SHTC3 sensor on board" caption="SHTC3 sensor on the board" width="400px" />

---

## Datasheet

For an in-depth look at technical specifications, refer to the official SHTC3 Datasheet:  

<QuickLink  
  title="SHTC3 Datasheet"  
  description="Detailed technical documentation for the SHTC3 sensor"  
  url="https://soldered.com/productdata/2022/03/Soldered_SHTC3_datasheet.pdf"  
/>  

---

## How the sensor works  

The SHTC3 integrates a **capacitive humidity sensor** and a **bandgap temperature sensor** into a single compact package. Internally, it includes signal conditioning, analog-to-digital conversion (ADC), calibration memory, and an I2C interface for seamless data retrieval.  

The sensor continuously measures temperature and humidity, converting the readings into digital signals with built-in compensation for accurate and stable performance.  

---

## I2C communication  

The SHTC3 uses the I2C protocol to communicate with a microcontroller. It operates with a fixed I2C address of **0x70** and supports fast mode (400 kHz) for rapid data transmission.  

Upon request, the sensor responds with two 16-bit values—one for humidity and one for temperature—along with a CRC checksum for data integrity.  

---

## Measurement process  

The measurement process is as follows:

1. **Power-up and initialization**  
   - The sensor enters idle mode when powered on.  
   - A wake-up command (0x3517) is required before taking measurements.  

2. **Taking a measurement**  
   - The sensor executes a single humidity and temperature measurement upon receiving the appropriate command.  
   - Data conversion is completed in 10.8ms (high-resolution mode).  

3. **Data retrieval**  
   - The microcontroller sends an I2C read command to retrieve the latest humidity and temperature readings.  
   - The sensor provides a CRC-protected 16-bit output for both values.  

