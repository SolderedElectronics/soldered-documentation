---
slug: /arduino/bootloader
title: Arduino - Burning the Arduino Bootloader
sidebar_label: Burning the Arduino Bootloader
id: arduino-bootloader
hide_title: false
pagination_prev: null
---

The bootloader is a small piece of software that allows uploading of sketches onto the Arduino board. It comes preprogrammed on the Arduino boards, but when the MCU is bought on its own it usually doesn't have the bootloader preprogrammed. The easiest way to burn the bootloader to standard Atmel chips (ATTINY, ATMEGA ...) is by using a second preprogrammed board as a programmer, which will be covered below. It this example, we will be using a Dasduino CORE to bootload another Dasduino CORE

---

## 1. Connect the boards
Atmel boards are programmed with the SPI interface (MOSI, MISO, SCK signals). Check pinout schemes for both of your boards to find those pins! For this example, both programmer and target board will be Dasduino CORE boards. Connections are available below:

| **Programmer board** 	| **Target board** 	|
|---	|---	|
| MISO (D12) 	| MISO (D12) 	|
| MOSI (D11) 	| MOSI (D11) 	|
| SCK (D13) 	| SCK (D13) 	|
| D(10), or any digital pin! 	| RESET 	|
| VCC 	| VCC 	|
| GND 	| GND 	|

<CenteredImage src="/img/arduino/bootloader/connection.png" alt="Connection example" caption="Connection example" width="800px"/>

---

## 2. Burn the bootloader 
Connect the **programmer** board to the computer via USB. In Arduino IDE open the `ArduinoISP` example by going to: `File->Examples->11.ArduinoISP->ArduinoISP`.
<CenteredImage src="/img/arduino/bootloader/example.jpg" alt="Path to the example" caption="Path to the example" width="800px"/>

Upload the code to the **programmer** board.

After succesfully uploading the code, go to `Tools->Board` and change it to the target board. For `Tools->Programmer` select **Arduino as ISP** and click **Burn Bootloader**
<CenteredImage src="/img/arduino/bootloader/burn-bootloader.jpg" alt="Path to the example" caption="Path to the example" width="300px"/>

---

## 3. Troubleshooting

<ExpandableSection title="Error: Missing programmer">

```
avrdude: Yikes!  Invalid device signature.
         Double check connections and try again, or use -F to override
         this check.

Error while burning the bootloader: Failed chip erase: uploading error: exit    status 1
```

Check your selection in `Tools->Programmer`.

</ExpandableSection>

<ExpandableSection title="Error: Failed chip erase: uploading error: exit status 1">

```
Error while burning the bootloader: Failed chip erase: uploading error: exit status 1
```

Make sure you've selected the target board in `Tools->Board` and that you've connected the **RESET** pin correctly.

</ExpandableSection>

<ExpandableSection title="avrdude: Error: Could not find USBtiny device">

```
Error while burning bootloader.
avrdude: Error: Could not find USBtiny device (0x2341/0x49)
```

Make sure you've selected **Arduino as ISP** in `Tools->Programmer`, and **not** ArduinoISP or other similar options.

</ExpandableSection>

<ExpandableSection title="Can't upload code after bootloading">

Make sure that your target board is wired properly.

</ExpandableSection>