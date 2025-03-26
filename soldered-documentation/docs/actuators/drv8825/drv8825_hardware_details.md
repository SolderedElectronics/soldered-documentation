---
slug: /drv8825/hardware 
title: Hardware details
id: drv8825-hardware 
hide_title: False
---

## Pinout

<CenteredImage src="/img/drv8825/333000_pinout.jpg" alt="Pinout" />
Click [**here**](/img/drv8825/333000_pinout.jpg) for a high reoslution image of the pinout.

### Pin details

| Pin Marking 	| Pin Name 	| Description 	|
|---	|---	|---	|
| **VIN** 	| Motor Supply Voltage (+) 	| Positive DC voltage input for the stepper. 	|
| **GND** 	| Motor Ground (-) 	| Ground connection for the stepper motor power supply. 	|
| **B2** 	| Stepper Coil B2 	| Second terminal of Coil B in the stepper motor. 	|
| **B1** 	| Stepper Coil B1 	| First terminal of Coil B in the stepper motor. 	|
| **A1** 	| Stepper Coil A1 	| First terminal of Coil A in the stepper motor. 	|
| **A2** 	| Stepper Coil A2 	| Second terminal of Coil A in the stepper motor. 	|
| **Fault** 	| Fault pin 	| Logic low when in fault condition (overtemp, overcurrent) 	|
| **GND** 	| Signal Ground (Microcontroller) 	| Ground reference for the control signals from the microcontroller 	|
| **EN** 	| Enable input 	| Logic high to disable outputs, logic low to enable. 	|
| **M0** 	| Microstep mode 0 	| Set the step mode 	|
| **M1** 	| Microstep mode 1 	| Set the step mode 	|
| **M2** 	| Microstep mode 2 	| Set the step mode 	|
| **RST** 	| Reset input 	| Initialises the indexer logic and disables the H-bridge outputs. 	|
| **SLP** 	| Sleep mode input 	| Logic high to disable device outputs, logic low to enter low-power sleep mode. 	|
| **STEP** 	| Step input 	| Rising edge causes the indexer to move one step. 	|
| **DIR** 	| Direction input 	| Sets the direction of stepping. 	|

<WarningBox>**45V is the maximum** supported Motor supply voltage!</WarningBox>

---

## Jumper Details

This board contains hardware jumpers, se below for  their locations and functions: