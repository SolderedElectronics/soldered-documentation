---
slug: /mcp2518/how-it-works 
title: CAN Transceiver MCP2518 - How it works
id: mcp2518-how-it-works 
sidebar_label: How it works
hide_title: false
---  

The **MCP2518FD** is a CAN FD controller made by Microchip Technology. It acts as a bridge between a microcontroller's SPI bus and a CAN network, handling the full CAN protocol stack in hardware so the microcontroller only needs to read and write messages over SPI.

<CenteredImage src="/img/mcp2518/onboard.png" alt="MCP2518FD onboard" caption="MCP2518FD onboard" width="500px" />

---

## Datasheet

For detailed technical specifications, please refer to the official MCP2518FD Datasheet:  

<QuickLink  
  title="MCP2518FD Datasheet"  
  description="Complete technical documentation for the MCP2518FD IC"  
  url="https://ww1.microchip.com/downloads/aemDocuments/documents/OTH/ProductDocuments/DataSheets/External-CAN-FD-Controller-with-SPI-Interface-DS20006027B.pdf"  
/>  

---

## How the MCP2518FD works

CAN bus uses **differential signaling** on two wires — CANH and CANL — which are driven to a voltage difference of about 2 V for a dominant bit and left floating (same voltage) for a recessive bit. This differential approach makes CAN highly resistant to electrical noise, which is why it is the standard in automotive and industrial environments. All nodes on the bus share the same two wires; any node can transmit and all others receive simultaneously.

The MCP2518FD sits between the microcontroller's SPI bus and the CAN physical layer (handled by a separate CAN transceiver IC, also on this board). When the microcontroller wants to send a message, it writes the CAN ID, data length, and payload into the chip over SPI. The MCP2518FD then serializes that data into CAN frames, arbitrates for bus access using the CAN protocol, and transmits. On the receive side, the chip monitors the bus, filters incoming frames by ID using its 32 configurable hardware filters, and notifies the microcontroller via the INT pin when a matching message arrives.

CAN 2.0B supports payloads of up to 8 bytes at bit rates up to 1 Mbps. CAN FD (Flexible Data-Rate) extends this to 64-byte payloads and allows the data phase to run at a different (typically higher) bit rate than the arbitration phase — for example, 125 kbps arbitration with 500 kbps or 2 Mbps data, selected at initialization time.

The Arduino library wraps all SPI transactions and frame formatting. You call `CAN.begin()` with the desired bit rate, then `CAN.sendMsgBuf()` to transmit or `CAN.readMsgBuf()` to receive — the chip handles arbitration, error detection, retransmission, and CRC checking automatically.
