---
slug: /inputronic-grid/arduino/troubleshooting 
title: Troubleshooting
id: inputronic-grid-arduino-3 
hide_title: False
pagination_next: null
---
This page contains some tips in case you experience problems using your Inputronic GRID module.

<ExpandableSection title="My Inputronic GRID won't initialize!">

#### Check wiring  
Ensure that your Qwiic cable is properly connected. If you are manually wiring the module using standard I2C pins, confirm that you haven't swapped the **SDA** and **SCL** lines. Consult your microcontroller's documentation for the correct I2C pin assignments.

#### Check the I2C Address  
The Inputronic GRID uses a software-configurable I2C address, which defaults to `0x30`. If you previously changed the address using the `setAddress()` command and forgot what you set it to, the device will not initialize at `0x30`. Use a standard **I2C Scanner sketch** on your Arduino to scan the bus and find the module's current address. 

#### Power supply  
Make sure the module is receiving stable **3.3V** power. If the voltage drops too low, the onboard ATtiny microcontroller will not boot correctly.

</ExpandableSection>

<ExpandableSection title="Touch pads are not responding or registering ghost touches!">

#### Check grounding
Capacitive touch sensing relies on a stable electrical ground. Ensure your main microcontroller and the Inputronic GRID share a solid, common ground connection.

#### Remove physical interference
Keep the top surface of the grid clean and free of moisture. Avoid placing the module directly on conductive metallic surfaces, as this can severely interfere with the capacitive fields of the touch pads and cause false triggers.

#### Give the module time to calibrate
When the ATtiny404 powers on, it briefly calibrates the baseline capacitance of the pads. Make sure you are not touching the grid during the first second after powering it up.

</ExpandableSection>