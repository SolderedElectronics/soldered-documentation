---
slug: /inkplate/6motion/hardware/esp32
title: ESP32 co-processor
id: 6motion-hardware-esp32
hide_title: true
---


<SectionTitle title="ESP32 co-processor" backgroundImage="/img/esp32.jpg" />  

Inkplate 6 MOTION features an **ESP32-C3-WROOM-02** module, which serves as a **WiFi co-processor**. It communicates with the **STM32** via **SPI**, using **AT commands** to handle network operations.  

In our documentation and code, you may sometimes see the **ESP32 co-processor** referred to as the **ESP32 modem**, as it functions similarly to traditional modems by processing network-related tasks.  

<CenteredImage src="/img/inkplate_6_motion/esp32.jpg" alt="ESP32-C3 on Inkplate 6 MOTION" caption="ESP32-C3 co-processor on Inkplate 6 MOTION" width="500px"/>  

---

## ESP-AT Firmware  

<WarningBox>Overwriting the ESP32 firmware that comes pre-installed on Inkplate 6 MOTION will **disable WiFi functionality!**</WarningBox>  

The ESP32-C3 runs **ESP-AT**, an official firmware by **Espressif** that enables the ESP32 to act as a co-processor controlled via AT commands. This setup allows the STM32 to request the ESP32 to **connect to WiFi, download files, and transmit data** over SPI.  

<InfoBox>The ESP32 on Inkplate 6 MOTION is running the official **esp-at** firmware. Learn more in Espressif’s official repository:<QuickLink 
  title="ESP-AT" 
  description="Official repository by Espressif, control your ESP32 device with AT commands." 
  url="https://github.com/espressif/esp-at" 
/></InfoBox>  

The **ESP-AT binary** used on Inkplate 6 MOTION was built using Espressif's official tools. If you’re interested in compiling your own version, refer to the [**ESP-AT documentation**](https://docs.espressif.com/projects/esp-at/en/latest/esp32/index.html).  

<WarningBox>Build details and the official binary for Inkplate 6 MOTION’s ESP32-C3 will be available soon.</WarningBox>  

---

## Using ESP32 with the Inkplate Library  

The Inkplate library includes a **software driver** that manages the ESP32 co-processor, making WiFi features easy to use. Check out the [**WiFi example**](/inkplate/6motion/wifi/wifi-basics/) for practical implementation.  

If you're curious about **how the driver works internally**, you can explore its **low-level communication** with the ESP32 in the [**source files**](https://github.com/SolderedElectronics/Inkplate_Motion_Arduino_Library/tree/main/src/system/wifi) inside the Inkplate MOTION library (`src/system/wifi`).  

Additionally, Espressif provides an **[AT Command Set](https://docs.espressif.com/projects/esp-at/en/latest/esp32/AT_Command_Set/index.html)** detailing all the available AT commands. The Inkplate driver only uses a **subset of these commands**, focusing on essential WiFi functionality.  

<InfoBox>Want to send your own AT commands? Check out this example:<QuickLink  
  title="Inkplate_6_Motion_WiFi_Command_Sender.ino"  
  description="An Inkplate 6 MOTION Arduino library example where you can send AT commands via Serial and receive responses from the ESP32."  
  url="https://github.com/SolderedElectronics/Inkplate_Motion_Arduino_Library/blob/main/examples/Inkplate6Motion/Diagnostics/Inkplate_6_Motion_WiFI_Command_Sender/Inkplate_6_Motion_WiFI_Command_Sender.ino"  
/></InfoBox>  