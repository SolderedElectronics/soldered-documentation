---
slug: /SPK0641HT-microphone/arduino/troubleshooting 
title: MEMS Microphone SPK0641HT4H Breakout - Troubleshooting
sidebar_label: Troubleshooting
id: spk0641ht-arduino-5
hide_title: true
pagination_next: null
---

# Troubleshooting

This page lists common issues and quick checks when using the **SPK0641HT4H-1 PDM microphone**.

<ExpandableSection title="Microphone won’t initialize">

- Double-check wiring:  
  - **3V3 → 3.3 V**  
  - **GND → GND**  
  - **CLK → PDM clock pin (e.g. IO4 on ESP32)**  
  - **DATA → PDM data pin (e.g. IO27 on ESP32)**  
  - **SEL → Optional (for left/right channel selection)**  

- Ensure your code calls `mic.begin(dataPin, clkPin, sampleRate, bitDepth, bufferSize)`.  
- Use supported sample rates (commonly **16 kHz–48 kHz**) and 16-bit depth.  
- Check that your board provides a **stable 3.3 V supply**.

</ExpandableSection>

<ExpandableSection title="No audio data / mic.read() returns 0">

- Verify the **clock pin** is providing a proper signal (in MHz range, e.g. 1–3 MHz for 16 kHz sample rate).  
- If you see only zeros, lower the buffer size or sample rate as a test.  
- Make sure you are regularly calling `mic.read()` in `loop()` so buffers don’t overflow.  
- Use the **Serial Plotter** example to confirm raw output before moving to streaming or saving.

</ExpandableSection>

<ExpandableSection title="Distorted or clipped audio">

- Gain may be too high: reduce with `mic.setGainDb(x)` (try 0 dB or 6 dB instead of 10 dB).  
- Check your sound source isn’t too close or too loud. The microphone’s **acoustic overload point is ~120 dB SPL**.  
- Use the high-pass filter (`mic.setHPF(true)`) to remove DC offset and low-frequency noise.  
- Ensure your data handling (e.g., saving to SD) isn’t dropping samples.

</ExpandableSection>

<ExpandableSection title="No sound in web or WAV examples">

- Confirm your SD card is FAT32 formatted and wiring for **CS/MISO/MOSI/SCK** is correct (for WAV example).  
- For the **voice-to-web example**, connect to the ESP32’s Wi-Fi AP and open the page at the printed IP in Serial Monitor.  
- If you hear only static, check **sample rate matching**: browser expects **16 kHz PCM**, so keep ESP32 configured for 16 kHz.  
- Some browsers block autoplay of audio – click “Start” to begin streaming.

</ExpandableSection>

<ExpandableSection title="SEL pin confusion">

- **SEL high = left channel**, **SEL low = right channel**.  
- If you only use one microphone, SEL can be tied to **GND** or **3V3** (doesn’t matter, just pick a channel).  
- When using **two microphones on the same DATA line**, set one SEL high and the other low for stereo.

</ExpandableSection>

<ExpandableSection title="Audio seems too quiet">

- The microphone sensitivity is around **–26 dBFS**. That means normal speech won’t fill the entire waveform range.  
- Increase digital gain with `mic.setGainDb(10.0f)` or process audio in software after capture.  
- Make sure you’re interpreting samples as signed **16-bit PCM** (not unsigned).

</ExpandableSection>

<ExpandableSection title="ESP32 freezes or resets during recording">

- SD writes can block if the card is slow – try a higher-quality card.  
- Lower the sample rate (e.g. 16 kHz) to reduce throughput.  
- Ensure **heap/stack** are sufficient; use smaller buffers if needed.  
- Avoid powering mic and SD card from USB alone if unstable – provide a stable 3.3 V regulator.

</ExpandableSection>
