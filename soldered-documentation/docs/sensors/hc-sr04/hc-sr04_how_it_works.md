---
slug: /hc-sr04/how-it-works 
title: How it works
id: hc-sr04-how-it-works 
hide_title: False
---  

The Qwiic compatibility is made possible with the [**Atmel ATTINY404-F**](https://soldered.com/productdata/2022/03/Soldered_ATTINY404_datasheet.pdf). When using Qwiic, you are essentially communicating with an onboard ATTINY404-F MCU via **I2C communication**, and the MCU controls the Trig and Echo pins of the sensor.

<CenteredImage src="/img/hc-sr04/ATiny404.jpg" alt="ATiny404-F on board" caption="ATTINY404-F on board" width="400px" />

---

## User Guide

For an in-depth look at the technical specifications of the ultrasonic sensor itself, refer to the official HC-SR04 User Guide:  

<QuickLink  
  title="HC-SR04 User Guide"  
  description="User guide for the HC-SR04 ultrasound sensor"  
  url="https://www.handsontec.com/dataspecs/HC-SR04-Ultrasonic.pdf"  
/>

---

## How the sensor works

The HC-SR04 is an affordable and easy-to-use distance-measuring sensor that has a range from 2cm to 400cm.

The sensor is composed of two ultrasonic transducers. One is a transmitter that outputs ultrasonic sound pulses, and the other is a receiver that listens for reflected waves.

<CenteredImage src="/img/hc-sr04/how_it_works.png" alt="Sensor receiver and transmitter" caption="Sensor receiver and transmitter" width="500px" />

Piezoelectric crystals are used as sensor elements. They oscillate at high frequencies when electrical energy is applied to them. Piezoelectric crystals generate an electrical signal when an ultrasound wave hits the sensor surface in reverse.

<CenteredImage src="/img/hc-sr04/construction.png" alt="Construction of the sensor itself" caption="Construction of the sensor itself" width="300px" />

The trigger pin is used to initiate the ultrasonic sound pulses, and the echo pin produces a pulse when the reflected signal is received. The length of the pulse is proportional to the time it takes for the transmitted signal to be detected.

<CenteredImage src="/img/hc-sr04/pin_functions.png" alt="How the echo and trigger pins work" caption="How the echo and trigger pins work" width="500px" />

---

## Qwiic I2C communication

This product uses the onboard ATTINY404-F MCU to implement I2C communication. The breakout board operates with a default I2C address of **0x30** but can be changed with onboard switches. To change the breakout board's address, check out the [**Address selection**](/hc-sr04/hardware#address-selection-qwiic-version). When detected, the ATTINY404-F receives data from the sensor and passes it to the main MCU using the **I2C data line**.