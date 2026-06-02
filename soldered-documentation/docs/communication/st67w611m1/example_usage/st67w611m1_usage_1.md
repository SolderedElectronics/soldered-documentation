---
slug: /st67w611m1/example_usage/getting-started 
title: Getting started
id: st67w611m1-usage-1 
hide_title: false
sidebar_label: Getting started
---

<WarningBox>
The following guide is specifically made for the STM32 NUCLEO-U5A5ZJ-Q development board that uses the STM32U5A5 microcontroller. This breakout will work with other STM32 boards but the configuration process might differ in some steps.
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

<CenteredImage src="/img/st67w611m1/nav_3.png" alt="Installing the X-CUBE-ST67W61 package" caption="Installing the X-CUBE-ST67W61 package" width="1200px"/>

This package contains all the necessary drivers for the ST67W611 Wi-Fi module **Which come preflashed on our board**, middleware, utilities and the required `ST67W6X_HTTPS_Client` project.

---

## Connections

Below is a connection diagram for **STM32 NUCLEO-U5A5ZJ-Q** which will be used in the next chapter's project example.

<WarningBox>
Due to the highly sensitive nature of the ST67W611M1 chip, we recommend you to instead of using header pins, solder your wires directly to the onboard pins.
</WarningBox>
| **STM32 NUCLEO-U5A5ZJ-Q** 	| **ST67W611M1 Breakout** 	|
|---	|---	|
|3V3|3V3|
|GND|GND|
|PA6|MISO|
|PA5|CLK|
|PA7|MOSI|
|PD14|CS|
|PE13|RDY|
|PE9|BOOT|
|PE11|EN|


<CenteredImage src="/img/st67w611m1/DSC00944.jpg" alt="Connection Example" caption="Connection Example" width="2000px"/>
