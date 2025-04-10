---
slug: /arduino/quick-start-guide
title: Quick start guide
id: arduino-quick-start-guide 
hide_title: False
pagination_prev: null
---

To get started with Arduino, complete a few simple steps to install the required software.

## 1. Install Arduino IDE
If you haven't installed it yet, download and install the Arduino IDE from the [official website](https://www.arduino.cc/en/software).

<InfoBox>Arduino IDE 2.0 or newer is recommended.</InfoBox> 

<CenteredImage src="/img/arduino/quick-start-guide/ide_download.jpg" alt="Download options for the latest release" caption="Download options for the latest release" width="600px"/>

<CenteredImage src="/img/arduino/quick-start-guide/ide.jpg" alt="Arduino IDE 2.0" caption="Arduino IDE 2.0" width="600px"/>

---

## 2. Install Dasduino board definition
Copy the following URL:
```
https://github.com/SolderedElectronics/Dasduino-Board-Definitions-for-Arduino-IDE/raw/master/package_Dasduino_Boards_index.json
```
And add it to the `Additional boards manager URLs` in Arduino settings:

<CenteredImage src="/img/arduino/quick-start-guide/ide_preferences.jpg" alt="Arduino IDE 2.0" caption="Arduino IDE 2.0" width="600px"/>
<CenteredImage src="/img/arduino/quick-start-guide/preferences.jpg" alt="Preferences menu in settings" caption="Preferences menu in settings" width="600px"/>
<CenteredImage src="/img/arduino/quick-start-guide/additional_boards_manager.jpg" alt="Adding the Dasduino boards link to Arduino IDE" caption="Adding the Dasduino boards link to Arduino IDE" width="600px"/>

Now, you can open the Boards Manager, search for Dasduino, and install the board definition for your specific board. Check the definition's description to ensure your board is included in that specific definition!

<CenteredImage src="/img/arduino/quick-start-guide/boards_manager.jpg" alt="Adding Dasduino boards to Arduino IDE" caption="Adding Dasduino boards to Arduino IDE" width="600px"/>

---

## 3. Connect the Dasduino board via USB
Use the provided **USB-C cable** to connect the Dasduino board to your computer.

<CenteredImage src="/img/arduino/quick-start-guide/usb_connection.png" alt="Connection via USB" caption="Connection via USB" width="600px"/>

---

## 4. Connections
To test if everything is working, we will use a basic circuit that consists of a single LED, a resistor, and two wires. Connect the circuit as shown below. Connect the red wire to the pin marked **14** and the black wire to the pin marked **GND**.

<CenteredImage src="/img/arduino/quick-start-guide/circuit.png" alt="Wiring example" caption="Wiring example" width="600px"/>

---

## 5. Upload your first code
In this example, we will use a modified version of the premade example called `Blink` to test if everything is running correctly. Simply copy the code below into the Arduino IDE.

```cpp
void setup() {
  // initialize digital pin LED_BUILTIN as an output.
  pinMode(14, OUTPUT);
}

// the loop function runs over and over again forever
void loop() {
  digitalWrite(14, HIGH);  // turn the LED on (HIGH is the voltage level)
  delay(1000);             // wait for a second
  digitalWrite(14, LOW);   // turn the LED off by making the voltage LOW
  delay(1000);             // wait for a second
}
```

Click on the `Board and port select` dropdown menu and select the `Select other board and port` button.

<CenteredImage src="/img/arduino/quick-start-guide/board_select.jpg" alt="Board select dropdown menu" caption="Board select dropdown menu" width="600px"/>

Search for your specific board. In this example, we use DasduinoCONNECTPLUS. Select the port to which the board is connected. If more ports are available, in most cases the correct port is the one with the largest number in its name.

<CenteredImage src="/img/arduino/quick-start-guide/select_board_and_port.jpg" alt="Board and Port selection" caption="Board and Port selection" width="600px"/>

Upload the code to the board by pressing the `Upload` button in the top left corner.

<CenteredImage src="/img/arduino/quick-start-guide/upload_button.jpg" alt="Upload code button" caption="Upload code button" width="600px"/>

<InfoBox>If the code doesn't upload, try selecting a different port.</InfoBox>

If all of the steps were completed correctly, your LED should blink as shown in the video below:

<CenteredImage src="/img/arduino/quick-start-guide/led_blinking.gif" alt="Upload code button" caption="Upload code button" width="600px"/>