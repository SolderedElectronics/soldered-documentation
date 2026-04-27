---
slug: /barcode-scanner-de2120/how-it-works
title: DE2120 Barcode Scanner – How It Works
sidebar_label: How it works
id: barcode-scanner-de2120-how-it-works
hide_title: true
---

# How it works

The **DE2120** is a compact embedded barcode scan engine manufactured by **DYScan**. Unlike laser-based scanners that sweep a single line across a barcode, the DE2120 uses a **CMOS image sensor** to capture a full 640×480 pixel frame and applies onboard image processing and decoding algorithms — enabling it to read both 1D and 2D barcodes from a single snapshot.

<CenteredImage
  src="/img/barcode-scanner-de2120/onboard.JPG"
  alt="DE2120 barcode scanner on breakout board"
  caption="DE2120 barcode scanner on breakout board"
  width="500px"
/>

## Datasheet

{/*
TODO: Upload datasheet to Soldered CDN and update the URL below
<QuickLink
  title="DE2120 Datasheet"
  description="Detailed technical documentation for the DE2120 2D barcode scan engine"
  url="https://soldered.com/productdata/XXXX/de2120_datasheet.pdf"
/>
*/}

## How scanning works

When a scan is triggered, the DE2120 illuminates the target with its **5600 K white LEDs**, captures a frame with the CMOS sensor, and passes the image to an onboard **32-bit decoder CPU**. The decoder identifies the barcode symbology present in the image, decodes the data, and outputs the result as an ASCII string over the **UART (TTL serial) interface**, terminated by a carriage return (`\r`).

The host microcontroller reads this string using the Arduino library's `readBarcode()` function and can then process or display it.

## UART communication

The module communicates over **TTL serial** at a default baud rate of **9600 bps**. It ships from the factory configured at 115200 bps, but the library automatically negotiates the baud rate down to 9600 bps on first connection.

The communication protocol uses ASCII commands in the following format:

```
^_^COMMAND<ARG>.
```

The module responds with an **ACK** byte (`0x06`) on success or a **NACK** byte (`0x15`) on failure. Barcode scan results are sent as plain ASCII strings terminated with a carriage return.

## Scanning modes

The DE2120 supports three operating modes:

| Mode | Description |
|------|-------------|
| **Manual (Trigger)** | Scans only when a scan command is sent via software or the hardware TRIG pin is pulled low. Default mode. |
| **Continuous** | Scans repeatedly without any trigger. Configurable repeat interval for duplicate codes (output once, no interval, 0.5 s, or 1 s). |
| **Motion Sense** | Activates scanning automatically when motion is detected in front of the sensor. Sensitivity is configurable. |

## Supported barcode symbologies

### 1D Barcodes

| Symbology | Notes |
|-----------|-------|
| UPC-A | Standard retail |
| UPC-E | Compact retail |
| EAN-8 | Short European Article Number |
| EAN-13 | Standard European Article Number |
| Code 128 | High-density alphanumeric |
| GS1-128 | Code 128 with GS1 Application Identifiers |
| Code 39 | Alphanumeric, widely used in industry |
| Code 93 | Compact variant of Code 39 |
| Code 11 | Telecommunications |
| Interleaved 2 of 5 | Numeric, used in shipping |
| Matrix 2 of 5 | Numeric |
| Industrial 2 of 5 | Numeric |
| Standard 2 of 5 | Numeric |
| Codabar (NW-7) | Medical, logistics |
| MSI Plessey | Retail shelf labels |
| GS1 Databar (RSS) | Small item identification |
| China Post | Chinese postal code |

### 2D Barcodes

| Symbology | Notes |
|-----------|-------|
| QR Code | Widely used 2D matrix code |
| Data Matrix | Compact 2D matrix, industrial use |
| PDF417 | Stacked linear barcode, ID documents |
| Micro PDF417 | Compact variant of PDF417 |
| Aztec | 2D matrix, transport tickets |

## Illumination and aiming

The DE2120 has two independent light sources controlled via software:

- **White illumination LEDs (5600 K):** Flood the target with visible light to ensure the CMOS sensor captures a clear image, even in low-light environments. Enabled by default.
- **Red aiming reticle LED (625 nm):** Projects a visible red line to help the user aim at the barcode. Enabled by default.

Both can be independently toggled using `scanner.lightOn()` / `scanner.lightOff()` and `scanner.reticleOn()` / `scanner.reticleOff()`.

## Depth of field

Reading distance varies with barcode size and print quality. The table below shows typical ranges

<CenteredImage src="/img/barcode-scanner-de2120/barcode_depth_of_field.png" alt="Depth of field" caption="DE2120 Depth of field" width="1000px"/>
