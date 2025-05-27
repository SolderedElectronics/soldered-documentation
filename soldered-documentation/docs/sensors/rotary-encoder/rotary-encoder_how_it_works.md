---
slug: /rotary-encoder/how-it-works
title: "Rotary Encoder \u2013 How it works"
id: rotary-encoder-how-it-works
hide_title: false
---
Rotary encoder is a **positional sensor** which is used for determining the **angular position of a rotating shaft**, and generates an **electrical output signal** related to that position. Breakout board uses **EC11E1534408** rotary encoder by [ALPS](https://eu.mouser.com/ProductDetail/Alps-Alpine/EC11E1534408?qs=PoKhxlfUXjJk5yy1jIb28A%3D%3D&srsltid=AfmBOoqWdrLCWfukAif74HADQ5xgEWlmpqFwtwPZqIAtxNFYmnJB0LJY) When using an Qwiic version you are essentially communicating with an onboard ATTINY404 MCU via **I2C communication**.

<CenteredImage src="/img/rotary-encoder/333188_ATTiny_highlighted.jpg" alt="ATTINY404 on the board" caption="ATTINY404 on the board" width="400px" />

---

## Datasheet

For an in-depth look at technical specifications, refer to the official EC11E1534408 Datasheet:

<QuickLink  
  title="EC11E1534408 Datasheet"  
  description="Detailed technical documentation for the EC11E1534408 sensors"  
  url="https://soldered.com/productdata/2023/08/Soldered_rotary-encoder_datasheet.pdf"  
/>  

---

## How the encoder works

Rotary encoder contains a disc of evenly spaced **contact zones** that rotate with the shaft. Contact zones are connected to the **common pin**. When the disk starts rotating, the pins also start making contact with the common pin and the two square wave otput signals are created accordingly. Any of the two outputs can be used to determine the rotated position by counting the pulses, but to determine the direction of rotation both signals need to be considered. Output signals are **displaced at 90 degrees out of phase** from each other.

<CenteredImage src="/img/rotary-encoder/incremental_encoder.gif" alt="Conceptual drawing of a rotary incremental encoder" caption="Conceptual drawing of a rotary incremental encoder" width="400px" />

<CenteredImage src="/img/rotary-encoder/Quadrature_Diagram.svg" alt="Conceptual drawing of output signals" caption="Conceptual drawing of output signals" width="400px" />

---

## I2C communication - Qwiic

Qwiic versions of the product use onboard ATTINY404 MCU to implement I2C communication. Breakout board perates with a default I2C address of **0x30**  but can be changed with onboard switches,to change breakout board's address, check the [**Address selection**](/documentation/hall-effect-sensor/hardware#address-selection/). When detected, ATTINY404 recives data from sensor and passes it to the main MCU using I2C data line. To check in detail how to ATTINY404 is preprogrammed, check [**firmware github page**](https://github.com/SolderedElectronics/Soldered-Hall-Effect-Sensor-Arduino-Library/tree/dev/extras/attiny_firmware).

