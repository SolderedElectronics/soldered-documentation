---
slug: /pir-sensor/how-it-works 
title: How it works
id: pir-sensor-how-it-works 
hide_title: False
---  

## Communication (Standard version)

We can communicate with the sensor using two pins: **Sensor output(SOUT)** and **Delayed output(DOUT)**.

<CenteredImage src="/img/pir-sensor/pins.webp" alt="Sensor pins" caption="Sensor pins" width="400px" />

**Sensor output** immediately sends a signal after motion is detected.

**Delayed output** sends a delayed signal with a period defined by the onboard potentiometer:

<CenteredImage src="/img/pir-sensor/potentiometer.webp" alt="Onboard potentiometer" caption="Onboard potentiometer" width="400px" />

---

## Communication (Qwiic version)

The Qwiic compatibility is made possible with the [**Atmel ATTINY404-N**](https://soldered.com/productdata/2022/03/Soldered_ATTINY404_datasheet.pdf). When using Qwiic, you are essentially communicating with an onboard ATTINY404-N MCU via **I2C communication**, and the MCU detects the sensor's impulse.

<CenteredImage src="/img/pir-sensor/atmel.webp" alt="ATTINY404-N on board" caption="ATTINY404-N on board" width="400px" />

The breakout board operates with a default I2C address of **0x30** but it can be changed using onboard switches. To change the breakout board's address, check out the [**Address selection**](/pir-sensor/hardware#address-selection-qwiic-version/). When detected, the ATTINY404-N receives data from the sensor and passes it to the main MCU using the **I2C data line**.

---

## How the sensor works

A **Passive Infrared (PIR) sensor** is an electronic device that detects motion by measuring the infrared radiation (heat) emitted by objects in its field of view. These sensors are commonly used in security systems, automatic lighting, and smart home applications.

All objects emit **infrared radiation**, and the amount emitted depends on their temperature. The PIR sensor has two **pyroelectric** sensors that detect changes in infrared levels.

The sensor detects a moving object as it enters its field of view, causing a change in infrared levels. Once motion is detected, **the sensor is triggered** and it sends a signal.