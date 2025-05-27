---
slug: /tcrt5000/how-it-works
title: "Obstacle sensor TCRT5000 \u2013 How it works"
id: tcrt5000-how-it-works
hide_title: false
---
This board utilizes **TCRT5000 infrared reflective sensor** by [**Vishay**](https://www.digikey.gr/en/products/detail/vishay-semiconductor-opto-division/TCRT5000/1681167) and * to detect color and objects. This board also includes additional features to make it easier to use. It adds a *LM393 Voltage comparator** by [**Texas Instruments**](https://eu.mouser.com/ProductDetail/Texas-Instruments/LM393M-NOPB?qs=QbsRYf82W3GpBNun7wKZlw%3D%3D&utm_id=20109199385&utm_source=google&utm_medium=cpc&utm_marketing_tactic=emeacorp&gad_source=1&gbraid=0AAAAADn_wf2fKvpBFkLrBUUl8dO2RQg0h&gclid=Cj0KCQjwy46_BhDOARIsAIvmcwMsdd1u6kOcRmTTIs-3gcSdmuLKAzoQu5R-yEysSeXZ3OPvm47trKQaAineEALw_wcB) and a **potentiometer** to adjust its sensitivity.

<CenteredImage src="/img/tcrt5000/tcrt5000_onboard_highlighted.jpg" alt="TCRT5000 on board" caption="TCRT5000 on board" width="400px" />

<CenteredImage src="/img/tcrt5000/lm393_onboard_highlighted.jpg" alt="LM393 on board" caption="LM393 on board" width="400px" />

<CenteredImage src="/img/tcrt5000/potentiometer_highlighted.jpg" alt="Potentiometer on board" caption="Potentiometer on board" width="400px" />

## Datasheet
For an in-depth look at tehnical specifications, refer to the official TCRT5000 and LM393 Datasheets:

<QuickLink  
  title="TCRT5000 Datasheet"  
  description="Detailed technical documentation for the TCRT5000 infrared sensor"  
  url="https://soldered.com/productdata/2022/03/Soldered_TCRT5000_datasheet.pdf"  
/>  

<QuickLink  
  title="LM393 Datasheet"  
  description="Detailed technical documentation for the MCP4018 Voltage comparator"  
  url="https://docs.rs-online.com/943a/0900766b8170d70c.pdf"  
/>  

---

## How the sensor works

The sensor itself works by transmitting infrared light from the LED and registering any reflected light on its photoresistor, this alters the flow of current between its emiter and collctor according to the level of light it receives. 

<CenteredImage src="/img/tcrt5000/how_the_sensor_works.jpg" alt="How the sensor works" caption="How the sensor works" width="400px" />