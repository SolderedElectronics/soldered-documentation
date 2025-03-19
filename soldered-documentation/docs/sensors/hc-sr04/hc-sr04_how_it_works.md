---
slug: /hc-sr04/how-it-works 
title: How it works
id: hc-sr04-how-it-works 
hide_title: False
---  

The Qwiic compatibility is made possible with the [**Atmel ATiny404-F**](https://soldered.com/productdata/2022/03/Soldered_ATTINY404_datasheet.pdf)

<CenteredImage src="/img/hc-sr04/ATiny404.jpg" alt="ATiny404-F on board" caption="ATiny404-F on board" width="400px" />

---

## User Guide

For an in-depth look at technical specifications of the ultrasonic sensor itself, refer to the official HC-SR04 User Guide:  

<QuickLink  
  title="HC-SR04 User Guide"  
  description="User guide for the HC-SR04 ultrasound sensor"  
  url="https://www.handsontec.com/dataspecs/HC-SR04-Ultrasonic.pdf"  
/>  

---

## How the sensor works

The HC-SR04 is an affordable and easy to use distance measuring sensor which has a range from 2cm to 400cm.

The sensor is composed of two ultrasonic transducers. One is a transmitter which outputs ultrasonic sound pulses and the other is receiver which listens for reflected waves.

<CenteredImage src="/img/hc-sr04/how_it_works.png" alt="Sensor reciever and transmitter" caption="Sensor reciever and transmitter" width="500px" />

Piezoelectric crystals are used for sensor elements. Piezoelectric crystals will oscillate at high frequencies
when electric energy is applied to it. The Piezoelectric crystals will generate electrical signal when
ultrasound wave hit the sensor surface in reverse.

<CenteredImage src="/img/hc-sr04/construction.png" alt="Construction of the sensor itself" caption="Construction of the sensor itself" width="300px" />

The trigger pin is used to trigger the ultrasonic sound pulses and the echo pin produces a pulse when the reflected signal is received. The length of the pulse is proportional to the time it took for the transmitted signal to be detected.

<CenteredImage src="/img/hc-sr04/pin_functions.png" alt="How the echo and trigger pins work" caption="How the echo and trigger pins work" width="500px" />