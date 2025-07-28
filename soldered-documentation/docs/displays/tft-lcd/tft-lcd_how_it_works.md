---
slug: /tft-lcd/how-it-works
title: 2.4" TFT LCD Breakout with Touch - How it works
id: tft-lcd-how-it-works
sidebar_label: How it works
hide_title: false
---

The **2.4" TFT LCD Breakout with Touch** features a vibrant color display based on the **ILI9341** driver, which communicates over a **SPI interface** and includes **resistive touch** capabilities. This module is ideal for visual interfaces in embedded projects, offering full color support and fast refresh rates.

<CenteredImage src="/img/tft-lcd/tftlcd.png" alt="TFT LCD Breakout 2.4 with Touch" caption="TFT LCD 2.4 with Touch" width="400px" />


## Datasheets and References

<QuickLink  
  title="ILI9341 Datasheet"  
  description="Detailed register and graphics command set documentation"  
  url="https://cdn-shop.adafruit.com/datasheets/ILI9341.pdf"
/>

---

## How the Display Works

The display is controlled by the **ILI9341** driver chip using SPI commands. It supports:

- Drawing primitives (lines, rectangles, circles)
- Text rendering via GFX-compatible fonts
- Full-screen image rendering (bitmaps)
- Rotation and mirroring

All drawing operations are handled by sending SPI commands to the display.

---

## Touchscreen Functionality

The display includes a **4-wire resistive touchscreen** managed by the **XPT2046** controller, which communicates via **SPI**.

When pressed, the touch panel generates analog voltage levels corresponding to X and Y coordinates. These are read by the XPT2046's internal ADC and transmitted as 12-bit values to the microcontroller.

- **Touch interface:** SPI  
- **Controller:** XPT2046  
- **Output:** Raw X, Y coordinates and pressure  

<InfoBox>
Touch data must be read through the `CST` (chip select) pin using SPI. Make sure MISO (`D0`) is connected to your microcontroller to receive data.
</InfoBox>


---

## Display Communication (SPI)

| Signal | Description                       |
|--------|-----------------------------------|
| `CLK`  | SPI clock                         |
| `DI`   | MOSI (data to display)            |
| `CSL`  | Chip Select for ILI9341           |
| `DC`   | Data/Command control              |
| `RST`  | Optional hardware reset           |
| `BL`   | Backlight power or PWM control    |

---

## Rendering Pipeline

1. Microcontroller sends commands over SPI
2. ILI9341 decodes instructions and modifies internal RAM
3. Pixels are refreshed on screen accordingly
4. For touch input, the appropriate controller returns X/Y data