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

// Audio callback function, gives full information of current audio source (optional but good to have)
void my_audio_info(I2SAudio::msg_t m) 
{
  Serial.printf("%s: %s\n", m.s, m.msg);
}

void setup()
{
  // Declare callback function
  I2SAudio::audio_info_callback = my_audio_info;

  // Set pins used to connect to amplifier board
  audio.setPinout(I2S_BCLK, I2S_LRCLK, I2S_DOUT);
}
```

<FunctionDocumentation
  functionName="I2SAudio audio()"
  description="Create I2SAudio object and setup I2S configuration."
  returnType="None"
  parameters={[
    { type: 'uint8_t', name: 'I2S_PORT', description: 'I2S controller port number' },
  ]}
/>

<FunctionDocumentation
  functionName="I2SAudio::audio_info_callback"
  description="Sets audio callback function to log the events. Gives detailed message about current audio source."
/>

<FunctionDocumentation
  functionName="audio.setPinout()"
  description="Sets the pins for I2S interface protocol."
  returnType="Bool"
  returnDescription="Returns true if setup was successful."
  parameters={[
    { type: 'uint8_t', name: 'BCLK', description: 'Bit clock pin' },
    { type: 'uint8_t', name: 'LRCLK', description: 'Left/Right clock for channel selection' },
    { type: 'uint8_t', name: 'DOUT', description: 'Data out pin from microcontroller' },
  ]}
/>

## Playing audio from SD card

To play audio from SD card, SPI communication is initialized to read the files on the card. Functions `connecttoFS()` and `setVolume()` are used to select the audio file and volume control.

<InfoBox> **Supported file types are: WAV, MP3, M4A.** </InfoBox>

```cpp
// Declare SD card SPI pins
#define SD_CS          5
#define SPI_MOSI      23
#define SPI_MISO      19
#define SPI_SCK       18

void setup()
{
  // Manually control the SPI chip select, pulled high to deselect the bus 
  pinMode(SD_CS, OUTPUT);
  digitalWrite(SD_CS, HIGH);

  // Begin SPI communication with set frequency at 1MHz
  SPI.begin(SPI_SCK, SPI_MISO, SPI_MOSI);
  SPI.setFrequency(1000000);

  // Initialize the SD card over SPI bus
  SD.begin(SD_CS);

  // Set volume, default 0 ... 21
  audio.setVolume(5); 

  // IIR filter to adjust bass and treble (3 band equalizer)
  // setTone(0, 0, 0) is default setting, values can be between -40 ... +6 (dB)
  // audio.setTone(2, -10, 2);


  // setBalance(); values between -16 ... 16 mute the left or right channel
  // audio.setBalance(16);

  // Open stored file from SD card in correct format and pass to audio buffer
  audio.connecttoFS(SD, "example.wav");
}

void loop() 
{
  // audio.loop() must be called constantly
  audio.loop();

  // Prevent distortion
  vTaskDelay(1);
}
```

<FunctionDocumentation
  functionName="audio.setVolume()"
  description="Control the output volume of the speakers."
  returnType="None"
  parameters={[
    { type: 'uint8_t', name: 'vol', description: 'Set volume to value from 0 to 21.' }
  ]}
/>

<FunctionDocumentation
  functionName="audio.setTone()"
  description="Built-in IIR filter that simulates a 3 band equalizer."
  returnType="None"
  parameters={[
    { type: 'int8_t', name: 'gainLowPass', description: 'Adjusts the low frequencies gain (bass). ' }, 
    { type: 'int8_t', name: 'gainBandPass', description: 'Adjusts the mid frequencies gain (midrange).' },
    { type: 'int8_t', name: 'gainHighPass', description: 'Adjusts the high frequencies gain (treble).' }
  ]}
/>

<FunctionDocumentation
  functionName="audio.setBalance()"
  description="Controls the Left/Right channel balance."
  returnType="None"
  parameters={[
    { type: 'int8_t', name: 'balance', description: 'Control output channel balance, values between -16 ... 16 mute the left or right channel.' }
  ]}
/>

<FunctionDocumentation
  functionName="audio.connecttoFS()"
  description="Opens the file specified on SD card and passes it to audio buffer for playback."
  returnType="Bool"
  returnDescription="Returns true if file was found in correct format and passed to buffer."
  parameters={[
  { type: 'fs::FS', name: 'fs', description: 'File system module.' },
  { type: 'const char*', name: 'path', description: 'Specify the file name on SD card with correct format' }
  ]}
/>

<FunctionDocumentation
  functionName="audio.loop()"
  description="Keep audio process running for audio playback, must be called constantly."
  parameters={[
  ]}
/>

## Full Example

<QuickLink 
  title="Audio_Over_SD_Card.ino"
  description="Full example on GitHub"
  url="https://github.com/SolderedElectronics/Soldered-I2S-Audio-Amplifier-Arduino-Library/blob/main/examples/Audio_Over_SD_Card/Audio_Over_SD_Card.ino" 
/> 