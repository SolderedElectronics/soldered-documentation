---
slug: /button,led&buzzerboar/arduino/troubleshooting 
title: Button, LED & Buzzer Board - Troubleshooting
sidebar_label: Troubleshooting
id: button,led&buzzerboar-arduino-3 
hide_title: false
pagination_next: null
---

This page contains some tips in case you are having problems using this product.

<ExpandableSection title="The board won't initialize!">

#### Check wiring
Ensure that your Qwiic cable is properly connected and in good condition. Try using the same cable with another Qwiic-compatible device to verify that it works. If the issue persists, swap it out for a different cable to rule out any possible damage or defects.

#### Check I2C pins
If you are connecting the board using standard I2C pins on your microcontroller, double-check that you are using the correct ones. Different microcontrollers have designated I2C pins that may not always be labeled the same way. Refer to your microcontroller's documentation to confirm the correct pin assignments.

#### Scan for I2C devices
Run an [**I2C scanner sketch**](https://github.com/SolderedElectronics/Soldered-Hacky-Codes/tree/main/I2C_Scanner) on your microcontroller to check if the board is detected. If the scanner does not find any devices, there might be a wiring issue, incorrect pull-up resistors, or a problem with the microcontroller's I2C bus.

#### Check for conflicting devices
If you have multiple I2C devices connected to the same bus, ensure that none of them have conflicting addresses. Verify that no other device on the bus shares the same I2C address as the Button, LED & Buzzer Board.

#### Try reinitializing
If the board fails to initialize on the first attempt, try calling `board.begin()` again in your code or resetting your microcontroller. Some initialization issues may be resolved by a simple reboot.

</ExpandableSection>

<ExpandableSection title="Button presses are not detected!">

#### Check readButtons() bitmask
Make sure you are correctly masking the return value of `readButtons()`. Each button corresponds to a specific bit: `0x01` for BTN1, `0x02` for BTN2, and `0x04` for BTN3. Using the wrong mask will result in missed presses.

#### Add a small delay in the loop
If button presses seem to be missed or unreliable, ensure your `loop()` is not running too fast. A small `delay(20)` at the end of the loop gives the board enough time to process and report button states correctly.

#### Check physical button contact
Verify that the button is not stuck or damaged. Press it firmly and check if the reading changes. If a button appears to always read as pressed, inspect the board for any debris or solder bridges around the button.

</ExpandableSection>

<ExpandableSection title="LEDs are not lighting up!">

#### Check RGB values
Ensure you are passing non-zero values to `setLED()` or `setAllLEDs()`. A call like `board.setLED(0, 0, 0, 0)` turns the LED off — double-check that at least one channel value is greater than 0.

#### Check the LED index
`setLED()` accepts an index of 0, 1, or 2. Passing an out-of-range index will have no effect. Verify that you are targeting the correct LED.

#### Verify power supply
Make sure the board is receiving stable power. Insufficient voltage or a weak USB connection can cause LEDs to behave unexpectedly.

</ExpandableSection>

<ExpandableSection title="The buzzer is not making any sound!">

#### Check the frequency value
`setBuzzer(0)` silences the buzzer. Make sure you are passing a non-zero frequency (e.g. `1000` for 1 kHz). Frequencies that are too high or too low may not produce audible sound.

#### Remove the delay
If you are using a `delay()` in your loop, make sure it is short enough to allow the buzzer signal to be generated correctly. Long delays can interrupt PWM generation and silence the buzzer.

#### Check board initialization
The buzzer is controlled through the onboard ATTiny404. If `board.begin()` did not succeed, buzzer commands will have no effect. Confirm the board initializes correctly before sending buzzer commands.

</ExpandableSection>

<InfoBox>In case you haven't found the answer to your question, please **contact us** via [**this**](https://soldered.com/contact/) link.</InfoBox>
