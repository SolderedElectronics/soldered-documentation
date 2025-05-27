---
slug: /rs-232/arduino/troubleshooting
title: "RS-232 Transceiver \u2013 Arduino troubleshooting"
id: rs-232-arduino-3
hide_title: false
pagination_next: null
---
This page contains some tips in case you are having problems using this product.

<ExpandableSection title="The RS-232 communication won't initialize!">

#### Check wiring
Ensure that the RS-232 breakout board is correctly wired to the Dasduino CONNECTPLUS:

*   **TX** on the Dasduino should connect to **DIN1 (TTL Transmit)** on the breakout board.
*   **RX** on the Dasduino should connect to **ROUT1 (TTL Receive)** on the breakout board.
*   Ensure that **DOUT1 (RS-232 Transmit)** and **RIN1 (RS-232 Receive)** are properly connected between both breakout boards.
  
#### Verify baud rate
Both devices must use the same baud rate. If you’re using 9600, ensure that both the sender and receiver are configured with this value in their code.

#### Check common ground
Both devices must share a common ground. Ensure that the GND pin of the RS-232 breakout board is connected to the GND pin of the Dasduino.

#### Test with a loopback
To verify if each RS-232 breakout board is functioning:
1.  Connect **TX** to **RX** directly on the same breakout board.   
2.  Send data from the Dasduino and check if it echoes back correctly.
   
#### Try running our examples

If you’re confident that your wiring and configuration are correct, try running our [**RS-232 Communication Example**](rs-232_arduino_2.md#sender-code).

</ExpandableSection>

<ExpandableSection title="I can't receive or send data!">   

#### Trim received data

RS-232 communication often appends extra characters like spaces or newline characters (\\n). Use `.trim()` in your code to clean up received strings before processing them.

#### Verify TX/RX connections

Ensure that:
*   The sender’s **TX pin** is connected to the receiver’s **RX pin**.  
*   The sender’s **RX pin** is connected to the receiver’s **TX pin**.
    
#### Check voltage levels

Ensure that both devices are powered correctly:
*   The RS-232 breakout board should be powered with 5V from the Dasduino.
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