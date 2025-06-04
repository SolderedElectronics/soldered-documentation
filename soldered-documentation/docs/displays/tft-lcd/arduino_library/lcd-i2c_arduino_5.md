---  
slug: /lcd-i2c/arduino/troubleshooting  
title: Troubleshooting  
id: tft-lcd-arduino-5  
hide_title: False  
pagination_next: null  
---

This page provides some tips in case you are experiencing issues with the LCD I2C display.

<ExpandableSection title="My LCD is not displaying anything!">

#### Check wiring
Ensure that your I2C wiring is correct. Verify that the SDA (Data) and SCL (Clock) pins are connected properly to your microcontroller. Also, ensure the LCD has power and that the backlight is enabled.

#### Verify I2C address
The LCD I2C modules often come with a default I2C address, but it might vary. Run an [**I2C scanner sketch**](https://github.com/SolderedElectronics/Soldered-Hacky-Codes/tree/main/I2C_Scanner) on your microcontroller to check if the sensor is detected.

#### Adjust potentiometer
Some LCD I2C displays have a small potentiometer on the back that controls the contrast. If nothing appears on the screen, try adjusting the potentiometer to see if the text becomes visible.

#### Check for power issues
Make sure the LCD display is receiving proper power. If the screen is dim or shows faint text, it could be underpowered. Ensure your power supply is stable and provides sufficient voltage (usually 5V or 3.3V depending on the module).

#### Reinitialize the LCD
If the screen fails to display, try reinitializing the LCD by calling the initialization function again in your code or restarting your microcontroller to reset the display.

</ExpandableSection>

<ExpandableSection title="My LCD is showing weird characters!">

#### Check wiring and I2C address
Weird characters can indicate incorrect wiring or a mismatch in the I2C address. Verify your I2C wiring and ensure you’re using the correct address.

#### Adjust contrast using the potentiometer
If the display is showing unreadable text, try adjusting the contrast with the potentiometer on the back of the LCD. If the contrast is too low, the characters might not be properly visible.

#### Make sure you are using the right library
Sometimes, using an incompatible or outdated library can cause display issues. If you're using our display, use our [**library**](https://github.com/SolderedElectronics/Soldered-16x2-LCD-Arduino-Library) as well!

#### Check for electrical interference
Ensure that the wiring is kept short and the display is not near sources of electrical noise, such as motors or other high-power devices. Interference can cause unpredictable behavior on the display.

</ExpandableSection>

<ExpandableSection title="My display is flickering!">

#### Check power supply
Flickering can often be caused by an unstable power supply. Make sure the display is receiving the correct voltage (typically 5V or 3.3V). If you're using a USB power source, try a different one or use a more stable power supply.

#### Verify wiring connections
Loose or poor wiring connections can also cause flickering. Double-check all connections, especially the SDA and SCL lines. If the wires are too long, try shortening them to improve the signal integrity.

#### Test with different code
If the flickering occurs only when running a specific part of your code, it could be related to the program’s logic. Try running a simple LCD example sketch to check if the issue persists.

</ExpandableSection>

<ExpandableSection title="Other common issues">

#### My LCD is not refreshing or updating properly
Ensure you are calling lcd.clear() or lcd.setCursor() when updating text. Failing to move the cursor or clear the display might cause new text to overlap with old text.

#### LCD display is not responding to commands
If the display is unresponsive, try resetting your microcontroller or reinitializing the LCD. Some initialization issues can be resolved by a simple reset of the board.

#### Characters are not displayed properly
Make sure your code is properly sending data to the LCD. If you're using custom characters, check that the createChar() function is being called correctly and that you're addressing the right location for the custom characters.

</ExpandableSection>

<InfoBox>In case you haven't found the answer to your question, please **contact us** via [**this**](https://soldered.com/contact/) link.</InfoBox>