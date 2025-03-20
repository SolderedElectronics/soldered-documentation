---
slug: /ch340/hardware 
title: Hardware details
id: ch340-hardware 
hide_title: False
---

## Pinout

<CenteredImage src="/img/ch340/pinout.png" alt="USB-UART CH340 converter pinout diagram" caption="USB-UART CH340 converter pinout diagram"/>

Click [**here**](https://soldered.com/productdata/2022/03/USB-UART-converter.png) for a high reoslution image of the pinout.

## Pin Details

<WarningBox>**Mandatory pins** for basic operation are **VCC, GND, RXD** and **TXD**.</WarningBox>

| Pin Marking | Pin Name      | Description                                                                          |
| ----------- | ------------- | ------------------------------------------------------------------------------------ |
| **VCC**     | Power Input   | Main power input (usually **5V**) for the CH340 module.                              |
| **GND**     | Ground        | Common ground for all signals and power connections.                                 |
| **RXD**     | Receive Data  | Serial data input (data received from the USB host or external device).              |
| **TXD**     | Transmit Data | Serial data output (data sent to the USB host or external device).                   |

<InfoBox>**Optional pins** for additional features are **3V3, 5V** and **R232**.</InfoBox>

| Pin Marking | Pin Name      | Description                                                                          |
| ----------- | ------------- | ------------------------------------------------------------------------------------ |
| **3V3**     | 3.3V Output   | Provides a **3.3V** output from the CH340, useful for powering low-voltage circuits. |
| **5V**      | 5V Output     | Provides a **5V** output, typically used to power external devices.                  |
| **R232**    | RS-232 Signal | Used for RS-232 communication (specific function depends on implementation).         |

<InfoBox>**Hardware flow control pins** (**CTS, RTS, DTR, DSR, DCD**) can be used for **advanced serial communication**. </InfoBox> 

| Pin Marking | Pin Name            | Description                                                           |
| ----------- | ------------------- | --------------------------------------------------------------------- |
| **CTS**     | Clear to Send       | Hardware flow control signal, used to indicate when data can be sent. |
| **RTS**     | Request to Send     | Hardware flow control signal, used to request data transmission.      |
| **DTR**     | Data Terminal Ready | Signals that the device is ready to communicate.                      |
| **DSR**     | Data Set Ready      | Indicates that the device is ready to receive data.                   |
| **DCD**     | Data Carrier Detect | Detects the presence of a connected device in serial communication.   |

<InfoBox>The CH340 USB-UART converter is compatible with **Windows, macOS, and Linux**. Ensure that you select the correct driver for your operating system.</InfoBox>

<WarningBox>Make sure you're using a **data-capable USB cable**. Some USB cables only provide power and do not support data transfer.</WarningBox>

<WarningBox>Ensure that **GND** is properly connected to establish a common reference for all signals.</WarningBox>

<WarningBox>Ensure that **RXD (Receive) is connected to TXD (Transmit) on the target device**, and **TXD is connected to RXD**. Incorrect wiring will result in no communication.</WarningBox>

---

## Jumper Details

| Jumper  | Default State            | Function                  |
| ------- | ------------------------ | ------------------------- |
| **JP1** | **NC** (Normally closed) | Connects 3V3 with an LED. |

<CenteredImage src="/img/ch340/jp1pwrled.png" alt="USB-UART CH340 converter pinout diagram" caption="JP1 on the board" width="500px"/>

---

## Voltage Selection Switch

Used for selecting 5V or 3V3 Power supply on the VCC pin.

<CenteredImage src="/img/ch340/voltageswitch.png" alt="USB-UART CH340 converter pinout diagram" caption="Voltage switch on the board" width="500px"/>

---

## Dimensions

- **Board Dimensions:** 38 × 22 mm (1.5 × 0.9 inch)  
- **Header Pin Holes:** 1.5 mm  
- **Screw Holes:** Designed for M3 screws (3.2 mm diameter)  
- Soldered boards are LEGO compatible! 🧱 

---

## Hardware repository

Schematics, KiCad files, Gerber files and more can be found in the GitHub repository:

<QuickLink 
  title="USB-UART CH340 converter board Hardware design" 
  description="GitHub hardware repository for this product"
  url="https://github.com/SolderedElectronics/USB-UART-CH340C-converter-board-hardware-design/tree/main" 
/> 


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

- **Copper layers** (`.Cu.gbr`) – Defines the traces and pads on the board.  
- **Solder mask layers** (`.Mask.gbr`) – Specifies the protective solder mask.  
- **Silkscreen layers** (`.Silkscreen.gbr`) – Contains text and component markings.  
- **Paste layers** (`.Paste.gbr`) – Used for stencil fabrication in SMD assembly.  
- **Drill files** (`.drl`) – Provides drilling coordinates for vias and holes.  
- **Board outline** (`.Edge_Cuts.gbr`) – Defines the shape of the PCB.  
- **Gerber job file** (`.gbrjob`) – Describes the set of Gerber files used for production.  

These files are ready for fabrication and can be used in PCB manufacturing.

#### Compliance  

The **Compliance** section includes important regulatory and safety documentation for this product. These files ensure compliance with relevant industry standards and legal requirements.  

- **CE** – Certification document confirming compliance with EU safety, health, and environmental requirements.  
- **UKCA** – UKCA (UK Conformity Assessed) certification for the UK market.  
- **Safety Instructions** – Safety guidelines and precautions in English and in German.
- **Info.txt** – Contains product details such as SKU, country of origin, HS tariff code, and barcode.  
