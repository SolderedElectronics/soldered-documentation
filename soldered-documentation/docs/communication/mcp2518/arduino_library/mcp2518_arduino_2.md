---
slug: /mcp2518/arduino/can20examples 
title: CAN Transciever MCP2518 - CAN2.0 Communication example
id: mcp2518-arduino-2 
sidebar_label: CAN2.0 Communication example
hide_title: False
---

This page contains a full communication example between two **Dasduino COREs** using the **MCP2518** modules and **CAN2.0** protocol.

## Sending frames through CAN network using CAN 2.0

To start sending frames through CAN, first initialize the class instance, to check how to to that, visit the page before this one. To send a frame through CAN, call the `sendMsgBuf()` function. check the example below:

```cpp

#include "CANBus-SOLDERED.h"

// Change according to your setup
const int SPI_CS_PIN = 10;

CANBus CAN(SPI_CS_PIN); // Set CS pin

void setup()
{
  Serial.begin(115200); //Begin serial communication with PC

  while (CAN_OK != CAN.begin(CAN_125KBPS))  // Initialize CAN BUS with baud rate of 125 kbps
    // This should be in while loop because MCP2518
    // needs some time to initialize and start function
    // properly.
  {
    Serial.println("CAN init fail, retry..."); // Print information message
    delay(100);
  }
  Serial.println("CAN init ok!");
}

unsigned char stmp[8] = {0, 1, 2, 3, 4, 5, 6, 7}; // Buffer which stores data to send

void loop()
{

  CAN.sendMsgBuf(0x01, 0, 8, stmp); // Send data in CAN network
  delay(10); // Wait a bit for CAN module to send data
  CAN.sendMsgBuf(0x04, 0, 8, stmp); // Send same data again
  delay(500); // Wait a bit not to overfill network
  Serial.println("CAN BUS sendMsgBuf ok!"); // Print message
}

```

<FunctionDocumentation
  functionName="CAN.sendMsgBuf()"
  description="Send data in CAN network."
  returnType="bool"
  parameters={[
    { type: 'unsigned long', name: 'id', description: 'ID of transmitter.' },
    { type: 'byte', name: 'ext', description: 'Frame size (0 - Normal frame, 1 - Extended frame).' },
    { type: 'byte long', name: 'len', description: 'Length of buffer in bytes.' },
    { type: 'const byte', name: 'buf', description: 'Buffer which contains data to send.' },
  ]}
/>

---

## Receiving data through CAN network using CAN 2.0

To start receiving data from CAN netwrk, first check if there is data coming by using the `checkReceive()` function. After that, call the `readMsgBuf()` function to save received data into a buffer. To check the ID of transmitter call the `getCanId()` function. Check the example below:

```cpp
#include "CANBus-SOLDERED.h"

// Change pins accordingly
const int SPI_CS_PIN = 10;

CANBus CAN(SPI_CS_PIN); //Set CS pin

void setup()
{
  Serial.begin(115200); //Begin serial communication with PC

  while (CAN_OK != CAN.begin(CAN_125KBPS))  // Initialize CAN BUS with baud rate of 125 kbps
    // This should be in while loop because MCP2518
    // needs some time to initialize and start function
    // properly.
  {
    Serial.println("CAN init fail, retry..."); // Print information message
    delay(100);
  }
  Serial.println("CAN init ok!");
}


void loop()
{
  unsigned char len = 0; // Variable to store length of incoming data
  unsigned char buf[8];  // Buffer to store incoming data

  if (CAN_MSGAVAIL == CAN.checkReceive()) // Check if data coming
  {

    CAN.readMsgBuf(&len, buf);  // You should call readMsgBuff before getCanId
    // This function saves incoming data into buffer buf
    // It saves len number of bytes
    unsigned long id = CAN.getCanId(); // Get ID of transmitter
    Serial.print("Get Data From id: "); // Print ifnormatio message
    Serial.println(id); // Print ID of transmitter
    Serial.print("Len = ");
    Serial.println(len);// Print length of the data
    for (int i = 0; i < len; i++)
    {
      Serial.print(buf[i]); // Print array with received data
      Serial.print("\t"); // Print tabulator to format printing
    }
    Serial.println(); // Print new line at the end
  }
}
```

<FunctionDocumentation
  functionName="CAN.checkReceive()"
  description="This function checks if data is comming."
  returnType="byte"
/>

<FunctionDocumentation
  functionName="CAN.readMsgBuf()"
  description="This function saves incoming data into a buffer."
  returnDescription="Number"
  returnType="int"
  parameters={[
    { type: 'byte', name: 'len', description: 'Length of buffer in bytes.' },
    { type: 'byte', name: 'buf', description: 'Buffer which contains data to send.' },
  ]}
/>

<FunctionDocumentation
  functionName="CAN.getCanId()"
  description="This function returns the ID of transmitter"
  returnType="unsigned long"
/>

After all is connected properlly,you can open two separate Serial monitors on different ports by opening two different sketches. If all the steps were done correctly, Serial monitor output should look like this:


<CenteredImage src="/img/mcp2518/CAN_send_20.png" alt="Serial monitor on sending part of communication" caption="Serial monitor on sending part of communication." />

<CenteredImage src="/img/mcp2518/CAN_receive_20.png" alt="Serial monitor on receiving part of communication" caption="Serial monitor on receiving part of communication." />
