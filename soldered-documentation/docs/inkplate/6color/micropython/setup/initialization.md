---  
slug: /inkplate/6color/micropython/setup/initialization
title: Inkplate 6COLOR – Micropython
sidebar_label: Setting up Inkplate
id: init
hide_title: true  
---

<SectionTitle title="Setting up Inkplate" backgroundImage="img/arduino_bg.jpg" />

To get started with MicroPython on your Inkplate 6COLOR, follow these next few steps. If you are new to MicroPython, check out our official [MicroPython Guide](https://soldered.com/documentation/micropython/overview) for a full setup and overview on how it works.

---

Using MicroPython on your Inkplate board is very simple and straightforward, just plug in a USB cable, load the MicroPython firmware and the required libraries and run your script on Inkplate itself.

## Setting up Inkplate with MicroPython

In order to get started with running your code on Inkplate, connect the device to your computer via USB and follow these steps:

1. Download the `Inkplate-firmware.bin` file onto your computer
   
2. Flash the **.bin** file onto the Inkplate device, this can be done via [Soldered MicroPython Helper VS Code Extension](https://marketplace.visualstudio.com/items?itemName=SolderedElectronics.soldered-micropython-helper) or the [Thonny IDE](https://thonny.org)

### Flashing with the Micropython Helper extension

After [setting up the MicroPython Helper extension](https://soldered.com/documentation/micropython/getting-started-with-vscode), go to `Install Micropython on your board` and pick `Upload Binary file from PC`, choose the **Inkplate-firmware.bin** file and wait for it to flash on the device.

<CenteredImage src="/img/6color/vscode_upload_file.png" alt="Inkplate 6 color Thonny" caption="Upload .bin file to device" width="500px"/>

### Flashing via Thonny IDE

In the Thonny IDE, go to `Run -> Configure interpreter` and on the bottom of the window go to `Install or update Micropython`. 

<CenteredImage src="/img/6color/thonny_cfg_install.png" alt="Inkplate 6 color Thonny" caption="Install or update Micropython" width="500px"/>

On the bottom of that window click on the `≡` button and pick `Select local MicroPython image`, choose the Inkplate-firmware.bin file on your computer and press `Install`.

<CenteredImage src="/img/6color/thonny_cfg_install_select_img.png" alt="Inkplate 6 color Thonny" caption="Select Micropython image" width="500px"/>

3. [Install the mpremote package](https://docs.micropython.org/en/latest/reference/mpremote.html)

4. With the mpremote package, we can **flash the Inkplate modules** onto the device with the following command:

```
  mpremote mip install github:SolderedElectronics/Inkplate-micropython/YOUR_DEVICE
```

or if you're running a Windows OS:

```
  python -m mpremote mip install github:SolderedElectronics/Inkplate-micropython/YOUR_DEVICE
```

Use the following command to install the MicroPython library for INKPLATE 6COLOR:

```
  mpremote mip install github:SolderedElectronics/Inkplate-micropython/Inkplate6COLOR
```

**You only have to do steps 1-4 once when writing MicroPython firmware on your Inkplate!**

<SuccessBox> Now you can upload examples and write code with the IDE of your choosing! </SuccessBox>

---

## Initializing Inkplate

Here is a basic Inkplate object creation and display initialization which we will use in every example in following tutorials:

```python
# Include inkplate library
from inkplate6COLOR import Inkplate

# Create Inkplate object
inkplate = Inkplate()

# Initialize the display, needs to be called only once
inkplate.begin()
```

<FunctionDocumentation
  functionName="inkplate.Inkplate()"
  description="Creates an Inkplate object from the Inkplate class."
  returnType="none"
/>
<FunctionDocumentation
  functionName="inkplate.begin()"
  description="In short, this function initializes the Inkplate object. It starts I2C, allocates the required memory for the frame buffer, and initializes the onboard peripherals."
  returnType="none"
/>

Now, let's explore some basic examples!