---
slug: /nrf24l01/hardware 
title: Hardware details
id: nrf24l01-hardware 
hide_title: False
---

## Pinout
<CenteredImage src="/img/nfr24l01/pinout.jpg" alt="NRF24L01 adapter pinout diagram" caption="NRF24L01 adapter pinout diagram"/>

---

## Pin Details

| Pin Marking 	| Pin Name 	| Description 	|
|---	|---	|---	|
| **IQR** 	| Interrupt 	| Maskable interrupt pin. 	|
| **MISO** 	| SPI Communication 	| SPI Slave Data Input. 	|
| **MOSI** 	| SPI Communication 	| SPI Slave Data Output, with tri-state option. 	|
| **SCK** 	| Clock 	| SPI Clock. 	|
| **CSN** 	| Digital pin 	| SPI Chip Select. 	|
| **CE** 	| Digital pin 	| Chip Enable Activates RX or TX mode. 	|
| **3V3** 	| Power 	| Supply voltage. 	|
| **GND** 	| Ground 	| Common ground for power and signals. 	|

---

## Power Consumption
- **Idle modes:**
    - **Supply current in power down mode:** ~ 900 nA
    - **Supply current in standby-I mode:** ~ 22 uA
    - **Supply current in standby-II mode:** ~320 uA
- **Transmit modes:**
    - **Supply current at 0dBm output power:** 11.3 mA
    - **Supply current at -6dBm output power:** 9.0 mA
    - **Supply current at -12dBm output power:** 9.0 mA
    - **Supply current at -6dBm output power:** 9.0 mA