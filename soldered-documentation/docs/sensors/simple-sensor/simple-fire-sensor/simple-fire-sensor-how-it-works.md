---
slug: /simple-sensor/simple-fire-sensor/simple-fire-sensor-how-it-works
title: How it works
id: simple-fire-sensor-how-it-works
hide_title: False
---

Both the regular and Qwiic versions of the sensor use a phototransistor to detect infrared radiation. The difference between them is the onboard **IC**, which processes the provided data. The regular version uses a simple **LM393 voltage comparator** by [**Texas Instruments**](https://eu.mouser.com/ProductDetail/Texas-Instruments/LM393M-NOPB?qs=QbsRYf82W3GpBNun7wKZlw%3D%3D&utm_id=20109199385&utm_source=google&utm_medium=cpc&utm_marketing_tactic=emeacorp&gad_source=1&gbraid=0AAAAADn_wf2fKvpBFkLrBUUl8dO2RQg0h&gclid=Cj0KCQjwy46_BhDOARIsAIvmcwMsdd1u6kOcRmTTIs-3gcSdmuLKAzoQu5R-yEysSeXZ3OPvm47trKQaAineEALw_wcB), while the Qwiic version uses an **ATTiny404 MCU** to process the data and implement **I2C communication**. 

<CenteredImage src="/img/simple-sensor/simple-fire-sensor/333042_ATTINY404_highlighted.jpg" alt="ATTiny404 MCU on board of Qwiic version" caption="ATTiny404 MCU on board of Qwiic version" width="400px" />

<CenteredImage src="/img/tcrt5000/lm393_onboard_highlighted.jpg" alt="LM393 on board" caption="LM393 on board" width="400px" />