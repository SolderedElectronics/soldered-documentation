---
slug: /rs-485/arduino/geting-started
title: "RS-485 Transceiver \u2013 Arduino Getting Started"
id: rs-485-arduino-1
hide_title: false
---
## Arduino library

To test the **RS-485 Transceiver Breakout Board** with **Arduino**, you can use the **HardwareSerial** library, which is built into the Arduino IDE and does not require additional installation. Since RS-485 communication uses differential signals, this example is sufficient to showcase its functionality.

<InfoBox>
First time Arduino user? For a detailed tutorial on how to get started with Arduino, see this section of our docs:

<QuickLink title="Getting started with Arduino" description="A full, comprehensive tutorial on how to fully set up and upload code for the first time on an Arduino board, from scratch!" url="/documentation/arduino/quick-start-guide" />

</InfoBox>

---

## Connections

Below is an example connection diagram for **Dasduino CONNECTPLUS** and the **RS-485 Transceiver Breakout Board**. These pins will be used in the examples throughout this documentation.

| **Dasduino CONNECTPLUS** | **RS-485 Breakout Board** |
| ------------------------ | ------------------------- |
| IO13 (TX)(*User Choice)  | D (Driver Input)          |
| IO14 (RX)(*User Choice)  | R (Receiver Output)       |
| IO12 (DE)                | DE (Driver Enable)        |
| IO2 (NRE)                | NRE (Receiver Enable)     |
| 5V                       | VCC                       |
| GND                      | GND                       |
| A                        | RS-485 Bus Line A         |
| B                        | RS-485 Bus Line B         |
|                          |

<InfoBox>

If your RS-485 breakout board is at one end of the bus, **close jumper JP2** to enable the termination resistor. If it’s not at an endpoint, **leave JP2 open**.

</InfoBox>

<InfoBox>
If you prefer, you can use a second RS-485 channel for additional communication:

| **Dasduino CONNECTPLUS** | **RS-485 Breakout Board** |
| ------------------------ | ------------------------- |
| IO27 (TX)(*User Choice)  | D (Driver Input)          |
| IO26 (RX)(*User Choice)  | R (Receiver Output)       |
| IO25 (DE)                | DE (Driver Enable)        |
| IO24 (NRE)               | NRE (Receiver Enable)     |
| 5V                       | VCC                       |
| GND                      | GND                       |
| A                        | RS-485 Bus Line A         |
| B                        | RS-485 Bus Line B         |


</InfoBox>