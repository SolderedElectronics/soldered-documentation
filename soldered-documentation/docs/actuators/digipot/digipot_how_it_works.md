---
slug: /digipot/how-it-works
title: "Digital potentiometer \u2013 How it works"
id: digipot-how-it-works
hide_title: false
---
The **Digital potentiometer** is a device that uses digital communication to set its resistance instead of a physical rotationg part. This module is based on MCP4018 integrated chip by [**Microchip**](https://www.microchip.com/en-us/product/mcp4018) which has a total of 128 steps between 0 and max ressitance values.

<CenteredImage src="/img/digipot/MCP4018_highlighted.jpg" alt="MCP4018 on board" caption="MCP4018 on board" width="400px" />

## Datasheet

For an in-depth look at technical specifications, refer to the official MCP4018 Datasheet:  

<QuickLink  
  title="MCP4018 Datasheet"  
  description="Detailed technical documentation for the MCP4018 digital potentiometer"  
  url="https://soldered.com/productdata/2020/05/Soldered_MCP4018_datasheet.pdf"  
/>  

---

## How the digipot works
Unlike their analog counterparts, digital potentiometers utilize **electronic signals** to alter resistance levels precisely. Within it is a **network of resistive elements and switches**, resistive elements are devided into sections that are controlled by its corresponding switch. By togglin these switches on or off, the effective resistance between the terminals can be changed.

<CenteredImage src="/img/digipot/Digital_Potentiometer_Principle.svg" alt="Digital potentiometer principle using a resistor ladder" caption="Digital potentiometer principle using a resistor ladder" width="400px" />


