---
slug: /nula_w55rp20/arduino/getting-started
title: NULA Ether W55RP20 - Getting started with Arduino
sidebar_label: Getting started with Arduino
id: nula_w55rp20-arduino-1
hide_title: True
pagination_next: null
---

# Getting started with Arduino

## Arduino board definition

To program your **NULA Ether W55RP20**, use the **official Raspberry Pi core for Arduino** maintained by **Earle Philhower**.  
This package includes support for all RP2040-based boards and can be configured to work with the NULA Ether W55RP20.

<QuickLink
  title="RP2040 Arduino core"
  description="Official Arduino core for Raspberry Pi RP2040 chips, by Earle Philhower."
  url="https://github.com/earlephilhower/arduino-pico"
/>

<InfoBox>

**New to Arduino?**  
If this is your first time setting up Arduino, follow our beginner's guide for installation, connecting your board, and uploading your first sketch:

<QuickLink
  title="Getting started with Arduino"
  description="Step-by-step guide to installing Arduino and uploading your first program."
  url="/arduino/quick-start-guide"
/>
</InfoBox>

---

## Installing the RP2040 board package

You can install the **Raspberry Pi RP2040 boards** package directly from the **Arduino Boards Manager**:

1. Open **Arduino IDE**
2. Go to **Tools → Board → Boards Manager**
3. In the search bar, type **rp2040** or **Earle**
4. Find **Raspberry Pi Pico/RP2040/RP2350 by Earle Philhower** and click **Install**

Alternatively, install it manually by adding the package URL to **File → Preferences → Additional Boards Manager URLs**:

```
https://github.com/earlephilhower/arduino-pico/releases/download/global/package_rp2040_index.json
```

Once installed, select your board from the menu:  
**Tools → Board → Raspberry Pi Pico**

<InfoBox>Hold the **BOOT** button while connecting the USB-C cable to enter BOOTSEL mode if the board is not detected automatically.</InfoBox>

---

## Installing the Ethernet library

The NULA Ether W55RP20 uses the **W55RP20lwIP** library. Install it from the Arduino Library Manager:

1. Go to **Tools → Manage Libraries**
2. Search for **W55RP20**
3. Install **W55RP20lwIP**

---

## Example sketch

This sketch connects to a "quote of the day" service over TCP, sends a hello message, and prints the response. Make sure an Ethernet cable is connected to the RJ45 port before uploading.

```cpp
#include <W55RP20lwIP.h>

const char* host = "djxmmx.net";
const uint16_t port = 17;

Wiznet55rp20lwIP eth(20 /* chip select */);

void setup() {
  Serial.begin(115200);
  delay(5000);
  Serial.println("Starting Ethernet port");

    if (!eth.begin()) {
    Serial.println("No wired Ethernet hardware detected. Check pinouts, wiring.");
    while (1) {
      delay(1000);
    }
  }

  while (!eth.connected()) {
    Serial.print(".");
    delay(500);
  }
  
  Serial.println("");
  Serial.println("Ethernet connected");
  Serial.println("IP address: ");
  Serial.println(eth.localIP());
}

void loop() {
  static bool wait = false;

  Serial.print("connecting to ");
  Serial.print(host);
  Serial.print(':');
  Serial.println(port);

  WiFiClient client;
  if (!client.connect(host, port)) {
    Serial.println("connection failed");
    delay(5000);
    return;
  }

  Serial.println("sending data to server");
  if (client.connected()) {
      client.println("hello from RP2040");
  }

  unsigned long timeout = millis();
  while (client.available() == 0) {
    if (millis() - timeout > 5000) {
      Serial.println(">>> Client Timeout !");
      client.stop();
      delay(60000);
      return;
    }
  }

  Serial.println("receiving from remote server");
  while (client.available()) {
    char ch = static_cast<char>(client.read());
    Serial.print(ch);
  }

  Serial.println();
  Serial.println("closing connection");
  client.stop();

  if (wait) {
      delay(300000);  // execute once every 5 minutes, don't flood remote service
  }
  wait = true;
}
```

Open the **Serial Monitor** at **115200 baud**. The board will connect via Ethernet, print its IP address, then connect to the quote-of-the-day server and print the response.
