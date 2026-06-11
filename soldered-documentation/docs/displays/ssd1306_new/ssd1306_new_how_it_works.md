---
slug: /ssd1306_new/how-it-works 
title: How it works
id: ssd1306_new-how-it-works 
hide_title: False
---  

---

## Overview

**OLEDs** are organic LEDs built from carbon-based materials. Unlike regular LEDs, which emit light from a point source, OLEDs are thin sheets that produce diffuse light across their surface.

---

## Datasheet

See the official SSD1306 datasheet for full technical specifications:

<QuickLink  
  title="SSD1306 Datasheet"  
  description="Detailed technical documentation for the SSD1306 display"  
  url="https://soldered.com/cdn/shop/files/Soldered_SSD1306_datasheet.pdf"  
/>  

---

## Structure

An OLED has a thin carbon-based **semiconductor layer** that emits light when current passes through adjacent electrodes. At least one electrode must be transparent for light to escape. The color of the emitted light depends on the emissive material. White-light OLEDs typically combine red, green, and blue emitters.

<WarningBox>Image coming soon.</WarningBox>

---

## SSD1306

The **SSD1306** is a single-chip **CMOS OLED/PLED driver** for dot-matrix graphic displays. It has 128 segments and 64 commons.

It reads display data directly from an internal 128x64-bit **Graphic Display Data RAM (GDDRAM)** and receives commands from a microcontroller over I2C.

---

## I2C communication

The SSD1306 communicates over I2C at address **0x3C** by default. Shorting the **JP6** jumper changes it to **0x3D** (see jumper details [**here**](/ssd1306_new/hardware#jumper-details)).
