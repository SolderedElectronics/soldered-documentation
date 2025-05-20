---
slug: /inkplate/6motion/additional-resources
title: 6Motion - Additional resources
id: 6motion-additional-resources
---

To upload your own sketch or an Arduino example to **Inkplate 6 MOTION**, follow this brief guide.  

<InfoBox>You are uploading code to the onboard **STM32H743**. The **ESP32 co-processor** comes pre-programmed with firmware and **should not be modified**!</InfoBox>  

---

## 1. Connect Inkplate via USB and power it on 

Use the provided **USB-C cable** to connect Inkplate 6 MOTION to your computer. Ensure that the board is powered on by pressing the **POWER ON** button. The **blue power LED** will light up when properly connected.  

<CenteredImage src="/img/inkplate_6_motion/6motion_usb_connect.jpg" alt="Connect Inkplate 6 MOTION via USB" caption="Connecting Inkplate via USB-C" width="500px" />  

---

## 2. Press the PROGRAMMING button

To enter **programming mode**, press the **PROGRAMMING button** located next to **USER2**.  

<CenteredImage src="/img/inkplate_6_motion/prog_button.jpg" alt="Inkplate 6 MOTION programming button" caption="Programming button, next to USER2" width="500px" />  

If your **Inkplate 6 MOTION is inside an enclosure**, use the **programming tool** provided to press the button externally.  

<CenteredImage src="/img/inkplate_6_motion/programming_tool.png" alt="Inkplate 6 MOTION programming tool" caption="Using the programming tool for enclosures" width="500px" />  

<InfoBox>To confirm the device is in programming mode, open the **Serial Monitor** (115200 baud) on Inkplate 6 MOTION’s port. It should display:  
`Programming mode active.`</InfoBox>  

---

## 3. Upload the code

Click **Upload** in the Arduino IDE. Once the process completes, **Inkplate will restart automatically** and run the newly uploaded code. The programming tool is provided within Inkplate's enclosure. 

---

## Troubleshooting

If uploading fails, try using the BOOT switch. This is a switch on the back of the PCB that can be used to force programming mode manually:  

1. **Set the BOOT switch to position `1`** (this puts the STM32 in bootloader mode).  
2. **Press the RESET button** to restart the board.  
3. **Upload your code** via Arduino.  
4. Once done, **switch BOOT back to `0`** to return to normal operation.  

Also, verify you are using Arduino IDE 2.0. Inkplate 6 MOTION requires **Arduino IDE 2.0** or later for proper **board and library support**. If you are using an older version, update to **Arduino 2.0+** for the best compatibility.

If you are having problems with uploading a sketch where it uploads to a certain perecntage, please [**contact us via support**](https://soldered.com/contact/).