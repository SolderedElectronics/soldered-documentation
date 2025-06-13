---  
slug: /inkplate/4tempera/quick-start-guide  
title: Inkplate 4TEMPERA - Quick start guide  
id: 4tempera-quick-start-guide  
hide_title: true  
---

<SectionTitle title="Quick start guide" backgroundImage="/img/arduino_bg.jpg" />

To get started with Arduino on Inkplate 4TEMPERA, follow a few simple steps to install the required software.

---

### 1. Install Arduino IDE

If you haven’t installed it yet, download and install the Arduino IDE from the **[official website](https://www.arduino.cc/en/software)**.  
<WarningBox>Arduino IDE 2.0 or newer is required for Inkplate 4TEMPERA.</WarningBox>

<CenteredImage src="/img/inkplate_4_tempera/arduino_ide.png" alt="Install Arduino IDE" caption="Arduino IDE 2.0" width="600px" />

### 2. Install Inkplate boards definition

Copy the following URL:

```
https://github.com/SolderedElectronics/Dasduino-Board-Definitions-for-Arduino-IDE/raw/master/package_Dasduino_Boards_index.json
```

And add it to the `Additional boards manager URLs` in Arduino settings:

<CenteredImage src="/img/inkplate_4_tempera/add_board_def.png" alt="Add Inkplate to Arduino boards Manager" caption="Adding the Inkplate boards link to Arduino IDE" width="600px" />

Now you can open the Boards Manager, search for Inkplate Boards, and install the Inkplate Boards board definitions.  
Click `Install` here:  
<CenteredImage src="/img/inkplate_4_tempera/install_board.png" alt="Install Inkplate boards" caption="Adding Inkplate boards to Arduino IDE" width="400px" />

### 3. Install Inkplate library

In the Arduino Library Manager, search for the Inkplate Motion library and click `Install`:  
<CenteredImage src="/img/inkplate_4_tempera/install_lib.png" alt="Install Inkplate library" caption="Installing Inkplate library" width="400px" />

<InfoBox>It's also possible to install the library manually by downloading it from the [**GitHub repository**](https://github.com/SolderedElectronics/Inkplate-Arduino-library).</InfoBox>

### 4. Install CH340 driver

<InfoBox>Mac and Linux users can skip this step because the CH340 driver is already installed.</InfoBox>

The CH340 is an onboard chip that enables serial communication over USB. If the driver is not installed, download it from **[this link](https://soldered.com/productdata/2023/02/CH34x_Install_Windows_v3_4.zip)**. Start the installation and follow the instructions:  
<CenteredImage src="/img/inkplate_4_tempera/ch340.png" alt="Install CH340 Driver" caption="Installing the CH340 Driver on Windows" width="350px" />

### Done!

Inkplate 4TEMPERA setup is complete. Now, try out some examples from the Arduino library—upload them and see the results for yourself! For details on how to upload code, see the next page in the documentation:

---

## Uploading code

To upload your own sketch or an Arduino example to **Inkplate 4TEMPERA**, follow this brief guide.

### 1. Connect Inkplate via USB and power it on

Use the provided **USB-C cable** to connect Inkplate 4TEMPERA to your computer. Ensure that the board is powered on by pressing the **POWER ON** button. The **blue power LED** will light up when properly connected.

<CenteredImage src="/img/inkplate_4_tempera/10_usb_connect.png" alt="Inkplate 4TEMPERA onboard USB-C connector" caption="Inkplate 4TEMPERA onboard USB-C connector" width="500px" />

<CenteredImage src="/img/inkplate_4_tempera/10_power_button.png" alt="Inkplate 4TEMPERA onboard POWER button" caption="Inkplate 4TEMPERA onboard POWER button" width="500px" />

### 2. Create a sketch

For the purposes of this documentation, we will use a pre-made example. Go to  
`File->Examples->InkplateLibrary->Inkplate4TEMPERA->Basic->Inkplate4TEMPERA_Hello_World`

<CenteredImage src="/img/inkplate_4_tempera/arduino_sketch.png" alt="Selecting a basic example for Inkplate 4TEMPERA" caption="Selecting a basic example for Inkplate 4TEMPERA" width="800px" />

### 3. Upload the code

Before uploading the code, select the correct board definition. The table below should help you out:

| Board Definition                   | Board Description                                                     |
| ---------------------------------- | --------------------------------------------------------------------- |
| Soldered inkplate_4_tempera        | The newer and more stylish version of the product, with a purple PCB. |
| e-radionica.com Inkplate 4TEMPERA   | The older version, with a blue PCB.                                   |

Click **Upload** in the Arduino IDE.

<CenteredImage src="/img/inkplate_4_tempera/upload_button.png" alt="Arduino IDE Upload Button" caption="Arduino IDE Upload Button" width="800px" />

Once the process completes, **Inkplate will restart automatically** and run the newly uploaded code. Arduino's upload log should read:
```
Leaving...
Hard resetting via RTS pin...
```

### Troubleshooting

Having trouble uploading your first code? Check out our [troubleshooting page](/documentation/inkplate/10/faq-troubleshooting/):