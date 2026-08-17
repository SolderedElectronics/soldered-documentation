---
slug: /button-led-buzzer-board/arduino/getting-started
title: Button, LED & Buzzer Board - Getting started
sidebar_label: Getting started
id: button_led_buzzer_board-arduino-1
hide_title: false
---

## Arduino library

This library isn't in the Arduino Library Manager yet, so download it directly from the GitHub repository:

<QuickLink  
  title="Soldered-Button-LED-Buzzer-Board-Arduino-Library"  
  description="Arduino library for the Button, LED & Buzzer Board with Qwiic by Soldered"  
  url="https://github.com/SolderedElectronics/Soldered-Button-LED-Buzzer-Board-Arduino-Library"  
/>

Click **Code → Download ZIP** on the repository page, then in the Arduino IDE go to **Sketch → Include Library → Add .ZIP Library...** and select the downloaded file.

<InfoBox>

**First time Arduino user?** For a detailed tutorial on how to get started with Arduino, see this section of our docs:

<QuickLink  
  title="Getting started with Arduino"  
  description="A full, comprehensive tutorial on how to fully set up and upload code for the first time on an Arduino board, from scratch!"  
  url="/arduino/quick-start-guide"  
/>  

</InfoBox>

---

## Connections

| **NULA Deepsleep** | **Button, LED & Buzzer Board** |
| ------------------ | ------------------------------ |
| Qwiic              | Qwiic                          |

<InfoBox>The board answers on I2C address **0x30** by default. If you changed it with the onboard DIP switch, pass the new address to the constructor: `ButtonLedBuzzerBoard_Soldered board(0x31);`</InfoBox>

---

## Examples

The library ships five example sketches:

<QuickLink
  title="FullDemo.ino"
  description="Exercises the buttons, LEDs and buzzer together - a good first upload to check everything works"
  url="https://github.com/SolderedElectronics/Soldered-Button-LED-Buzzer-Board-Arduino-Library/blob/main/examples/FullDemo/FullDemo.ino"
/>

The remaining four - `Buttons`, `LEDs`, `Buzzer` and `ButtonInteraction` - are covered on the pages that follow.

