---
slug: /ws2812b/hardware
title: WS2812B - Hardware details
id: ws2812b-hardware
hide_title: false
---

## Pinout

<CenteredImage src="/img/ws2812b/pinout.jpg" alt="Pinout" />

Click [**here**](https://soldered.com/productdata/2022/03/Smart-LED-WS2812B-Stick10.png) for a high-resolution image of the pinout.

<CenteredImage src="/img/ws2812b/pixel_pinout.jpg" alt="Pinout" />

Click [**here**](https://soldered.com/productdata/2022/03/Smart-LED-WS2812B-Pixel.png) for a high-resolution image of the pinout.

<CenteredImage src="/img/ws2812b/ring7_pinout.jpg" alt="Pinout" />

Click [**here**](https://soldered.com/productdata/2022/03/Smart-LED-WS2812B.png) for a high-resolution image of the pinout.

<ErrorBox>The pinout images for the Ring12 and Ring24 versions haven't been generated yet! We're working on it!</ErrorBox>

### Pin details

<InfoBox>Ignore the **DIN** and **DOUT** pins if using the Pixel version!</InfoBox>

| Pin Marking | Pin Name      | Description                                                          |
| ----------- | ------------- | -------------------------------------------------------------------- |
| **VCC**     | Power (+5V)   | Supplies power to the LED strip. Typically powered by a 5V source.   |
| **GND**     | Ground        | Common ground for both the power and signal.                         |
| **DIN**     | Data Input    | Input pin for receiving the data signal from the microcontroller.    |
| **DOUT**    | Data Output   | Output pin for passing the data signal to the next LED (in a chain). |

<InfoBox>The **DIN** pin is used to receive data from a microcontroller such as an Arduino or Raspberry Pi. The **DOUT** pin passes the data to the next LED in a daisy-chained setup.</InfoBox>
<WarningBox>Ensure a stable **5V** power supply to avoid damage to the LEDs!</WarningBox>

---

## Dimensions

- **LED Dimensions:** 5mm x 5mm (per LED chip)
- **LED Pitch (spacing between LEDs):** 10mm
- **Stick10 version**
   - **Screw Holes:** Designed for M3 screws (3.2 mm diameter)
   - **Dimensions:** 80 x 10 mm (3.15 x 0.4 inch)
- **Pixel version**
   - **Dimensions:** Diameter of 10mm (0.4 inch)
- **Ring7 version**
   - **Dimensions:** Diameter of 23mm (0.9 inch)
- **Ring12 version**
   - **Dimensions:** Outer diameter of 44mm (1.6 inch)
- **Ring24 version**
   - **Dimensions:** Outer diameter of 67mm (2.6 inch)
- Soldered boards are LEGO compatible! 🧱

---

## Power and Voltage Requirements

The **WS2812B** operates with a **5V** supply, which is typically delivered to the **VCC** pin. It can handle up to **60mA** per LED at full white (RGB) brightness, and power consumption will depend on the color and brightness settings used.

- **Operating Voltage:** 5V DC
- **Current Consumption:** Up to 60mA per LED at full brightness (white color)
- **Power Supply Recommendation:** Use a **5V DC power supply** that can provide sufficient current for the total number of LEDs in the chain.

<WarningBox>Ensure that the power supply can handle the total current draw. For example, a 1-meter strip with 30 LEDs at full brightness can draw up to 1.8A of current.</WarningBox>

---

## Hardware repository

Schematics, KiCad files, Gerber files, and more can be found in the GitHub repository:

<QuickLink 
  title="Smart LED WS2812B Stick10 Hardware Design" 
  description="GitHub hardware repository for this product"
  url="https://github.com/SolderedElectronics/Smart-LED-WS2812B-Stick10-hardware-design" 
/> 

<QuickLink 
  title="Smart LED WS2812B Pixel Hardware Design" 
  description="GitHub hardware repository for this product"
  url="https://github.com/SolderedElectronics/Smart-LED-WS2812B-Pixel-hardware-design" 
/> 

<QuickLink 
  title="Smart LED WS2812B Ring7 Hardware Design" 
  description="GitHub hardware repository for this product"
  url="https://github.com/SolderedElectronics/Smart-LED-WS2812B-Ring7-hardware-design" 
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