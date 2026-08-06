---
slug: /inkplate/6motion/faq-troubleshooting
title: Inkplate 6MOTION - FAQ and troubleshooting
sidebar_label: FAQ and troubleshooting
id: 6motion-faq-troubleshooting
hide_title: true
---


<SectionTitle title="FAQ and troubleshooting" backgroundImage="/img/faq.webp" />

Here, we've gathered the most frequently asked questions and answers to help you get the most out of your Inkplate 6MOTION. Whether you're new to e-paper development or troubleshooting an issue, this page is here to guide you through common problems and solutions.

<ExpandableSection title="I can't upload code to Inkplate 6MOTION">
If you're having trouble uploading code, try the following troubleshooting steps.

#### Restart and manually enter programming mode
- Disconnect the device and power it off completely.
- Reconnect via USB while holding the PROG button.  
  This sometimes forces the device into programming mode.

#### Use the BOOT switch (manual bootloader mode)
If the above method doesn't work, use the BOOT switch on the back of the PCB to force programming mode:

1. Set the BOOT switch to position `1` (this puts the STM32 in bootloader mode).  
2. Press the RESET button to restart the board.  
3. Upload your code via Arduino.  
4. Once done, switch BOOT back to `0` to return to normal operation.

#### Verify Arduino IDE version
Inkplate 6MOTION requires Arduino IDE 2.0+ for proper board and library support.  
If you're using an older version, update to Arduino 2.0 or later to avoid compatibility issues.

