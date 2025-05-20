---
slug: /inkplate/6motion/quick-start-guide
title: 6Motion - Quick start guide
id: 6motion-quick-start-guide
hide_title: true
---

<SectionTitle title="Quick start guide" backgroundImage="/img/arduino_bg.jpg" />

To get started with Arduino on Inkplate 6 MOTION, a few simple steps need to be completed to install the required software.

---

## 1. Install STM32CubeProgrammer

This software is required to upload code to Inkplate 6 MOTION. [**Download it from the official website**](https://www.st.com/en/development-tools/stm32cubeprog.html) and install it.

<WarningBox>Without STM32CubeProgrammer, uploading code to Inkplate 6 MOTION will not be possible, and the Arduino IDE will return an error.</WarningBox>

---

## 2. Install Arduino IDE

If you haven’t installed it yet, download and install the Arduino IDE from the **[official website](https://www.arduino.cc/en/software)**.
<WarningBox>Arduino IDE 2.0 or newer is required for Inkplate 6 MOTION.</WarningBox>

<CenteredImage src="/img/inkplate_6_motion/arduino_ide.png" alt="Install Arduino IDE" caption="Arduino IDE 2.0" width="600px" />

---

## 3. Install Inkplate 6 MOTION board definition

Copy the following URL:

```
https://github.com/SolderedElectronics/Dasduino-Board-Definitions-for-Arduino-IDE/raw/master/package_Dasduino_Boards_index.json
```

And add it to the `Additional boards manager URLs` in Arduino settings:

<CenteredImage src="/img/inkplate_6_motion/add_board_def.png" alt="Add Inkplate to Arduino boards Manager" caption="Adding the Inkplate boards link to Arduino IDE" width="600px" />

Now, you can open the Boards Manager, search for Inkplate MOTION, and install the Inkplate MOTION board definitions.
Click `Install` here:
<CenteredImage src="/img/inkplate_6_motion/motion_install_board.png" alt="Install Inkplate MOTION boards" caption="Adding Inkplate MOTION boards to Arduino IDE" width="400px" />

---

## 4. Install Inkplate MOTION library

In the Arduino Library Manager, search for the Inkplate Motion library and click `Install`:
<CenteredImage src="/img/inkplate_6_motion/motion_install_lib.png" alt="Install Inkplate MOTION library" caption="Installing Inkplate MOTION library" width="400px" />

<InfoBox>It's also possible to install the library manually by downloading it from the [**GitHub repository**](https://github.com/SolderedElectronics/Inkplate_Motion_Arduino_Library).</InfoBox>

---

## 5. Install CH340 driver

<InfoBox>Mac and Linux users can skip this step, the CH340 driver is already installed.</InfoBox>

The CH340 is an onboard chip that enables serial communication over USB. If the driver is not installed, download it from **[this link](https://soldered.com/productdata/2023/02/CH34x_Install_Windows_v3_4.zip)**. Start the installation and follow the instructions:
<CenteredImage src="/img/inkplate_6_motion/ch340.png" alt="Install CH340 Driver" caption="Installing the CH340 Driver on Windows" width="350px" />

---

## Done!

Inkplate 6 MOTION setup is complete. Now, try out some examples from the Arduino library—upload them and see the results for yourself! See the next page in the documentation for details on how to upload code:

<QuickLink 
  title="Uploading code"
  description="Detailed tutorial on how to upload code for Inkplate 6 MOTION"
  url="/inkplate/6motion/uploading-code" 
/>

If you experience any issues, check the FAQ:
<QuickLink 
  title="F.A.Q. and troubleshooting" 
  description="Solve the most common issues with using Inkplate 6 MOTION"
  url="/inkplate/6motion/faq-troubleshooting" 
/>

