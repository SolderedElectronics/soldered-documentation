---
slug: /simple-sensor/simple-light-sensor/simple-light-sensor-how-it-works
title: How it works
id: simple-light-sensor-how-it-works
hide_title: False
---

Both the regular and Qwiic versions of the sensor use a LDR to measure the intensity of light. The difference between them is the onboard **IC** that processes the data provided by the LDR. The regular version uses a simple **LM393 voltage comparator** by [**Texas Instruments**](https://eu.mouser.com/ProductDetail/Texas-Instruments/LM393M-NOPB?qs=QbsRYf82W3GpBNun7wKZlw%3D%3D&utm_id=20109199385&utm_source=google&utm_medium=cpc&utm_marketing_tactic=emeacorp&gad_source=1&gbraid=0AAAAADn_wf2fKvpBFkLrBUUl8dO2RQg0h&gclid=Cj0KCQjwy46_BhDOARIsAIvmcwMsdd1u6kOcRmTTIs-3gcSdmuLKAzoQu5R-yEysSeXZ3OPvm47trKQaAineEALw_wcB), while the Qwiic version uses an **ATTiny404 MCU** to process the data and implement **I2C communication**. 

<CenteredImage src="/img/simple-sensor/simple-light-sensor/333041_ATTINY404_highlighted.jpg" alt="ATTiny404 MCU on board of Qwiic version" caption="ATTiny404 MCU on board of Qwiic version" width="400px" />

<CenteredImage src="/img/simple-sensor/simple-light-sensor/333046_LM393_highlighted.jpg" alt="LM393 on board of regular version" caption="LM393 on board of regular version" width="400px" />

---

## Datasheet
For an in-depth look at technical specifications, refer to the official LDR /   ATTiny404 / LM393 Datasheet:
<QuickLink  
  title="LDR Datasheet"  
  description="Detailed technical documentation for the Light dependent resistor."  
  url="https://components101.com/sites/default/files/component_datasheet/LDR%20Datasheet.pdf"  
/> 
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
The Light Dependent Resistor, or LDR, is a transducer (a device that converts one form of energy to another) that senses light intensity and converts it into electric current. The resistance of the LDR is inversely proportional to the light intensity to which it is exposed. That means that as the intensity increases, the resistance decreases.

<CenteredImage src="/img/simple-sensor/simple-light-sensor/light-sensor_graph.jpg" alt="LM393 on board of regular version" caption="LM393 on board of regular version" width="400px" />

---

## I2C communication - Qwiic

Qwiic versions of the product use onboard ATTINY404 MCU to implement I2C communication. Breakout board operates with a default I2C address of **0x30**  but can be changed with onboard switches,to change breakout board's address, check the [**Address selection**](/documentation/simple-sensor/simple-light-sensor/simple-light-sensor-hardware#address-selection-for-qwiic-version). When detected, ATTINY404 recives data from sensor and passes it to the main MCU using I2C data line. To check in detail how to ATTINY404 is preprogrammed, check [**firmware github page**](https://github.com/SolderedElectronics/Soldered-Digital-Light-Sensor-Arduino-Library/blob/dev/extras/attiny_firmware/attiny_firmware.ino).
