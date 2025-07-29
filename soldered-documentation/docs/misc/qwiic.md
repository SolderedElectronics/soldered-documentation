---
slug: /qwiic
title: Qwiic - Qwiic (formerly easyC)
sidebar_label: Qwiic (formerly easyC)
id: qwiic
hide_title: false
pagination_next: null
pagination_prev: null
---

## What's Qwiic?

<CenteredImage src="/img/easyc-about.png" alt="Qwiic (formerly easyC) demonstration" width="350px" />

**Qwiic** is a **solder-free, plug-and-play connection system** designed for **I2C communication** between microcontroller boards, sensors, and actuators. With Qwiic, you can **focus on coding and prototyping** without dealing with messy wiring or soldering.  
- You can **chain multiple devices together** without extra wiring.  
- The **polarized connectors** prevent incorrect connections, so you **never** mix up VCC/GND or SDA/SCL.  
- Since Qwiic (formerly easyC) is based on **I2C**, multiple sensors and modules can be connected to a single microcontroller (daisy chain), simplifying wiring for complex projects.  
- Works with **any board that has a Qwiic connector**, including all Dasduino boards. If your board **doesn’t have a Qwiic connector**, you can use an **adapter** to convert standard pin headers into a Qwiic cable.  

---

## Name Change

<InfoBox>
**EasyC was our original name for this connector system, but we are now transitioning to Qwiic.** Functionally, easyC and Qwiic are the same. Both use the **JST-SH 4-pin connector (1.00mm pitch)** and are fully compatible with:
- **SparkFun Qwiic**
- **Soldered easyC**
- **Adafruit STEMMA QT**
</InfoBox>

---

## Hardware Details

The **4-pin Qwiic cable** follows this **standard color coding**:  

| Color      | Function             |
| ---------- | -------------------- |
| **Black**  | **GND** (Ground)     |
| **Red**    | **5V / 3V3** (Power) |
| **Blue**   | **SDA** (I2C Data)   |
| **Yellow** | **SCL** (I2C Clock)  |

<CenteredImage src="/img/easyc_connector_closeup.jpg" alt="Qwiic (formerly easyC) cable closeup" width="350px" caption="Qwiic connector closeup" />

<InfoBox>Find the mechanical drawing of the **female connector** [**here**](https://soldered.com/productdata/2018/07/Soldered_A1001-SR04_datasheet.pdf) and the **male connector** on the cable [**here**](https://soldered.com/productdata/2018/07/Soldered_A1001-H04_datasheet.pdf).</InfoBox>

<InfoBox>Qwiic-compatible boards by Soldered always have a **voltage regulator** onboard, which means you can connect **any Qwiic breakout to boards with 5V or 3V3 logic level!**</InfoBox>

---

## Related Video

<YouTubeEmbed videoId="fkst0veJaEw" width={520} />

---

## Related products

<QuickLink 
  title="Qwiic cable" 
  description="Qwiic (formerly easyC) compatible cables with connectors on both ends, available in various lengths."
  url="https://soldered.com/product/easyc-cable/"
  image="/img/333311.webp" 
/>  
<QuickLink 
  title="Qwiic adapter" 
  description="Qwiic (formerly easyC) adapter to turn a header pin connection into two female Qwiic ports."
  url="https://soldered.com/product/easyc-adapter/"
  image="/img/333015.jpg" 
/>  
<QuickLink 
  title="Qwiic Raspberry Pi adapter" 
  description="Qwiic (formerly easyC) adapter to extend Raspberry Pi's onboard header pins into a female Qwiic port."
  url="https://soldered.com/product/raspberry-pi-easyc-adapter/"
  image="/img/333019.jpg" 
/>  

