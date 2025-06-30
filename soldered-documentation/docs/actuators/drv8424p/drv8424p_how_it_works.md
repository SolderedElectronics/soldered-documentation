---  
slug: /drv8424p/how-it-works  
title: DRV8424P - How it works
sidebar_label: How it works
id: drv8424p-how-it-works  
hide_title: False  
pagination_next: null
---  

This is a **DRV8424P dual motor H-bridge driver breakout** designed to control two brushed DC motors or one bipolar stepper motor. It uses the **DRV8424P** driver from Texas Instruments, which allows for **bidirectional control**, **adjustable current regulation**, and **low power sleep mode**.

---  

## Datasheet

For detailed technical information, refer to the official DRV8424P datasheet:

<QuickLink  
  title="DRV8424P Datasheet"  
  description="Technical documentation for the DRV8424P H-bridge driver"  
  url="https://soldered.com/productdata/2022/03/Soldered_drv8424_datasheet.pdf"  
/>

---  

## What does the DRV8424P do?

The DRV8424P enables efficient, precise control of two DC motors or one bipolar stepper motor. It offers **peak currents up to 2A per H-bridge** and supports both **PWM** and **PH/EN** control schemes. The device includes several protections:

- **Overcurrent protection**
- **Undervoltage lockout**
- **Overtemperature shutdown**
- **Fault indication pin (FAULT)**

It operates over a wide voltage range (**4.5V to 33V**) and supports fast switching thanks to its internal low-RDS(on) FETs.

---  

## Motor control overview

Each H-bridge (A and B) is driven by a pair of logic pins:

- **IN1 / IN2**: Sets the direction and speed via PWM or logic level.
- **SLEEP**: An active-low pin used to put the driver into low-power mode.
- **FAULT**: An open-drain, active-low output that signals a fault condition.

To control a **DC motor**, connect it to the **OUT1** and **OUT2** pins of one H-bridge. To control a **stepper motor**, use both H-bridges simultaneously: one for coil A and one for coil B.

---  

## Example configuration

For typical brushed DC motor usage:

- **AIN1 / AIN2** and **BIN1 / BIN2** are controlled via PWM or logic levels to adjust speed and direction.
- Pull **SLEEP** high to activate the driver.
- Monitor **FAULT** for safety issues.

For a bipolar stepper motor:

- Use both A and B bridges to control coil pairs.
- A common sequence (e.g., full-step, half-step, microstepping) energizes each pair accordingly.

<InfoBox>Logic pins are compatible with **3.3V and 5V microcontrollers**</InfoBox>

---  

## Output Behavior Table (per H-bridge)

| IN1 | IN2 | Motor Behavior      |
|-----|-----|---------------------|
|  0  |  0  | Coast (Hi-Z)        |
|  0  |  1  | Reverse             |
|  1  |  0  | Forward             |
|  1  |  1  | Brake (Low output)  |

---  

## Applications

- Robotics
- Automated gates
- CNC and 3D printers
- General motorized systems