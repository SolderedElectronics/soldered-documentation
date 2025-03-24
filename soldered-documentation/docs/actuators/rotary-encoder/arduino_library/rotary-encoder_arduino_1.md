---
slug: /rotary-encoder/arduino/geting-started 
title: Getting started
id: rotary-encoder-arduino-1 
hide_title: False
---

## Arduino Library

To install the Arduino library, you can use the **Arduino library manager** or download it from the GitHub repository:
<QuickLink  
  title="Rotary encoder with Qwiic Arduino library"  
  description="Rotary encoder with Qwiic Arduino library by Soldered"  
  url="https://github.com/SolderedElectronics/Soldered-Rotary-Encoder-With-easyC-Arduino-Library"  
/>  


<InfoBox>

**First time Arduino user?** For a detailed tutorial on how to get started wtih Arduino, see this section of our docs:

<QuickLink  
  title="Getting started with Arduino"  
  description="A full, comprehensive tutorial on how to fully set up and upload code for the first time on an Arduino board, from scratch!"  
  url="#"  
/>  

</InfoBox>

---

## Connections

Below is an example connection diagram for **Dasduino CONNECTPLUS**. These pins will be used in the examples throughout this documentation. To change circuit boards address, check the [**Address selection**](/documentation/rotary-encoder/hardware#address-selection).

| **Dasduino CONNECTPLUS** | **Breakout Board** |
| ------------------------ | ------------------ |
| Qwiic                    | Qwiic              |

<InfoBox> Qwiic versions also contain UPDI headers for onboard ATTINY404 programing, they are not used for encoder communication! </InfoBox>