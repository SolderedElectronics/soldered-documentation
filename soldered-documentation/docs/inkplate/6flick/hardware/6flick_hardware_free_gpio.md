---
slug: /inkplate/6flick/hardware/free-gpio  
title: Inkplate 6FLICK – Free GPIO pins
sidebar_label: Free GPIO pins
id: hardware-free-gpio
---

Inkplate 6FLICK's onboard **ESP32 WROVER-E** has some pins reserved for internal use (for example, the connection to the e-paper display) and cannot be used for end-user applications. This page contains a list of the available GPIO pins that can be used for external applications.

If you don't need pin details and are just interested in the pins, here are the Inkplate 6FLICK pins that are **not connected to any external component**:
``ESP32: IO36, IO39``, ``GPIO EXPANDER 1: P1-7, P1-7``,  ``GPIO EXPANDER 2: P0-0 to P1-7``

<CenteredImage src="/img/inkplate_6_flick/free_gpio.jpg" alt="Inkplate 6FLICK free pins" caption="Inkplate 6FLICK free pins" />

See the table below for pin functions and what each pin is connected to:

## Free pin table



| **PIN**      | **CONNECTED TO** | **FUNCTION**                                                               |
|--------------|------------------|----------------------------------------------------------------------------|
| TXD          | CH340            | UART transmit pin                                                          |
| RXD          | CH340            | UART receive pin                                                           |
| IO12         | SDCARD           | ADC2_CH5, TOUCH5, RTC_GPIO15, MTDI, HSPIQ, HS2_DATA2, SD_DATA2, EMAC_TXD3 |
| IO13         | SDCARD           | ADC2_CH4, TOUCH4, RTC_GPIO14, MTCK, HSPID, HS2_DATA3, SD_DATA3, EMAC_RX_ER |
| IO14         | SDCARD           | ADC2_CH6, TOUCH6, RTC_GPIO16, MTMS, HSPICLK, HS2_CLK, SD_CLK, EMAC_TXD2    |
| IO15         | JP3 [**Check jumper details**](/documentation/inkplate/6flick/hardware/jumpers/#board-jumpers)             | ADC2_CH3, TOUCH3, MTDO, HSPICS0, RTC_GPIO13, HS2_CMD, SD_CMD, EMAC_RXD3    |
| IO34         | JP6 [**Check jumper details**](/documentation/inkplate/6flick/hardware/jumpers/#board-jumpers)             | ADC1_CH6, RTC_GPIO4                                                        |
| IO35         | V_BAT            | ADC1_CH7, RTC_GPIO5                                                        |
| IO36         | **FREE**    | ADC1_CH0, RTC_GPIO0                                                        |
| IO39         | **FREE** | ADC1_CH3, RTC_GPIO3                                                        |
|P1-1| JP7 [**Check jumper details**](/documentation/inkplate/6flick/hardware/jumpers/#board-jumpers)| SD_DATA1, EMAC_TX_ER |
|P1-5| JP8 [**Check jumper details**](/documentation/inkplate/6flick/hardware/jumpers/#board-jumpers)| SD_DATA1, EMAC_TX_ER |
|P1-6| **FREE** | SD_DATA1, EMAC_TX_ER |
|P1-7| **FREE** | SD_DATA1, EMAC_TX_ER |
| GPIO Expander 2: P0-0 - P1-7| **FREE** |SD_DATA1, EMAC_TX_ER |