---
slug: /ws2812b/hardware 
title: Hardware details
id: ws2812b-hardware 
hide_title: False
---

## Pinout

<CenteredImage src="/img/ws2812b/pinout.jpg" alt="Pinout" />

Click [**here**](https://soldered.com/productdata/2022/03/Smart-LED-WS2812B-Stick10.png) for a high resolution image of the pinout.

### Pin details

| Pin Marking | Pin Name      | Description                                                          |
| ----------- | ------------- | -------------------------------------------------------------------- |
| **VCC**     | Power (+5V)   | Supplies power to the LED strip. Typically powered by a 5V source.   |
| **GND**     | Ground        | Common ground for both the power and signal.                         |
| **DIN**     | Data Input    | Input pin for receiving the data signal from the microcontroller.    |
| **DOUT**    | Data Output   | Output pin for passing the data signal to the next LED (in a chain). |

<InfoBox>The **DIN** pin is used to receive data from a microcontroller such as an Arduino or Raspberry Pi. The **DOUT** pin passes the data to the next LED in a daisy-chained setup.</InfoBox>
<WarningBox>Ensure a stable **5V** power supply to avoid damage to the LEDs!</WarningBox>

---

## Dimensions

- **LED Dimensions:** 5mm x 5mm (per LED chip)
- **LED Pitch (spacing between LEDs):** 10mm
- **Stick10 version**
   - **Screw Holes:** Designed for M3 screws (3.2 mm diameter)
   - **Dimensions**: 80 x 10 mm (3.15 x 0.4 inch)
- **Pixel version**
   - **Dimensions**: Diameter of 10mm (0.4 inch)
- **Ring7 version**
   - **Dimensions**: Diameter of 23mm (0.9 inch)
- **Ring12 version**
   - **Dimensions**: Outer diameter of 44mm (1.6 inch)
- **Ring24 version**
   - **Dimensions**: Outer diameter of 67mm (2.6 inch)
- Soldered boards are LEGO compatible! 🧱

---

## Power and Voltage Requirements

The **WS2812B** operates with a **5V** supply, which is typically delivered to the **VCC** pin. It can handle up to **60mA** per LED at full white (RGB) brightness, and power consumption will depend on the color and brightness settings used.

- **Operating Voltage:** 5V DC
- **Current Consumption:** Up to 60mA per LED at full brightness (white color)
- **Power Supply Recommendation:** Use a **5V DC power supply** that can provide sufficient current for the total number of LEDs in the chain.

<WarningBox>Ensure that the power supply can handle the total current draw. For example, a 1-meter strip with 30 LEDs at full brightness can draw up to 1.8A of current.</WarningBox>

---

## Control Protocol

The **WS2812B** LEDs use a **single-wire** control protocol for data transmission. The data is sent in a **serial protocol**, meaning that the data is transmitted one bit at a time, allowing for precise control of each individual LED in the strip.

- **Control Protocol:** Single-wire (data)
- **Microcontroller Compatibility:** Compatible with **Arduino**, **Raspberry Pi**, and other microcontrollers with a **PWM** output.
