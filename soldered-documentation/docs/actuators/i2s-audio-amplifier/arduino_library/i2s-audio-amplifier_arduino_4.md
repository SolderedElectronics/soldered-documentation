---
slug: /i2s-audio-amplifier/arduino/stream-playback
title: Stereo I2S Audio Amplifier - URL Stream Playback
sidebar_label: URL Stream Playback
id: i2s-audio-amplifier-arduino-4
hide_title: False
---

Example to receive a online audio webstream:

```cpp
void setup() 
{
    // Set volume, default 0 ... 21
    audio.setVolume(10); 
    
    // Connect to online audio URL and start streaming
    audio.connecttohost("http://stream.antennethueringen.de/live/aac-64/stream.antennethueringen.de/");
}
```

<FunctionDocumentation
  functionName="audio.connecttohost()"
  description="Function which connects to online host URL to play audio."
  returnType="Bool"
  returnDescription="Returns true if request was successful."
  parameters={[
  { type: 'const char*', name: 'host', description: ' Host URL. ' },
  { type: 'const char*', name: 'user', description: '(Optional) Username for authentication.' },
  { type: 'const char*', name: 'password', description: '(Optional) Password for authentication.' }
  ]}
/>

## Full Example

Full example is listed below:

```cpp
#include "Soldered_I2S_Audio_Amplifier.h"
#include "WiFi.h"

// Declare GPIOs used
#define I2S_DOUT 25
#define I2S_BCLK 27
#define I2S_LRCLK 26

// Network credentials
const char* SSID = "";
const char* PASSWORD = "";

// Create an instance of audio player object
I2SAudio audio;

void setup() 
{
    Serial.begin(115200);

    // Connect to existing WiFi network
    WiFi.begin(SSID, PASSWORD);
    while (WiFi.status() != WL_CONNECTED)
    {
        Serial.print(".");
        delay(1000);
    } 

    // Set audio amplifier pins to output I2S digital audio
    audio.setPinout(I2S_BCLK, I2S_LRCLK, I2S_DOUT);

    // Set volume, default 0 ... 21
    audio.setVolume(10); 
    
    // Connect to online audio URL and start streaming
    audio.connecttohost("http://stream.antennethueringen.de/live/aac-64/stream.antennethueringen.de/");
}

void loop()
{
    // audio.loop() must be called constantly
    audio.loop();

    // Prevent distortion
    vTaskDelay(1);
}
```

<QuickLink 
  title="URL_Stream_Playback.ino"
  description="Full example on our GitHub"
  url="https://github.com/SolderedElectronics/Soldered-I2S-Audio-Amplifier-Arduino-Library/blob/main/examples/URL_Stream_Playback/URL_Stream_Playback.ino" 
/> 