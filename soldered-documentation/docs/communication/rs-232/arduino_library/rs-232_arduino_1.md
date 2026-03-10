---
slug: /rs-232/arduino/geting-started
title: Rs 232 - Getting started
sidebar_label: Getting started
id: rs-232-arduino-1
hide_title: false
---

## Arduino library

To test the Arduino, you can use the SoftwareSerial/HardwareSerial librarys which dont need to be downloaded since they are built into the device. Since the device requires no additional coding, this example is enough to showcase it.

<InfoBox>

**First time Arduino user?** For a detailed tutorial on how to get started with Arduino, see this section of our docs:

<QuickLink  
  title="Getting started with Arduino"  
  description="A full, comprehensive tutorial on how to fully set up and upload code for the first time on an Arduino board, from scratch!"  
  url="/documentation/arduino/quick-start-guide"  
/>  

</InfoBox>

---

## Connections

Below is an example connection diagram for **Dasduino CONNECTPLUS** and the **RS-232 Transceiver Breakout Board**. These pins will be used in the examples throughout this documentation.

| **Dasduino CONNECTPLUS** | **RS-232 Breakout Board** |
| ------------------------ | ------------------------- |
| IO13 (TX) (user choice)  | DIN1 (TTL Transmit)       |
| IO14 (RX) (user choice)  | ROUT1 (TTL Receive)       |
| 5V                       | 5V                        |
| GND                      | GND                       |

<InfoBox>

If you prefer, you can use a second RS-232 channel for additional communication:

| **Dasduino CONNECTPLUS** | **RS-232 Breakout Board** |
| ------------------------ | ------------------------- |
| IO27 (TX) (user choice)  | DIN2 (TTL Transmit)       |
| IO26 (RX)  (user choice) | ROUT2 (TTL Receive)       |
| 5V                       | 5V                        |
| GND                      | GND                       |

</InfoBox>