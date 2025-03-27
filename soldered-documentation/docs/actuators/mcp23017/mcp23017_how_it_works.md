---
slug: /mcp23017/how-it-works 
title: How it works
id: mcp23017-how-it-works 
hide_title: False
---  

The I/O expander board works and communicates thanks to the **MCP23017** chip by [**Microchip Technology**](https://www.microchip.com/)

<CenteredImage src="/img/mcp23017/chip.jpg" alt="TXB0104 chip on board" caption="TXB0104 chip on board" width="400px" />

---

## Datasheet

For an in-depth look at technical specifications, refer to the official MCP23017 Datasheet:  

<QuickLink  
  title="MCP23017 Datasheet"  
  description="Detailed technical documentation for the MCP23017 chip"  
  url="https://soldered.com/productdata/2022/03/Soldered_MCP23017_datasheet.pdf"  
/>  

---

## How it works

Along with the communication hardware, this chip we are using contains **two 8bit GPIO** (general purpose input output) modules, providing a total of 16 inputs/outputs. For each of them, we can determine whether it is an input or output. If the GPIO pin works as a digital input, then its functionality can simply be described as a voltage comparator. Depending on the IC’s power supply, the controller determines which voltage range is considered low, and which is at a high level. When we use GPIO as an input, we actually want to determine if some physical (analog signal) is above a certain voltage level, and according to that we assign the value “HIGH” or if it is below a certain level, we assign “LOW” value to it. Often, signals we want to determine as “HIGH” or “LOW” are not constant but their voltage can change. That is why this IC uses the so-called **Schmitt trigger**. This way, a security zone, into which the measured signal can enter without the controller recognizing it as wrong value, is ensured.

<CenteredImage src="/img/mcp23017/communication.webp" alt="Schmitt-trigger filtering" caption="Schmitt-trigger filtering" width="400px" />

If we have determined for some GPIO pin to work as a digital output, we have a simpler situation. Through communication, we get the information on whether to set the pin as “LOW” or “HIGH”. If we have received “LOW”, the output is connected to the ground, and if we have received “HIGH” the output is connected to the power supply. GPIO inputs have a built-in **pull-up resistor** so we can simply add push buttons and switches without additional hardware onto them.

 This IC has another interesting feature – **hardware interrupt**. It can be programmed so that the breakout sets an interrupt if it comes to a change on one or the other GPIO module, so, according to that, on the board we have two pins marked with **INTA** and **INTB**.