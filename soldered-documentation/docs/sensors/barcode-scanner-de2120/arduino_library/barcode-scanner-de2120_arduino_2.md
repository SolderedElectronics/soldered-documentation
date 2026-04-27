---
slug: /barcode-scanner-de2120/arduino/examples
title: DE2120 Barcode Scanner – Scanning Examples
sidebar_label: Scanning examples
id: barcode-scanner-de2120-arduino-2
hide_title: true
---

# Scanning examples

## Basic scan

This example initializes the DE2120 scanner over **HardwareSerial** (UART2 on ESP32), then continuously polls for barcodes and prints any result to the Serial Monitor.

Open the Serial Monitor at **115200 baud** to observe scan results.

```cpp
#include "HardwareSerial.h"
HardwareSerial scannerSerial(2); // Use UART2

#include "DE2120-SOLDERED.h"
DE2120_Soldered scanner;

#define BUFFER_LEN 40
char scanBuffer[BUFFER_LEN];

void setup()
{
  Serial.begin(115200);
  Serial.println("DE2120 Barcode Scanner");

  scannerSerial.begin(115200, SERIAL_8N1, 4, 5); // RX=GPIO4, TX=GPIO5
  delay(500);

  if (scanner.begin(scannerSerial) == false)
  {
    Serial.println("Scanner did not respond. Check wiring and ensure POR232 barcode was scanned. Freezing...");
    while (1);
  }
  Serial.println("Scanner online!");
}

void loop()
{
  if (scanner.readBarcode(scanBuffer, BUFFER_LEN))
  {
    Serial.print("Code found: ");
    for (int i = 0; i < strlen(scanBuffer); i++)
      Serial.print(scanBuffer[i]);
    Serial.println();
  }
  delay(200);
}
```

## Function reference

<FunctionDocumentation
  functionName="scanner.begin(HardwareSerial &serialPort)"
  description="Initializes the DE2120 scanner on the specified HardwareSerial port. Automatically negotiates the baud rate down to 9600 bps if needed. Returns false if the scanner does not respond."
  returnDescription="bool, true if the scanner was detected and initialized successfully"
/>

<FunctionDocumentation
  functionName="scanner.begin(SoftwareSerial &serialPort)"
  description="Initializes the DE2120 scanner on the specified SoftwareSerial port. Automatically negotiates the baud rate. Returns false if the scanner does not respond."
  returnDescription="bool, true if the scanner was detected and initialized successfully"
/>

<FunctionDocumentation
  functionName="scanner.readBarcode(char *resultBuffer, uint8_t size)"
  description="Checks for incoming barcode data. When a complete barcode string (terminated by a carriage return) is received, it is copied into resultBuffer and the function returns true. Returns false if no complete barcode is available yet."
  returnDescription="bool, true when a complete barcode has been received"
/>

## Full example

<QuickLink
  title="HardwareScan.ino"
  description="Basic barcode scanning example using HardwareSerial (UART2) on ESP32"
  url="https://github.com/SolderedElectronics/Soldered-Barcode-Scanner-DE2120-Arduino-Library/blob/main/examples/HardwareScan/HardwareScan.ino"
/>

---

## Configuring the scanner

This example demonstrates how to send configuration commands to the scanner at runtime using `sendCommand()`. It toggles **Code ID** — a feature that prepends a symbology identifier character to every decoded barcode (e.g. `A` for Code 128, `Q` for QR Code), which is useful when your application needs to distinguish barcode types.

Open the Serial Monitor at **115200 baud** and type `y` to enable Code ID or `n` to disable it. The scanner will also print any barcodes it reads while waiting for input.

```cpp
#include "SoftwareSerial.h"
SoftwareSerial softSerial(4, 5); // RX=4, TX=5 — change to match your wiring

#include "DE2120-SOLDERED.h"
DE2120_Soldered scanner;

#define BUFFER_LEN 40
char scanBuffer[BUFFER_LEN];

void setup()
{
  Serial.begin(115200);
  Serial.println("DE2120 Barcode Scanner");

  if (scanner.begin(softSerial) == false)
  {
    Serial.println("Scanner did not respond. Check wiring and ensure POR232 barcode was scanned. Freezing...");
    while (1);
  }
  Serial.println("Scanner online!");
}

void loop()
{
  flushRx();

  Serial.println();
  Serial.println("Transmit Code ID with barcode? (y/n)");

  while (Serial.available() == false)
  {
    if (scanner.readBarcode(scanBuffer, BUFFER_LEN))
    {
      Serial.print("Code found: ");
      for (int i = 0; i < strlen(scanBuffer); i++)
        Serial.print(scanBuffer[i]);
      Serial.println();
    }
    delay(200);
  }

  switch (Serial.read())
  {
    case 'y':
      Serial.println("Code ID enabled");
      scanner.sendCommand("CIDENA", "1");
      break;
    case 'n':
      Serial.println("Code ID disabled");
      scanner.sendCommand("CIDENA", "0");
      break;
    default:
      Serial.println("Command not recognized");
      break;
  }
}

void flushRx()
{
  while (Serial.available())
  {
    Serial.read();
    delay(1);
  }
}
```

