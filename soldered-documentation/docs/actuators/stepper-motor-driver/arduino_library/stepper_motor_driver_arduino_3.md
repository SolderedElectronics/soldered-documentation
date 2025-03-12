---
slug: /basic-stepper-driver/arduino/troubleshooting
title: Troubleshooting
id: stepper-arduino-3
hide_title: False
pagination_next: null
---

This page contains some tips in case you are having problems using this product.

<ExpandableSection title="My stepper won't turn!">

#### Check Power Supply  
Is your stepper motor powered by an **external power source**? If you are trying to power it directly from your microcontroller, it might be drawing too much current, causing voltage drops or even brownouts, which prevent the motor from turning. **DC motors require significant current**, and most microcontrollers are not designed to supply enough power.  

<InfoBox>Quick tip: If your stepper motor operates at **5V**, you can repurpose an old USB cable by exposing its **VCC** and **GND** wires to provide power from a USB port.  </InfoBox>

---

#### Verify Wiring & Connections  
Incorrect wiring is one of the most common reasons a stepper motor won't turn. Double-check:
- That the **IN1, IN2, IN3, IN4** pins from the driver board are correctly connected to **digital output** pins on your microcontroller.
- If the wires are **misplaced or swapped**, the stepper motor may just vibrate or fail to turn properly.  
- Ensure the **GND of the stepper driver is connected to the GND of your microcontroller**.

<WarningBox>Careful! If wired incorrectly, the stepper motor may **overheat significantly** due to excessive current draw! </WarningBox>

---

#### Try Different Microcontroller Pins  
Not all microcontroller pins support **digital output** functions. Some may be reserved for special functions (such as I²C, UART, or ADC inputs) and may not work correctly as stepper driver outputs. Try switching to different pins, this can sometimes resolve the issue.

---

#### Test with Another Stepper Motor  
If you have another stepper motor available, swap it out and see if the issue persists. If the replacement motor works, the original motor may be faulty.  

---

#### Ensure Code is Correct  
If everything seems correctly wired, **check your code**:
- Are you using the correct **library and commands** to drive the motor?
- Are you calling `stepper.run()` frequently enough in your loop?
- Are you setting **speed and acceleration** properly?  

For testing and troubleshooting, it's best to run unmodified examples from the library.

</ExpandableSection>

<InfoBox>In case you haven't found the answer to your question, please **contact us** via [**this**](https://soldered.com/contact/) link.</InfoBox>