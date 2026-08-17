---
slug: /nula-dual-esp32-c5/hardware
title: NULA Dual ESP32-C5 - Hardware details
sidebar_label: Hardware details
id: nula_dual_esp32-c5-hardware
hide_title: True
---

# Hardware details

## Pinout

<CenteredImage src="/img/nula_dual_esp32-c5/Pinout.png" alt="NULA Dual ESP32-C5 pinout" caption="NULA Dual ESP32-C5 Pinout Diagram"/>

Click [**here**](/img/nula_dual_esp32-c5/Pinout.png) for a high-resolution version of the pinout.

---

## Pin Details

| Pin Marking | Type      | Description                                                        |
| ----------- | --------- | ------------------------------------------------------------------ |
| **VBAT**    | Power     | Same net as the JST battery connector - an alternate connection point for a 3.7 V Li-Ion/Li-Poly battery. |
| **VCC**     | Power     | Output of the onboard power-source selection circuit. When USB-C is connected it follows the USB 5 V rail minus a Schottky drop (roughly **4.6 - 4.7 V**), otherwise it follows the battery voltage - not a fixed, stable voltage, and not an input. |
| **3V3**     | Power     | Regulated 3.3 V output from the onboard regulator.                 |
| **GND**     | Ground    | Common ground reference.                                           |
| **RESET**   | Control   | Active-low reset input, also wired to the onboard reset button.    |
| **RXD**     | UART      | UART0 receive pin (**IO12**). Shared with the onboard CH340K bridge through a 1 kΩ series resistor, so it also carries programming and Serial Monitor traffic. |
| **TXD**     | UART      | UART0 transmit pin (**IO11**). Also shared with the CH340K bridge.  |
| **IO0**     | GPIO/ADC  | General-purpose I/O, ADC capable (A0).                             |
| **IO1**     | GPIO/ADC  | General-purpose I/O, ADC capable (A1).                             |
| **IO2**     | GPIO/ADC/SPI | ADC capable (A2). Default SPI **MISO**. Also the LP core's dedicated I2C data pin (LP_SDA). |
| **IO3**     | GPIO/ADC  | ADC capable (A3). Also the LP core's dedicated I2C clock pin (LP_SCL). |
| **IO4**     | GPIO/ADC/I2C | ADC capable (A4). Default I2C **SDA** pin (used by `Wire.begin()` with no arguments) - also feeds the Qwiic connector. Also the LP core's dedicated UART RX pin (LP_RX). |
| **IO5**     | GPIO/ADC/I2C | ADC capable (A5). Default I2C **SCL** pin - also feeds the Qwiic connector. Also the LP core's dedicated UART TX pin (LP_TX). |
| **IO6**     | GPIO/ADC/SPI | ADC capable (A6). Default SPI **SCK**.                          |
| **IO7**     | GPIO/ADC/SPI | ADC capable (A7). Default SPI **MOSI**. Also a boot strapping pin - see the note below. |
| **IO8**     | GPIO/ADC  | ADC capable (A8). Also drives the onboard WS2812B status LED, so anything you connect here interacts with that LED too. |
| **IO9**     | GPIO/ADC  | General-purpose I/O, ADC capable (A9).                             |
| **IO10**    | GPIO/ADC/SPI | ADC capable (A10). Default SPI **CS**.                          |
| **IO13**    | GPIO/ADC  | General-purpose I/O, ADC capable (A13). Also the ESP32-C5's native USB **D-** pin, which this board leaves unused. |
| **IO14**    | GPIO/ADC  | General-purpose I/O, ADC capable (A14). Also the ESP32-C5's native USB **D+** pin, which this board leaves unused. |
| **IO23**    | GPIO/ADC  | General-purpose I/O, ADC capable (A23).                            |
| **IO24**    | GPIO/ADC  | General-purpose I/O, ADC capable (A24).                            |
| **IO25**    | GPIO/ADC  | General-purpose I/O, ADC capable (A25). Also a boot strapping pin - see the note below. |
| **IO28**    | GPIO/ADC  | ADC capable (A28). Also wired to the onboard USER/boot-select button, with a 10 kΩ pull-up, and it is the chip's boot strapping pin. |

<InfoBox>All GPIO pins operate at **3.3 V logic** - **do not connect 5 V signals directly to GPIO pins**. Always verify signal levels before connecting external peripherals.</InfoBox>

