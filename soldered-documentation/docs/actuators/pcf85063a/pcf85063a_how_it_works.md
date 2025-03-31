---
slug: /pcf85063a/how-it-works 
title: How it works
id: pcf85063a-how-it-works 
hide_title: False
---  

The **PCF85063A** is an RTC by **NXP Semiconductors**. When using our board, you are essentially communicating with the onboard PCF85063A directly via **I2C communication**.

<CenteredImage src="/img/pcf85063a/onboard.webp" alt="PCF85063A onboard" caption="PCF85063A onboard" />

---

## Datasheet

For an in-depth look at technical specifications, refer to the official PCF85063A Datasheet:  

<QuickLink  
  title="PCF85063A Datasheet"  
  description="Detailed technical documentation for the PCF85063A RTC"  
  url="https://soldered.com/productdata/2022/03/Soldered_PCF85063A_datasheet.pdf"  
/>  

---

## Overview

The **Real-Time Clock (RTC)** component provides accurate time and date information for the system. The time and date are updated every second based on a one pulse per second interrupt from a **32.768-kHz crystal**. Clock accuracy is based on the crystal provided and is typically 20 ppm.
The RTC keeps track of the second, minute, hour, day of the week, day of the month, day of the year, month, and year. The day of the week is automatically calculated from the day, month, and year. Daylight saving time may be optionally enabled and supports any start and end date, as well as a programmable saving time. The start and end dates may be absolute like 24 March or relative like the second Sunday in May.

---

## I2C Communication

The PCF85063A uses the I2C protocol to communicate with a microcontroller. It operates with a fixed I2C address of **0x51**. Upon request, the RTC returns the current second, hour, day, week, and month. Upon initialization, the RTC must be supplied with the current time and date.