---
slug: /hall-effect-sensor/how-it-works 
title: How it works
id: hall-effect-sensor-how-it-works 
hide_title: False
---  

SI7211-B-00-IV is an integrated circuit by [**Silicon Labs**](https://www.silabs.com/sensors/magnetic/si721x/device.si7211-00-iv?tab=specs). When using our board, you are essentially communicating with the onboard SI7211-B-00-IV directly via **I2C communication**.

<CenteredImage src="/img/hall-effect-sensor/333081_onboard_highlighted.jpg" alt="SI7211-B-00-IV sensor on board" caption="SI7211-B-00-IV sensor on the board" width="400px" />

---

## Datasheet

For an in-depth look at technical specifications, refer to the official SI7211-B-00-IV Datasheet:  

<QuickLink  
  title="SI7211-B-00-IV Datasheet"  
  description="Detailed technical documentation for the SI7211-B-00-IV sensor"  
  url="https://soldered.com/productdata/2022/03/Soldered_si7211x_datasheet.pdf"  
/>  

---

## How the sensor works  

A SI7211-B-00-IV consists of a thin rectangular semiconductive material (indium arsenide, gallium arsenide) through which flows a continuous current. When the sensor is exposed to a magnetic field perpendicular to the current, the **magnetic (Lorentz) force** deflect the charge carriers within the semiconductor. This deflection causes a difference in potentials, known as **Hall Voltage**, proportional to the strength of the magnetic field. The Hall Voltage generated is **typically very small (in microvolts)**, so it is **amplified by an internal high gain amplifier**.

---

## I2C communication - Qwiic

The SI7211-B-00-IV uses the I2C protocol to communicate with a microcontroller by using an onboard Atmel microcontroller. It operates with a default I2C address of **0x30**  but can be changed with onboard switches.
When detected, the sensor digitizes the component of the magnetic field in the z axis of the device **positive field is defined as pointing into the device from the bottom**. The digitized field is then converted to an output format of analog PWM or digital.

---

