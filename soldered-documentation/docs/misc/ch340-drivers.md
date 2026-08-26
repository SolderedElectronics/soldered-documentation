---
slug: /ch340-drivers
title: CH340 drivers
sidebar_label: CH340 drivers
id: ch340-drivers
hide_title: false
pagination_next: null
pagination_prev: null
---

## What is the CH340?

The **CH340** is a small chip that converts USB into a serial (UART) connection. Many of our boards use one so that a single USB-C cable can both power the board and carry the serial connection your computer needs to upload code and read `Serial` output.

Your computer needs a **driver** to talk to that chip. Windows and macOS do not include one, so on a fresh machine the board plugs in, gets power, and still does not appear as a port in the Arduino IDE or Thonny. Nothing is broken — the driver just is not there yet.

<InfoBox>If your board does not appear in **Tools → Port**, and you have already tried a different cable and a different USB port, the CH340 driver is the most likely cause.</InfoBox>

---

## Do I need this?

Plug the board in and check what your computer already thinks it is.

**On Windows**, open **Device Manager** (right-click the Start button → *Device Manager*):

| What you see | What it means |
| --- | --- |
| **Ports (COM & LPT)** → *USB-SERIAL CH340 (COM5)* | The driver is installed. Nothing to do — use that COM port. |
| **Other devices** → *USB Serial*, with a yellow warning triangle | The chip is there but has no driver. Follow the Windows steps below. |
| Nothing appears or disappears when you plug in | Not a driver problem. Try another USB-C cable, then another USB port. |

To be certain which chip you have, right-click the device → **Properties → Details → Hardware Ids**. A CH340 reports a hardware ID beginning with `USB\VID_1A86`, where `VID_1A86` is WCH, the manufacturer of the chip.

**On macOS**, the board shows up as `/dev/cu.wchusbserial*` once the driver is installed. **On Linux**, it appears as `/dev/ttyUSB0` with no driver installation needed.

---

## Windows

<QuickLink
  title="CH341SER driver for Windows"
  description="Official WCH driver installer. Covers the whole CH340 and CH341 family."
  url="https://www.wch-ic.com/downloads/CH341SER_EXE.html"
/>

1. Download and run the installer from the link above.
2. Click **Install** and wait for the success message.
3. **Unplug the board and plug it back in.** This step matters — see the note below.
4. Check **Device Manager** again. The board should now be listed under **Ports (COM & LPT)** with a COM number.

<WarningBox>**Use version 3.9 (September 2024) or newer.** Older packages predate some chips in the CH340 family and will install without error while still leaving the board undetected. If a driver you already installed is not working, this is very often why.</WarningBox>

<InfoBox>**On Windows on ARM** — Snapdragon machines and other Copilot+ PCs — you need the driver just as much, and you need a recent version specifically, because ARM64 support was added later than the x86 and x64 support. Version 3.9 and newer include it.</InfoBox>

### The driver installed, but the board still is not detected

Installing a driver adds it to Windows' driver store; it does not always attach it to a device that Windows has already given up on. If the board is still sitting under **Other devices** after installing:

1. Unplug the board and plug it back in. This is enough most of the time.
2. If it is still there, right-click it → **Update driver** → **Search automatically for drivers**.
3. If it is *still* there, right-click it → **Uninstall device**, then unplug and replug.

---

## macOS

<QuickLink
  title="CH340 driver for macOS"
  description="Official WCH CH34x serial driver download for macOS"
  url="https://www.wch-ic.com/downloads/CH34XSER_MAC_ZIP.html"
/>

Download the package, open the `.dmg` and follow the installer.

<InfoBox>macOS may ask you to allow the driver in **System Settings → Privacy & Security** after installing. If the board is still not detected once you have allowed it, restart your Mac.</InfoBox>

---

## Linux

The CH340 driver is part of the kernel, so there is nothing to install. The board appears as `/dev/ttyUSB0` (or `ttyUSB1`, and so on) as soon as you plug it in.

If the port exists but you get a permission error when uploading, add yourself to the group that owns serial ports, then log out and back in:

```bash
sudo usermod -a -G dialout $USER
```

<InfoBox>On some Ubuntu installations the `brltty` service, which supports braille displays, claims CH340 devices and makes the port vanish a second or two after you plug the board in. If that is happening, `sudo apt remove brltty` frees the port.</InfoBox>

---

## Which boards use a CH340?

Not all of them do — some of our boards connect over the microcontroller's own USB hardware and need no driver at all. If you are unsure, check the **Hardware details** page for your board, or use the Device Manager check above, which tells you what the board actually is rather than what it ought to be.
