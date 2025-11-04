---
slug: /i2s-audio-amplifier/how-it-works 
title: Stereo I2S Audio Amplifier - How it works
sidebar_label: How it works
id: i2s-audio-amplifier-how-it-works 
hide_title: False
---

## MAX98357A

**MAX98357A** is an easy-to-use digital PCM input **Class D** amplifier with **Class AB** audio performance. It supports standard **I2S** digital audio data, eliminating the need for and external master clock (MCLK) signal that would typically be used for PCM communication. The amplifier supports **sample rates** from **8kHz to 96kHz** using **16, 24, 32-bit** audio data. From a single 2.5V to 5.5V supply, it delivers up to **3.2 watts** of power into a 4Ω speaker at 5V with 92% efficiency and low distortion (0.013% THD+N at 1kHz). It can be configured to output the left channel, right channel, or mixed (L/2 + R/2) signal for both **mono** and **stereo** configurations.

<CenteredImage src="/img/i2s-audio-amp/i2s-audio-amp-chip-select.png" alt="MAX98367A on board" caption="Dual MAX98367A on board" width="700px"/>

---

## Datasheet
For an in-depth look at technical specifications, refer to the official MAX98357A Datasheet:

<QuickLink  
  title="MAX98357A Datasheet"  
  description="Detailed technical documentation for the MAX98357A Class D Amplifier"  
  url="https://soldered.com/productdata/2025/10/max98357a_datasheet_soldered.pdf"  
/>

---

## How It Works

<CenteredImage src="/img/i2s-audio-amp/i2s-audio-amp-diagram.png" alt="MAX98367A diagram" caption="Simplified block diagram by Analog Devices" width="700px"/>

**MAX98357A** takes a digital audio signal in I2S format, that incoming signal is then processed by a built-in **DAC (digital-to-analog converter)** inside the chip and further amplified by a **Class D** output stage. The filterless (output connects straight to the speaker without external filters) Class D amplifier offers much higher efficiency than Class AB amplifier due to the switching operation of the output stage transistors, delivering power efficiently with little heat. The amplifier automatically detects the audio format and sample rate. 

### Gain selection