## Function reference

<FunctionDocumentation
  functionName='scanner.sendCommand(const char *cmd, const char *arg = "")'
  description="Sends a raw configuration command to the scanner. The library automatically wraps the command in the required protocol format (^_^COMMAND<ARG>.). Waits up to 3 seconds for an ACK or NACK response."
  returnDescription="bool, true if the scanner acknowledged the command (ACK), false on NACK or timeout"
/>

<FunctionDocumentation
  functionName="scanner.enableDecodeBeep()"
  description="Enables the audible beep on successful barcode decode. Enabled by default."
  returnDescription="bool, true on success"
/>

<FunctionDocumentation
  functionName="scanner.disableDecodeBeep()"
  description="Disables the audible beep on successful barcode decode."
  returnDescription="bool, true on success"
/>

<FunctionDocumentation
  functionName="scanner.lightOn()"
  description="Turns on the white illumination LEDs."
  returnDescription="bool, true on success"
/>

<FunctionDocumentation
  functionName="scanner.lightOff()"
  description="Turns off the white illumination LEDs."
  returnDescription="bool, true on success"
/>

<FunctionDocumentation
  functionName="scanner.reticleOn()"
  description="Turns on the red aiming reticle LED."
  returnDescription="bool, true on success"
/>

<FunctionDocumentation
  functionName="scanner.reticleOff()"
  description="Turns off the red aiming reticle LED."
  returnDescription="bool, true on success"
/>

<FunctionDocumentation
  functionName="scanner.enableContinuousRead(uint8_t repeatInterval = 2)"
  description="Switches the scanner to continuous scanning mode. The repeatInterval parameter controls how duplicate codes are handled: 0 = output once, 1 = continuous with no interval, 2 = 0.5 s interval, 3 = 1 s interval."
  returnDescription="bool, true on success"
/>

<FunctionDocumentation
  functionName="scanner.disableContinuousRead()"
  description="Returns the scanner to manual (trigger) mode."
  returnDescription="bool, true on success"
/>

<FunctionDocumentation
  functionName="scanner.enableMotionSense(uint8_t sensitivity = 50)"
  description="Enables motion-triggered scanning. Valid sensitivity values: 15, 20, 30, 50, 100."
  returnDescription="bool, true on success"
/>

<FunctionDocumentation
  functionName="scanner.disableMotionSense()"
  description="Disables motion sensing and returns the scanner to manual mode."
  returnDescription="bool, true on success"
/>

<FunctionDocumentation
  functionName="scanner.enableAll1D()"
  description="Enables all supported 1D barcode symbologies."
  returnDescription="bool, true on success"
/>

<FunctionDocumentation
  functionName="scanner.disableAll1D()"
  description="Disables all 1D barcode symbologies."
  returnDescription="bool, true on success"
/>

<FunctionDocumentation
  functionName="scanner.enableAll2D()"
  description="Enables all supported 2D barcode symbologies."
  returnDescription="bool, true on success"
/>

<FunctionDocumentation
  functionName="scanner.disableAll2D()"
  description="Disables all 2D barcode symbologies."
  returnDescription="bool, true on success"
/>

<FunctionDocumentation
  functionName="scanner.changeReadingArea(uint8_t percent)"
  description="Sets the percentage of the camera frame to scan for barcodes. Valid values: 100 (full width), 80, 60, 40, 20 (center region). Narrowing the area can speed up decoding in controlled environments."
  returnDescription="bool, true on success"
/>

<FunctionDocumentation
  functionName="scanner.factoryDefault()"
  description="Resets all scanner settings to factory defaults. Note: this will temporarily disconnect the scanner from serial as it restarts."
  returnDescription="bool, true on success"
/>

## Full example

<QuickLink
  title="SendCommand.ino"
  description="Example showing how to send configuration commands to the DE2120 scanner at runtime"
  url="https://github.com/SolderedElectronics/Soldered-Barcode-Scanner-DE2120-Arduino-Library/blob/main/examples/SendCommand/SendCommand.ino"
/>

<InfoBox>

For a full interactive menu covering all scanner settings (flashlight, reticle, reading area, scanning mode, and symbologies), see the **SerialSettings** example in the library:

<QuickLink
  title="SerialSettings.ino"
  description="Full interactive configuration menu for the DE2120 scanner"
  url="https://github.com/SolderedElectronics/Soldered-Barcode-Scanner-DE2120-Arduino-Library/blob/main/examples/SerialSettings/SerialSettings.ino"
/>

</InfoBox>
