---
slug: /i2s-audio-amplifier/arduino/examples 
title: Stereo I2S Audio Amplifier - Sound over SD card
sidebar_label: Sound over SD card
id: i2s-audio-amplifier-arduino-2 
hide_title: False
---

## Initialization

<InfoBox>
**Important notes for uploading code:**
- Under **Tools -> Board**, select **ESP32 Dev Module** and correct serial port
- Set:
  - PSRAM: **Enabled**
  - Partition Scheme: **Huge APP (NO OTA)**
</InfoBox>

To use the amplifier we need to initialize the audio object by including the library and setting the pins to which the amplifier board is connected.

```cpp
#include "Soldered_I2S_Audio_Amplifier.h"

// Declare amplifier GPIOs used
#define I2S_DOUT 25
#define I2S_BCLK 27
#define I2S_LRCLK 26

I2SAudio audio;

audio.setPinout(I2S_BCLK, I2S_LRCLK, I2S_DOUT);
```

## Playing audio from SD card
