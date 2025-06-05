---
slug: /tft-lcd/how-it-works
title: How it works
id: tft-lcd-how-it-works
hide_title: false
---

The **TFT LCD Breakout 2.4" with Touch** features a vibrant color display based on the **ILI9341** driver, which communicates over a **SPI interface** and includes **resistive touch** capabilities. This module is ideal for visual interfaces in embedded projects, offering full color support and fast refresh rates.

<CenteredImage src="/img/tft-lcd/tftlcd.png" alt="TFT LCD Breakout 2.4 with Touch" caption="TFT LCD 2.4 with Touch" width="400px" />

---

## Driver and Communication

The breakout uses the **ILI9341 TFT display driver**, which supports SPI communication and 240x320 resolution. Most drawing operations are handled through this controller.

- **Resolution**: 240 × 320 pixels
- **Colors**: 65K full color (RGB565)
- **Interface**: SPI (Serial Peripheral Interface)
- **Touch panel**: 4-wire resistive


---

## Datasheets and References

<QuickLink  
  title="ILI9341 Datasheet (Sitronix)"  
  description="Detailed register and graphics command set documentation"  
  url="https://cdn-shop.adafruit.com/datasheets/ILI9341.pdf"
/>

<QuickLink  
  title="Touchscreen Controller (XPT2046) Datasheet"  
  description="Touch panel controller for resistive screens (SPI)"  
  url="https://www.ti.com/lit/ds/symlink/xpt2046.pdf"
/>

---

## SPI Interface

The ILI9341 communicates using SPI, which allows for fast transmission with minimal pins. Typical connections include:

| Function | Description             |
|----------|-------------------------|
| `CLK`    | SPI Clock (SCK)         |
| `DI`     | MOSI – Data to display  |
| `CSL`    | Chip select for display |
| `DC`     | Data/Command selector   |
| `RST`    | Optional hardware reset |
| `BL`     | Backlight (connect to VCC) |
| `CST`    | Chip select for touchscreen (XPT2046) |

> Note: MISO (D0) is not needed unless you're reading from the display or touchscreen controller.

---

## Initialization Process

1. **Power-on Reset**  
   Upon power-up, the ILI9341 needs to be initialized using a specific command sequence over SPI.

2. **Display Setup**  
   This includes setting the pixel format (e.g., RGB565), memory access mode (rotation), and enabling the display output.

3. **Touch Initialization (Optional)**  
   The XPT2046 touch controller is also SPI-based and requires its own CS pin. It returns analog X/Y positions based on resistive input.

---

## How Rendering Works

The display supports:

- Drawing pixels, lines, rectangles, circles
- Writing text (via GFX-compatible fonts)
- Filling the screen
- Pushing full-frame bitmap data

All commands are transmitted as SPI byte sequences to the ILI9341, which handles internal RAM addressing and pixel control.

---

## Touchscreen Functionality

The touchscreen is a **4-wire resistive panel** handled by the **XPT2046** chip. To read touch input:

- The microcontroller selects the **CST** pin (CS for touch)
- Sends SPI commands to initiate an ADC read
- X/Y values are returned as 12-bit coordinates

Many libraries handle this behind the scenes.

---

## Summary

| Feature              | Value                         |
|----------------------|-------------------------------|
| Display Driver       | ILI9341                       |
| Resolution           | 240 × 320                     |
| Color Depth          | 16-bit RGB (5-6-5)            |
| Interface            | SPI (up to 40MHz)             |
| Touchscreen IC       | XPT2046 (SPI)                 |
| Touch Type           | 4-wire resistive              |

---

## Applications

- Battery-powered visual interfaces
- Touch-based menu navigation
- Graphing and plotting in portable instruments
- Custom dashboards and GUIs

<InfoBox>To get started, check out the example sketches in the Inkplate Arduino Library or Adafruit GFX/ILI9341 examples. Most are compatible with this breakout by changing pin definitions.</InfoBox>
