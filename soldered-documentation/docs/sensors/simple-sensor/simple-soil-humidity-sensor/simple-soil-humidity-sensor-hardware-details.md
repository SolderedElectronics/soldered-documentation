---
slug: /simple-sensor/simple-soil-humidity-sensor/simple-soil-humidity-sensor-hardware
title: Hardware details
id: simple-soil-humidity-sensor-hardware
hide_title: False
---

## Pinout

<CenteredImage src="/img/simple-sensor/simple-soil-humidity-sensor/333040_pinout.jpg" alt="Pinout" />
Click [**here**](/img/simple-sensor/simple-soil-humidity-sensor/333040_pinout.jpg) for a high resolution image of the pinout.

<ErrorBox>The pinout image for the regular board hasn't been generated yet! We're working on it!</ErrorBox>
---

# Pin details for regular version

| Pin Marking | Pin Name | Description                                     |
| ----------- | -------- | ----------------------------------------------- |
| **GND**     | Ground   | Common ground for power and signals.            |
| **A0**      | Data     | Analog output pin.                              |
| **D0**      | Data     | Digital output pin.                             |
| **VCC**     | Power    | Supply voltage                                  |


### Dimensions for regular version

- **Soil humidity sensor Dimensions:** 55 x 38 mm (2.2 x 1.5 inch)
- **Simple sensor Dimensions:** 22 × 22 mm (0.9 × 0.9 inch)  
- **Header Pin Holes:** 1.5 mm  
- **Screw Holes:** Designed for M3 screws (3.2 mm diameter)  
- Soldered boards are LEGO compatible! 🧱 

---

## Pin details for Qwiic version
For the Qwiic version, connection is achieved using a Qwiic connector.

<InfoBox> Qwiic versions also contain UPDI headers for preprogramming the onboard ATTINY404 MCU, they are used only for debugging purposes. </InfoBox>

### Dimensions for Qwiic version

- **Soil humidity sensor Dimensions:** 55 x 38 mm (2.2 x 1.5 inch)
- **Simple sensor Dimensions:** 38 × 22 mm (1.5 × 0.9 inch)  
- **Header Pin Holes:** 1.5 mm  
- **Screw Holes:** Designed for M3 screws (3.2 mm diameter)  
- Soldered boards are LEGO compatible! 🧱 

### Address selection for Qwiic version
This board contains hardware address switches. See below for instructions on how to change the breakout board's address.

<CenteredImage src="/img/simple-sensor/simple-soil-humidity-sensor/333040_add_highlighted.jpg" alt="Address Switches" />

| Address | SW3 | SW2 | SW1 |
|:---:|:---:|:---:|:---:|
| 0x30 | 0 | 0 | 0 |
| 0x31 | 0 | 0 | 1 |
| 0x32 | 0 | 1 | 0 |
| 0x33 | 0 | 1 | 1 |
| 0x34 | 1 | 0 | 0 |
| 0x35 | 1 | 0 | 1 |
| 0x36 | 1 | 1 | 0 |
| 0x37 | 1 | 1 | 1 |      

---