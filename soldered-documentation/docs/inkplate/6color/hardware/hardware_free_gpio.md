---  
slug: /inkplate/6color/hardware/free-gpio  
title: Inkplate 6COLOR – Free GPIO pins  
sidebar_label: Free GPIO pins  
id: hardware-free-gpio  
---

Inkplate 6COLOR's onboard **ESP32 WROVER-E** has some pins reserved for internal use (for example, the connection to the e-paper display) and cannot be used for end-user applications. This page contains a list of the available GPIO pins that can be used for external applications.

If you don't need pin details and are just interested in the pins, here are the Inkplate 6COLOR pins that are **not connected to any external component**:
``ESP32: IO2, IO4, IO5, IO25, IO26``, ``GPIO EXPANDER: P0-0 to P1-7``

<CenteredImage src="/img/6color/free-gpio.webp" alt="Inkplate 6color free pins" caption="Inkplate 6color free pins" />

See the table below for pin functions and what each pin is connected to:

## Free pin table



| **PIN**      | **CONNECTED TO** | **FUNCTION**                                                               |
|--------------|------------------|----------------------------------------------------------------------------|
| TXD          | CH340            | UART transmit pin                                                          |
| RXD          | CH340            | UART receive pin                                                           |
| IO12         | SDCARD           | ADC2_CH5, TOUCH5, RTC_GPIO15, MTDI, HSPIQ, HS2_DATA2, SD_DATA2, EMAC_TXD3 |
| IO13         | SDCARD           | ADC2_CH4, TOUCH4, RTC_GPIO14, MTCK, HSPID, HS2_DATA3, SD_DATA3, EMAC_RX_ER |
| IO14         | SDCARD           | ADC2_CH6, TOUCH6, RTC_GPIO16, MTMS, HSPICLK, HS2_CLK, SD_CLK, EMAC_TXD2    |
| IO15         | JP6 [**Check jumper details**](/documentation/inkplate/6color/hardware/jumpers/#board-jumpers)             | ADC2_CH3, TOUCH3, MTDO, HSPICS0, RTC_GPIO13, HS2_CMD, SD_CMD, EMAC_RXD3    |
| IO34         | JP1 [**Check jumper details**](/documentation/inkplate/6color/hardware/jumpers/#board-jumpers)             | ADC1_CH6, RTC_GPIO4                                                        |
| IO35         | V_BAT            | ADC1_CH7, RTC_GPIO5                                                        |
| IO36         | WAKEUP BUTTON    | ADC1_CH0, RTC_GPIO0                                                        |
| IO39         | JP5 [**Check jumper details**](/documentation/inkplate/6color/hardware/jumpers/#board-jumpers)           | ADC1_CH3, RTC_GPIO3                                                        |
| IO2          | **FREE**         | ADC2_CH2, TOUCH2, RTC_GPIO12, HSPIWP, HS2_DATA0, SD_DATA0                  |
| IO4          | **FREE**         | ADC2_CH0, TOUCH0, RTC_GPIO10, HSPIHD, HS2_DATA1, SD_DATA1, EMAC_TX_ER      |
| IO5          | **FREE**         | VSPICS0, HS1_DATA6, EMAC_RX_CLK                                            |
| IO25         | **FREE**         | DAC_1, ADC2_CH8, RTC_GPIO6, EMAC_RXD0                                      |
| IO26         | **FREE**         | DAC_2, ADC2_CH9, RTC_GPIO7, EMAC_RXD1                                      |
| P0-0 TO P1-7 | **FREE**         | SD_DATA1, EMAC_TX_ER                                                       |
