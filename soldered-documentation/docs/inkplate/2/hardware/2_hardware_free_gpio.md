---  
slug: /inkplate/2/hardware/free-gpio  
title: Inkplate 2 – Free GPIO pins  
sidebar_label: Free GPIO pins  
id: 2-hardware-free-gpio  
---

Inkplate 2's onboard **ESP32 WROVER-E** has some pins reserved for internal use (for example, the connection to the e-paper display) and cannot be used for end-user applications. This page contains a list of the available GPIO pins that can be used for external applications.

If you don't need pin details and are just interested in the pins, here are the Inkplate 2 pins that are **not connected to any external component**:
``IO2, IO5, IO12, IO13, IO14, IO15, IO25, IO26, IO34, IO35, IO36, IO39``

<CenteredImage src="/img/inkplate_2/free_pins.webp" alt="Inkplate 2 free pins" caption="Inkplate 2 free pins" />

See the table below for pin functions and what each pin is connected to:

## Free pin table

| **PIN** 	| **CONNECTED TO** 	| **FUNCTION** 	|
|---	|---	|---	|
| RXD 	| CH340 	| UART receive pin 	|
| TXR 	| CH340 	| UART transmit pin 	|
| IO0 	| EXTERNAL PULL-UP RESISTOR 	| ADC, RTC_GPIO, TOUCH, EMAC_TX_CLK 	|
| IO2 	| **FREE** 	| ADC, TOUCH, RTC_GPIO, HSPIWP, HS2_DATA0, SD_DATA0 	|
| IO4 	| **FREE** 	| ADC, TOUCH0, RTC_GPIO10, HSPIHD, HS2_DATA1, SD_DATA1, EMAC_TX_ER  	|
| IO5 	| **FREE** 	| VSPICSO, HS1_DATA6, EMAC_RX_CLK 	|
| IO12 	| **FREE** 	| ADC, TOUCH5, RTC_GPIO15, MTDI, HSPIQ, HS2_DATA2, SD_DATA2, EMAC_TXD3 	|
| IO13 	| **FREE** 	| ADC, TOUCH4, RTC_GPIO14, MTCK, HSPID, HS2_DATA3, SD_DATA3, EMAC_RX_ER 	|
| IO14 	| **FREE** 	| ADC, TOUCH6, RTC_GPIO16, MTMS, HSPICLK, HS2_CLK, SD_CLK, EMAC_TXD2 	|
| IO15 	| **FREE** 	| ADC, TOUCH3, MTDO, HSPICSO, RTC_GPIO13, HS2_CMD, SD_CMD, EMAC_RXD3 	|
| IO25 	| **FREE** 	| DAC, ADC, RTC_GPIO6, EMAC_RXD0 	|
| IO26 	| **FREE** 	| DAC, ADC, RTC_GPIO7, EMAC_RXD1 	|
| IO34 	| **FREE** 	| ADC, RTC_GPIO4 	|
| IO35 	| **FREE** 	| ADC, RTC_GPIO4 	|
| IO36 	| **FREE** 	| ADC, RTC_GPIO0 	|
| IO39 	| **FREE** 	| ADC, RTC_GPIO3 	|

