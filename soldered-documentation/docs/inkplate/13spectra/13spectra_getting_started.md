---  
slug: /inkplate/13spectra/quick-start-guide  
title: Inkplate 13SPECTRA - Quick start guide  
sidebar_label: Quick start guide
id: 13spectra-quick-start-guide  
hide_title: true  
---

<SectionTitle title="Quick start guide" backgroundImage="/img/arduino_bg.jpg" />

To get started with Arduino on Inkplate 13SPECTRA, a few simple steps need to be completed to install the required software.

---

### 1. Install Arduino IDE

If you haven’t installed it yet, download and install the Arduino IDE from the **[official website](https://www.arduino.cc/en/software)**.  
<WarningBox>Arduino IDE 2.0 or newer is required for Inkplate 13SPECTRA.</WarningBox>

<CenteredImage src="/img/inkplate10/arduino_ide.png" alt="Install Arduino IDE" caption="Arduino IDE 2.0" width="600px" />

### 2. Install Inkplate boards definition

Copy the following URL:

```
https://raw.githubusercontent.com/SolderedElectronics/Inkplate-Board-Definitions-for-Arduino-IDE/refs/heads/main/package_Inkplate_Boards_index.json
```

And add it to the `Additional boards manager URLs` in Arduino settings:

<CenteredImage src="/img/inkplate10/add_board_def.png" alt="Add Inkplate to Arduino boards Manager" caption="Adding the Inkplate boards link to Arduino IDE" width="600px" />

Now, you can open the Boards Manager, search for Inkplate Boards, and install the Inkplate Boards board definitions.  
Click `Install` here:  
<CenteredImage src="/img/inkplate10/install_board.png" alt="Install Inkplate boards" caption="Adding Inkplate boards to Arduino IDE" width="400px" />

### 3. Install Inkplate library

In the Arduino Library Manager, search for the Inkplate library and click `Install`:  
<CenteredImage src="/img/inkplate10/install_lib.png" alt="Install Inkplate library" caption="Installing Inkplate library" width="400px" />

<InfoBox>It's also possible to install the library manually by downloading it from the [**GitHub repository**](https://github.com/SolderedElectronics/Inkplate-Arduino-library).</InfoBox>

### 4. Install CH340 driver

The CH340 is an onboard chip that enables serial communication over USB.

<InfoBox>Linux users can skip this step because the CH340 driver is already installed.</InfoBox>

#### Windows

If the driver is not installed, download it from **[this link](https://soldered.com/productdata/2023/02/CH34x_Install_Windows_v3_4.zip)**. Start the installation and follow the instructions:  
<CenteredImage src="/img/inkplate10/ch340.png" alt="Install CH340 Driver" caption="Installing the CH340 Driver on Windows" width="350px" />

#### Mac

On macOS, the CH340 driver needs to be installed manually. Download it from the official WCH website, open the `.dmg` file, and follow the installation instructions:

<QuickLink 
  title="CH340 driver for macOS" 
  description="Official WCH CH34x serial driver download for macOS"
  url="https://www.wch-ic.com/downloads/CH34XSER_MAC_ZIP.html" 
/>

<WarningBox>After installing the driver, you also have to **enable it manually** in macOS security settings:  
**System Settings → Login Items & Extensions → CH34xVPCDriver → ⓘ (info) button → enable the driver**.  
The board will not show up as a serial port until the driver is enabled.</WarningBox>

### Done!

Inkplate 13SPECTRA setup is complete. Now, try out some examples from the Arduino library—upload them and see the results for yourself! If you need some help with uploading code, check out the section below.

---

## Uploading code
To upload your own sketch or an Arduino example to **Inkplate 13SPECTRA**, follow this brief guide.

### 1. Connect Inkplate via USB and power it on

Use the provided **USB-C cable** to connect Inkplate 13SPECTRA to your computer. Ensure that the board is powered on by pressing the **POWER ON** button. The **blue power LED** will light up when properly connected.

### 2. Create a sketch

Let's create the most basic Inkplate code which writes `Hello World!` to the e-Paper display. Go to `File->New Sketch` and paste this code in:

```cpp

#include <Inkplate.h>   // Include the Inkplate library
Inkplate display;   // Create an Inkplate object for Inkplate 13SPECTRA

void setup(){
    display.begin(); // Initialize the display hardware
    display.clearDisplay(); // Clear the frame buffer (does NOT clear the physical screen)
    display.setCursor(10,10) // Set the text position to (10,10) pixels
    display.setTextSize(6); // Set text size to 6 (default is 1)
    display.print("Hello World!"); // Print "Hello World!" at the set position
    display.display(); // Refresh the e-paper display to show changes
}

void loop(){
    // No code needed here for this example
}

```

### 3. Upload the code

Before uploading the code, select the correct board definition. For Inkplate 13, select `Soldered Inkplate 13SPECTRA`.

<CenteredImage src="/img/13spectra/board_select.png"  alt="Selected board definition for Inkplate 13SPECTRA" caption="Select Soldered Inkplate 13SPECTRA" width="500px"/>

Click **Upload** in the Arduino IDE.

<CenteredImage src="/img/13spectra/upload_button.png" alt="Arduino IDE Upload Button" caption="Arduino IDE Upload Button" width="500px" />

Once the process completes, **Inkplate will restart automatically** and run the newly uploaded code. Arduino's upload log should read:
```
Leaving...
Hard resetting via RTS pin...
```

That's how you know you did everything correctly!

## Troubleshooting

Having problems with uploading your first code? Check out our [LINK PLACEHOLDER - troubleshooting page]