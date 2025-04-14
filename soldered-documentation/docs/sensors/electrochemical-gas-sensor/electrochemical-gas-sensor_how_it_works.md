---
slug: /electrochemical-gas-sensor/how-it-works 
title: How it works
id: electrochemical-gas-sensor-how-it-works 
hide_title: False
---  

The breakout board consists of a sensor by **SGX**. For the sensor to maintain its bias, a **potentiometer** is needed. For that we are using the **LMP91000** by **Texas Instruments**. Finally, to get readings that can be sent via I2C, we are using the **ADS1115IDGS** analog-to-digital converter by **Texas Instruments**

<CenteredImage src="/img/electrochemical-gas-sensor/sensor.webp" alt="Sensor on board" caption="Gas sensor on board" width="60%" />

<CenteredImage src="/img/electrochemical-gas-sensor/lmp91000.webp" alt="LMP91000 on board" caption="LMP91000 on board" width="60%" />

<CenteredImage src="/img/electrochemical-gas-sensor/ads1115.webp" alt="ADS1115IDGS on board" caption="ADS1115IDGS on board" width="60%" />

---

## Datasheet
  
<QuickLink  
  title="LMP91000 Datasheet"  
  description="Detailed technical documentation for the LMP91000 potentiometer"  
  url="https://www.ti.com/lit/ds/symlink/lmp91000.pdf?ts=1744317455622&ref_url=https%253A%252F%252Fwww.mouser.at%252F"  
/>

<QuickLink  
  title="ADS1115IDGS Datasheet"  
  description="Detailed technical documentation for the ADS1115IDGS"  
  url="https://www.ti.com/lit/ds/symlink/ads1115.pdf?ts=1744268937468&ref_url=https%253A%252F%252Fwww.ti.com%252Fproduct%252Fde-de%252FADS1115%252Fpart-details%252FADS1115IRUGT"  
/>

<InfoBox>You can find the datasheet for each specific sensor [**here**](hardware#sensor-datasheets)</InfoBox>

---

## How the sensor works

**Electrochemical sensors** use a chemical reaction to measure the concentration of specific gases in various environments. They work by reacting with the gas of interest and producing an electrical signal proportional to the gas concentration. The sensor operates by allowing charged molecules to pass through a thin layer of electrolyte.

## How the potentiometer works

The **electrochemical gas sensor** requires a bias circuit known as a potentiostat to maintain the correct bias potential between the sensing and reference electrodes as stated on the individual sensor datasheet:

<CenteredImage src="/img/electrochemical-gas-sensor/bias table.png" alt="ADS1115IDGS on board" caption="Bias value table for SGX sensors" width="40%"/>

The gas sensor produces an output current proportional to the gas concentration. A current to voltage converter, also known as a trans-impedance amplifier, is required to convert the small currents from the electrochemical cell into
a useful voltage for measurement.