---
slug: /rs-485/arduino/troubleshooting
title: Rs 485 - Troubleshooting
id: rs-485-arduino-3
hide_title: false
pagination_next: null
---

This page contains some tips in case you are having problems using this product.

<ExpandableSection title="The RS-485 communication won't initialize!">

#### Check wiring
Ensure that the RS-485 breakout board is correctly wired to the Dasduino CONNECTPLUS:

*   **D (Driver Input)** on the RS-485 breakout board should connect to **TX** on the Dasduino.
*   **R (Receiver Output)** on the RS-485 breakout board should connect to **RX** on the Dasduino.
*   **DE (Driver Enable)** should connect to a GPIO pin (e.g., GPIO 12) on the Dasduino and be set HIGH during transmission.
*   **NRE (Receiver Enable)** should connect to a GPIO pin (e.g., GPIO 11) on the Dasduino and be set LOW during reception.
*   Ensure that **A** and **B** lines are properly connected between both RS-485 breakout boards.
  
  
#### Verify baud rate
Both devices must use the same baud rate. If you’re using 115200, ensure that both the sender and receiver are configured with this value in their code.

#### Check common ground
Both devices must share a common ground. Ensure that the GND pin of the RS-485 breakout board is connected to the GND pin of the Dasduino.

#### Test with a loopback
To verify if each RS-485 breakout board is functioning:
1.  Connect **A** to **B** directly on the same breakout board.   
2.  Send data from the Dasduino and check if it echoes back correctly.


#### Termination Resistor Configuration
Ensure JP2 is correctly configured:
*   Close JP2 if your RS-485 breakout board is at one end of the bus.
*   Leave JP2 open if your breakout board is not at an endpoint.

#### Try running our examples

If you’re confident that your wiring and configuration are correct, try running our [**RS-485 Communication Example**](rs-485_arduino_2.md#sender-code).

</ExpandableSection>

<ExpandableSection title="I can't receive or send data!">   

#### Trim received data

RS-485 communication often appends extra characters like spaces or newline characters (\\n). Use `.trim()` in your code to clean up received strings before processing them.

#### Verify TX/RX connections    
*   The sender’s **TX pin** is connected to the receiver’s **D (Driver Input)**.
*   The receiver’s **RX pin** is connected to the sender’s **R (Receiver Output)**.

### Check DE/NRE logic   
*   The sender sets **DE HIGH** during transmission.
*   The receiver sets **NRE LOW** during reception.
  
#### Check voltage levels

Ensure that both devices are powered correctly:
*   The RS-485 breakout board should be powered with 5V from the Dasduino.
*   Ensure that there is no voltage mismatch between devices.
    
#### Debug with Serial Monitor

Add debugging messages `Serial.println()` in your code to confirm whether data is being sent or received correctly.

</ExpandableSection> 

<ExpandableSection title="The LED doesn't turn on/off!">

#### Test LED circuit

Manually test the LED by connecting it directly to 5V and GND through a resistor. If it doesn’t light up, there may be an issue with your LED or wiring.

#### Verify GPIO output

Use a simple sketch to toggle the GPIO pin controlling the LED:

```cpp
void setup() {
  pinMode(33, OUTPUT);
}

void loop() {
  digitalWrite(33, HIGH); // Turn on LED
  delay(1000);
  digitalWrite(33, LOW);  // Turn off LED
  delay(1000);
}
```
</ExpandableSection>