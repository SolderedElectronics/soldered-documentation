---
slug: /mq/how-it-works 
title: MQ Gas Sensors – How it works
sidebar_label: How it works
id: mq-how-it-works 
hide_title: False
---  

## How the sensor works

An **MQ sensor** is a type of gas sensor that operates on a chemiresistive principle, meaning it detects gases by measuring changes in electrical resistance.

The core component of an MQ sensor is a **metal oxide semiconductor (MOS)**, typically made of tin dioxide (SnO₂). In clean air, this material has a high resistance, but when exposed to certain gases, a chemical reaction occurs that alters its **conductivity**.

<CenteredImage src="/img/mq/shema.png" alt="Basic MQ sensor diagram" caption="Basic MQ sensor diagram" width="400px" />

---

## Datasheets
The measuring range, preheat time, available gasses to detect and much more can be found in the datasheets:

| Sensor      | Datasheet | 
| ----------- | --------- | 
| MQ2         | [Link](https://soldered.com/productdata/2015/02/Soldered_MQ-2_datasheet.pdf)     | 
| MQ3    | [Link](https://soldered.com/productdata/2015/02/Soldered_MQ-3_datasheet.pdf)   |
| MQ4   | [Link](https://soldered.com/productdata/2015/09/Soldered_MQ-4_datasheet.pdf)     |
| MQ5    | [Link](https://soldered.com/productdata/2022/03/Soldered_MQ-5_datasheet.pdf)  | 
| MQ6    | [Link](https://soldered.com/product/lpg-butane-sensor-mq6-breakout-with-easyc/)    |
| MQ7    | [Link](https://soldered.com/product/co-sensor-mq7-breakout-with-easyc/)     |
| MQ8      | [Link](https://soldered.com/productdata/2015/09/Soldered_MQ-8_datasheet.pdf) | 
| MQ9        | [Link](https://soldered.com/productdata/2015/09/Soldered_MQ-9_datasheet.pdf) | 
| MQ131      | [Link](https://soldered.com/productdata/2021/01/Soldered_o3.winsen-mq131_datasheet.pdf) | 
| MQ135      | [Link](https://soldered.com/productdata/2022/03/Soldered_MQ-135_datasheet.pdf) | 
| MQ137      | [Link](https://soldered.com/productdata/2022/03/Soldered_MQ-137_datasheet.pdf) | 
| MQ138      | [Link](https://soldered.com/productdata/2022/03/Soldered_MQ-138_datasheet.pdf) | 

---

## Communication (Native)

There are two pins used for communicating with the sensor: **analog** and **digital**.

The **analog pin** outputs the voltage from the sensor, which is then used by the dasduino board to calculate the levels of a particular gas. As stated previously, the resistance of the sensor falls as the concentration of gas increases. We can determine the gas concentration in ppm/ppb by using the ratio of the resistance measured during calibration (Ro) to the current sensor resistance (Rs).

<CenteredImage src="/img/mq/curve.png" alt="Example of an MQ sensor resistance curve" caption="Example of an MQ sensor resistance curve"  />

The curve that the resistance follows for a specific gas must be approximated by the sensor. This is achieved by identifying attributes of the curves and applying a linear or exponential **regression method**. This process is explained in detail in the link below:

<QuickLink 
  title="Understanding a gas sensor" 
  description="Detailed guide on how to calculate the approximate curve of resistance by Jaycon"
  url="https://www.jaycon.com/understanding-a-gas-sensor/"
/>

<InfoBox> 
All of our sensors have a pre-configured regression method for each sensor! Check them out [**here**](https://github.com/SolderedElectronics/Soldered-MQ-Gas-Sensor-Arduino-Library/blob/main/src/sensorConfigData.h)
</InfoBox> 





The **digital pin** works through the onboard potentiometer. Adjusting the potentiometer sets the voltage (gas concentration) at which the digital pin will be set to HIGH. This is commonly used as a trigger for an alarm if the concentration of a gas becomes too high.

<CenteredImage src="/img/mq/potentiometer.jpg" alt="Onboard potentiometer" caption="Onboard potentiometer"  />

---

## Communication (Qwiic)

The Qwiic compatibility is made possible with the [**Atmel ATTINY404-SSNR**](https://soldered.com/productdata/2022/03/Soldered_ATTINY404_datasheet.pdf). When using Qwiic, you are essentially communicating with an onboard ATTINY404-SSNR MCU via **I2C communication**, and the MCU detects the sensor's voltage level.

<CenteredImage src="/img/mq/atmel.jpg" alt="ATTINY404-SSNR on board" caption="ATTINY404-SSNR on board" width="400px" />

The breakout board operates with a default I2C address of **0x30**; however, it can be changed using onboard switches. To change the breakout board's address, check out the [**Address selection**](/documentation/mq/hardware/#address-selection-qwiic-version). When detected, the ATTINY404-SSNR receives data from the sensor and passes it to the main MCU using the **I2C data line**.