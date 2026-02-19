---
slug: /nula-core/arduino
title: NULA Core - Getting started with Arduino
sidebar_label: Getting started with Arduino
id: core_arduino_1
pagination_next: null
hide_title: True
---

# Getting started with Arduino

<InfoBox>

**Are you a first-time Arduino user?**  
For a step-by-step guide on installing Arduino, connecting your board, and uploading your first sketch, see this section of our docs:

<QuickLink  
  title="Getting started with Arduino"  
  description="A comprehensive beginner’s guide to setting up Arduino and uploading your first program."  
  url="/documentation/arduino/quick-start-guide"  
/>
</InfoBox>

## NULA board definitions

To program your **NULA Core**, you will have to install the board definitions which are like complete packages of software so that Arduino can compile and upload your code correctly. To do that follow the next few steps below:

**Copy the following URL:**

```
https://github.com/SolderedElectronics/Dasduino-Board-Definitions-for-Arduino-IDE/raw/master/package_Dasduino_Boards_index.json
```

and add it to **Additional Boards Manager** under **File -> Preferences** in your Arduino IDE.

<CenteredImage src="/img/arduino/quick-start-guide/additional_boards_manager.jpg" alt="Adding the NULA boards link to Arduino IDE" caption="Adding the NULA boards link to Arduino IDE" width="600px"/>

Now, install new boards via **Tools -> Board -> Boards Manager**. In the search box, type in `nula` or `dasduino` and select the **NULA AVR Boards by Soldered**.

<CenteredImage src="/img/nula-core/nula-avr-boards.png" alt="Adding NULA boards to Arduino IDE" caption="Adding NULA boards to Arduino IDE" width="600px"/>


Once installed, select your board from the menu:
**Tools -> Board -> NULA AVR Boards -> NULA CORE** and start writing your sketches!

---

## Example sketch

Once your board is selected and connected via USB-C, try uploading this simple example to verify everything is working:

```cpp
void setup() {
  Serial.begin(115200);
  Serial.println("Hello from NULA Core!");
}

void loop() {
  delay(1000);
  Serial.println("Running...");
}
```

<InfoBox> If uploading fails, double-check that the **correct board and port are selected.** </InfoBox>