#### Still having issues?
If none of these steps resolve the issue, contact our support team [**here**](https://soldered.com/contact/) with details of your setup and the troubleshooting steps you've tried.
</ExpandableSection>



<ExpandableSection title="My display won't refresh, what am I doing wrong?">
If your Inkplate 6MOTION display is not refreshing, follow these steps to diagnose and resolve the issue.

#### 1. Verify that the code is uploading correctly
- **Enable verbose output** in Arduino under **File → Preferences**, then check the **compile and upload logs**.
- When uploading via **STM32CubeProgrammer**, a successful upload should print:

```
RUNNING Program ... 
Address:      : 0x8000000
Start operation achieved successfully
```

#### 2. Test with an official example
Make sure you're testing with an **unmodified Arduino example** from the Inkplate Motion library. Running custom code might be **almost correct** but could still prevent the display from refreshing properly.

Try uploading these tested examples:

<QuickLink 
  title="Inkplate_6_Motion_Simple_BW" 
  description="Example on how to draw simple graphics in black and white mode"
  url="https://github.com/SolderedElectronics/Inkplate_Motion_Arduino_Library/blob/main/examples/Inkplate6Motion/Basic/Inkplate_6_Motion_Simple_BW/Inkplate_6_Motion_Simple_BW.ino" 
/>

<QuickLink 
  title="Inkplate_6_Motion_Simple_Grayscale" 
  description="Example on how to draw simple graphics in grayscale"
  url="https://github.com/SolderedElectronics/Inkplate_Motion_Arduino_Library/blob/main/examples/Inkplate6Motion/Basic/Inkplate_6_Motion_Simple_Grayscale/Inkplate_6_Motion_Simple_Grayscale.ino" 
/>

#### 3. Check your power source
- Some **laptop or PC USB ports provide insufficient current**, which may cause Inkplate to get stuck while refreshing.
- Try a **different USB port, power adapter, or USB cable** to ensure the board is receiving stable power.

#### 4. Inspect the e-paper flat cable and panel
- Examine the **flat-flex cable connector** to ensure it's properly seated.
- Check the **edges of the e-paper panel** for any visible damage or cracks.
<CenteredImage src="/img/inkplate_6_motion/flat_cable.jpg" alt="Inkplate 6MOTION e-Paper flat cable" caption="E-paper flat cable connector" width="500px"/>

#### 5. Still having issues?
If none of these steps resolve the issue, **contact our support team** [**here**](https://soldered.com/contact/) with details of your setup and troubleshooting steps taken.
</ExpandableSection>

<ExpandableSection title="My display refreshes but has artifacts/streaks">
If you notice **artifacts, streaks, or ghosting** on your Inkplate 6MOTION display, follow these steps to clean the screen and check for potential connection issues.

#### 1. Run a display cleaning cycle
Try running the following sketch, which performs **30** full refresh cycles to remove any persistent artifacts:

```cpp
#include <InkplateMotion.h>
Inkplate inkplate;
int cleanTimes = 30;

void setup()
{
    inkplate.begin(INKPLATE_BLACKWHITE);
    for(int i = 0; i < cleanTimes; i++)
    {
        inkplate.clearDisplay();
        inkplate.display();
        delay(500);
        inkplate.fillRect(0, 0, 1024, 758, BLACK);
        inkplate.display();
        delay(500);
    }
}

void loop()
{
    // Do nothing
}
```

#### 2. Check the e-paper flat cable connector
If artifacts persist after cleaning or appear as long vertical lines or streaks, it may indicate a loose, improperly connected or possibly **damaged** flat cable.

Try re-seating the e-paper flat cable by carefully disconnecting and reconnecting it.

<CenteredImage src="/img/inkplate_6_motion/flat_cable.jpg" alt="Inkplate 6MOTION e-Paper flat cable" caption="E-paper flat cable connector" width="500px"/>

#### 3. Still having issues?
If none of these steps resolve the issue, **contact our support team** [**here**](https://soldered.com/contact/) with details of your setup and the troubleshooting steps you've tried.
</ExpandableSection>

<ExpandableSection title="Can I use partial update all the time on Inkplate 6MOTION?">
To preserve display quality and extend the lifespan of the panel, it's recommended to perform a full update (`inkplate.display()`) after a certain number of partial updates. 

In the [**accelerometer example**](https://github.com/SolderedElectronics/Inkplate_Motion_Arduino_Library/blob/main/examples/Inkplate6Motion/Advanced/Sensors_Other/Inkplate_6_MOTION_Accelerometer_Cube/Inkplate_6_MOTION_Accelerometer_Cube.ino), we managed to achieve up to 75 partial updates before requiring a full refresh. In most other examples, we use 20-30 partial updates before a full update. Your results may vary depending on the content and update frequency, but we strongly recommend incorporating full updates periodically to avoid ghosting and degradation.

To simplify this process, you can use the `setFullUpdateTreshold()` function, which automatically handles full refreshes at defined intervals. Learn more about this function [**here**](/inkplate/6motion/basics/partial-update#partial-update).
</ExpandableSection>

<ExpandableSection title="How to connect a battery to Inkplate?">
All Inkplate models have a 2-pin 2.0mm JST connector for connecting a 3.7V Li-ion battery. Inkplate 6MOTION features an onboard MCP73831 charging IC, which automatically charges the battery when connected via USB and switches over to battery power on its own when you unplug it.

<CenteredImage src="/img/inkplate_6_motion/battery_jst_connector.jpg" alt="Inkplate 6MOTION battery JST connector" caption="JST battery connector" width="500px"/>

<WarningBox>**Warning:** Battery polarity must be correct! Connecting a battery with reversed polarity may permanently damage your Inkplate. See [**this**](/inkplate/6motion/hardware/battery/) page in the documentation for info regarding the battery.</WarningBox>
</ExpandableSection>

<ExpandableSection title="Where can I find hardware files and schematics for Inkplate 6MOTION?">
All hardware design files, including schematics, KiCad project files, gerber files, and more, are available in the [**Inkplate 6MOTION hardware repository on GitHub**](https://github.com/SolderedElectronics/Soldered-Inkplate-6-MOTION-hardware-design).

Additionally, this documentation contains detailed hardware design insights on the [**hardware design page**](/inkplate/6motion/hardware/design/).
</ExpandableSection>

<ExpandableSection title="Where can I download the 3D files for the enclosure for Inkplate 6MOTION?">
They're in the [**3D files folder**](https://github.com/SolderedElectronics/Soldered-Inkplate-6-MOTION-hardware-design/tree/main/OUTPUTS/V2.1.0/3D%20files) of the Inkplate 6MOTION hardware repository, all in `.step` format:

- `Inkplate 6 Motion Bottom.step`
- `Inkplate 6 Motion Top (C-1).step` and `Inkplate 6 Motion Top (C-2).step`
- `LED Slot.step`
- `Rotary magnet holder.step`
- `Tool for programming button.step`

Read `Print info.txt` in the same folder before printing, it covers the settings we use.

<InfoBox>Looking for the PCB itself rather than the enclosure? That's `Soldered Inkplate 6 Motion 3D.step`, one level up in the [**OUTPUTS folder**](https://github.com/SolderedElectronics/Soldered-Inkplate-6-MOTION-hardware-design/tree/main/OUTPUTS/V2.1.0).</InfoBox>
</ExpandableSection>

<ExpandableSection title="Does Inkplate 6MOTION support Micropython?">
No, Inkplate 6MOTION does not support MicroPython. While MicroPython is available on several other Inkplate models, this board is based on an STM32 microcontroller, which changes the development approach enough that the MicroPython port would be a separate effort. Because of this, we decided not to focus on a MicroPython driver for this board.

If you're looking for MicroPython-compatible Inkplate devices, check out our [**MicroPython-supported Inkplate boards**](https://github.com/SolderedElectronics/Inkplate-micropython).
</ExpandableSection>

<ExpandableSection title="Can I use Inkplate 6MOTION as an e-reader/monitor?">
Short answer: No.  

Inkplate 6MOTION is an e-paper development platform and functions similarly to an Arduino with an integrated e-paper display. While it is not designed to be a plug-and-play e-reader or monitor, you could write your own Arduino sketch to display data sent from a PC via USB.

However, if you're looking for a true e-ink monitor experience, Inkplate 6MOTION is not the right choice.
</ExpandableSection>

<ExpandableSection title="Can I use Inkplate 6MOTION with ESPHome/Home Assistant?">
At this time, Inkplate 6MOTION is not officially supported by ESPHome.  

There is currently no ESPHome display component for this model, but we are actively working on expanding ESPHome compatibility for all Inkplate devices. Stay tuned for future updates!
</ExpandableSection>

<InfoBox>In case you haven't found the answer to your question, please **Contact us** via [**this**](https://soldered.com/contact/) link.</InfoBox>