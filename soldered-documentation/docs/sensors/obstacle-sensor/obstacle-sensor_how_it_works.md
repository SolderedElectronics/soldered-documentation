---
slug: /obstacle-sensor/how-it-works
title: "Obstacle Sensor \u2013 How it works"
id: obstacle-sensor-how-it-works
hide_title: false
---
This board utilizes **TCRT5000 infrared reflective sensor** by [**Vishay**](https://www.digikey.gr/en/products/detail/vishay-semiconductor-opto-division/TCRT5000/1681167) to detect the presence of objects or colors. To make it easier to use, this board employs a preprogrammed **ATTiny404 IC** for binary output and **I2C communication**.

<CenteredImage src="/img/obstacle-sensor/333004_TCRT5000_highlighted.jpg" alt="TCRT5000 IR sensor on board" caption="TCRT5000 IR sensor on board" width="400px" />

<CenteredImage src="/img/obstacle-sensor/333004_ATTINY404_highlighted.jpg" alt="ATTiny404 IC on board" caption="ATTiny404 IC on board" width="400px" />

---

## Datasheet

For an in-depth look at technical specifications, refer to the official TCRT5000 Datasheet:

<QuickLink  
  title="TCRT5000 Datasheet"  
  description="Detailed technical documentation for the TCRT5000 infrared sensor"  
  url="https://soldered.com/productdata/2022/03/Soldered_TCRT5000_datasheet.pdf"  
/> 

---

## How the sensor works
The sensor itself works by transmitting infrared light from the LED and registering any reflected light on its photoresistor. This alters the flow of current between its emitter and collector according to the level of light it receives.

<CenteredImage src="/img/obstacle-sensor/how_the_sensor_works.jpg" alt="How the TCRT5000 sensor works" caption="How the TCRT5000 sensor works" width="400px" />

---

## I2C communication - Qwiic
This board uses an onboard ATTiny404 MCU to implement I2C communication. The board operates on a default I2C address of **0x30**, but it can be changed using onboard switches. To change the board's address, check the [**Address selection**](/documentation/obstacle-sensor/hardware#address-selection/). When detected, ATTiny404 receives data from the sensor and passes it to the main MCU using the I2C data line. To check in detail how the ATTiny404 is preprogrammed, check the [**firmware GitHub page**](https://github.com/SolderedElectronics/Soldered-Obstacle-Sensor-Arduino-Library/tree/dev/extras/attiny_firmware).