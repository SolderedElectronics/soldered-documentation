---  
slug: /inkplate/2/quick-start-guide  
title: Inkplate 2 - Quick start guide  
sidebar_label: Quick start guide
id: 2-quick-start-guide  
hide_title: true  
---

<SectionTitle title="Quick start guide" backgroundImage="/img/arduino_bg.jpg" />

To get started with Arduino on Inkplate 2, a few simple steps need to be completed to install the required software.

---

### 1. Install Arduino IDE

If you haven’t installed it yet, download and install the Arduino IDE from the **[official website](https://www.arduino.cc/en/software)**.  
<WarningBox>Arduino IDE 2.0 or newer is required for Inkplate 2.</WarningBox>

<CenteredImage src="/img/inkplate_2/arduino_ide.png" alt="Install Arduino IDE" caption="Arduino IDE 2.0" width="600px" />

### 2. Install Inkplate boards definition

Copy the following URL:

```
https://github.com/SolderedElectronics/Dasduino-Board-Definitions-for-Arduino-IDE/raw/master/package_Dasduino_Boards_index.json
```

And add it to the `Additional boards manager URLs` in Arduino settings:

<CenteredImage src="/img/inkplate_2/add_board_def.png" alt="Add Inkplate to Arduino boards Manager" caption="Adding the Inkplate boards link to Arduino IDE" width="600px" />

Now, you can open the Boards Manager, search for Inkplate Boards, and install the Inkplate Boards board definitions.  
Click `Install` here:  
<CenteredImage src="/img/inkplate_2/install_board.png" alt="Install Inkplate boards" caption="Adding Inkplate boards to Arduino IDE" width="400px" />

### 3. Install Inkplate library

In the Arduino Library Manager, search for the Inkplate Motion library and click `Install`:  
<CenteredImage src="/img/inkplate_2/install_lib.png" alt="Install Inkplate library" caption="Installing Inkplate library" width="400px" />

<InfoBox>It's also possible to install the library manually by downloading it from the [**GitHub repository**](https://github.com/SolderedElectronics/Inkplate-Arduino-library).</InfoBox>

### 4. Install CH340 driver

<InfoBox>Mac and Linux users can skip this step because the CH340 driver is already installed.</InfoBox>

The CH340 is an onboard chip that enables serial communication over USB. If the driver is not installed, download it from **[this link](https://soldered.com/productdata/2023/02/CH34x_Install_Windows_v3_4.zip)**. Start the installation and follow the instructions:  
<CenteredImage src="/img/inkplate_2/ch340.png" alt="Install CH340 Driver" caption="Installing the CH340 Driver on Windows" width="350px" />

### Done!

Inkplate 2 setup is complete. Now, try out some examples from the Arduino library—upload them and see the results for yourself! See the next page in the documentation for details on how to upload code:

---

## Uploading code
To upload your own sketch or an Arduino example to **Inkplate 2**, follow this brief guide.



### 1. Connect Inkplate via USB and power it on

Use the provided **USB-C cable** to connect Inkplate 2 to your computer. The board is powered on!

<CenteredImage src="/img/inkplate_2/inkplate2usbc.png" alt="Inkplate 2 onboard USB-C connector" caption="Inkplate 2 onboard USB-C connector" width="500px" />


### 2. Create a sketch

For the needs of this documentation, we will be using a premade example. Go to `File->Examples->InkplateLibrary->Inkplate2->Basic->Inkplate2_Hello_World`

<CenteredImage src="/img/inkplate_2/arduino_sketch.png" alt="Selecting a basic example for Inkplate 2" caption="Selecting a basic example for Inkplate 2" width="700px" />

### 3. Upload the code

Before uploading the code, select the correct board definition. The table below should help you out:

| Board Definition               | Board Description                                                                                          |
| ------------------------------ | ---------------------------------------------------------------------------------------------------------- |
| Soldered Inkplate2            | The newer and more stylish version of the product, and the PCB is purple.                                  |

Click **Upload** in the Arduino IDE.

Once the process completes, **Inkplate will restart automatically** and run the newly uploaded code. Arduino's upload log should read:
```
Leaving...
Hard resetting via RTS pin...
```

### Troubleshooting

Having problems with uploading your first code? Check out our [troubleshooting page](/documentation/inkplate/2/faq-troubleshooting/):





