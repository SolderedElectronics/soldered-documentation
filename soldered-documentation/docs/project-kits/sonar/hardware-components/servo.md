---
slug: /sonar/hardware/servo
title: Sonar Project - Servo SG90
sidebar_label: Servo Motor
id: servo-motor
hide_title: false
---

## Servo Motor TowerPro SG90
Servo motor consist of a DC motor, a potentiometer, and a control board. As the motor turns, the resistance on the potentiometer changes. In this way, the control board can precisely regulate the rotation, speed, acceleration, and direction of the turn. This means the motor will only work as hard as is required to complete the task at hand. It is capable of turning 90 degrees in both directions, for a total range of 180 degrees.

<CenteredImage src="/img/sonar-project/microservo.png" alt="Image of Micro Servo Motor" caption="Servo Motor TowerPro SG90" width="600px"/>


We control servo motors by sending out **PWM (Pulse Width Modulation)** signal through control wire. The resulting signal consist of a series of square wave-like pulses. Depending on pulse width the rotor turns towards desired position.

---

## Full product details

<QuickLink 
  title="Servo motor TowerPro SG90" description="101246"
  url="https://solde.red/101246"
  image="/img/sonar-project/microservo.png" 
/>

---

## Connections to motor

| MCU Pin | Motor wire | 
|:---:|:---:|
| VCC | Red |
| GND | Brown |
| Any PWM Pin | Orange |

---

## Sweep both directions example


<ReactPlayer src='../../../videos/sonar-project/servo-demo.mp4' width='100%' height='auto' muted='true' autoPlay='true' loop='true'/>

---

### Example code

```cpp
#include <ESP32_Servo.h>

Servo myservo;  // Create servo object to control a servo
// Twelve servo objects can be created on most boards

int pos = 0;    // Variable to store the servo position

void setup() {
// Attaches the servo on pin 15 to the servo object
// with MIN and MAX pusle width (optional but recommended)
  myservo.attach(15, 500, 2400);   
}

void loop() {
  for (pos = 0; pos <= 180; pos += 1) { // Goes from 0 degrees to 180 degrees
    // In steps of 1 degree
    myservo.write(pos);              // Tell servo to go to position in variable 'pos'
    delay(15);                       // Waits 15ms for the servo to reach the position
  }
  for (pos = 180; pos >= 0; pos -= 1) { // Goes from 180 degrees to 0 degrees
    myservo.write(pos);              // Tell servo to go to position in variable 'pos'
    delay(15);                       // Waits 15ms for the servo to reach the position
  }
}
```