<InfoBox>**What are the LP pins?** Besides the main high-performance (HP) core that runs your Arduino sketch, the ESP32-C5 has a separate low-power (LP) core that can keep simple tasks going (like watching a sensor over I2C) while the HP core sleeps to save power. The LP core's I2C and UART peripherals are fixed to specific pins, and they are not extra pins - they sit on GPIOs the board already uses: **LP_SDA/LP_SCL** on IO2/IO3, and **LP_RX/LP_TX** on IO4/IO5, which are also the default I2C pins feeding the Qwiic connector. So if you drive the LP UART, you give up the I2C bus and Qwiic on those two pins. In Arduino, IO2/IO3 are also available as the second I2C bus, `Wire1`. You only need to think about any of this if you program the LP core directly (for example through ESP-IDF's LP-core APIs) - for normal sketches on the HP core, these behave as regular GPIO/I2C/UART pins.</InfoBox>

<InfoBox>**Strapping pins.** The ESP32-C5 samples **IO7**, **IO25** and **IO28** at reset to decide how it boots. They work as ordinary GPIO once the board is running, but external pull-ups, pull-downs or loads on them can stop the board from booting or from entering download mode. If you need to attach something to one of these, prefer a pin that is free of strapping duty, or make sure your circuit does not hold the pin during reset.</InfoBox>

---

## USB and serial

The USB-C port is wired to an onboard **CH340K** USB-to-UART bridge, which talks to the module over **UART0** (**IO11** = TX, **IO12** = RX). The same two lines are broken out on the **TXD** and **RXD** header pins through 1 kΩ series resistors.

- Your computer sees the board as a **USB serial port**, so a CH340 driver may be needed on Windows and macOS. Most recent systems ship with one.
- The bridge's DTR and RTS lines drive the reset and boot pins, so uploads start automatically without touching any buttons.
- Because serial goes through the bridge rather than the chip's own USB peripheral, the ESP32-C5's **native USB** (USB-Serial-JTAG, USB HID, USB debugging) is **not available** on the USB-C port. Its D-/D+ pins, IO13 and IO14, are free for other uses.

<InfoBox>Anything you attach to **TXD** or **RXD** shares the bus with the programming traffic. A device that drives those lines can block uploads and garble the Serial Monitor - use a different UART on other GPIO pins if you need a permanent serial peripheral.</InfoBox>

---

## Onboard LEDs

| LED           | Colour | Meaning                                                                 |
| ------------- | ------ | ----------------------------------------------------------------------- |
| **PWR**       | Purple | Lit whenever the 3.3 V rail is up. Can be disabled with **JP2**.        |
| **CHRG**      | Red    | On while the battery is charging, off once charging finishes.            |
| **RX**        | Blue   | Flickers on serial traffic from your computer to the board.              |
| **TX**        | White  | Flickers on serial traffic from the board to your computer.              |
| **WS2812B**   | RGB    | Addressable status LED on **IO8**, available as `RGB_BUILTIN` in Arduino. |

---

## Qwiic Connector

<CenteredImage src="/img/easyc_transparent.png" alt="Qwiic connector" width="550px" />

<InfoBox>The **NULA Dual ESP32-C5** includes a **Qwiic connector** for plug-and-play I²C peripherals. This allows fast prototyping with sensors, displays, and other modules without soldering.</InfoBox>

<QuickLink
  title="Qwiic details and specifications"
  description="Learn more about Qwiic hardware compatibility and connector pinout."
  url="/qwiic"
/>

---

## JST Battery Connector

The **NULA Dual ESP32-C5** includes a **JST connector** for connecting a **3.7 V Li-Ion or Li-Poly battery**, enabling fully wireless, battery-powered operation.

<InfoBox>Connect a **3.7 V Li-Ion or Li-Poly battery** via the onboard JST connector. The board includes an integrated battery charging circuit - when powered via USB-C, the battery will charge automatically.</InfoBox>

<QuickLink
  title="Li-Ion Battery 3.7 V"
  description="Rechargeable 3.7 V Li-Ion battery compatible with the NULA Dual ESP32-C5's JST connector."
  url="https://soldered.com/categories/power-sources-batteries/batteries/lithium-batteries/"
  image="/img/li-ion-battery/333284.jpg"
/>

---

## Power Supply

- **USB-C port** used for programming and power input (5 V), protected by a **500 mA** resettable fuse.
- **JST battery connector** (also mirrored on the **VBAT** header pin) for a 3.7 V Li-Ion/Li-Poly battery. The onboard **TP4056** charger runs at roughly **400 mA** and charges the battery whenever USB-C is connected.
- An automatic power-source-selection circuit picks USB 5 V over the battery whenever both are present, exposed on the **VCC** header pin.
- A **TPS7A2633** regulator steps that supply down to a stable **3.3 V** rail for the module and all peripherals. It can supply up to 500 mA, but bear in mind the 500 mA input fuse is shared with battery charging.
- Logic level is **3.3 V** - **do not connect 5 V signals directly to GPIO pins**.

