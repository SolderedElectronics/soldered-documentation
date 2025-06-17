---
slug: /w5500/how-it-works 
title: W5500 - How it works
id: w5500-how-it-works 
sidebar_label: How it works
hide_title: False
---  

The **W5500** chip is a **Hardwired TCP/IP** embedded **Ethernet controller** that provides an easier Internet connection for embedded systems. The W5500 enables users to add Internet connectivity to their applications with a single chip that embeds the **TCP/IP stack**, **10/100 Ethernet MAC**, and **PHY**. WIZnet's Hardwired TCP/IP is the market-proven technology that supports **TCP, UDP, IPv4, ICMP, ARP, IGMP, and PPPoE protocols**. The W5500 also includes a 32Kbyte internal memory buffer for Ethernet packet processing. If you use the W5500, you can implement an Ethernet application simply by adding a basic socket program.

<CenteredImage src="/img/w5500/w5500_highlighted.png" alt="W5500 onboard" caption="W5500 onboard" width="500px" />

---

## Datasheet

For detailed technical specifications, please refer to the official W5500 Datasheet:  

<QuickLink  
  title="W5500 Datasheet"  
  description="Complete technical documentation for the W5500 IC"  
  url="https://soldered.com/productdata/2022/03/Soldered_W5500_datasheet-1.pdf"  
/>  

---

## How It Works

To communicate with the W5500, a microcontroller uses a simple interface called SPI (Serial Peripheral Interface). Through this connection, the microcontroller can open up to 8 separate network "sockets" simultaneously, enabling it to send and receive data over the internet using common protocols such as TCP and UDP. The W5500 also includes its own memory to store incoming and outgoing data, which makes data handling faster and more efficient.

### SPI Operation Mode

The W5500 is controlled by an SPI frame that communicates with the external host. The **W5500 SPI Frame** consists of three phases: **Address Phase**, **Control Phase**, and **Data Phase**. The **Address Phase** specifies a 16-bit offset address for a W5500 register or TX/RX memory. The **Control Phase** specifies the block to which the offset (set by the Address Phase) belongs, along with the Read/Write access mode and the SPI operation mode (Variable Length Data Mode / Fixed Length Data Mode). The **Data Phase** supports either a variable length (N bytes, where 1 ≤ N) or fixed lengths of 1, 2, or 4 bytes. If the SPI operation mode is set to Variable Length Data Mode (VDM), the SPI bus signal SCSn must be controlled by the external host following the SPI frame steps. In Variable Length Data Mode, the SCSn Control Start (assertion, i.e., a high-to-low transition) signals to the W5500 the start of the SPI frame (Address Phase), and the SCSn Control End (de-assertion, i.e., a low-to-high transition) signals the end of the SPI frame (the end of the Data Phase for a variable N-byte transfer).

<CenteredImage src="/img/w5500/SPI_frame_format.png" alt="SPI Frame Format" caption="SPI Frame Format" width="500px" />