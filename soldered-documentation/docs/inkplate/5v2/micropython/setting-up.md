---
slug: /inkplate/5v2/micropython/setting-up
title: Inkplate 5v2 MicroPython - Setting up Inkplate with MicroPython
sidebar_label: Setting up Inkplate with MicroPython
id: setting-up
---

To get started with MicroPython on your Inkplate 5v2, follow the steps below. If you are new to MicroPython, check out our [MicroPython guide](https://soldered.com/documentation/micropython/overview) for a full setup and an overview of how it works.

---

MicroPython runs directly on the Inkplate board. You plug in a USB cable, load the MicroPython firmware and the required libraries, then run your script on the Inkplate itself.

## Setting up Inkplate with MicroPython

To run your code on Inkplate, connect the device to your computer via USB and follow these steps:

1. Download the `Inkplate-firmware.bin` file onto your computer
   
2. Flash the `.bin` file onto the Inkplate device. You can do this with the [Soldered MicroPython Helper VS Code Extension](https://marketplace.visualstudio.com/items?itemName=SolderedElectronics.soldered-micropython-helper) or the [Thonny IDE](https://thonny.org)

### Flashing with the Micropython Helper extension

After [setting up the MicroPython Helper extension](https://soldered.com/documentation/micropython/getting-started-with-vscode), go to `Install Micropython on your board` and pick `Upload Binary file from PC`. Choose the `Inkplate-firmware.bin` file and wait for it to flash onto the device.

<CenteredImage src="/img/inkplate10-micropython/vscode_upload_file.png" alt="Uploading the firmware binary from VS Code" caption="Upload .bin file to device" width="500px"/>

### Flashing via Thonny IDE

In the Thonny IDE, go to `Run -> Configure interpreter` and on the bottom of the window go to `Install or update Micropython`. 

<CenteredImage src="/img/inkplate10-micropython/thonny_cfg_install.png" alt="Installing or updating MicroPython in Thonny" caption="Install or update Micropython" width="500px"/>

On the bottom of that window click the `≡` button and pick `Select local MicroPython image`. Choose the `Inkplate-firmware.bin` file on your computer and press `Install`.

<CenteredImage src="/img/inkplate10-micropython/thonny_cfg_install_select_img.png" alt="Selecting the MicroPython image in Thonny" caption="Select Micropython image" width="500px"/>

3. [Install the mpremote package](https://docs.micropython.org/en/latest/reference/mpremote.html)



4. With the mpremote package, you can upload the Inkplate modules onto the device with this command:

```
  mpremote mip install github:SolderedElectronics/Inkplate-micropython/boards/YOUR_DEVICE
```

or if you're running a Windows OS:

```
  python -m mpremote mip install github:SolderedElectronics/Inkplate-micropython/boards/YOUR_DEVICE
```

<QuickLink
  title="Installing MicroPython on Inkplate"
  description="Guide that walks you through MicroPython setup on your Inkplate"
  url="https://soldered.com/documentation/micropython/overview"
/>

Use this command to install the MicroPython library for Inkplate 5v2:

```
  mpremote mip install github:SolderedElectronics/Inkplate-micropython/boards/inkplate5v2
```

You only have to do steps 1-4 once, when first writing MicroPython firmware to your Inkplate.

<SuccessBox> Now you can upload examples and write code in the IDE of your choice. </SuccessBox>

<QuickLink
  title="Inkplate MicroPython Library"
  description="GitHub repo for Inkplate MicroPython library"
  url="https://github.com/SolderedElectronics/Inkplate-micropython"
/>