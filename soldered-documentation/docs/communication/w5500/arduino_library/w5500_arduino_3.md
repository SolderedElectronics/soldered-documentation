---
slug: /w5500/arduino/WebClient
title: WebClient example
id: w5500-arduino-3
hide_title: False

---

This example shows you how to make an HTTP request using the W5500 module. It returns a Google search for the term "Arduino". The results of this search are viewable as HTML in the Serial Monitor.

<InfoBox>This example is a modification of a tutorial from `docs.arduino.cc`. A link to the specific example and many more can be found at the bottom of the page!</InfoBox>

```cpp

#include <SPI.h>
#include <Ethernet.h>

#define CS_PIN 5
// Enter a MAC address for your controller below.
byte mac[] = { 0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED };

// if you don't want to use DNS (and reduce your sketch size)
// use the numeric IP instead of the name for the server:
//IPAddress server(74,125,232,128);  // numeric IP for Google (no DNS)
char server[] = "www.google.com";    // name address for Google (using DNS)

// Set the static IP address to use if the DHCP fails to assign
IPAddress ip(192, 168, 0, 177);
IPAddress myDns(192, 168, 0, 1);

// Initialize the Ethernet client library
// with the IP address and port of the server
// that you want to connect to (port 80 is default for HTTP):
EthernetClient client;

// Variables to measure the speed
unsigned long beginMicros, endMicros;
unsigned long byteCount = 0;
bool printWebData = true;  // set to false for better speed measurement

void setup() {
  Ethernet.init(CS_PIN);   
  // Open serial communications and wait for port to open:
  Serial.begin(115200);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  }

  // start the Ethernet connection:
  Serial.println("Initialize Ethernet with DHCP:");
  if (Ethernet.begin(mac) == 0) {
    Serial.println("Failed to configure Ethernet using DHCP");
    // Check for Ethernet hardware present
    if (Ethernet.hardwareStatus() == EthernetNoHardware) {
      Serial.println("Ethernet shield was not found.  Sorry, can't run without hardware. :(");
      while (true) {
        delay(1); // do nothing, no point running without Ethernet hardware
      }
    }
    if (Ethernet.linkStatus() == LinkOFF) {
      Serial.println("Ethernet cable is not connected.");
    }
    // try to congifure using IP address instead of DHCP:
    Ethernet.begin(mac, ip, myDns);
  } else {
    Serial.print("  DHCP assigned IP ");
    Serial.println(Ethernet.localIP());
  }
  // give the Ethernet shield a second to initialize:
  delay(1000);
  Serial.print("connecting to ");
  Serial.print(server);
  Serial.println("...");

  // if you get a connection, report back via serial:
  if (client.connect(server, 80)) {
    Serial.print("connected to ");
    Serial.println(client.remoteIP());
    // Make a HTTP request:
    client.println("GET /search?q=arduino HTTP/1.1");
    client.println("Host: www.google.com");
    client.println("Connection: close");
    client.println();
  } else {
    // if you didn't get a connection to the server:
    Serial.println("connection failed");
  }
  beginMicros = micros();
}

void loop() {
  // if there are incoming bytes available
  // from the server, read them and print them:
  int len = client.available();
  if (len > 0) {
    byte buffer[80];
    if (len > 80) len = 80;
    client.read(buffer, len);
    if (printWebData) {
      Serial.write(buffer, len); // show in the serial monitor (slows some boards)
    }
    byteCount = byteCount + len;
  }

  // if the server's disconnected, stop the client:
  if (!client.connected()) {
    endMicros = micros();
    Serial.println();
    Serial.println("disconnecting.");
    client.stop();
    Serial.print("Received ");
    Serial.print(byteCount);
    Serial.print(" bytes in ");
    float seconds = (float)(endMicros - beginMicros) / 1000000.0;
    Serial.print(seconds, 4);
    float rate = (float)byteCount / seconds / 1000.0;
    Serial.print(", rate = ");
    Serial.print(rate);
    Serial.print(" kbytes/second");
    Serial.println();

    // do nothing forevermore:
    while (true) {
      delay(1);
    }
  }
}

```

<FunctionDocumentation
  functionName="Ethernet.begin()"
  description="Initializes the Ethernet library and network settings."
  returnDescription="version Ethernet.begin(mac) returns true on success, false on error. Other versions don't return anything."
  parameters={[ 
    { type: '6 byte array', name: 'mac', description: 'MAC address for the device.' },
    { type: '4 byte array', name: 'ip', description: 'Optional, IP address of the device.' },
    { type: '4 byte array', name: 'dns', description: 'Optional, IP address of the DNS server.' },
    { type: '4 byte array', name: 'gateway', description: 'Optional, IP address of the network gateway.' },
    { type: '4 byte array', name: 'subnet', description: 'Optional, subnet mask of the network.' },
  ]}
/>

<FunctionDocumentation
  functionName="Ethernet.hardwareStatus()"
  description="Tells which WIZnet Ethernet controller chip was detected during Ethernet.begin(), if any."
  returnType="None"
/>

<FunctionDocumentation
  functionName="Ethernet.linkStatus()"
  description="Tells whether the link is active, only available when using the W5200 and W5500 chips."
  returnDescription="Returns link status; Unknown, LinkON, or LinkOFF."
/>

<FunctionDocumentation
  functionName="client.connect()"
  description="Connects to a specified IP address and port."
  returnDescription="Returns true if the connection succeeds, false if not."
  parameters={[ 
    { type: '4 byte array', name: 'ip', description: 'The IP address that the client will connect to.' },
    { type: 'String', name: 'servername', description: 'The domain name the client will connect to.' },
    { type: 'int', name: 'port', description: 'The port that the client will connect to.' }
  ]}
/>

<FunctionDocumentation
  functionName="client.write()"
  description="Write data to the server the client is connected to."
  returnDescription="Number"
  returnType="int"
  parameters={[ 
    { type: 'byte or char', name: 'val', description: 'A value to send as a single byte or char.' },
    { type: 'byte or char', name: 'buf', description: 'An array to send as a series of bytes or chars.' },
    { type: 'int', name: 'len', description: 'The length of the buffer.' },
  ]}
/>

<FunctionDocumentation
  functionName="client.stop()"
  description="Disconnect from the server."
  returnType="None"
/>

## Serial Monitor output

<CenteredImage src="/img/w5500/httpserial.png" alt="Output from Serial Monitor" caption="Output from Serial Monitor" width="1200px" />

---

## Full example
Check out the original example from `docs.arduino.cc` below:

<QuickLink 
  title="Ethernet WebClient example" 
  url="https://docs.arduino.cc/tutorials/ethernet-shield-rev2/web-client/"
/>