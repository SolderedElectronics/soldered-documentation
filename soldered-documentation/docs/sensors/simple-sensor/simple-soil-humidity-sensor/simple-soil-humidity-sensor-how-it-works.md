---
slug: /simple-sensor/simple-soil-humidity-sensor/simple-soil-humidity-sensor-how-it-works
title: Simple Sensor - How it works
id: simple-soil-humidity-sensor-how-it-works
hide_title: false
---

Both the regular and Qwiic versions of the sensor use an external breakout board with 2 exposed nickle-plated prongs. The difference between them is the onboard **IC**, which processes the provided data. The regular version uses a simple **LM393 voltage comparator** by [**Texas Instruments**](https://eu.mouser.com/ProductDetail/Texas-Instruments/LM393M-NOPB?qs=QbsRYf82W3GpBNun7wKZlw%3D%3D&utm_id=20109199385&utm_source=google&utm_medium=cpc&utm_marketing_tactic=emeacorp&gad_source=1&gbraid=0AAAAADn_wf2fKvpBFkLrBUUl8dO2RQg0h&gclid=Cj0KCQjwy46_BhDOARIsAIvmcwMsdd1u6kOcRmTTIs-3gcSdmuLKAzoQu5R-yEysSeXZ3OPvm47trKQaAineEALw_wcB), while the Qwiic version uses an **ATTiny404 MCU** to process the data and implement **I2C communication**. 

<CenteredImage src="/img/simple-sensor/simple-soil-humidity-sensor/333040_ATTINY404_highlighted.jpg" alt="ATTiny404 MCU on board of Qwiic version" caption="ATTiny404 MCU on board of Qwiic version" width="400px" />

<CenteredImage src="/img/simple-sensor/simple-soil-humidity-sensor/333045_LM393_highlighted.jpg" alt="LM393 on board of regular version" caption="LM393 on board of regular version" width="400px" />

---

## DataSheet
For an in-depth look at technical specifications, refer to the official ATTiny404 / LM393 Datasheet:

<QuickLink  
  title="ATTiny404 Datasheet"  
  description="Detailed technical documentation for the LM393 Voltage Comparator."  
  url="https://docs.rs-online.com/943a/0900766b8170d70c.pdf"  
/>  
<QuickLink  
  title="LM393 Datasheet"  
  description="Detailed technical documentation for the ATTiny404 microcontroller."  
  url="https://ww1.microchip.com/downloads/en/devicedoc/50002687a.pdf"  
/> 

---

## How the sensor works
The soil humidity sensor uses an extarnal breakout board that contains two exposed nickle-plated prongs. As soil gets more humid, the resistance becomes smaller and the internal voltage between the prongs gets bigger. The sensor includes an IC to provide additional functionality and simplify its operation.

<CenteredImage src="/img/simple-sensor/simple-soil-humidity-sensor/Soil-Moisture-Sensor-Working.gif" alt="How the rain sensor works" caption="How the rain sensor works" width="400px" />

---

## I2C communication - Qwiic

Qwiic versions of the product use onboard ATTINY404 MCU to implement I2C communication. Breakout board operates with a default I2C address of **0x30**  but can be changed with onboard switches,to change breakout board's address, check the [**Address selection**](http://localhost:3000/documentation/simple-sensor/simple-soil-humidity-sensor/simple-soil-humidity-sensor-hardware#address-selection-for-qwiic-version). When detected, ATTINY404 recives data from sensor and passes it to the main MCU using I2C data line. To check in detail how to ATTINY404 is preprogrammed, check [**firmware github page**](https://github.com/SolderedElectronics/Soldered-Simple-Soil-Humidity-Sensor-Arduino-Library/blob/dev/extras/attiny_firmware/attiny_firmware.ino).