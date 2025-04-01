---
slug: /rotary-encoder/how-it-works 
title: How it works
id: rotary-encoder-how-it-works 
hide_title: False
---  

A rotary encoder is a **positional sensor** used for determining the **angular position of a rotating shaft** and generates an **electrical output signal** related to that position. The breakout board uses the **EC11E1534408** rotary encoder by [ALPS](https://eu.mouser.com/ProductDetail/Alps-Alpine/EC11E1534408?qs=PoKhxlfUXjJk5yy1jIb28A%3D%3D&srsltid=AfmBOoqWdrLCWfukAif74HADQ5xgEWlmpqFwtwPZqIAtxNFYmnJB0LJY). When using a Qwiic version, you are essentially communicating with an onboard ATTINY404 MCU via **I2C communication**.

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

A rotary encoder contains a disc of evenly spaced **contact zones** that rotate with the shaft. The contact zones are connected to the **common pin**. When the disk starts rotating, the pins begin making contact with the common pin, thereby creating two square wave output signals. Either of the two outputs can be used to determine the rotated position by counting the pulses, but to determine the direction of rotation, both signals need to be considered. The output signals are **displaced at 90 degrees out of phase** with each other.

<CenteredImage src="/img/rotary-encoder/incremental_encoder.gif" alt="Conceptual drawing of a rotary incremental encoder" caption="Conceptual drawing of a rotary incremental encoder" width="400px" />

<CenteredImage src="/img/rotary-encoder/Quadrature_Diagram.svg" alt="Conceptual drawing of output signals" caption="Conceptual drawing of output signals" width="400px" />

---

## I2C communication - Qwiic

Qwiic versions of the product use an onboard ATTINY404 MCU to implement I2C communication. The breakout board operates with a default I2C address of **0x30**, but this can be changed with onboard switches. To change the breakout board's address, check the [**Address selection**](/documentation/hall-effect-sensor/hardware#address-selection). When detected, the ATTINY404 receives data from the sensor and passes it to the main MCU using the I2C data line. For detailed information on how the ATTINY404 is preprogrammed, check the [**firmware GitHub page**](https://github.com/SolderedElectronics/Soldered-Hall-Effect-Sensor-Arduino-Library/tree/dev/extras/attiny_firmware).