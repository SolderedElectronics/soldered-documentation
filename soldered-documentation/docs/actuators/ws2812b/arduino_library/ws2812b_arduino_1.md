---
slug: /ws2812b/arduino/geting-started 
title: Getting started
id: ws2812b-arduino-1 
hide_title: False
---

## Arduino library

To install the Arduino library, you can use the **Arduino library manager** or download it from the GitHub repository:
<QuickLink  
  title="Smart LEDs Arduino library"  
  description="Smart Leds Arduino library by Soldered"  
  url="https://github.com/SolderedElectronics/Soldered-WS2812-Smart-Leds-Arduino-Library/tree/main"  
/>  

<InfoBox>

**First time Arduino user?** For a detailed tutorial on how to get started wtih Arduino, see this section of our docs:

<QuickLink  
  title="Getting started with Arduino"  
  description="A full, comprehensive tutorial on how to fully set up and upload code for the first time on an Arduino board, from scratch!"  
  url="#"  
/>  

</InfoBox>

---

## Connections

Below is an example connection diagram for **Dasduino CONNECTPLUS**. These pins will be used in the examples throughout this documentation.

| **Dasduino CONNECT**  | **Smart LED WS2812B** |
| --------------------- | --------------------- |
| VCC (3.3V)            | VCC                   |
| GND                   | GND                   |
| IO2 (any digital pin) | DIN                   |

<InfoBox>The DOUT pin on a WS2812B LED strip is used to pass the data signal to the next LED or another strip in a daisy-chain configuration.</InfoBox>

---

## External Power Supply

When working with WS2812B LEDs, it’s important to provide adequate power to both the Arduino and the LED strip, especially if you have a large number of LEDs. The WS2812B strip can draw significant current, which may not be provided sufficiently by the Arduino board alone. Here's how to set up an external power supply for both components.

### Components Needed:

- **External 5V power supply** (Rated for the current draw of your LED strip, typically 60mA per LED at full brightness)
- **Power source wires** (For connecting the external power supply to the LED strip and Arduino)
- **Common ground** (To ensure the proper signal transmission between the Arduino and the WS2812B strip)

### Steps for Connecting:

1. **Powering the WS2812B LED Strip**:
   - Connect the **VCC** of the WS2812B LED strip to the **5V** output of the external power supply.
   - Connect the **GND** of the WS2812B LED strip to the **GND** terminal of the external power supply.
   - Be sure to choose a power supply that can provide enough current for the number of LEDs you're using. A typical 60-LED strip can draw up to 3.6A at full brightness.

2. **Powering the Arduino**:
   - Connect the **5V** of the Arduino to the **5V** terminal of the external power supply, or use the **Vin** pin if you're supplying a higher voltage (e.g., 7-12V).
   - Connect the **GND** of the Arduino to the **GND** terminal of the external power supply to ensure a common ground.

3. **Data Line Connection**:
   - Connect the **IO2** (or your chosen digital pin) on the Arduino to the **DIN** pin on the first LED of the WS2812B strip. This pin is used to send the control signal from the Arduino to the LEDs.
   - Ensure the data signal is at the appropriate voltage level (typically 5V) to avoid signal degradation.

4. **Important Notes**:
   - Always connect the ground of the Arduino, the external power supply, and the WS2812B strip together to create a common reference point for the data signal.
   - If using a high number of LEDs, consider adding a capacitor (e.g., 1000µF, 6.3V or higher) across the power and ground of the WS2812B strip to help stabilize the power supply.
   - A 330Ω resistor placed in series with the data line can help prevent spikes in the data signal and protect your components.
