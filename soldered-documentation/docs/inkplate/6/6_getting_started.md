---  
slug: /inkplate/6/quick-start-guide/  
title: Quick start guide  
id: quick-start-guide  
hide_title: True  
pagination_prev: null  
---  
<SectionTitle title="Quick start guide" backgroundImage="/img/arduino_bg.jpg" />

To get started with Arduino on Inkplate 6, follow a few simple steps to install the required software.

---

### 1. Install Arduino IDE

If you haven’t installed it yet, download and install the Arduino IDE from the **[official website](https://www.arduino.cc/en/software)**.  
<WarningBox>Arduino IDE 2.0 or newer is required for Inkplate 6.</WarningBox>

<CenteredImage src="/img/inkplate10/arduino_ide.png" alt="Install Arduino IDE" caption="Arduino IDE 2.0" width="600px" />

### 2. Install Inkplate board definitions

Copy the following URL:

```
https://github.com/SolderedElectronics/Dasduino-Board-Definitions-for-Arduino-IDE/raw/master/package_Dasduino_Boards_index.json
```

Then add it to the `Additional boards manager URLs` in the Arduino settings:

<CenteredImage src="/img/inkplate10/add_board_def.png" alt="Add Inkplate to Arduino boards Manager" caption="Adding the Inkplate boards link to Arduino IDE" width="600px" />

Now you can open the Boards Manager, search for Inkplate Boards, and install the Inkplate Boards board definitions.  
Click `Install` here:  
<CenteredImage src="/img/inkplate10/install_board.png" alt="Install Inkplate boards" caption="Adding Inkplate boards to Arduino IDE" width="400px" />

### 3. Install Inkplate library

In the Arduino Library Manager, search for the Inkplate Motion library and click `Install`:  
<CenteredImage src="/img/inkplate10/install_lib.png" alt="Install Inkplate library" caption="Installing Inkplate library" width="400px" />

<InfoBox>It's also possible to install the library manually by downloading it from the [**GitHub repository**](https://github.com/SolderedElectronics/Inkplate-Arduino-library).</InfoBox>

### 4. Install CH340 driver

<InfoBox>Mac and Linux users can skip this step because the CH340 driver is already installed.</InfoBox>

The CH340 is an onboard chip that enables serial communication over USB. If the driver is not installed, download it from **[this link](https://soldered.com/productdata/2023/02/CH34x_Install_Windows_v3_4.zip)**. Start the installation and follow the instructions:  
<CenteredImage src="/img/inkplate10/ch340.png" alt="Install CH340 Driver" caption="Installing the CH340 Driver on Windows" width="350px" />

### Done!

Inkplate 6 setup is complete. Now try out some examples from the Arduino library—upload them and see the results for yourself!

---

## Uploading code

To upload your own sketch or an Arduino example to **Inkplate 6**, follow this brief guide.

### 1. Connect Inkplate via USB and power it on

Use the provided **USB-C cable** to connect Inkplate 6 to your computer. Ensure that the board is powered on by pressing the **POWER ON** button. The **blue power LED** will light up when it is properly connected.

<CenteredImage src="/img/inkplate10/10_usb_connect.png" alt="Inkplate 6 onboard USB-C connector" caption="Inkplate 6 onboard USB-C connector" width="500px" />

<CenteredImage src="/img/inkplate10/10_power_button.png" alt="Inkplate 6 onboard POWER button" caption="Inkplate 6 onboard POWER button" width="500px" />

### 2. Create a sketch

For this documentation, we will use a pre-made example. Go to `File->Examples->InkplateLibrary->Inkplate6->Basic->Inkplate6_Hello_World`.

<CenteredImage src="/img/6/hello_world.png" alt="Selecting a basic example for Inkplate 6" caption="Selecting a basic example for Inkplate 6" width="1000px" />

### 3. Upload the code

Click **Upload** in the Arduino IDE.

<CenteredImage src="/img/6/upload.png" alt="Arduino IDE Upload Button" caption="Arduino IDE Upload Button" width="1000px" />

Once the process completes, **Inkplate will restart automatically** and run the newly uploaded code. Arduino's upload log should read:
```
Leaving...
Hard resetting via RTS pin...
```

### Troubleshooting

Having problems uploading your first code? Check out our [troubleshooting page](/documentation/inkplate/6/faq-troubleshooting/)