---
slug: /adc/arduino/troubleshooting
title: Adc - Troubleshooting
id: adc-arduino-5
hide_title: false
pagination_next: null
---

This page contains some tips if you are having problems using the **1015** or **1115** ADCs.

<ExpandableSection title="My ADC won't initialize!">

#### Check wiring
Ensure that the connections to your ADC are secure and in good condition. Double-check the wiring for the power supply, ground, and the data pins (SCL, SDA, etc.) to confirm everything is set up correctly. Use known working cables to rule out any possible cable issues.

#### Check I2C pins
If you are using I2C to communicate with your ADC, make sure the SCL (Serial Clock) and SDA (Serial Data) lines are connected to the correct pins on your microcontroller. I2C pin assignments may vary depending on the microcontroller you're using. Refer to your microcontroller's datasheet to verify proper pin configuration.

#### Verify Power Supply
The **1015** and **1115** ADCs require stable power (typically 3.3V or 5V depending on the version you're using). Make sure the ADC is receiving the correct voltage and check for any power supply instability.

#### Run an I2C Scanner
Try running an [**I2C scanner sketch**](https://github.com/SolderedElectronics/Soldered-Hacky-Codes/tree/main/I2C_Scanner) on your microcontroller to ensure the ADC is detected on the I2C bus. If the scanner doesn’t detect any devices, there could be an issue with your wiring, pull-up resistors, or the I2C bus itself.

#### Test with a Different I2C Device
To rule out any issues with the I2C bus or your microcontroller, connect a different known-good I2C device to the same bus and check if it communicates successfully.

#### Reinitialize the ADC
If the ADC fails to initialize after the first attempt, try calling the initialization function again in your code, such as `ADC.begin()` for your microcontroller. Sometimes, a simple retry or a reboot can resolve initialization issues.

</ExpandableSection>

<ExpandableSection title="My ADC is not reading properly!">

#### Check Sensor Connections
Ensure that your sensor is correctly connected to the ADC input. A loose or faulty connection between the sensor and the ADC can lead to inaccurate or no readings. Ensure that all signal connections (e.g., Vout) are secure.

#### Verify Reference Voltage
The **1015** and **1115** ADCs use a reference voltage for conversions. Ensure that the reference voltage is set appropriately for your input signal range. If you're using an external reference, check that it is stable and within the correct range.

#### Check the Input Signal
Verify that the input signal falls within the ADC's acceptable voltage range. Signals outside the ADC's input voltage range (e.g., above the reference voltage) can cause incorrect readings or damage the ADC.

#### Verify Proper I2C Communication
If you're using I2C communication, double-check the wiring and confirm that your SDA and SCL lines are properly connected. You can also try running the [I2C scanner](https://github.com/SolderedElectronics/Soldered-Hacky-Codes/tree/main/I2C_Scanner) sketch again to ensure proper communication.

#### Use a Known-Good Signal Source
To rule out issues with your input signal, test the ADC with a known-good voltage source, such as a stable reference or a calibrated signal generator. This helps to ensure the ADC is functioning correctly.

#### Adjust Gain or Resolution
If you're getting low or inaccurate readings, you may need to adjust the ADC’s gain or resolution settings. The **1015** and **1115** ADCs offer different resolution options (e.g., 12-bit, 16-bit). Experiment with different settings to see if it improves the accuracy of the readings.

#### Test with Different Software Libraries
Sometimes, software libraries can have bugs or be incompatible with your hardware version. Try using a different ADC library to see if that resolves the issue.

</ExpandableSection>

<ExpandableSection title="Other common issues">

#### My ADC is giving fluctuating or noisy readings
Verify Power Supply  
Fluctuations in the ADC's readings may be caused by power supply instability. Ensure that the ADC is receiving a clean and stable voltage.

#### Use Decoupling Capacitors
Fluctuations may also occur if there is noise on the power rails. Try adding decoupling capacitors near the ADC's power pins to reduce noise and stabilize the voltage.

#### ADC doesn't respond after firmware update
Revert to Previous Version  
If you recently updated the firmware on your microcontroller and the issue arose afterward, try reverting to the previous firmware version to see if that resolves the issue.

#### Sensor data is inaccurate or fluctuating
Check Grounding  
Improper grounding of the ADC can lead to fluctuating data. Ensure that the ADC and all connected components share a common ground with the microcontroller.

#### Slow Response Time
Adjust Conversion Time  
The **1015** and **1115** ADCs may have configurable conversion times. If the response time is too slow for your application, you can reduce the conversion time, but be aware that this may impact the accuracy of the readings.

#### No output from the ADC
Verify Input Voltage  
If you’re receiving no output from the ADC, check that the input signal is within the allowable voltage range for the ADC. A signal below or above the ADC’s reference voltage will result in no output.

#### My ADC is heating up
Check Power and Usage  
If the ADC is getting too hot, it could indicate an issue with the power supply or an excessive current draw. Ensure that the power supply voltage is correct (typically 3.3V or 5V, depending on your ADC variant) and that the ADC is not being overloaded.

#### Inaccurate Conversion Result
Check for Clipping  
If your input signal is outside the ADC's input range, the output could be clipped, leading to inaccurate readings. Verify that the input signal is within the specified range for your ADC.

</ExpandableSection>

<InfoBox>In case you haven't found the answer to your question, please **contact us** via [**this**](https://soldered.com/contact/) link.</InfoBox>