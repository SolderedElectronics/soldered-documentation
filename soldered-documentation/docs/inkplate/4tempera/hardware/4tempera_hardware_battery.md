---
slug: /inkplate/4tempera/hardware/battery
title: Inkplate 4TEMPERA – Battery
id: 4tempera-hardware-battery
hide_title: true
---

<SectionTitle title="Battery" backgroundImage="/img/inkplate_2/hardware.png" />

<WarningBox>Inkplate 4TEMPERA comes with a built-in battery, so skip this page unless you want to replace the battery.</WarningBox>  


<WarningBox>This page contains important information about using a battery with Inkplate 4TEMPERA. For safety reasons, **please read this page carefully!**</WarningBox>  

Inkplate 4TEMPERA includes a **2-pin 2mm JST connector**, allowing you to connect a **3.7V Li-ion battery**. The onboard charging IC, **MCP73831**, **automatically charges the battery** when the Inkplate is plugged into **USB-C** and switches to battery power when unplugged. A **charging indicator LED** provides real-time charging status.  

<CenteredImage src="/img/inkplate10/battery_jst_connector.png" alt="Inkplate 4TEMPERA battery JST connector" caption="JST battery connector" width="500px"/>  

<CenteredImage src="/img/inkplate10/CHRG_LED.jpg" alt="Inkplate 4TEMPERA Onboard charging indicator LED" caption="Onboard charging indicator LED" width="500px"/>  

---

<InfoBox>The **correct battery polarity** is crucial! Check the **markings on the PCB** before connecting a battery. When orienting the **JST connector with the notch at the top**, the **positive (+) terminal is on the left**, and the **negative (-) terminal is on the right**.</InfoBox>  

<CenteredImage src="/img/inkplate10/battery_polarity.png" alt="Battery polarity on Inkplate 4TEMPERA" caption="Battery polarity on Inkplate 4TEMPERA" width="500px"/>  

<WarningBox>**Battery polarity can vary!** Some Li-ion batteries have reversed polarity. **Connecting a battery with the wrong polarity may permanently damage your Inkplate!** Double-check before plugging it in.</WarningBox>  

---

## Compatible batteries

Inkplate 4TEMPERA is compatible with **3.7V Li-ion batteries with protection**. If you purchased the **Inkplate 4TEMPERA enclosure and battery kit**, it includes a **[3000mAh 3.7V Li-ion battery](https://soldered.com/product/li-ion-battery-3000mah-3-7v/)** with a built-in protection circuit.  

<CenteredImage src="/img/inkplate_6_motion/li-ion-w-proteciton.webp" alt="3.7V li-ion battery with protection" caption="3.7V li-ion battery with protection" width="500px"/>  

Any of **[Soldered’s 3.7V Li-ion batteries](https://soldered.com/categories/power-sources-batteries/batteries/lithium-batteries/)** will work as long as they fit inside your enclosure.  

<InfoBox>Due to shipping restrictions, **we cannot ship Li-ion batteries outside the EU**. If you're in the US, we recommend checking out [Adafruit's Li-ion battery stock](https://www.adafruit.com/category/574).</InfoBox>  

Check out our [battery documentation](/documentation/li-ion-battery/overview/) page.

---

## Charging IC (MCP73831)

The **MCP73831** is a compact, single-cell **Li-ion/Li-Polymer charge management controller** that regulates the **charging process**, ensuring safe and efficient charging via USB. The chip follows a **constant-current/constant-voltage (CC/CV) charging profile**, automatically switching to **trickle charge** when the battery nears full capacity.

Key features:  
- **Automatic charge termination** when the battery is full  
- **Overvoltage and overcurrent protection**  
- **Charge status indicator** (connected to the onboard LED)  

<InfoBox>For full technical details, refer to the **MCP73831 datasheet**:<QuickLink  
  title="MCP73831/2 Data Sheet"  
  description="Official data sheet for MCP73831/2 charger by Microchip"  
  url="https://ww1.microchip.com/downloads/en/DeviceDoc/MCP73831-Family-Data-Sheet-DS20001984H.pdf"  
/></InfoBox>