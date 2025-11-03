---
slug: /SPK0641HT-microphone/arduino/voice-to-web
title: MEMS Microphone SPK0641HT4H Breakout - Voice to WEB
sidebar_label: Voice to WEB
id: spk0641ht-arduino-4
hide_title: true
---

# Voice to Web

## Stream live microphone audio to your browser

This example sets up an **ESP32** as a Wi-Fi Access Point with a tiny web page that plays the **SPK0641HT4H-1** microphone stream in real time over **WebSockets**.

<InfoBox>**WebSockets library** is recommended for this example. You can download it through Arduino Library Manager tab.</InfoBox>

```cpp
#include <WiFi.h>
#include <WebServer.h>
#include <WebSocketsServer.h>
#include "Soldered-Microphone-SPK0641HT.h"

const char* ssid = "RP2350_Audio_Stream";
const char* password = "123456789";

WebServer server(80);
WebSocketsServer webSocket(81);

const int SAMPLE_RATE = 16000;
const int CHANNELS = 1;
const int BIT_DEPTH = 16;
const int SAMPLES_PER_BUFFER = 160;
const int BYTES_PER_BUFFER = SAMPLES_PER_BUFFER * 2;

uint8_t audioBuffer1[BYTES_PER_BUFFER];
uint8_t audioBuffer2[BYTES_PER_BUFFER];
uint8_t* currentBuffer = audioBuffer1;
uint8_t* sendBuffer = audioBuffer2;
int bufferIndex = 0;
bool bufferReady = false;

unsigned long lastAudioSend = 0;
const int AUDIO_SEND_INTERVAL = 10;

Microphone mic;
int clientCount = 0;

void handleRoot() {
  String ip = WiFi.softAPIP().toString();
  String html = R"html(
  <!DOCTYPE html><html><head><meta charset="utf-8"/><title>Audio Stream</title>
  <style>body{font-family:system-ui;margin:24px}button{padding:10px 16px;font-size:16px}</style>
  </head><body>
  <h1>ESP32 Live Microphone Audio</h1>
  <button id="btn">Start</button>
  <div id="status">Disconnected</div>
  <script>
  let ac, ws, jb=[], playing=false;
  document.getElementById('btn').onclick = () => {
    if(playing) return;
    ac = new (window.AudioContext||window.webkitAudioContext)({sampleRate:16000});
    ws = new WebSocket('ws://)html";
  html += ip;
  html += R"html(:81); ws.binaryType='arraybuffer';
    ws.onopen=()=>{document.getElementById('status').textContent='Connected'; start();}
    ws.onclose=()=>{document.getElementById('status').textContent='Disconnected';}
    ws.onmessage=e=>{ if(e.data instanceof ArrayBuffer){ jb.push(new Int16Array(e.data)); } }
  };
  function start(){
    const bs=256; const sp=ac.createScriptProcessor(bs,1,1);
    let cur=null, pos=0; playing=true;
    sp.onaudioprocess=e=>{
      const out=e.outputBuffer.getChannelData(0);
      for(let i=0;i<bs;i++){
        if(cur && pos<cur.length){ out[i]=cur[pos++]/32768.0; }
        else { cur = jb.length? jb.shift(): null; pos=0; out[i]=0; }
      }
    };
    sp.connect(ac.destination);
  }
  </script></body></html>
  )html";
  server.send(200, "text/html", html);
}

void webSocketEvent(uint8_t num, WStype_t type, uint8_t * payload, size_t length) {
  if (type == WStype_CONNECTED) clientCount++;
  else if (type == WStype_DISCONNECTED) clientCount--;
}

void readMicData() {
  if (bufferReady) return;
  int16_t samples[SAMPLES_PER_BUFFER];
  int n = mic.read(samples, SAMPLES_PER_BUFFER);
  if (n > 0) {
    for (int i=0;i<n;i++) {
      if (bufferIndex*2+1 < BYTES_PER_BUFFER) {
        currentBuffer[bufferIndex*2]   = samples[i] & 0xFF;
        currentBuffer[bufferIndex*2+1] = (samples[i] >> 8) & 0xFF;
        bufferIndex++;
      }
    }
    if (bufferIndex >= SAMPLES_PER_BUFFER) { bufferReady = true; bufferIndex = 0; }
  }
}

void handleAudioStreaming() {
  unsigned long now = millis();
  if (clientCount > 0 && bufferReady && (now - lastAudioSend >= AUDIO_SEND_INTERVAL)) {
    uint8_t* tmp = sendBuffer; sendBuffer = currentBuffer; currentBuffer = tmp;
    webSocket.broadcastBIN(sendBuffer, BYTES_PER_BUFFER);
    bufferReady = false; lastAudioSend = now;
  }
}

void setup() {
  Serial.begin(115200);
  WiFi.softAP(ssid, password);
  server.on("/", handleRoot);
  server.begin();
  webSocket.begin();
  webSocket.onEvent(webSocketEvent);

  const int PDM_CLK = 4;
  const int PDM_DIN = 27;
  mic.begin(PDM_DIN, PDM_CLK, SAMPLE_RATE, BIT_DEPTH, SAMPLES_PER_BUFFER);
  mic.setHPF(true);
  mic.setGainDb(10.0f);
}

void loop() {
  server.handleClient();
  webSocket.loop();
  readMicData();
  handleAudioStreaming();
}
```

<FunctionDocumentation functionName="mic.begin(int pinData, int pinClk, uint32_t sampleRate, uint16_t bitDepth, size_t samplesPerBuffer)" description="Initializes the microphone driver and PDM capture on ESP32 with the chosen pins and audio parameters." returnDescription="bool, true on success" />

<FunctionDocumentation functionName="mic.setHPF(bool enabled)" description="Enables a high-pass filter to reduce DC and very low-frequency components." returnDescription="None" />

<FunctionDocumentation functionName="mic.setGainDb(float gainDb)" description="Applies digital post-decimation gain (dB)." returnDescription="None" />

<FunctionDocumentation functionName="mic.read(int16_t* dst, size_t samples)" description="Reads up to 'samples' PCM16 values from the capture buffer." returnDescription="int, number of samples read" />


<CenteredImage src="/img/spk0641ht/connection.jpg" alt="SPK0641HT4H-1 Pinout" caption="Connection example." width="700px"/>

<br></br>

<CenteredImage src="/img/spk0641ht/voicetoweb.png" alt="SPK0641HT4H-1 Pinout" caption="Expected output." width="700px"/>

## Full example

<QuickLink 
  title="voiceToWAV_ESP32.ino" 
  description="Record microphone audio to WAV on ESP32"
  url="https://github.com/SolderedElectronics/Soldered-Microphone-SPK0641HT-Library/blob/2ba6ce042027f8a597832bc7647984d21e26915d/examples/voiceToWeb/voiceToWeb.ino" 
/>