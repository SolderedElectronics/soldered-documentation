---
slug: /digital-compass/hardware 
title: Digital Compass - Hardware details
sidebar_label: Hardware details
id: digital-compass-hardware 
hide_title: False
---

## Pinout

<CenteredImage src="/img/digital-compass/333392_pinout.png" alt="Digital Compass pinout image" />

Click [**here**](/img/digital-compass/333392_pinout.png) for a high-resolution image of the pinout.

## Pin details

| Pin Marking | Pin Name | Description |
| --- | --- | --- |
| **VCC** | Power | Supply voltage. |
| **GND** | Ground | Common ground for power and signals. |
| **SDA**     | Data     | I2C data line for communication. |                |
| **SCL**     | Clock    | I2C clock line for communication. |

---

## Qwiic
<CenteredImage src="/img/easyc_transparent.png" alt="EasyC/qwiic cable" width="550px" />
 
<InfoBox>This board is fully **Qwiic-compatible**! Just plug it into your board using a **Qwiic/easyC/STEMMA QT cable** and start coding!</InfoBox>

<QuickLink 
  title="Qwiic (formerly easyC) details and specifications" 
  description="Learn about hardware specifications, compatibility, and usage of the Qwiic connector." 
  url="/qwiic" 
/>

---

## Dimensions 
- **Board Dimensions:** 22 x 22mm(0.9 x 0.9 inch)
- **Header Pin Holes:** 1.5 mm
- **Screw Holes:** Designed for M3 screws (3.2 mm diameter)
- Soldered boards are LEGO compatible! 🧱

---

## Jumper Details
This board contains hardware jumpers. See below for their locations and functions:

<FlickityCarousel
    images={[
        { src: '/img/digital-compass/jp1_highlighted.jpg', alt: 'Digital Compass jumper 1', caption: 'JP1'},
        { src: '/img/digital-compass/jp2_highlighted.jpg', alt: 'Digital Compass jumper 2', caption: 'JP2'},
        { src: '/img/digital-compass/jp3_highlighted.jpg', alt: 'Digital Compass jumper 3', caption: 'JP3'},
        { src: '/img/digital-compass/jp4_highlighted.jpg', alt: 'Digital Compass jumper 4', caption: 'JP4'},
    ]}
/>