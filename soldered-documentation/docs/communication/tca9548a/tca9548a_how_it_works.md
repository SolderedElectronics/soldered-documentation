---
slug: /tca9548a/how-it-works 
title: How it works
id: tca9548a-how-it-works 
hide_title: False
---  

The **I2C multiplexer breakout board** works and communicates thanks to the **TCA9548A** chip by [**Texas Instruments**](https://www.ti.com/product/TCA9548A?dcmp=dsproject&hqs=pf).
The **TCA9548A chip** enables communication between a microcontroller and up to **eight I2C devices** with identical addresses. This is achieved by multiplexing the I2C bus, allowing the microcontroller to communicate with one device at a time by selecting its corresponding channel.

<CenteredImage src="/img/tca9548a/chip.png" alt="TCA9548A chip on board" caption="TCA9548A chip on board" width="400px" />


---

## Datasheet

For an in-depth look at technical specifications, refer to the official TCA9548A  Datasheet:  

<QuickLink title="TCA9548A Datasheet" 
description="Detailed technical documentation for the TCA9548A chip" 
url="https://soldered.com/productdata/2022/03/Soldered_tca9548a_datasheet.pdf" /> 

---

## Multiplexing Functionality


The TCA9548A works as a switch for I2C communication. It has:

*   **One main I2C bus (SDA/SCL)** connected to the microcontroller.
*   **Eight independent channels (SDA0-SDA7 and SCL0-SCL7)** for connecting I2C devices.
    

Through **I2C commands** the TCA9548A simplifies complex I2C setups by enabling multiple devices with identical addresses to coexist on a single bus, you can activate a specific channel enabling communication with the device connected to that channel while isolating the others. This ensures no address conflicts between devices with identical I2C addresses.
The default I2C address of the TCA9548A is **0x70**, but it can be adjusted using the **A0**, **A1**, and **A2** pins where each combination is listed on the hardware details page. Up to eight multiplexers can be connected to a single bus, allowing communication with up to **64 devices**.

<CenteredImage src="/img/tca9548a/diagram.png" alt="Multiplexing diagram" caption="Multiplexing diagram" width="400px" />

---

## Interrupt Handling

The TCA9548A supports interrupt functionality:

*   Devices connected to individual channels can signal interrupts via their respective SDA lines.
*   The multiplexer passes these interrupts through its main SDA line, allowing the microcontroller to detect them.