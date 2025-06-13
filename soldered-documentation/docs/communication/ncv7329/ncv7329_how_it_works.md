---
slug: /ncv7329/how-it-works 
title: NCV7329 – How it works
sidebar_label: How it works
id: ncv7329-how-it-works 
hide_title: False
---  

The LIN Transceiver NCV7329 Breakout, manufactured by [**Onsemi**](https://www.onsemi.com/products/interfaces/wired-transceivers-modems/NCV7329), enables reliable LIN bus communication between microcontrollers and automotive networks. Operating as an interface between the digital logic and the LIN bus, it ensures signal conversion, low power consumption, and protection features. Designed for master-slave communication, it facilitates seamless data exchange in automotive and industrial applications.

<CenteredImage src="/img/ncv7329/ncvonboard.png" alt="jp1" caption="NCV7329 on the board"/>

---

## Understanding LIN Bus Communication

The **Local Interconnect Network (LIN)** is a serial communication protocol commonly used in automotive applications to facilitate cost-effective communication between components. It operates on a **single-wire bus** and employs a **master-slave architecture**, ensuring deterministic and collision-free data exchange.

---

## Master-Slave Architecture

In a LIN network:

- **Master Node**: Oversees the communication process by initiating data frames and managing the communication schedule.
- **Slave Nodes**: Respond to the master's requests by providing data or executing commands as needed.

<CenteredImage src="/img/ncv7329/typapp.png" alt="app" caption="NCV7329 typical application"/>

---

## Communication Process

The communication sequence in a LIN network involves:

1. **Header Transmission**: The master node sends a header to the bus, signaling the start of a communication frame.
2. **Response**: The targeted slave node responds with the appropriate data or acknowledges the command.

---

## Operating States

The **NCV7329 LIN Transceiver** operates in three primary states: **Normal Mode, Sleep Mode, and Standby Mode**, ensuring efficient communication and power management.

In **Normal Mode**, the transceiver is fully active, allowing data transmission and reception on the LIN bus. The TXD (Transmit Data) and RXD (Receive Data) pins function normally, relaying information between the microcontroller and the LIN bus. The **EN pin must be set HIGH** to keep the transceiver in this state.

**Sleep Mode** is a low-power state designed to minimize energy consumption when the LIN bus is inactive. In this mode, communication is disabled, but the transceiver can still wake up if it detects activity on the LIN bus or if the **EN pin is set HIGH**.

**Standby Mode** is an intermediate state in which the transceiver monitors the LIN bus for wake-up signals while consuming less power than in Normal Mode. When a valid wake-up event occurs, the transceiver quickly transitions back to Normal Mode for full operation.

<CenteredImage src="/img/ncv7329/opstates.png" alt="op" caption="NCV7329 operating state diagram"/>