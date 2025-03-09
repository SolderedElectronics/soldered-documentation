---
slug: /qwiic 
title: Qwiic (formerly easyC)
id: qwiic
hide_title: False
pagination_next: null
pagination_prev: null
---

## Overview

<CenteredImage src="/img/easyc-about.png" alt="Qwiic (formerly easyC demonstration)" width="350px" />

**Qwiic** is a **solder-free, plug-and-play connection system** designed for **I2C communication** between microcontroller boards, sensors, and actuators. With Qwiic, you can **focus on coding and prototyping** without dealing with messy wiring or soldering. 
- You can **chain multiple devices together** without extra wiring. This allows for **efficient expansion** of projects, such as IoT-enabled weather stations.  
- The **polarized connectors** prevent incorrect connections, so you never mix up **SDA and SCL lines** or accidentally reverse a connection.  
- Since Qwiic/easyC is based on **I2C**, multiple sensors and modules can be **connected in parallel** to a single microcontroller, simplifying wiring for complex projects.  
- Works with **any board that supports I2C** and has a Qwiic connector (all Dasduino boards). If your board **doesn’t have a Qwiic connector**, you can use an **adapter** to convert standard pin headers into a Qwiic cable.   

---

## Name change

<InfoBox>**EasyC was our original name for our connector system, but we are retiring it in favor of Qwiic**. Functionally, easyC and Qwiic are the same. Both use the **JST-SH 4-pin connector (1.00mm pitch)** and are fully compatible with **SparkFun Qwiic and Adafruit STEMMA QT**.</InfoBox>

<InfoBox>Find the mechanical drawing of the female connector [**here**](https://soldered.com/productdata/2018/07/Soldered_A1001-SR04_datasheet.pdf) and the male connector on the cable [**here**](https://soldered.com/productdata/2018/07/Soldered_A1001-H04_datasheet.pdf).</InfoBox>

The **4-pin EasyC/Qwiic cable** follows this **standard color coding**:  

| Color      | Function            |
| ---------- | ------------------- |
| **Black**  | **GND** (Ground)    |
| **Red**    | **3.3V** (Power)    |
| **Blue**   | **SDA** (I2C Data)  |
| **Yellow** | **SCL** (I2C Clock) |

---

## Related video

<YouTubeEmbed videoId="fkst0veJaEw" width={520} />