---
slug: /ssd1306/how-it-works 
title: Ssd1306 – How it works
id: ssd1306-how-it-works 
hide_title: False
---  

On this page, we will explain how an OLED display actually functions.

---

## Overview
**OLEDs** are organic LEDs, which means that their key building blocks are organic (i.e., carbon-based) materials. Unlike LEDs, which are point light sources, OLEDs are manufactured as sheets that act as diffuse-area light sources. **OLED technology** is developing rapidly, and there are a handful of product offerings with efficacy, lifetime, and color quality specifications comparable to their LED counterparts. However, OLEDs are still several years away from widespread use as a source of general illumination, largely due to their high cost.

---

## Datasheet

For an in-depth look at technical specifications, refer to the official SSD1306 Datasheet:  

<QuickLink  
  title="SSD1306 Datasheet"  
  description="Detailed technical documentation for the SSD1306 display"  
  url="soldered.com/productdata/2022/03/Soldered_SSD1315_datasheet.pdf"  
/>  

---

## Structure
An OLED is a solid-state device consisting of a thin, carbon-based **semiconductor layer** that emits light when electricity is applied by adjacent electrodes. In order for light to escape from the device, at least one of the electrodes must be transparent. The intensity of the light emitted is controlled by the amount of electric current applied by the electrodes, and the light's color is determined by the type of emissive material used. To create white light, most devices use red, green, and blue emitters that can be arranged in several configurations.

<CenteredImage src="/img/ssd1306/333100_structure.jpg" alt="Structure of OLED display" caption="Structure of OLED display" width="500px" />

---

## SSD1306

**SSD1306** is a single-chip **CMOS OLED/PLED driver** with a controller for an organic/polymer light-emitting diode dot-matrix graphic display system. It consists of 128 segments and 64 commons. 

The SSD1306 displays data directly from its internal 128 x 64-bit **Graphic Display Data RAM (GDDRAM)**. Data/commands are sent from a general MCU through the hardware-selectable **I2C Interface**.


---

## I2C communication

The SSD1306 uses the I2C protocol to communicate with a microcontroller. It operates with an I2C address of **0x3C** (it can also operate with an address of **0x3D** when shorting the **JP6** jumper—see the jumper details [**here**](/ssd1306/hardware#jumper-details)).