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

To program the **NULA Ether W55RP20**, use the **RP2040 Arduino core** by Earle Philhower:

<QuickLink
  title="RP2040 Arduino core"
  description="Arduino core for Raspberry Pi RP2040 chips, by Earle Philhower."
  url="https://github.com/earlephilhower/arduino-pico"
/>

<InfoBox>

**New to Arduino?** Follow our beginner's guide for installation and uploading your first sketch:

<QuickLink
  title="Getting started with Arduino"
  description="Step-by-step guide to installing Arduino and uploading your first program."
  url="/arduino/quick-start-guide"
/>
</InfoBox>

---

## Installing the board package

Install the **Raspberry Pi RP2040 boards** package from the Arduino Boards Manager:

1. Open **Arduino IDE**
2. Go to **Tools → Board → Boards Manager**
3. Search for **rp2040** or **Earle**
4. Find **Raspberry Pi Pico/RP2040/RP2350 by Earle Philhower** and click **Install**

Or add the URL manually in **File → Preferences → Additional Boards Manager URLs**:

```
https://github.com/earlephilhower/arduino-pico/releases/download/global/package_rp2040_index.json
```

After installing, go to **Tools → Board** and select **Soldered NULA Ethernet W55RP20** (internally identified as `soldered_nula_ethernet_w55rp20`), not the generic "Raspberry Pi Pico" entry. This board-specific variant configures the correct pin mapping for this board, including the onboard NeoPixel status LED and the microSD/SPI1 assignment.

<WarningBox>Selecting a generic "Raspberry Pi Pico" board instead of the Soldered-specific one is a common mistake and can lead to misconfigured pins or a status LED that doesn't behave as expected.</WarningBox>

<InfoBox>Hold the **BOOT** button while connecting the USB-C cable to enter BOOTSEL mode if the board is not detected automatically.</InfoBox>

---

## The Ethernet library is already installed

Unlike most Arduino libraries, **you don't need to install anything separately for Ethernet**. The `W55RP20lwIP` library ships bundled with the RP2040 board package you just installed. Once the board package is in place, it's available directly:

1. Go to **File → Examples**
2. Scroll down to the **lwIP_w55rp20** section
3. Open the **WiFiClient-W55RP20** example to see it working, or just `#include <W55RP20lwIP.h>` in your own sketch as shown below

<InfoBox>Searching the Arduino Library Manager for "W55RP20" won't find anything; it's not a separately listed library. If you don't see it under File → Examples, double-check you actually selected the Soldered NULA Ethernet W55RP20 board entry and not a generic one. Some example menus only show entries relevant to the currently selected board.</InfoBox>

---

## Example sketch

This sketch connects to a "quote of the day" service over TCP and prints the response. Make sure an Ethernet cable is plugged into the RJ45 port before uploading.

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
    delay(300000); // run once every 5 minutes
  }
  wait = true;
}
```

Open the **Serial Monitor** at **115200 baud**. The board will print its IP address, connect to the server, and print the response.

---

## Function reference

<FunctionDocumentation
  functionName="Wiznet55rp20lwIP eth()"
  description="Creates the Ethernet object. The argument is the GPIO pin connected to the W5500 chip select."
  returnDescription="None."
  parameters={[
    { type: 'int', name: 'cs', description: 'Chip select pin number. Use 20 for the NULA Ether W55RP20.' },
  ]}
/>

<FunctionDocumentation
  functionName="eth.begin()"
  description="Initializes the W55RP20 Ethernet hardware and waits for a DHCP lease. Must be called before any network operations."
  returnDescription="bool - true if initialization succeeded, false if the hardware was not detected."
  parameters={[]}
/>

<FunctionDocumentation
  functionName="eth.connected()"
  description="Checks whether the board has an active Ethernet link and a valid IP address."
  returnDescription="bool - true if the link is up and DHCP has assigned an IP."
  parameters={[]}
/>

<FunctionDocumentation
  functionName="eth.localIP()"
  description="Returns the IP address assigned to the board by DHCP."
  returnDescription="IPAddress - the board's current IP address."
  parameters={[]}
/>

<FunctionDocumentation
  functionName="client.connect()"
  description="Opens a TCP connection to the specified host and port."
  returnDescription="bool - true if the connection was established, false otherwise."
  parameters={[
    { type: 'const char*', name: 'host', description: 'Hostname or IP address of the remote server.' },
    { type: 'uint16_t', name: 'port', description: 'TCP port number to connect to.' },
  ]}
/>

<FunctionDocumentation
  functionName="client.connected()"
  description="Checks whether the TCP connection to the remote server is still active."
  returnDescription="bool - true if the connection is open."
  parameters={[]}
/>

<FunctionDocumentation
  functionName="client.println()"
  description="Sends a string followed by a carriage return and newline over the TCP connection."
  returnDescription="None."
  parameters={[
    { type: 'String', name: 'data', description: 'The string to send.' },
  ]}
/>

<FunctionDocumentation
  functionName="client.available()"
  description="Returns the number of bytes received from the server that are ready to be read."
  returnDescription="int - number of bytes available."
  parameters={[]}
/>

<FunctionDocumentation
  functionName="client.read()"
  description="Reads one byte from the receive buffer."
  returnDescription="int - the next byte, or -1 if no data is available."
  parameters={[]}
/>

<FunctionDocumentation
  functionName="client.stop()"
  description="Closes the TCP connection and releases the socket."
  returnDescription="None."
  parameters={[]}
/>

