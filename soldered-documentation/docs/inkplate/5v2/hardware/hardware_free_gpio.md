---  
slug: /inkplate/5v2/hardware/free-gpio  
title: Inkplate 5v2 – Free GPIO pins  
sidebar_label: Free GPIO pins  
id: hardware-free-gpio      
---

Inkplate 5v2's onboard **ESP32 WROVER-E** has some pins reserved for internal use (for example, the connection to the e-paper display) and cannot be used for end-user applications. This page contains a list of the available GPIO pins that can be used for external applications.

If you don't need pin details and are just interested in the pins, here are the Inkplate 5v2 pins that are **not connected to any external component**:
``P1-3, P1-4, P1-5, P1-6, P1-7``. These are all on the GPIO expander peripheral.

<CenteredImage src="/img/5v2/free_pins.webp" alt="Inkplate 5v2 free pins" caption="Inkplate 5v2 free pins" />

See the table below for pin functions and what each pin is connected to:

## Free pin table

| **PIN** | **CONNECTED TO** | **FUNCTION**                                                          |
|---------|------------------|-----------------------------------------------------------------------|
| IO12    | SDCARD           | ADC, TOUCH5, RTC_GPIO15, MTDI, HSPIQ, HS2_DATA2, SD_DATA2, EMAC_TXD3  |
| IO13    | SDCARD           | ADC, TOUCH4, RTC_GPIO14, MTCK, HSPID, HS2_DATA3, SD_DATA3, EMAC_RX_ER |
| IO14    | SDCARD           | DC, TOUCH6, RTC_GPIO16, MTMS, HSPICLK, HS2_CLK, SD_CLK, EMAC_TXD2     |
| IO15    | JP3 [**Check jumper details**](/documentation/inkplate/5v2/hardware/jumpers/#board-jumpers)             | ADC, TOUCH3, MTDO, HSPICSO, RTC_GPIO13, HS2_CMD, SD_CMD, EMAC_RXD3    |
| IO34    | JP6 [**Check jumper details**](/documentation/inkplate/5v2/hardware/jumpers/#board-jumpers)             | ADC, RTC_GPIO4                                                        |
| IO35    | BATTERY          | ADC, RTC_GPIO4                                                        |
| IO36    | WAKEUP BUTTON    | ADC, RTC_GPIO0                                                        |
| IO39    | JP2 [**Check jumper details**](/documentation/inkplate/5v2/hardware/jumpers/#board-jumpers)             | ADC, RTC_GPIO0                                                        |
| P1-1    | JP8 [**Check jumper details**](/documentation/inkplate/5v2/hardware/jumpers/#board-jumpers)             | I/O                                                                   |
| P1-2    | JP7 [**Check jumper details**](/documentation/inkplate/5v2/hardware/jumpers/#board-jumpers)             | I/O                                                                   |
| P1-3    | **FREE**         | I/O                                                                   |
| P1-4    | **FREE**         | I/O                                                                   |
| P1-5    | **FREE**         | I/O                                                                   |
| P1-6    | **FREE**         | I/O                                                                   |
| P1-7    | **FREE**         | I/O                                                                   |