---
slug: /mcp2518/how-it-works 
title: CAN Transciever MCP2518 - How it works
id: mcp2518-how-it-works 
sidebar_label: How it works
hide_title: False
---  

The **MCP2518FD** module is a cost-effective and small-footprint CAN FD controller that can be easily added to a microcontroller with an available SPI interface. MCP2518FD supports both CAN frames in the Classical format (CAN2.0B) and CAN Flexible Data Rate (CAN FD) format.

<CenteredImage src="/img/mcp2518/onboard.png" alt="MCP2518FD onboard" caption="MCP2518FD onboard" width="500px" />

---

## Datasheet

For detailed technical specifications, please refer to the official MCP2518FD Datasheet:  

<QuickLink  
  title="MCP2518FD Datasheet"  
  description="Complete technical documentation for the MCP2518FD IC"  
  url="https://soldered.com/productdata/2022/03/Soldered_MCP2518FD_datasheet.pdf"  
/>  

---

## How the MCP2518FD works

The chip connects to the main microcontroller through a standard **SPI** (Serial Peripheral Interface), allowing it to send and receive data on a CAN network. It supports both the older **CAN 2.0B** standard and the newer **CAN FD**, which allows faster data transmission and larger data payloads. Internally, it handles message filtering, prioritization, and error checking to ensure reliable communication. It's commonly used in automotive, industrial, and embedded systems where multiple devices need to communicate efficiently over a robust, high-speed network
