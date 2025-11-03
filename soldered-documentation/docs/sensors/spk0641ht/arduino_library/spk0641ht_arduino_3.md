---
slug: /SPK0641HT-microphone/arduino/voice-to-wav
title: MEMS Microphone SPK0641HT4H Breakout - Voice to WAV
sidebar_label: Voice to WAV
id: spk0641ht-arduino-3
hide_title: true
---

# Voice to WAV

## Record microphone audio to a WAV file

This example demonstrates how to set up the **SPK0641HT4H-1** microphone with an **ESP32**, capture audio through its PDM interface, and store it as a **WAV file** on the **SD card**, ready to be transferred and played on a computer or phone.

```cpp
#include <Arduino.h>
#include "Soldered-Microphone-SPK0641HT.h"
#include "SdFat.h"

constexpr int PDM_CLK = 4;
constexpr int PDM_DIN = 27;
constexpr int SD_CS   = 5;

#if HAS_SDIO_CLASS
  #define SD_CONFIG SdioConfig(FIFO_SDIO)
#elif ENABLE_DEDICATED_SPI
  #define SD_CONFIG SdSpiConfig(SD_CS, DEDICATED_SPI, SD_SCK_MHZ(16))
#else
  #define SD_CONFIG SdSpiConfig(SD_CS, SHARED_SPI, SD_SCK_MHZ(16))
#endif

SdFs sd;
FsFile wavFile;
Microphone mic;

const int sampleRate = 32000;
const int numChannels = 1;
const int bitDepth = 16;
const int numSamples = 512;

struct WavHeader {
  char riff[4] = {'R','I','F','F'};
  uint32_t chunkSize = 36;
  char wave[4] = {'W','A','V','E'};
  char fmt[4]  = {'f','m','t',' '};
  uint32_t fmtChunkSize = 16;
  uint16_t audioFormat = 1;
  uint16_t numChannels = 1;
  uint32_t sampleRate  = 32000;
  uint32_t byteRate    = 128000;
  uint16_t blockAlign  = 4;
  uint16_t bitsPerSample = 32;
  char data[4] = {'d','a','t','a'};
  uint32_t dataChunkSize = 0;
};
WavHeader wavHeader;

enum RecState { IDLE, RECORDING, STOPPING };
RecState recState = IDLE;
bool hasSDCard = false;
unsigned long recordingStartTime = 0;
const unsigned long maxRecordingTime = 30000;
char currentFilename[15] = "";

void updateWavHeader() {
  wavHeader.sampleRate    = sampleRate;
  wavHeader.numChannels   = numChannels;
  wavHeader.bitsPerSample = bitDepth;
  wavHeader.byteRate      = sampleRate * numChannels * (bitDepth / 8);
  wavHeader.blockAlign    = numChannels * (bitDepth / 8);
}

bool writeWavHeader() {
  if (!wavFile.isOpen()) return false;
  updateWavHeader();
  if (!wavFile.seek(0)) return false;
  size_t bytesWritten = wavFile.write((uint8_t*)&wavHeader, sizeof(WavHeader));
  return bytesWritten == sizeof(WavHeader);
}

bool startRecording() {
  if (!hasSDCard) {
    Serial.println("No SD card detected!");
    return false;
  }

  int fileIndex = 0;
  char filename[15];
  do {
    snprintf(filename, sizeof(filename), "REC%03d.WAV", fileIndex++);
  } while (sd.exists(filename) && fileIndex < 1000);

  if (!wavFile.open(filename, O_RDWR | O_CREAT | O_TRUNC)) {
    Serial.println("File create failed");
    return false;
  }

  strncpy(currentFilename, filename, sizeof(currentFilename));
  wavHeader.dataChunkSize = 0;
  wavHeader.chunkSize = 36;

  if (!writeWavHeader()) {
    wavFile.close();
    return false;
  }

  recState = RECORDING;
  recordingStartTime = millis();
  Serial.printf("Recording: %s\n", filename);
  return true;
}

void stopRecording() {
  if (recState != RECORDING) return;
  recState = STOPPING;
  Serial.println("Stopping…");
}

void completeRecording() {
  if (!wavFile.isOpen()) return;
  uint32_t fileSize = wavFile.position();
  wavHeader.dataChunkSize = fileSize - sizeof(WavHeader);
  wavHeader.chunkSize = wavHeader.dataChunkSize + 36;

  if (!writeWavHeader()) Serial.println("Header update failed");
  wavFile.close();
  Serial.printf("Saved: %s (%lu bytes)\n", currentFilename, fileSize);
  recState = IDLE;
}

void setup() {
  Serial.begin(115200);
  delay(1000);

  Serial.println("ESP32 Microphone WAV Recorder");

  if (!sd.cardBegin(SD_CONFIG)) {
    Serial.println("SD init failed");
    hasSDCard = false;
  } else if (!sd.volumeBegin()) {
    Serial.println("FS init failed (format FAT32)");
    hasSDCard = false;
  } else {
    hasSDCard = true;
    Serial.println("SD ready");
  }

  Serial.println("Init microphone…");
  mic.begin(PDM_DIN, PDM_CLK, sampleRate, 16, 512);
  mic.setHPF(true);
  mic.setGainDb(10.0f);
  Serial.println("Mic ready");

  updateWavHeader();

  Serial.println("Press 'r' to start/stop (30s limit).");
}

void loop() {
  if (Serial.available()) {
    char command = Serial.read();
    if (command == 'r' || command == 'R') {
      if (recState == IDLE) startRecording();
      else if (recState == RECORDING) stopRecording();
    }
  }

  if (recState == RECORDING) {
    int16_t samples[numSamples];
    size_t count = mic.read(samples, numSamples);
    if (count > 0) {
      size_t bytesWritten = wavFile.write((uint8_t*)samples, count * sizeof(int16_t));
      if (bytesWritten != count * sizeof(int16_t)) {
        Serial.println("Write error");
        stopRecording();
      }
    }
    if (millis() - recordingStartTime >= maxRecordingTime) {
      Serial.println("30s limit reached");
      stopRecording();
    }
  } else if (recState == STOPPING) {
    completeRecording();
  }

  static unsigned long lastStatus = 0;
  if (millis() - lastStatus > 1000) {
    lastStatus = millis();
    if (recState == RECORDING) {
      unsigned long elapsed = (millis() - recordingStartTime) / 1000;
      unsigned long remaining = (maxRecordingTime / 1000) - elapsed;
      Serial.printf("Recording: %lus, Remaining: %lus\n", elapsed, remaining);
    }
  }
  delay(10);
}
```

