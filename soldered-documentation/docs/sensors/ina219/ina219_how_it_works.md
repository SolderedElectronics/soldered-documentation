---  
slug: /ina219/how-it-works  
title: INA219 - How it works
sidebar_label: How it works
id: ina219-how-it-works  
hide_title: False  
---  

The INA219 is an integrated circuit by **Texas Instruments**. When using our board, you are essentially communicating directly with the onboard INA219 via **I2C communication**.

<CenteredImage src="/img/ina219/onboard.webp" alt="INA219 sensor on board" caption="INA219 sensor on the board" width="400px" />

---

## Datasheet

For an in-depth look at technical specifications, refer to the official INA219 Datasheet:  

<QuickLink  
  title="INA219 Datasheet"  
  description="Detailed technical documentation for the INA219 sensor"  
  url="https://soldered.com/productdata/2022/03/Soldered_INA219_datasheet.pdf"  
/>

---

## How the sensor works

The INA219 is a small electronic sensor that measures how much **electric current** is flowing through a wire and how much **voltage** is present in a circuit. It’s super useful in electronics because it lets us monitor power usage in devices such as robots, batteries, and solar panels.

It is a **current shunt** and **power monitor** with an I2C interface. The device monitors both the **shunt voltage drop** and the **bus supply voltage**, with programmable conversion times and filtering. A programmable calibration value, combined with an internal multiplier, enables direct readouts of current in amperes. An additional multiplying register calculates power in watts.

<CenteredImage src="/img/ina219/schematic.png" alt="Simplified schematic of the INA219 sensor" caption="Simplified schematic of the INA219 sensor" width="600px" />

---

## I2C communication

The INA219 uses the I2C protocol to communicate with a microcontroller.

Writing to a register begins with the first byte transmitted by the microcontroller. This byte is the I2C address. The INA219 then acknowledges the receipt of a valid address. The next byte transmitted by the microcontroller is the address of the register to which data will be written. This register address value updates the register pointer to the desired register. The next two bytes are written to the register indicated by the register pointer. The INA219 acknowledges receipt of each data byte. The microcontroller may terminate data transfer by generating a START or STOP condition.