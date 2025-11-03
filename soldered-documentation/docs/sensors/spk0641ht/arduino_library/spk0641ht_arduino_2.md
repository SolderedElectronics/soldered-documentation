---
slug: /SPK0641HT-microphone/arduino/output-plotting
title: MEMS Microphone SPK0641HT4H Breakout - Output Plotting
sidebar_label: Initialization and Output plotting
id: spk0641ht-arduino-2
hide_title: true
---

# Initialization and Output plotting

## Visualize microphone samples in the Serial Plotter

This example initializes the **SPK0641HT4H-1** on **ESP32** and streams decimated PCM samples to the **Arduino Serial Plotter** for quick signal visualization.

```cpp
#include "Soldered-Microphone-SPK0641HT.h"

constexpr int PDM_CLK = 4;
constexpr int PDM_DIN = 19;

Microphone mic;

void setup() {
  Serial.begin(115200);
  mic.begin(PDM_DIN, PDM_CLK, 16000, 16, 512);
  mic.setHPF(true);
  mic.setGainDb(10.0f);
}

void loop() {
  const int range_limit = 3000;
  Serial.print(-range_limit); Serial.print(' ');
  Serial.print(range_limit);  Serial.print(' ');

  int16_t samples[256];
  size_t count = mic.read(samples, 256);

  for (size_t i = 0; i < (count < 8 ? count : 8); i++) {
    Serial.print(samples[i]);
    Serial.print(' ');
  }
  Serial.println();
}
```

## Function reference

<FunctionDocumentation
  functionName="mic.begin(int pinData, int pinClk, uint32_t sampleRate, uint16_t bitDepth, size_t samplesPerBuffer)"
  description="Initializes the microphone driver and PDM capture with given pins and audio parameters."
  returnDescription="bool, true on success"
/>

<FunctionDocumentation
  functionName="mic.setHPF(bool enabled)"
  description="Enables a high-pass filter to reduce DC and very low-frequency components."
  returnDescription="None"
/>

<FunctionDocumentation
  functionName="mic.setGainDb(float gainDb)"
  description="Applies digital gain (dB) after decimation."
  returnDescription="None"
/>

<FunctionDocumentation
  functionName="mic.read(int16_t* dst, size_t samples)"
  description="Reads up to 'samples' PCM16 values from the capture buffer. Returns how many were read."
  returnDescription="int, number of samples read"
/>

<CenteredImage src="/img/spk0641ht/connection.jpg" alt="SPK0641HT4H-1 Pinout" caption="Connection example." width="700px"/>

<br></br>

<CenteredImage src="/img/spk0641ht/initialization.png" alt="SPK0641HT4H-1 Pinout" caption="Expected output." width="700px"/>

## Full example

<QuickLink 
  title="outputPlotting.ino" 
  description="Example showing how to Initialize a microphone and show the values sampled from it on the Serial plotter"
  url="https://github.com/SolderedElectronics/Soldered-Microphone-SPK0641HT-Library/blob/2ba6ce042027f8a597832bc7647984d21e26915d/examples/outputPlotting/outputPlotting.ino" 
/>