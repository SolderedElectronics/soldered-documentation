---
slug: /mcp2518/arduino/canfdexamples 
title: CAN Transceiver MCP2518 - CANFD Communication example
id: mcp2518-arduino-3 
sidebar_label: CANFD Communication example
hide_title: false
---

This page contains a full communication example between two **NULA Mini** boards using the **MCP2518** modules and **CAN FD** protocol.

## Sending frames through CAN network using CAN FD

To start sending frames through CAN FD, first initialize the class instance - see the previous page for details. Use `CAN_125K_500K` (or another FD speed constant) in `begin()` to enable FD mode. CAN FD frames support payloads of up to 64 bytes; use `CANFD::len2dlc()` to convert the byte count to the DLC field:
```cpp
#include "CANBus-SOLDERED.h"
#include <SPI.h>

#define MAX_DATA_SIZE 64

// Change according to your setup
const int SPI_CS_PIN = 10;

// pin for CANBed FD
// const int SPI_CS_PIN = 17;
// const int CAN_INT_PIN = 7;

CANBus CAN(SPI_CS_PIN); // Set CS pin

unsigned char stmp[MAX_DATA_SIZE] = {0}; // Buffer which stores data to send

void setup()
{
  Serial.begin(115200); //Begin serial communication with PC

  while (0 != CAN.begin(CAN_125K_500K))// Initialize CAN BUS with baud rate of 125 kbps and arbitration rate of 500k
    // This should be in while loop because MCP2518
    // needs some time to initialize and start function
    // properly.
  {
    Serial.println("CAN init fail, retry..."); // Print information message
    delay(100);
  }
  Serial.println("CAN init ok!");

  for (int i = 0; i < MAX_DATA_SIZE; i++) // Fill buffer with ascending numbers 
  {
    stmp[i] = i;
  }
}


void loop()
{
  CAN.sendMsgBuf(0x01, 0, CANFD::len2dlc(MAX_DATA_SIZE), stmp); // Send data in CAN network
  delay(10); // Wait a bit for CAN module to send data
  CAN.sendMsgBuf(0x04, 0, CANFD::len2dlc(MAX_DATA_SIZE), stmp); // Send data in CAN network
  delay(500); // Wait a bit not to overfill network
  Serial.println("CAN BUS sendMsgBuf ok!"); // Print message
}
```

<FunctionDocumentation
  functionName="CANFD::len2dlc()"
  description="Converts a payload byte count (0-64) to the DLC (Data Length Code) field value required by CAN FD frames."
  returnDescription="DLC field value for the given byte length."
  returnType="uint8_t"
  parameters={[
    { type: 'uint8_t', name: 'len', description: 'Number of bytes in the payload (0-64).' },
  ]}
/>

---

## Receiving data through CAN network using CAN FD

To receive CAN FD frames, use the same `checkReceive()`, `readMsgBuf()`, and `getCanId()` functions as for CAN 2.0B - the library handles the larger payload automatically:

```cpp
#include "CANBus-SOLDERED.h"

#define MAX_DATA_SIZE 64

// Change according to your setup
const int SPI_CS_PIN = 10;

CANBus CAN(SPI_CS_PIN); // Set CS pin

unsigned char len = 0; // Variable to store length of incoming data
unsigned char buf[MAX_DATA_SIZE]; // Buffer to store incoming data

void setup()
{
  Serial.begin(115200); //Begin serial communication with PC

  while (0 != CAN.begin(CAN_125K_500K))// Initialize CAN BUS with baud rate of 125 kbps and arbitration rate of 500k
  {
    Serial.println("CAN init fail, retry..."); // Print information message
    delay(100);
  }
  Serial.println("CAN init ok!");
}

void loop()
{

  if (CAN_MSGAVAIL == CAN.checkReceive())
  {
    CAN.readMsgBuf(&len, buf);  // You should call readMsgBuff before getCanId
    // This function saves incoming data into buffer buf
    // It saves len number of bytes
    unsigned long id = CAN.getCanId(); // Get ID of transmitter
    Serial.print("Get Data From id: "); // Print information message
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

Once both boards are connected and their CAN FD sketches are running, open two Serial monitors. The output should look like this:


<CenteredImage src="/img/mcp2518/CAN_send_fd.png" alt="Serial monitor on sending part of communication" caption="Serial monitor on sending part of communication." />

<CenteredImage src="/img/mcp2518/CAN_receive_fd.png" alt="Serial monitor on receiving part of communication" caption="Serial monitor on receiving part of communication." />

<FunctionDocumentation
  functionName="CAN.checkReceive()"
  description="Checks whether a CAN message is waiting in the receive buffer."
  returnDescription="CAN_MSGAVAIL if a message is available, CAN_NOMSG otherwise."
  returnType="byte"
/>

<FunctionDocumentation
  functionName="CAN.readMsgBuf()"
  description="Reads the next available CAN message into the provided buffer. Call this after checkReceive() returns CAN_MSGAVAIL."
  returnDescription="CAN_OK on success."
  returnType="int"
  parameters={[
    { type: 'byte*', name: 'len', description: 'Pointer to a variable that receives the payload length in bytes.' },
    { type: 'byte*', name: 'buf', description: 'Pointer to a buffer that receives the payload data.' },
  ]}
/>

<FunctionDocumentation
  functionName="CAN.getCanId()"
  description="Returns the CAN ID of the most recently received message. Call after readMsgBuf()."
  returnDescription="11-bit (standard) or 29-bit (extended) CAN ID of the sender."
  returnType="unsigned long"
/>
