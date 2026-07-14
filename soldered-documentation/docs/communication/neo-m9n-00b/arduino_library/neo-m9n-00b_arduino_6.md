---
slug: /neo-m9n-00b/arduino/troubleshooting
title: NEO-M9N-00B - Troubleshooting
sidebar_label: Troubleshooting
id: neo-m9n-00b-arduino-6
hide_title: False
pagination_next: null
---

This page contains some tips if you are having problems using this product.

<ExpandableSection title="My GNSS module won't initialize!">

#### Check wiring
Make sure your Qwiic cable is properly connected and in good condition. Try using the same cable with another Qwiic-compatible device to verify that it works. If the issue persists, swap it out for a different cable to rule out any possible damage or defects.

#### Check I2C pins
If you are connecting the module using standard I2C pins on your microcontroller, double-check that you are using the correct ones. Different microcontrollers have designated I2C pins that may not always be labeled the same way. Check your microcontroller's documentation to confirm the correct pin assignments.

#### Scan for I2C devices
Run an [**I2C scanner sketch**](https://github.com/SolderedElectronics/Soldered-Hacky-Codes/tree/main/I2C_Scanner) on your microcontroller to check if the module is detected. If the scanner does not find any devices, there might be a wiring issue, incorrect pull-up resistors, or a problem with the microcontroller's I2C bus.

#### Try reinitializing
If the module fails to initialize on the first attempt, try calling `myGNSS.begin()` again in your code or resetting your microcontroller. Some initialization issues may be resolved by a simple reboot.

</ExpandableSection>

<ExpandableSection title="I'm not getting a GPS fix!">

#### Move to an open outdoor area
The NEO-M9N-00B requires a clear view of the sky to receive satellite signals. Walls, roofs, and dense foliage can block or weaken signals. Make sure you are outdoors with an unobstructed view above you.

#### Wait for a cold start to complete
On first power-up or after a long period without power, the module performs a cold start and may take several minutes to acquire a fix. Once a fix has been obtained at least once, subsequent warm starts are significantly faster.

#### Check the antenna connection
Make sure the GNSS antenna is securely connected to the module's antenna port. A loose or missing antenna will prevent satellite acquisition entirely.

#### Check the SIV count
Use `myGNSS.getSIV()` to read the number of satellites in view. A value of 0 indicates no satellites are being received. A fix typically requires at least 4 satellites.

#### Verify time and date validity
Use `myGNSS.getTimeValid()` and `myGNSS.getDateValid()` to check whether the module has a confirmed time and date lock. If these return false, the fix is not yet complete.

</ExpandableSection>

<ExpandableSection title="SPI isn't working!">

#### Check the JP4 jumper
SPI only works when the **JP4** jumper on the board is closed. With JP4 open (the default), the module stays in I2C + UART mode and won't respond to any SPI traffic.

#### Check the CS pin
Make sure the chip select pin defined in your sketch matches the one physically wired to the module's SDA/SPI CS pin.

#### Set the SPI protocol with u-center
Some modules don't respond to UBX commands over SPI with their factory settings. Connect the module over UART or I2C once, open it in [**u-center**](https://www.u-blox.com/en/product/u-center), and set the SPI port's input and output protocol to **UBX only**.

</ExpandableSection>

<InfoBox>In case you haven't found the answer to your question, please **contact us** via [**this**](https://soldered.com/contact/) link.</InfoBox>
