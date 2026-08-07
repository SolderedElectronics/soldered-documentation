---  
slug: /inkplate/5v2/hardware/battery  
title: Inkplate 5V2 – Battery
sidebar_label: Battery
id: hardware-battery  
---  

<WarningBox>This page contains important information about using a battery with Inkplate 5V2. For safety reasons, **please read this page carefully!**</WarningBox>  

Inkplate 5V2 has a 2-pin, 2mm JST connector for a 3.7V Li-ion battery. The onboard charging IC, **MCP73831**, charges the battery whenever Inkplate is plugged into USB-C, and switches to battery power when you unplug it. A charging indicator LED shows the current charging status.  

<CenteredImage src="/img/5v2/battery.jpg" alt="Inkplate 5V2 battery JST connector" caption="JST battery connector" width="500px"/>  

<CenteredImage src="/img/5v2/led.jpg" alt="Inkplate 5V2 Onboard charging indicator LED" caption="Onboard charging indicator LED" width="500px"/>  

---  

<InfoBox>Getting the battery polarity right is crucial. Check the markings on the PCB before you connect a battery. With the JST connector oriented so the notch is at the top, the positive (+) terminal is on the left and the negative (-) terminal is on the right. </InfoBox>  

<CenteredImage src="/img/inkplate10/battery_polarity.png" alt="Battery polarity on Inkplate 5V2" caption="Battery polarity on Inkplate 5V2" width="500px"/>  

<WarningBox>**Battery polarity can vary!** Some Li-ion batteries have reversed polarity, and connecting a battery the wrong way around may permanently damage your Inkplate. Double-check before plugging it in.</WarningBox>  

---  

## Compatible batteries

Inkplate 5V2 works with 3.7V Li-ion batteries that have protection. If you bought the Inkplate 5V2 enclosure and battery kit, it includes a **[1200mAh 3.7V Li-ion battery](https://soldered.com/product/li-ion-battery-1200mah-3-7v/)** with a built-in protection circuit.  

<CenteredImage src="/img/inkplate_6_motion/li-ion-w-proteciton.webp" alt="3.7V li-ion battery with protection" caption="3.7V li-ion battery with protection" width="500px"/>  

Any of **[Soldered's 3.7V Li-ion batteries](https://soldered.com/categories/power-sources-batteries/batteries/lithium-batteries/)** will work as long as they fit inside your enclosure.  

<InfoBox>Due to shipping restrictions, we can't ship Li-ion batteries outside the EU. If you're in the US, take a look at [Adafruit's Li-ion battery stock](https://www.adafruit.com/category/574).</InfoBox>  

Check out our [battery documentation](/li-ion-battery/overview/) page.  

---  

## Charging IC (MCP73831)  

The **MCP73831** is a compact, single-cell Li-ion/Li-Polymer charge management controller. It regulates the charging process so charging over USB stays safe and efficient. The chip follows a constant-current / constant-voltage (CC/CV) charging profile, and switches to trickle charge as the battery nears full capacity.  

Key features:  

- Automatic charge termination when the battery is full  
- Overvoltage and overcurrent protection  
- Charge status indicator, connected to the onboard LED  

<InfoBox>For full technical details, refer to the MCP73831 datasheet:<QuickLink  
  title="MCP73831/2 Data Sheet"  
  description="Official data sheet for MCP73831/2 charger by Microchip"  
  url="https://ww1.microchip.com/downloads/en/DeviceDoc/MCP73831-Family-Data-Sheet-DS20001984H.pdf"  
/></InfoBox>