<InfoBox>**Reading the battery level.** The battery voltage is not routed to any GPIO through a divider, so a sketch cannot measure the state of charge. If you need battery monitoring, wire your own divider from **VBAT** to a free analog-capable pin, keeping the divider output below 3.3 V.</InfoBox>

---

## Jumper Details

This board contains two hardware jumpers, both marked on the silkscreen and visible in the pinout diagram above:

{/* Add jumper images to /img/nula_dual_esp32-c5/ and uncomment the carousel below.

<FlickityCarousel
  images={[
    { src: '/img/nula_dual_esp32-c5/jp1.png', alt: 'nula-dual-esp32-c5-jp1', caption: 'JP1' },
    { src: '/img/nula_dual_esp32-c5/jp2.png', alt: 'nula-dual-esp32-c5-jp2', caption: 'JP2' },
  ]}
  jumpers={true}
/>

*/}

| Jumper  | Default State        | Function                                              |
| ------- | -------------------- | ----------------------------------------------------- |
| **JP1** | NC (Normally Closed) | Connects the onboard 10 kΩ I²C pull-up resistors to 3.3 V. |
| **JP2** | NC (Normally Closed) | Enables the power LED. Open it to save a little current on battery power. |

---

## Dimensions

- **Board dimensions:** 26 × 63 mm (1.02 × 2.48 inch)
- **Board thickness:** 1.6 mm, 2-layer PCB
- **Header pin holes:** 1.0 mm, on the standard 2.54 mm pitch
- **Screw hole:** One 3.2 mm hole, designed for an M3 screw

Soldered boards are LEGO compatible! 🧱

---

## Hardware repository

Schematics, KiCad files, Gerber files and more can be found in the GitHub repository:

<WarningBox>The hardware repository for this board is not available yet! We're working on it. In the meantime, please [**contact us**](https://soldered.com/contact/) to receive the hardware files.</WarningBox>

{/* Once the repo is live, replace the WarningBox above with:

<QuickLink
  title="NULA Dual ESP32-C5 Hardware Design"
  description="GitHub hardware repository for this product"
  url="https://github.com/SolderedElectronics/..."
/>

*/}

These pages describe hardware revision **v1.0**.

The hardware repository contains everything you need to understand, modify, or manufacture the board. The different output folders are versioned. You can check which board version you have specifically by finding the version mark on the PCB.

Below is an overview of the available files.

#### CAD files

We use KiCad, an open-source PCB design tool. You can open and edit the `.kicad_pro` project file, which includes both the schematic and PCB layout.

The `PANEL` files are used internally for production.

#### Schematic

The **OUTPUTS** folder contains the **schematic** in `.pdf` format, exported from KiCad.

#### BOM (Bill of Materials)

The bill of materials (BOM) is provided in two formats:

- A **standard `.csv` table**, listing all components, part numbers, and values.
- An **interactive BOM (`.html`)** that visually highlights each component on the PCB, making it easy to locate and reference parts.

#### 3D files

A **3D model** of the PCB is available in `.step` format, allowing you to inspect the board design in CAD software.

#### Gerber files

Gerber files are essential for PCB manufacturing, as they contain precise instructions for each layer of the board. The repository includes standard Gerber outputs in a .zip file, such as:

- **Copper layers** (`.Cu.gbr`) - Defines the traces and pads on the board.
- **Solder mask layers** (`.Mask.gbr`) - Specifies the protective solder mask.
- **Silkscreen layers** (`.Silkscreen.gbr`) - Contains text and component markings.
- **Paste layers** (`.Paste.gbr`) - Used for stencil fabrication in SMD assembly.
- **Drill files** (`.drl`) - Provides drilling coordinates for vias and holes.
- **Board outline** (`.Edge_Cuts.gbr`) - Defines the shape of the PCB.
- **Gerber job file** (`.gbrjob`) - Describes the set of Gerber files used for production.

These files are ready for fabrication and can be used in PCB manufacturing.

#### Compliance

The **Compliance** section includes important regulatory and safety documentation for this product. These files ensure compliance with relevant industry standards and legal requirements.

- **CE** - Certification document confirming compliance with EU safety, health, and environmental requirements.
- **UKCA** - UKCA (UK Conformity Assessed) certification for the UK market.
- **Safety Instructions** - Safety guidelines and precautions in English and in German.
- **Info.txt** - Contains product details such as SKU, country of origin, HS tariff code, and barcode.

