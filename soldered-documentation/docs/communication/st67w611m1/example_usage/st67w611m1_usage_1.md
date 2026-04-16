---
slug: /st67w611m1/example_usage/geting-started 
title: Getting started
id: st67w611m1-usage-1 
hide_title: False
---

<WarningBox>
The following guide is speciffically made for the **STM32 NUCLEO-U5A5ZJ-Q** development board that uses **STM32U5A5** microcontroller and will not work on other STM boards without additional modifications.
</WarningBox>

## Installing Required Packages

### Install STM32U5 MCU Package

Open **STM32CubeIDE** and navigate to: `Help -> Configuration Tool -> Manage Embedded Software Packages`.

<CenteredImage src="/img/st67w611m1/nav_1.png" alt="Location of manage Embedded Software Packages" caption="Location of manage Embedded Software Packages" width="1200px"/>

In the **STM32Cube MCU Packages** tab locate `STM32U5` package, select the latest version and press install.

<CenteredImage src="/img/st67w611m1/nav_2.png" alt="Installing the STM32U5 package" caption="Installing the STM32U5 package" width="1200px"/>

---

### Install X-CUBE-ST67W61 Expansion Package

In the same **Manage Embedded Software Packages** window switch to **STMicroelectronics** and search for `X-CUBE-ST67W61` and install the latest version.

<CenteredImage src="/img/st67w611m1/nav_3.png" alt="Installing the STM32U5 package" caption="Installing the STM32U5 package" width="1200px"/>

This package contains all the necessary drivers for the ST67W611 Wi-Fi module **Which come preflashed on our board**, middleware, utilities and the required `ST67W6X_HTTPS_Client` project.

---

## Connections

Below is an connection diagram for **STM32 NUCLEO-U5A5ZJ-Q**  which will be used in the next chapter's project example.

<WarningBox>
Due to the highly sensitive nature of the ST67W611M1 chip, we recommend you to instead of using header pins, solder your wires directly to the onboard pins.
</WarningBox>
| **STM32 NUCLEO-U5A5ZJ-Q** 	| **ST67W611M1** 	|
|---	|---	|
|3V3|3V3|
|GND|GND|
|MISO|PA6|
|CLK|PA5|
|MOSI|PA7|
|CS|PD14|
|RDY|PE13|
|BOOT|PE9|
|CHIP_EN|PE11|

