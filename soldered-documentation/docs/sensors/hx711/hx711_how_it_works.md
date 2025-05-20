---
slug: /hx711/how-it-works  
title: How it works  
id: hx711-how-it-works  
hide_title: False  
---

The **HX711** is a precision 24-bit analog-to-digital converter (ADC) designed for **weigh scales** and **industrial control applications**. Manufactured by [**AVIA**](http://en.aviaic.com/detail/730856.html), the HX711 provides high-precision digital output and can interface directly with **load cells** for **accurate weight measurements**.

<CenteredImage src="/img/hx711/standard_onboard.png" alt="HX711 Standard Board" caption="HX711 Regular Board" width="500px" />

<CenteredImage src="/img/hx711/easyc_onboard.png" alt="HX711 Standard Board" caption="HX711 Qwiic (easyC) Board" width="500px" />

---

## Datasheet

For detailed technical specifications, please refer to the official HX711 Datasheet:  

<QuickLink  
  title="HX711 Datasheet"  
  description="Complete technical documentation for the HX711 module"  
  url="https://soldered.com/productdata/2022/03/Soldered_hx711_datasheet.pdf"  
/>  

---

## How the HX711 works

The HX711 is designed for **measuring the output from load cells** and converting it into a digital signal that can be processed by a microcontroller. It operates with **high resolution** and **low power consumption**, making it ideal for applications like **weighing scales** and **force measurement systems**.

- **Load Cell Input** - The HX711 has two differential input channels that can interface directly with a load cell or other high-impedance sensors. It measures the small voltage changes produced by the load cell under pressure or weight.

- **Amplification** - The HX711 features an internal **programmable gain amplifier (PGA)**, which amplifies the signal from the load cell to a level suitable for digitization. The gain can be adjusted between 32, 64, or 128, depending on the application’s required precision.

- **Analog-to-Digital Conversion** - The HX711 uses **24-bit** **sigma-delta ADC** technology to convert the amplified analog signal into a high-resolution digital signal. This allows the HX711 to provide accurate measurements with minimal noise interference.

- **Digital Output** - Once the signal is converted, the HX711 transmits the digital data via its **serial interface** (either **TDM** or **SPI**), enabling easy integration with microcontrollers for further processing or display of the weight values.

---

## Communication Protocol

The HX711 uses a **serial interface** for communication with microcontrollers, making it easy to integrate into various systems. The two primary pins for communication are:

- **Data (DOUT)**: This pin transmits the digital data (weight values) from the HX711 to the microcontroller.  
- **Clock (PD_SCK)**: This pin is used to send clock pulses to the HX711, enabling it to output data sequentially.

With the HX711, the microcontroller can control the rate at which data is clocked out, making it adaptable for different applications. It operates in **single-wire interface** mode, so only two pins are necessary for communication, simplifying the connection between the HX711 and the microcontroller.

---

## Power and Precision

The HX711 operates with a **low-power supply voltage** and is optimized for energy-efficient operation, allowing it to be used in portable and battery-powered devices. Its **high precision** and **low noise** make it suitable for critical applications where accurate weight measurements are necessary.

---

## I2C communication - Qwiic

Qwiic versions of the product use an onboard ATTINY404 MCU to implement I2C communication. The breakout board operates with a default I2C address of **0x30** but can be changed using [**onboard switches**](/hx711/hardware#address-selection-qwiic-version/). When detected, the ATTINY404 receives data from the sensor and passes it to the main MCU using the I2C data line. To check in detail how the ATTINY404 is programmed, refer to the [**firmware GitHub page**](https://github.com/SolderedElectronics/Soldered-HX711-ADC-For-Weight-Scales-Arduino-Library/tree/dev/extras/attiny_firmware).

<CenteredImage src="/img/hx711/hx711_tiny_onboard.png" alt="attiny404 on the HX711 easyC Board" caption="attiny404 on the HX711 easyC Board" width="500px" />