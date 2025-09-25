---
slug: /inkplate/10/micropython/deep-sleep
title: Inkplate 10 MicroPython - Deep sleep
sidebar_label: Deep sleep
id: deep-sleep
---

Using deep sleep on Inkplate 10 is crucial for writing a sketch that maximizes fficiency. Since e-Paper does not require any power to retain the displayed image, Inkplate 10 can consume little or no current while in deep sleep mode, enabling a sketch to run for months on battery.

---

<InfoBox> When your ESP32 wakes up from deep sleep, it performs a reset and runs **main.py** again. That means your main script is executed on every every wake-up. </InfoBox>

<WarningBox> Make sure you’ve uploaded a **main.py** file to the ESP32. Put the code you want to run after each wake-up inside it.</WarningBox>

Basic example keeping a counter in **RTC memory** using **raw bytes.**

```python

```