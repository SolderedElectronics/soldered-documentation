---
slug: /nrf24l01/how-it-works 
title: How it works
id: nrf24l01-how-it-works 
hide_title: False
---  

The **nFR24L01+** is a wireless transciever module by  [**Nordic Semiconductor**](https://www.nordicsemi.com/Products/nRF54L15?utm_campaign=nRF54L15&utm_source=paidsearch&utm_medium=googleads&utm_feeditemid=&utm_device=c&utm_term=nrf54l15&utm_source=google&utm_medium=ppc&utm_campaign=nRF54L15&hsa_cam=22088148164&hsa_grp=171705928974&hsa_mt=b&hsa_src=g&hsa_ad=727766411652&hsa_acc=1116845495&hsa_net=adwords&hsa_kw=nrf54l15&hsa_tgt=kwd-2316120203756&hsa_ver=3&gad_source=1&gbraid=0AAAAADPygHImk7EFvqpsgUbNofR4u72sr&gclid=Cj0KCQjwh_i_BhCzARIsANimeoG5yURfxj8psW2VQohO961r5U7SQpyj3gU6Go36BEj4FgX8znpC0GgaApppEALw_wcB) that works on 2.4 GHz range, which is great for short-range communication. It features **Enhanced ShockBurst** which includes features such as **Automatic packet handling**, **Auto packet transaction handling** and **6 data pipe MultiCeiver** which means that one module can support up to 6 receiver addresses. It uses SPI interface to communicate with a MCU.

<CenteredImage src="/img/nrf24l01/nrf24l01_onboard_highlighted.jpg" alt="nRF24L01+ on the adapter board" caption="nRF24L01+ on the adapter board" width="500px" />

---

## Datasheet

For detailed tehnical specifications, please refer to the official nFR24L01+ Datasheet:
<QuickLink  
  title="nFR24L01+ Datasheet"  
  description="Complete technical documentation for the nRF24L01+ board"  
  url="https://soldered.com/productdata/2015/02/Soldered_nRF24L01Plus_datasheet.pdf"  
/>  

---

## How the nFR24L01+ Works

The nFR24L01+ module has a built-in state machine that controls the transitions between the different operating modes on the chip.

In **Power Down Mode**, module will be disabled, So the power consumption will be minimal, but **SPI** will be kept active so that register values can be accessed.

In **Standby Mode I and II** module is in intermediate state before going for **TX** or **RX** mode. In Mode I only crystal oscillator is active, but in Mode II, extra clock buffers are active as well.

In **RX Mode**, module continuously demodulates the signal from RF channel and sends that to the **baseband protocol engine (Enhanced ShockBurst)**. The engine checks the validity of the received packet by checking the address and CRC. If packet is valid it will write to the **RX FIFO** but **if it's full, packet will be discarded**.

<InfoBox>nRF24L01 module remains in the RX mode until we configure it to either go to Standby or Power Down Mode. If Enhanced ShockBurst feature is enabled, then it can enter to other modes.</InfoBox>

Module enters the **TX Mode** automatically when data is transmited. It stays in TX mode until transmission of the current packet is finished, after that it checks the **TX FIFO** for additional packets, if none are available, module goes to one of the standby modes.

<CenteredImage src="/img/nrf24l01/state_diagram.jpg" alt="Radio control state diagram" caption="Radio control state diagram" width="750px" />

---

## RF Channel Frequency

The **nRF24L01** module communicates using the **2.4GHz** ISM band, and the **channel bandwidth** is **1Mhz** at 1Mbps and **2Mhz** at 2Mbps, which means that at 1Mbps we can transmit or receive on 2400MHz, 2401MHz, 2402MHz ... 2525MHz and at 2Mbps on 2400MHz, 2402MHz... All that means that at 1Mbps communication **126 channels** and at 2Mbps **63 channels** are available.

<InfoBox>A transmitter and a receiver must be programmed with the same RF channel frequenca to be able to communicate with each other. If the transmitter is transmitting at 2500MHz, receiver must listen on the same channel!</InfoBox>

The  RF channel frequency is set by the `RF_CH` register according to the following formula: `F0=2400 + RF_CH [MHz]`

---

## Enhanced ShockBurst

Ehanced ShockBurst is a **packed based data link layer**. It features **automatic assembly and timing**, **automatic acknowledgement** and **re-transmissions** of packets. It enables the implementation of **ultra low power, high performance communication** with low cost microcontrollers.During transmit, ShockBurst assembles the packet and clocks the bits in the data packet into the transmitter for transmission. During receive, ShockBurst constantly searches for a valid address in the demodulated signal. When ShockBurst finds a valid address, it processes the rest of the packet and validates it by **CRC**. If the packet is valid the payload is moved into the RX FIFO. To find out more about Enhanced ShockBurst, its features and more, check out the [Datasheet](http://localhost:3000/documentation/nrf24l01/how-it-works#datasheet)

---

## Multiceiver

Multiceiver is a feature used in RX mode that contais a set of **6 parallerl data pipes with unique addresses**. A data pipe is a logical channel in the physical RF channel. Each data pipe has its own physical address decoding in the nRF24L01. nRF24L01 configured as PRX (primary receiver) can receive data addressed to six different data pipes in one frequency channel. Each data pipe has its own unique address and can be configured for individual behavior. Each pipe can have up to 5 byte configurable address. Data pipe 0 has a unique 5 byte address. Data pipes 1-5 share the 4 most significant address bytes. The **LSByte must be unique for all 6 pipes**. 

<CenteredImage src="/img/nrf24l01/multiceiver.jpg" alt="PRX using multiceiver" caption="PRX using multiceiver" width="750px" />

<CenteredImage src="/img/nrf24l01/address.jpg" alt="Addressing data pipes 0-5 example" caption="Addressing data pipes 0-5 example" width="750px" />

<InfoBox>Each data pipe address is configured in the `RX_ADDR_PX` registers</InfoBox>