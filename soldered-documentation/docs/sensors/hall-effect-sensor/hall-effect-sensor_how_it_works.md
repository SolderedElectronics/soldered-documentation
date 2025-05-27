---
slug: /hall-effect-sensor/how-it-works
title: "Hall Effect Sensor \u2013 How it works"
id: hall-effect-sensor-how-it-works
hide_title: false
---
Analog versions of the circuit board (both regular and Qwiic) use the SI7211-B-00-IV sensor, while digital (both regular and Qwiic) use SI7211-B-06-IV sensor by [**Silicon Labs**](https://www.silabs.com/sensors/magnetic/si721x/device.si7211-00-iv?tab=specs). When using a Qwiic version you are essentially communicating with an onboard ATTINY404 MCU via **I2C communication**.


<CenteredImage src="/img/hall-effect-sensor/333081_onboard_highlighted.jpg" alt="SI7211-B-00-IV sensor on board" caption="SI7211-B-00-IV sensor on the board of easyC breakout board" width="400px" />

<CenteredImage src="/img/hall-effect-sensor/hall-effect-sensor_ATTINY_highlighted.jpg" alt="ATTINY404 on the board" caption="ATTINY404 on the board of easyC breakout board" width="400px" />

---

## Datasheet

For an in-depth look at technical specifications, refer to the official SI7211-B-00-IV / SI7211-B-06-IV Datasheet:  

<QuickLink  
  title="SI721x Datasheet"  
  description="Detailed technical documentation for the SI721x sensors"  
  url="https://soldered.com/productdata/2022/03/Soldered_si7211x_datasheet.pdf"  
/>  

---

## How the sensor works  

A SI721x consists of a thin rectangular semiconductive material (indium arsenide, gallium arsenide) through which flows a continuous current. When the sensor is exposed to a magnetic field perpendicular to the current, the **magnetic (Lorentz) force** deflects the charge carriers within the semiconductor. This deflection causes a difference in potential, known as **Hall Voltage**, which is proportional to the strength of the magnetic field.
The Hall Voltage generated is **typically very small (in microvolts)**, so it is **amplified by an internal high gain amplifier**.

<CenteredImage src="/img/hall-effect-sensor/hall-effect-sensor_how_it_works.png" alt="visualization of sensor operation" caption="visualization of sensor operation" width="400px" />

---

## I2C communication - Qwiic

Qwiic versions of the product use an onboard ATTINY404 MCU to implement I2C communication. The breakout board operates with a default I2C address of **0x30**; however, this can be changed using the onboard switches. To change the breakout board's address, check the [**Address selection**](/documentation/hall-effect-sensor/hardware#address-selection/). When detected, the ATTINY404 receives data from the sensor and passes it on to the main MCU using the I2C data line. To check in detail how the ATTINY404 is preprogrammed, check the [**firmware github page**](https://github.com/SolderedElectronics/Soldered-Hall-Effect-Sensor-Arduino-Library/tree/dev/extras/attiny_firmware).


