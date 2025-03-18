---
slug: /logic-level-converter/how-it-works 
title: How it works
id: logic-level-converter-how-it-works 
hide_title: False
---

The Logic Level Converter Board by [**Soldered**](https://soldered.com/product/logic-level-converter-board/) enables safe voltage level shifting between 3.3V and 5V logic systems, facilitating communication between devices with differing voltage requirements. Using **MOSFETs** for **bidirectional signal conversion**, the board supports multiple communication protocols, including **I2C**, **SPI**, and **UART**.

<CenteredImage src="/img/logic-level-converter/llc_howitworks.png" alt="llc_howitworks" caption="Logic Level Converter board" width="500px" />

---

## MOSFET logic level shift

MOSFET logic level shifting is an efficient method to safely translate signals between devices with different voltage levels. It uses MOSFETs to allow signals to pass **from high-voltage systems** (e.g., 5V) to **low-voltage systems** (e.g., 3.3V) while ensuring the **safety of the low-voltage components**.

<CenteredImage src="/img/logic-level-converter/llc_mosfet.png" alt="llc_mosfet" caption="MOSFET level converter" width="500px" />

<InfoBox>The use of **MOSFETs** for logic level shifting ensures minimal power consumption and reliable signal translation, especially in bidirectional communication scenarios. </InfoBox>

MOSFETs operate by switching the signal voltage between the two levels, with the gate controlling the switch. A typical setup uses an N-channel MOSFET with pull-up resistors to allow both low-to-high and high-to-low signal translation.

**Enhancing** and **depleting** modes refer to how MOSFETs operate based on the voltage applied to the gate. In **enhancement mode**, a positive voltage at the gate creates a conductive channel between the source and drain, **allowing current to flow**. In **depletion mode**, the gate voltage depletes the channel, **reducing** or **stopping current flow**.

<CenteredImage src="/img/logic-level-converter/llc_enhance_deplete.png" alt="llc_enhance_deplete" caption="N-CHANNEL MOSFET Symbols" width="700px" />

<InfoBox>An **N-channel MOSFET** is a type of transistor that uses a negative charge to control current flow.</InfoBox>

MOSFET logic level shifting is commonly used for protocols like **I2C**, **SPI**, and **UART**, where bidirectional communication is needed. The I2C bus, for example, requires a safe voltage translation in both directions to prevent damage to the low-voltage devices.

<InfoBox>MOSFET logic level shifting allows for **safe communication** between devices with differing voltage levels, enabling **5V** and **3.3V** systems to interface without risk. </InfoBox>

<CenteredImage src="/img/logic-level-converter/llc_piduino.png" alt="llc_piduino" caption="Bidirectional Logic Level Converter usage example" width="500px" />

---

## How to connect it?

To use the MOSFET logic level converter, follow these steps:

- **Connect Power**:
   - Connect HVCC to the high-voltage power source (e.g., 5V) and LVCC to the low-voltage source (e.g., 3.3V).
   - Connect GND to the ground of both the high and low-voltage systems.
- **Wiring the Signals**:
  - Connect the HV1-HV4 pins to the high-voltage signal lines from your device (e.g., 5V microcontroller).
  - Connect the LV1-LV4 pins to the low-voltage signal lines (e.g., 3.3V sensor). 
- **Verify Connections**: 
   - Ensure the correct orientation and check that each signal is connected to the proper high or low-voltage side.

---

## Connection example

Since the SH21 sensor works at a 3.3V voltage, and Dasduino works at 5V, for connecting the sensor to Dasduino, we must use the Logic Level Converter Module that lowers these 5V to 3.3V as well as on all pins (VDD, SDA, SCL) and therefore ensures safe operation with the sensor.

<CenteredImage src="/img/logic-level-converter/llc_connecting.png" alt="llc_connecting" caption="Connecting the SHT21 with Dasduino using the Logic Level Converter" width="500px" />

> To connect the **Dasduino Connect controller** with the **SHT21 sensor** using the **logic level converter**:
> - Supply **5V** to the **HVCC** pin and **GND** to ground.
> - Connect **3.3V** to the **LVCC** pin and **GND** to the ground for the **Dasduino**.
> - Wire **SDA** and **SCL** signals from the sensor to the **A side**, and from the **B side** to the controller for communication.
