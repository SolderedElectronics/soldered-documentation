---
slug: /simple-sensor/simple-fire-sensor/simple-fire-sensor-how-it-works
title: How it works
id: simple-fire-sensor-how-it-works
hide_title: False
---

Both the regular and Qwiic versions of the sensor use a phototransistor to detect infrared radiation. The difference between them is the onboard **IC**, which processes the provided data. The regular version uses a simple **LM393 voltage comparator** by [**Texas Instruments**](https://eu.mouser.com/ProductDetail/Texas-Instruments/LM393M-NOPB?qs=QbsRYf82W3GpBNun7wKZlw%3D%3D&utm_id=20109199385&utm_source=google&utm_medium=cpc&utm_marketing_tactic=emeacorp&gad_source=1&gbraid=0AAAAADn_wf2fKvpBFkLrBUUl8dO2RQg0h&gclid=Cj0KCQjwy46_BhDOARIsAIvmcwMsdd1u6kOcRmTTIs-3gcSdmuLKAzoQu5R-yEysSeXZ3OPvm47trKQaAineEALw_wcB), while the Qwiic version uses an **ATTiny404 MCU** to process the data and implement **I2C communication**. 

<CenteredImage src="/img/simple-sensor/simple-fire-sensor/333042_ATTINY404_highlighted.jpg" alt="ATTiny404 MCU on board of Qwiic version" caption="ATTiny404 MCU on board of Qwiic version" width="400px" />

<CenteredImage src="/img/simple-sensor/simple-fire-sensor/333047_LM393_highlighted.jpg" alt="LM393 on board of regular version" caption="LM393 on board of regular version" width="400px" />

---

## Datasheet
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
The fire sensor operates on the principle of detecting infrared radiation emitted by an open flame. To detect that radiation, the sensor utilizes a photodiode (IR receiver) that changes its resistance, which in turn alters the internal voltage. The sensor includes an IC to provide additional functionality and simplify its operation.

---

## I2C communication - Qwiic

Qwiic versions of the product use onboard ATTINY404 MCU to implement I2C communication. Breakout board operates with a default I2C address of **0x30**  but can be changed with onboard switches,to change breakout board's address, check the [**Address selection**](/documentation/simple-sensor/simple-fire-sensor/simple-fire-sensor-hardware#address-selection-for-qwiic-version). When detected, ATTINY404 recives data from sensor and passes it to the main MCU using I2C data line. To check in detail how to ATTINY404 is preprogrammed, check [**firmware github page**](hhttps://github.com/SolderedElectronics/Soldered-Simple-Fire-Sensor-Arduino-library/blob/dev/extras/attiny_firmware/attiny_firmware.ino).
