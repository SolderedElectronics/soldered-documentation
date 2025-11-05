---
slug: /i2s-audio-amplifier/arduino/text-to-speech 
title: Stereo I2S Audio Amplifier - Text to Speech
sidebar_label: Text to Speech
id: i2s-audio-amplifier-arduino-3 
hide_title: False
---

This example shows how you can use **TTS (Text-to-Speech)** model from Google of OpenAI to generate audio for given text prompt.

```cpp
void setup() 
{
  // Generate audio for given text
  const char* prompt = "So many things to say, so little time.";

  // Google TTS
  audio.connecttospeech(prompt, "en"); 

  // OpenAI TTS
  //audio.openai_speech("openAI-secret-key", "tts-1", prompt, "", "shimer", "mp3", "1");
}
```

<FunctionDocumentation
  functionName="audio.connecttospeech()"
  description="Generate human-like audio from given text prompt using Google TTS model."
  returnType="Bool"
  returnDescription="Returns true if connection was successful."
  parameters={[
  { type: 'const char*', name: 'speech', description: 'Text prompt.' },
  { type: 'const char*', name: 'lang', description: 'Language in which to generate audio.' }
  ]}
/>

<FunctionDocumentation
  functionName="audio.openai_speech()"
  description="Generate human-like audio from given text prompt using OpenAI's TTS model."
  returnType="Bool"
  returnDescription="Returns true if request was valid."
  parameters={[
  { type: 'String', name: 'api_key', description: 'OpenAI API key.' },
  { type: 'String', name: 'model', description: 'TTS model (tts-1 or tts-1-hd).' },
  { type: 'String', name: 'input', description: 'Text to generate audio for (max. length is 4096 characters).' },
  { type: 'String', name: 'instructions', description: '(Optional) Description of desired characteristics of the generated audio.' },
  { type: 'String', name: 'voice', description: 'Voice to use when generating the audio. Supported voices: alloy, echo, fable, onyx, nova and shimmer' },
  { type: 'String', name: 'response_format', description: 'Optional. Format in which to play audio. Supported formats: MP3 (default), opus, aac and flac.' },
  { type: 'String', name: 'speed', description: '(Optional) Speed of generated audio, values ranging from 0.25 to 4 with 1.0 being default.' }
  ]}
/>

## Full Example

The full example is listed below:

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

// Audio callback function, gives full information of current audio source (optional but good to have)
void my_audio_info(I2SAudio::msg_t m) 
{
  Serial.printf("%s: %s\n", m.s, m.msg);
}

void setup() 
{
  Serial.begin(115200);

  // Declare callback function
  I2SAudio::audio_info_callback = my_audio_info;

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

  // Generate audio for given text
  const char* prompt = "So many things to say, so little time.";

  // Google TTS
  audio.connecttospeech(prompt, "en"); 

  // OpenAI TTS
  //audio.openai_speech("openAI-secret-key", "tts-1", prompt, "", "shimer", "mp3", "1");
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
  title="Text_to_Speech.ino"
  description="Full example on our GitHub"
  url="https://github.com/SolderedElectronics/Soldered-I2S-Audio-Amplifier-Arduino-Library/blob/main/examples/Text_to_Speech/Text_to_Speech.ino" 
/> 