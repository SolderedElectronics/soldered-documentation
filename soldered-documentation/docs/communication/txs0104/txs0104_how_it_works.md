---
slug: /txs0104/how-it-works 
title: How it works
id: txs0104-how-it-works 
hide_title: False
---  

The Logic Level Converter I2C TXS0104 Board by [**Soldered**](https://soldered.com/product/logic-level-converter-i2c-txs0104-breakout/) is specialized for signal conversion for I2C communication and enables safe voltage level shifting between 3.3V and 5V logic systems, facilitating communication between devices with differing voltage requirements.

<CenteredImage src="/img/txs0104/txsonboard.png" alt="howitworks" caption="TXS0104 on the Logic Level Converter board" width="500px" />

---

## How it works

The **TXS0104** is a **directionless voltage-level translator** designed to convert logic signals between different voltage levels. The **A port** supports input/output voltages from **1.65V to 3.6V**, while the B port handles voltages from **2.3V to 5.5V**. Built on a pass-gate architecture, the device incorporates **edge-rate accelerators** (one-shots) to enhance data transfer speeds. It also features **integrated 10-kΩ pull-up resistors**, commonly used in open-drain configurations, eliminating the need for external resistors. Although primarily intended for open-drain applications, the TXS0104E can also be used to translate **push-pull CMOS logic outputs**.

<CenteredImage src="/img/txs0104/functionaldiagram.png" alt="txs" caption="Functional Block Diagram" width="600px" />

---

## Enable and Disable

The TXB0104 has an OE input that is used to disable the device by setting OE = low, which places all I/Os in
the high-impedance (Hi-Z) state. The disable time (tdis) indicates the delay between when OE goes low and
when the outputs acutally get disabled (Hi-Z). The enable time (ten) indicates the amount of time the user must
allow for the one-shot circuitry to become operational after OE is taken high.

---

## How to connect it?

- **Connect Power**:
   - Connect HVCC to the high-voltage power source (e.g., 5V) and LVCC to the low-voltage source (e.g., 3.3V).
   - Connect GND to the ground of both the high and low-voltage systems.
- **Wiring the Signals**:
  - Connect the B1-B4 pins to the high-voltage signal lines from your device (e.g., 5V microcontroller).
  - Connect the A1-A4 pins to the low-voltage signal lines (e.g., 3.3V sensor). 
- **Verify Connections**: 
   - Ensure the correct orientation and check that each signal is connected to the proper high or low-voltage side.
