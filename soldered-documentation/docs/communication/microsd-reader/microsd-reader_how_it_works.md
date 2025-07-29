---
slug: /microsd-reader/how-it-works 
title: Microsd Reader – How it works
sidebar_label: How it works
id: microsd-reader-how-it-works 
hide_title: False
---  

The SD card reader's communication is handled by the **TXB0104** chip from **Texas Instruments**.

<CenteredImage src="/img/microsd-reader/texas.jpg" alt="TXB0104 chip on board" caption="TXB0104 chip on board" width="400px" />

---

## Datasheet

For an in-depth look at the technical specifications, refer to the official TXB0104 Datasheet:

<QuickLink  
  title="TXB0104 Datasheet"  
  description="Detailed technical documentation for the TXB0104 chip"  
  url="https://soldered.com/productdata/2022/03/Soldered_TXB0104PWR_datasheet.pdf"  
/>

---

## How an SD Card reader works

An SD card reader facilitates communication between an SD card and a host device by establishing electrical connections and enabling data transfer through standard protocols. Here’s a breakdown of its operation at the electrical level:

### Electrical interface and pin configuration

The micro SD card's SPI interface is implemented using the standard 8-pin micro SD card pinout, with pins corresponding to SPI signals. Here's how the micro SD card pinout relates to the SPI signals:

| Pin  | Pin Name | Description                             |
| ---- | -------- | --------------------------------------- |
| **1** | RSV      | Reserved (Not in use)                   |
| **2** | CS       | Chip selection for SPI                  |
| **3** | DI       | Data input                              |
| **4** | VDD      | Power supply                            |
| **5** | SCLK     | Serial clock for communication          |
| **6** | VSS      | Ground                                  |
| **7** | DAT0     | Data output                             |
| **8** | RSV      | Reserved (Not in use)                   |

<CenteredImage src="/img/microsd-reader/sd_card_pinout.png" alt="Pinout of an SD card" caption="Pinout of an SD card" width="300px" />

### Power-on & Initialization

Once inserted, the SD card reader:

1. Applies power (3.3V) to the SD card via the VDD pin.
2. Performs a voltage check to confirm that the SD card operates within specifications.
3. Activates the pull-up resistors to stabilize signals.
4. Initiates the SD protocol.

### Read operations

1. The host sends a read command via the DI pin.
2. The SD card locates the requested data and transmits it via the DAT0 pin.
3. Synchronization is ensured by the serial clock.

### Write operations

1. The host sends a write command via the DI pin along with data blocks.
2. The SD card writes the data to NAND flash memory while sending status responses.