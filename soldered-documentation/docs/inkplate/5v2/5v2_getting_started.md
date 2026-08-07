---  
slug: /inkplate/5v2/quick-start-guide/  
title: Inkplate 5V2 - Quick start guide  
sidebar_label: Quick start guide
id: quick-start-guide  
hide_title: True  
pagination_prev: null  
---  
<SectionTitle title="Quick start guide" />

To use Arduino with Inkplate 5V2, you first need to install the required software. Here's how.

---

### 1. Install Arduino IDE

If you haven't installed it yet, download and install the Arduino IDE from the **[official website](https://www.arduino.cc/en/software)**.  
<WarningBox>Arduino IDE 2.0 or newer is required for Inkplate 5V2.</WarningBox>

<CenteredImage src="/img/inkplate10/arduino_ide.png" alt="Install Arduino IDE" caption="Arduino IDE 2.0" width="600px" />

### 2. Install Inkplate boards definition

Copy the following URL:

```
https://github.com/SolderedElectronics/Inkplate-Board-Definitions-for-Arduino-IDE/raw/refs/heads/main/package_Inkplate_Boards_index.json
```

And add it to the `Additional boards manager URLs` in the Arduino settings:

<CenteredImage src="/img/5v2/add_board_def.png" alt="Add Inkplate to Arduino boards Manager" caption="Adding the Inkplate boards link to Arduino IDE" width="600px" />

Now open the Boards Manager, search for Inkplate Boards, and install the Inkplate Boards board definitions.  
Click `Install` here:  
<CenteredImage src="/img/5v2/install_board.png" alt="Install Inkplate boards" caption="Adding Inkplate boards to Arduino IDE" width="400px" />

### 3. Install Inkplate library

In the Arduino Library Manager, search for the Inkplate library and click `Install`:  
<CenteredImage src="/img/inkplate10/install_lib.png" alt="Install Inkplate library" caption="Installing Inkplate library" width="400px" />

<InfoBox>It's also possible to install the library manually by downloading it from the [**GitHub repository**](https://github.com/SolderedElectronics/Inkplate-Arduino-library).</InfoBox>

### 4. Install CH340 driver

<InfoBox>Mac and Linux users can skip this step because the CH340 driver is already installed.</InfoBox>

The CH340 is an onboard chip that handles serial communication over USB. If you don't have the driver yet, download it from **[this link](https://soldered.com/blogs/learn/ch340-driver-installation)**, then start the installation and follow the instructions:  
<CenteredImage src="/img/inkplate10/ch340.png" alt="Install CH340 Driver" caption="Installing the CH340 Driver on Windows" width="350px" />

### Done!

Inkplate 5V2 setup is complete. Try out some examples from the Arduino library, upload them and see the results for yourself.

---

## Light and Versatile Graphics Library (LVGL)

<InfoBox> If you want more customization and room for complex GUI design, LVGL is supported on Inkplate boards. Check out this **[page](/inkplate/lvgl-library)** to get started. </InfoBox>

---

## Uploading code

Here's how to upload your own sketch, or one of the Arduino examples, to Inkplate 5V2.

### 1. Connect Inkplate via USB and power it on

Use the provided USB-C cable to connect Inkplate 5V2 to your computer, then press the POWER ON button. The blue power LED lights up when the board is connected properly.

<CenteredImage src="/img/inkplate10/10_usb_connect.png" alt="Inkplate 5V2 onboard USB-C connector" caption="Inkplate 5V2 onboard USB-C connector" width="500px" />

<CenteredImage src="/img/inkplate10/10_power_button.png" alt="Inkplate 5V2 onboard POWER button" caption="Inkplate 5V2 onboard POWER button" width="500px" />

### 2. Create a sketch

We'll use a pre-made example here. Go to `File->Examples->InkplateLibrary->Inkplate5V2->Basic->Inkplate5V2_Hello_World`.

<CenteredImage src="/img/5v2/hello_world.png" alt="Selecting a basic example for Inkplate 5V2" caption="Selecting a basic example for Inkplate 5V2" width="700px" />

### 3. Upload the code

Click `Upload` in the Arduino IDE.

<CenteredImage src="/img/5v2/upload.png" alt="Arduino IDE Upload Button" caption="Arduino IDE Upload Button" width="500px" />

Once the upload finishes, Inkplate restarts on its own and runs the new code. Arduino's upload log should read:
```
Leaving...
Hard resetting via RTS pin...
```

### Troubleshooting

Having problems uploading your first code? Check out our [troubleshooting page](/inkplate/5v2/faq-troubleshooting/)