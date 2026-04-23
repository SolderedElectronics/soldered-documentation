---
slug: /inkplate/5v2/micropython/setting-up
title: Inkplate 5v2 MicroPython - Setting up Inkplate with MicroPython
sidebar_label: Setting up Inkplate with MicroPython
id: setting-up
---

To get started with MicroPython on your Inkplate 5v2, follow these next few steps. If you are new to MicroPython, check out our official **[MicroPython Guide](https://soldered.com/documentation/micropython/overview)** for a full setup and overview on how it works.

---

Using MicroPython on your Inkplate board is very simple and straightforward, just plug in a USB cable, load the MicroPython firmware and the required libraries and run your script on Inkplate itself.

## Setting up Inkplate with MicroPython

In order to get started with running your code on Inkplate, connect the device to your computer via USB and follow these steps:

1. Download the `Inkplate-firmware.bin` file onto your computer
   
2. Flash the **.bin** file onto the Inkplate device, this can be done via **[Soldered MicroPython Helper VS Code Extension](https://marketplace.visualstudio.com/items?itemName=SolderedElectronics.soldered-micropython-helper)** or the **[Thonny IDE](https://thonny.org)**

### Flashing with the Micropython Helper extension

After **[setting up the MicroPython Helper extension](https://soldered.com/documentation/micropython/getting-started-with-vscode)**, go to `Install Micropython on your board` and pick `Upload Binary file from PC`, choose the **Inkplate-firmware.bin** file and wait for it to flash on the device.

<CenteredImage src="/img/inkplate10-micropython/vscode_upload_file.png" alt="Inkplate 5v2 color Thonny" caption="Upload .bin file to device" width="500px"/>

### Flashing via Thonny IDE

In the Thonny IDE, go to `Run -> Configure interpreter` and on the bottom of the window go to `Install or update Micropython`. 

<CenteredImage src="/img/inkplate10-micropython/thonny_cfg_install.png" alt="Inkplate 5v2 color Thonny" caption="Install or update Micropython" width="500px"/>

On the bottom of that window click on the `≡` button and pick `Select local MicroPython image`, choose the Inkplate-firmware.bin file on your computer and press `Install`.

<CenteredImage src="/img/inkplate10-micropython/thonny_cfg_install_select_img.png" alt="Inkplate 5v2 color Thonny" caption="Select Micropython image" width="500px"/>

3. [Install the mpremote package](https://docs.micropython.org/en/latest/reference/mpremote.html)



4. With the mpremote package, we can **upload the Inkplate modules** onto the device with the following command:

```
  mpremote mip install github:SolderedElectronics/Inkplate-micropython/YOUR_DEVICE
```

or if you're running a Windows OS:

```
  python -m mpremote mip install github:SolderedElectronics/Inkplate-micropython/YOUR_DEVICE
```

<QuickLink
  title="Installing MicroPython on Inkplate"
  description="Guide that walks you through MicroPython setup on your Inkplate"
  url="#"
/>

Use the following command to install the MicroPython library for INKPLATE 5v2:

```
  mpremote mip install github:SolderedElectronics/Inkplate-micropython/Inkplate5v2
```

**You only have to do steps 1-4 once when writing MicroPython firmware on your Inkplate!**

<SuccessBox> Now you can upload examples and write code with the IDE of your choosing! </SuccessBox>

<QuickLink
  title="Inkplate MicroPython Library"
  description="GitHub repo for Inkplate MicroPython library"
  url="https://github.com/SolderedElectronics/Inkplate-micropython"
/>