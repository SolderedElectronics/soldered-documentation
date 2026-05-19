---
slug: /ws2812-grid/arduino/geting-started 
title: Getting started
id: ws2812-grid-arduino-1 
hide_title: False
---

## Arduino library

To install the Arduino library, you can use the **Arduino library manager** or download it from the GitHub repository:

<QuickLink
  title="[LIBRARY_NAME]"
  description="Arduino library for the Soldered Smart LED WS2812B Grid 8×8."
  url="[LIBRARY_URL]"
/>

<InfoBox>

**First time Arduino user?** For a detailed tutorial on how to get started with Arduino, see this section of our docs:

<QuickLink
  title="Getting started with Arduino"
  description="A full, comprehensive tutorial on how to fully set up and upload code for the first time on an Arduino board, from scratch!"
  url="/arduino/quick-start-guide"
/>

</InfoBox>

---

## Connections

The board exposes three signals on its header pins: **VCC**, **GND**, and **DIN** (data in). Below is an example connection for **Nula DeepSleep**. These pins are used in all examples throughout this documentation.

| **Nula DeepSleep**       | **WS2812B Grid** |
| ------------------------ | ---------------- |
| IO5                      | DIN              |
| 5V                       | VCC              |
| GND                      | GND              |

[Dodati sliku konekcije]

---

## Chaining multiple grids

The board also exposes a **DOUT** header pin. To chain two or more grids together, connect the first board's DOUT to the second board's DIN, and pass the same VCC and GND rails to all boards. Set the total grid width or height in the `WS2812Grid` constructor to match your physical arrangement.
