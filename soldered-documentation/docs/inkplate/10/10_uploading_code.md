---
slug: /inkplate/10/uploading-code
title: Uploading code
id: 10-uploading-code
---

To upload your own sketch or an Arduino example to **Inkplate 10**, follow this brief guide. 

---

## 1. Connect Inkplate via USB and power it on 

Use the provided **USB-C cable** to connect Inkplate 10 to your computer. Ensure that the board is powered on by pressing the **POWER ON** button. The **blue power LED** will light up when properly connected.  

<CenteredImage src="/img/inkplate10/10_usb_connect.png" alt="Inkplate 10 onboard USB-C connector" caption="Inkplate 10 onboard USB-C connector" width="500px" />  

---

## 2. Upload the code
Click **Upload** in the Arduino IDE. Once the process completes, **Inkplate will restart automatically** and run the newly uploaded code.

---

## Troubleshooting

If uploading fails, verify that the board is powered on and that the correct board is selected.

Also, verify you are using Arduino IDE 2.0. Inkplate 6 MOTION requires **Arduino IDE 2.0** or later for proper **board and library support**. If you are using an older version, update to **Arduino 2.0+** for the best compatibility.

If you are having problems with uploading a sketch where it uploads to a certain perecntage, please [**contact us via support**](https://soldered.com/contact/).

---

From here, you may continue browsing the **hardware** documentation or start exploring the **Arduino library**:

<QuickLink 
  title="Arduino library basics" 
  description="See how to initialize and update Inkplate 6 MOTION's e-Paper display."
  url="/inkplate/6motion/basics/initialization" 
/>