---
slug: /ssd1306/how-it-works 
title: How it works
id: ssd1306-how-it-works 
hide_title: False
---  

On this page, we will be going over how an OLED display actually functions

## Overview
OLEDs are organic LEDs, which means that their key building blocks are organic (i.e., carbon-based) materials. Unlike LEDs, which are small-point light sources, OLEDs are made in sheets that are diffuse-area light sources. OLED technology is developing rapidly, and there are a handful of product offerings with efficacy, lifetime, and color quality specs that are comparable to their LED counterparts. However, OLEDs are still some years away from widespread use as a source of general illumination, largely due to their high cost.

## Structure
An OLED is a solid-state device consisting of a thin, carbon-based semiconductor layer that emits light when electricity is applied by adjacent electrodes. In order for light to escape from the device, at least one of the electrodes must be transparent. The intensity of the light emitted is controlled by the amount of electric current applied by the electrodes, and the light's color is determined by the type of emissive material used. To create white light, most devices use red, green, and blue emitters that can be arranged in several configurations

<CenteredImage src="/img/ssd1306/333100_structure.jpg" alt="Structure of OLED display" caption="Structure of OLED display" width="500px" />

## Pros & Cons

| Pros                                          | Cons                                                                                          |
| -------------------------------------------------------------- | --------------------------------------------------------------------- |
| The plastic, organic layers of an OLED are thinner, lighter and more flexible than the crystalline layers in an LED or LCD.| While red and green OLED films have longer lifetimes (46,000 to 230,000 hours), blue organics currently have much shorter lifetimes (up to around 14,000 hours) |
| OLEDs are brighter than LEDs. Because the organic layers of an OLED are much thinner than the corresponding inorganic crystal layers of an LED, the conductive and emissive layers of an OLED can be multi-layered| Manufacturing processes are currently expensive|
| OLEDs do not require backlighting and thus consume less electricity| Water can easily damage OLEDs|

## I2C communication  

The SSD1306 uses the I2C protocol to communicate with a microcontroller. It operates with an I2C address of **0x3C**.