## Function reference

<FunctionDocumentation
  functionName="mic.begin(int pinData, int pinClk, uint32_t sampleRate, uint16_t bitDepth, size_t samplesPerBuffer)"
  description="Initializes the microphone driver and PDM capture. Host provides CLK; DATA is sampled and decimated to PCM with the chosen bit depth."
  returnDescription="bool, true on success"
/>

<FunctionDocumentation
  functionName="mic.setHPF(bool enabled)"
  description="Enables a high-pass filter to reduce DC offset and very low-frequency rumble."
  returnDescription="None"
/>

<FunctionDocumentation
  functionName="mic.setGainDb(float gainDb)"
  description="Applies digital gain (in dB) after decimation. Use modest values to avoid clipping."
  returnDescription="None"
/>

<FunctionDocumentation
  functionName="mic.read(int16_t* dst, size_t samples)"
  description="Fetches up to 'samples' PCM16 values from the PDM capture pipeline. Non-blocking; returns the number of samples actually read."
  returnDescription="int, number of samples read"
/>

<FunctionDocumentation
  functionName="startWav(File& f, uint32_t sampleRate, uint16_t bitDepth, uint16_t channels)"
  description="Writes a provisional 44-byte WAV header to an empty file. The data chunk size is patched later in finishWav()."
  returnDescription="None"
/>

<FunctionDocumentation
  functionName="finishWav(File& f)"
  description="Seeks back into the header and patches RIFF/data chunk sizes so the file is valid."
  returnDescription="None"
/>

<CenteredImage src="/img/spk0641ht/microsd.jpg" alt="SPK0641HT4H-1 Pinout" caption="Connection example." width="700px"/>

<br></br>

<CenteredImage src="/img/spk0641ht/voicetowav.png" alt="SPK0641HT4H-1 Pinout" caption="Expected output." width="700"/>

## Full example

<QuickLink 
  title="voiceToWAV_ESP32.ino" 
  description="Record microphone audio to WAV on ESP32"
  url="https://github.com/SolderedElectronics/Soldered-Microphone-SPK0641HT-Library/blob/main/examples/voiceToWAV_ESP32/voiceToWAV_ESP32.ino" 
/>

## Other supported boards

There is also an **RP2350 version** of this example with the same functionality, but adapted for RP2350 pinout and LittleFS:

<QuickLink 
  title="voiceToWAV_RP2350.ino" 
  description="Record microphone audio to WAV on RP2350 boards"
  url="https://github.com/SolderedElectronics/Soldered-Microphone-SPK0641HT-Library/blob/main/examples/voiceToWAV_RP2350/voiceToWAV_RP2350.ino" 
/>
