---
slug: /rs-232/arduino/examples
title: Rs 232 - Arduino (Example)
sidebar_label: Arduino (Example)
id: rs-232-arduino-2
hide_title: false
---

In this example, **two Dasduino ConnectPlus boards** are connected using the **RS-232 protocol** to enable **serial communication**. The objective is for one Dasduino (**Sender**) to transmit commands (**"ON" or "OFF"**) via RS-232 to the second Dasduino (**Receiver**), which processes these commands to control an **LED** (the LED is protected with a 330Ω resistor).

---

### Sender Code:

```cpp
#include <HardwareSerial.h>

HardwareSerial rs232Serial(1); // Use UART1

const String ON_COMMAND = "ON";
const String OFF_COMMAND = "OFF";

void setup() {
  Serial.begin(115200); // Debugging via Serial Monitor
  rs232Serial.begin(115200, SERIAL_8N1, 14, 13); // Initialize RS-232 communication (RX=14, TX=13)
}

void loop() {
  rs232Serial.println(ON_COMMAND); // Send "ON" command
  Serial.println("Sent: " + ON_COMMAND); // Debugging: Confirm data sent
  delay(2000);

  rs232Serial.println(OFF_COMMAND); // Send "OFF" command
  Serial.println("Sent: " + OFF_COMMAND); // Debugging: Confirm data sent
  delay(2000);
}
```

---

### Receiver Code:

```cpp
#include <HardwareSerial.h>

HardwareSerial rs232Serial(2); // Use UART2
#define LED_PIN 33              // Define GPIO pin for LED

const String ON_COMMAND = "ON";
const String OFF_COMMAND = "OFF";

void setup() {
  rs232Serial.begin(115200, SERIAL_8N1, 26, 27); // Initialize RS-232 communication (RX=26, TX=27)
  Serial.begin(115200);                           // Debugging via Serial Monitor
  pinMode(LED_PIN, OUTPUT);                       // Set LED pin as output
}

void loop() {
  if (rs232Serial.available()) {
    String command = rs232Serial.readStringUntil('\n'); // Read incoming command
    command.trim();                                     // Remove any extra whitespace or newline characters
    Serial.println("Received: " + command);             // Debugging: Print trimmed command

    if (command == ON_COMMAND) {
      digitalWrite(LED_PIN, HIGH); // Turn on LED
      Serial.println("LED turned ON");
    } else if (command == OFF_COMMAND) {
      digitalWrite(LED_PIN, LOW); // Turn off LED
      Serial.println("LED turned OFF");
    } else {
      Serial.println("Command is neither ON nor OFF");
    }
  }
}
```
---

<CenteredImage src="/img/rs-232/breadboard.png" alt="Breadboard connection for given example" caption="Breadboard connection for given example"/>


<CenteredImage src="/img/rs-232/sides.png" alt="Side by side serial monitor outputs" caption="Side by side serial monitor outputs"/>
  

<InfoBox>
**Why you should use a 330Ω resistor on the LED**  
A 330Ω resistor is recommended to limit the current flowing through the LED, preventing it from burning out. Without the resistor, the LED may draw excessive current, potentially damaging both the LED and the GPIO pin of your Dasduino board. 
</InfoBox>