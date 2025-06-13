---
slug: /drv8825/arduino/examples 
title: DRV8825 – Driving the motor (examples)
id: drv8825-arduino-2 
hide_title: False
---

This page contains simple examples with function documentation on how to drive the stepper motor.

---

## Initialization
To use the DRV8825 stepper driver, first, include the required library and create the driver object.
```cpp
#include <Basic-Stepper-Driver-SOLDERED.h>

#define dirPin 4
#define stepPin 5

BasicStepper stepper(BasicStepper::DRIVER, stepPin, dirPin);
//...
```
<FunctionDocumentation
  functionName="BasicStepper()"
  description="Constructor for the BasicStepper class, derived from AccelStepper. Initializes the stepper motor interface, sets the default parameters, and configures the output pins."
  returnDescription="None"
  parameters={[ 
    { type: 'uint8_t', name: 'interface', description: "Motor interface type, such as FULL4WIRE, FULL2WIRE, DRIVER, etc. Defaults to FULL4WIRE. See table below for more details." },
    { type: 'uint8_t', name: 'pin1', description: "Digital pin number for motor control. Defaults to pin 2." },
    { type: 'uint8_t', name: 'pin2', description: "Digital pin number for motor control. Defaults to pin 3." },
    { type: 'uint8_t', name: 'pin3', description: "Digital pin number for motor control. Defaults to pin 4." },
    { type: 'uint8_t', name: 'pin4', description: "Digital pin number for motor control. Defaults to pin 5." },
    { type: 'bool', name: 'enable', description: "If true, enables pin outputs. Defaults to true." }
  ]}
/>

| Interface Type             | Value | Description |
|---------------------------|-------|-------------|
| **DRIVER**                | `1`   | Uses a **step and direction** driver, requiring only 2 pins (STEP and DIR). Ideal for external stepper drivers like A4988, DRV8825. |
| **FULL2WIRE**             | `2`   | Controls a **2-wire stepper motor**, commonly used in unipolar configurations. Requires 2 control pins. |
| **FULL3WIRE**             | `3`   | Supports **3-wire stepper motors**, such as some older hard drive spindles. Requires 3 control pins. |
| **FULL4WIRE**             | `4`   | Standard **4-wire bipolar stepper motor** configuration. Requires 4 control pins. |
| **HALF3WIRE**             | `6`   | Used for **3-wire half-stepping motors**, allowing finer control over movement. |
| **HALF4WIRE**             | `8`   | Enables **half-stepping mode** for **4-wire stepper motors**, doubling the resolution for smoother motion. |

---

## Constant rotation
Let's start out with a basic example, turning the motor in one direction constantly.

```cpp
#include <Basic-Stepper-Driver-SOLDERED.h>

#define dirPin 4
#define stepPin 5

BasicStepper stepper(BasicStepper::DRIVER, stepPin, dirPin);
void setup() {
  stepper.setMaxSpeed(1000);
  stepper.setAcceleration(50);
  stepper.setSpeed(200);
}

void loop() {
  stepper.runSpeed();
}
```
<FunctionDocumentation
  functionName="stepper.setMaxSpeed()"
  description="Sets the maximum speed allowed for the motor. The motor will accelerate up to this speed during movement."
  returnDescription="None"
  parameters={[ 
    { type: 'float', name: 'speed', description: "Maximum speed in steps per second. Must be greater than 0." },
  ]}
/>

<FunctionDocumentation
  functionName="stepper.setAcceleration()"
  description="Sets the acceleration and deceleration rate for smooth motor control. Affects how quickly the motor reaches its max speed."
  returnDescription="None"
  parameters={[ 
    { type: 'float', name: 'acceleration', description: "Acceleration value in steps per second². Must be greater than 0." },
  ]}
/>

<FunctionDocumentation
  functionName="stepper.setSpeed()"
  description="Sets a constant speed for the motor when using runSpeed(). The speed will be limited by the setMaxSpeed() value."
  returnDescription="None"
  parameters={[ 
    { type: 'float', name: 'speed', description: "Speed in steps per second. Positive values rotate clockwise, negative values counterclockwise." },
  ]}
/>

<FunctionDocumentation
  functionName="stepper.runSpeed()"
  description="Moves the stepper motor at a constant speed based on the last setSpeed() value. This function must be called repeatedly in the loop for continuous motion."
  returnDescription="Returns true if the motor was stepped."
  parameters={[]}
/>

---

## Rotating a specified number of steps

In this example, we are using the **NEMA17** stepper motor which has **200 steps per revolution**. Let's rotate that motor for one quarter, then one half of one full rotation:

```cpp
#include <Basic-Stepper-Driver-SOLDERED.h>

#define dirPin 4
#define stepPin 5
#define motorInterfaceType 1

BasicStepper stepper(BasicStepper::DRIVER, stepPin, dirPin);
void setup() {
  stepper.setMaxSpeed(1000);
  stepper.setAcceleration(50);
  stepper.setSpeed(200);
}

void loop() {
  stepper.move(100);
  while(stepper.run()){}
  delay(2000);
  stepper.move(50);
  while(stepper.run()){}
  delay(2000);
}
```
<FunctionDocumentation
  functionName="stepper.move()"
  description="Sets the target position relative to the current position. This function does not immediately move the motor but sets the target steps to be executed when run() is called."
  returnDescription="None"
  parameters={[ 
    { type: 'long', name: 'relative', description: "The desired position relative to the current position. Negative values move counterclockwise." },
  ]}
/>

<FunctionDocumentation
  functionName="stepper.run()"
  description="Moves the motor towards the set target position while handling acceleration and deceleration automatically. Must be called repeatedly in the main loop for continuous operation."
  returnDescription="Returns true if the motor is still moving towards the target position."
  parameters={[]}
/>

You can also use `stepper.moveTo()` to set an **absolute target position** instead of a relative movement. Unlike `stepper.move()`, which moves the motor a certain number of steps from its current position, `moveTo()` moves the motor **to a specific step position** on the stepper's coordinate system. 

After calling `moveTo()`, you must call `run()` repeatedly in the loop to execute the movement. Keep in mind that `moveTo()` also **recalculates the speed** for the next step, so if you want to maintain a **constant speed**, you should call `setSpeed()` again after `moveTo()`:

```cpp
stepper.moveTo(1000); // Move to step position 1000
stepper.setSpeed(200); // Maintain a constant speed
while (stepper.run()); // Run until the target position is reached
```
<FunctionDocumentation
  functionName="stepper.moveTo()"
  description="Sets the target position for the stepper motor. The motor will move to this position when run() is called, handling acceleration and deceleration automatically."
  returnDescription="None"
  parameters={[ 
    { type: 'long', name: 'absolute', description: 'The absolute position (in steps) to move to. Negative values move counterclockwise from the home position.' }
  ]}
/>


---

## Full examples

Try these full working examples from the library:

<QuickLink 
  title="ConstantSpeed.ino" 
  description="Run the motor at constant speed"
  url="https://github.com/SolderedElectronics/Soldered-Basic-Stepper-Driver-Arduino-Library/blob/main/examples/ConstantSpeed/ConstantSpeed.ino" 
/>

<QuickLink 
  title="Blocking.ino" 
  description="Place the motor in certain positions"
  url="https://github.com/SolderedElectronics/Soldered-Basic-Stepper-Driver-Arduino-Library/blob/main/examples/Blocking/Blocking.ino" 
/>