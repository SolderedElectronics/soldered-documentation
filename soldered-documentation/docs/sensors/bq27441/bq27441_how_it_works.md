---
slug: /bq27441/how-it-works 
title: How it works
id: bq27441-how-it-works 
hide_title: False
---  

BQ27441 is an microcontroller pheripheral that provides system-side fuel gauging for single-cell Li-Ion batteries by **Texas Instruments**. When using our board, you are essentially communicationg with the onboard BQ27441 directly via **I2C communication**.

<CenteredImage src="/img/bq27441/bq27441_highlighted.jpg" alt="BQ27441 sensor on board" caption="BQ27441 sensor on the board" width="400px" />

---

## Datasheet

For an in-depth look at technical specifications, refer to the official BMP180 Datasheet:  

<QuickLink  
  title="BQ27441 Datasheet"  
  description="Detailed technical documentation for the BQ27441 sensor"  
  url="https://soldered.com/productdata/2022/03/Soldered_BQ27441_datasheet.pdf"  
/>  

---

## How the sensor works

The BQ27441 battery fuel gauge uses the patented **Impedance Track** algorithm for fuel gauging, and provides information such as remaining battery capacity [mah], state of charge [%] and battery voltage [mV].

### Impedance Track Algorithm
The algorithm uses three types of information to calculate remainig capacity (`SBS.RemainingCapacity()`) and full charge capacity (`SBS.FullChargeCapacity()`):
    - Chemical: **Depth of discharge** (DOD) and **Total chemical capacity Qmax** 
    - Electrical: **Internal battery resistance dependence on DOD**
    - External: **Load**, **Temperature**

`SBS.FullChargeCapacity()` is defined as the amount of charge passed from a fully charged state until the voltage defined in `DF:Terminate Voltage` flash constant is reached at a given rate of discharge, after subtarcting the reserve capacity (`DF:Reserve Capacity`)

<InfoBox>Note that it depends on the rate of discharge and is lower at higher rates and low temperatures because the cell i x R causes the Terminate Voltage threshold to be reached earlier. </InfoBox>

### Modes of Algorithm Operation
The algorithm differentiates between **charge**, **discharge**, and **relaxation** modes of operation. During charge mode, the `SBS.OperationStatus( )` **DSG** bit is cleared, and during discharge and relaxation mode, it is set. Entry and exit of each mode is controlled by **Data Flash** (DF) parameters in the subclass Gas Gauging. Relaxation mode is entered when `SBS.Current( )` goes below `DF:Quit` Current and after a `DF:Chg` Relax Time period. Discharge mode is entered when `SBS.Current( )` goes below `DF:Dsg` Current Threshold. Discharge mode is exited, relaxation mode is entered when SBS.Current( ) goes above `—DF:Quit` Current threshold and after a `DF:Dsg` Relax Time period. Charge mode is entered when `SBS.Current( )` goes above `DF:Chg` Current Threshold.

<CenteredImage src="/img/bq27441/operation_modes.jpg" alt="Example of the Algorithm Operation Mode Changes With Varying SBS.Current( )" caption="Example of the Algorithm Operation Mode Changes With Varying SBS.Current( )" width="600px" />

<InfoBox>For more in-depth at Impedance Track Algorithm, refer to the official [Datasheet](https://www.ti.com/lit/an/slua364b/slua364b.pdf?ts=1744806267910&ref_url=https%253A%252F%252Fwww.google.com%252F)</InfoBox>

---

## I2C communication - Qwiic
This board uses the onboard BQ27441 to implement I2C communication. The board operates on a default I2C address of **0x55**, but it can be changed using onboard switches. To check in detail how the BQ27441 is preprogrammed, check the [**firmware GitHub page**](https://github.com/SolderedElectronics/Soldered-BQ27441-Battery-Fuel-Gauge-Arduino-Library/blob/dev/extras/attiny_firmware/attiny_firmware.ino).