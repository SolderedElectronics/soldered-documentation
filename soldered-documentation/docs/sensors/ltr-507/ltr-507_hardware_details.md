---
slug: /ltr-507/hardware 
title: Hardware details
id: ltr-507-hardware 
hide_title: False
---

## Pinout

<ErrorBox>The pinout image for this board hasn't been generated yet! We're working on it!</ErrorBox>

## Pin details

| Pin Marking | Pin Name | Description                                     |
| ----------- | -------- | ----------------------------------------------- |
| **VCC**     | Power    | Supply voltage (both 5V and 3V3 are supported). |
| **GND**     | Ground   | Common ground for power and signals.            |
| **SDA**     | Data     | I2C data line for communication.                |
| **SCL**     | Clock    | I2C clock line for communication.               |
| **VLED**    | Power    | Supply voltage.                                 |
| **INT**     | Control  | Interrupt signal (from LTR-507).                |

<InfoBox>This breakout board operates at **3.3V logic level**, but includes an onboard regulator for **5V compatibility** so it can be connected to both 3V3 and 5V logic boards!</InfoBox>

---

## Qwiic (formerly easyC)  

<CenteredImage src="/img/easyc_transparent.png" alt="EasyC/qwiic cable" width="550px" />
 
<InfoBox> This board is fully **Qwiic-compatible**! Just plug it into your board using a **Qwiic/easyC/STEMMA QT cable** and start coding! </InfoBox>

<QuickLink 
  title="Qwiic (formerly easyC) details and specifications" 
  description="Learn about hardware specifications, compatibility, and usage of the Qwiic connector." 
  url="/qwiic" 
/>

---

## Power Consumption

The LTR-507ALS-01 sensor is designed for low power consumption, making it suitable for battery-powered applications. 

- **Low-power mode**: 0.2mA
- **Active mode**: 2.3 mA

<InfoBox>Power consumption can be minimized by utilizing **interrupt** and **sleep** modes!</InfoBox>

- **Interrupt Mode**:
By using interrupts, the sensor can **wake up** from its low-power state only when a **significant change** in **ambient light** or **proximity** is detected. This allows the sensor to stay in a **low-power mode** most of the time and only activate when it’s required to take action, further **saving power**.

- **Sleep Mode**:
The sensor can be placed in a sleep mode where it completely shuts down its internal circuitry, **consuming minimal current**. This is useful for scenarios where the sensor doesn't need to be active for extended periods. You can program it to **wake up periodically** or only upon receiving an **external trigger**.

---

## Dimensions

- **Board Dimensions:** 38 × 22 mm (1.5 × 0.9 inch)  
- **Header Pin Holes:** 1.5 mm  
- **Screw Holes:** Designed for M3 screws (3.2 mm diameter)  
- Soldered boards are LEGO compatible! 🧱 

---

## Jumper Details

| Jumper  | Default State            | Function                                                                                                                                                                      |
| ------- | ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **JP1** | **NC** (Normally closed) | Connects **SDA/SCL pull-up resistors to 5V** for I2C communication.                                                                                                           |
| **JP2** | **NC** (Normally closed) | Connects **SDA/SCL pull-up resistors to 3.3V** for I2C communication.                                                                                                         |
| **JP3** | **NC** (Normally closed) | Disconnect to remove VLED power supply.                                                                                                                                          |
| **JP4** | **NC** (Normally closed) | When connected, the **voltage regulator is powered by 5V**, stepping it down to **3.3V for the IC**.                                                                          |
| **JP5** | **NO** (Normally open)   | When shorted, it **bypasses the voltage regulator**, allowing the board to be powered **directly from 3.3V** via headers. **Ensure JP4 is disconnected if JP5 is connected**. |

---
