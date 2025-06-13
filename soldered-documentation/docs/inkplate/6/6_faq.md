---  
slug: /inkplate/6/faq-troubleshooting/  
title: Inkplate 6 - FAQ and troubleshooting  
sidebar_label: FAQ and troubleshooting
id: faq-troubleshooting  
hide_title: true  
---

<SectionTitle title="FAQ and troubleshooting" backgroundImage="/img/faq.webp" />

Here, we've gathered the most frequently asked questions along with detailed answers to help you get the most out of your device. We know that working with maker hardware and software can sometimes be challenging, so we created this resource to make things easier. Browse through the questions below—you might find the solution you're looking for.

<ExpandableSection title="I can't upload code to Inkplate 6">
If you're having trouble uploading code, try the following troubleshooting steps:

#### Restart device
- Disconnect the device and power it off completely.
- Reconnect via USB.

#### Make sure that the device is turned ON
This is a crucial step that is often forgotten. Make sure that the **ON** LED is turned on.

#### Verify Arduino IDE version
Inkplate 6 requires Arduino IDE 2.0+ for proper board and library support.  
If you're using an older version, update to Arduino IDE 2.0 or later to avoid compatibility issues.

#### Still having issues?
If none of these steps resolve the issue, contact our support team [**here**](https://soldered.com/contact/) with details of your setup and the troubleshooting steps you've tried.
</ExpandableSection>

<ExpandableSection title="Can I use partial update all the time on Inkplate 6?">
To preserve display quality and extend the lifespan of the panel, it's recommended to perform a full update (`inkplate.display()`) after a certain number of partial updates.
</ExpandableSection>

<ExpandableSection title="My display won't refresh, what am I doing wrong?">
If your Inkplate 6 display is not refreshing, follow these steps to diagnose and resolve the issue:

#### 1. Verify that the code is uploading correctly
- **Enable verbose output** in Arduino under **File → Preferences**, then check the **compile and upload logs**.
- When uploading, a successful upload should print:

```
Leaving... 
Hard resetting via RTS pin...
```

#### 2. Test with an official example
Make sure you're testing with an **unmodified Arduino example** from the Inkplate library. Running custom code might be almost correct, but it could still prevent the display from refreshing properly.

Try uploading these tested examples:

<QuickLink 
  title="Inkplate6_Hello_World.ino" 
  description="Writing 'Hello world' to the Inkplate 6." 
  url="https://github.com/SolderedElectronics/Inkplate-Arduino-library/blob/master/examples/Inkplate6/Basic/Inkplate6_Hello_World/Inkplate6_Hello_World.ino" 
/>

<QuickLink 
  title="Inkplate6_Full_Screen_Colors.ino" 
  description="Example of showing all of the colors of the Inkplate 6." 
  url="https://github.com/SolderedElectronics/Inkplate-Arduino-library/blob/master/examples/Inkplate6/Basic/Inkplate6_Full_Screen_Colors/Inkplate6_Full_Screen_Colors.ino" 
/>

#### 3. Check your power source
- Some **laptop or PC USB ports provide insufficient current**, which may cause Inkplate to get stuck while refreshing.
- Try a **different USB port, power adapter, or USB cable** to ensure the board is receiving stable power.

#### 4. Inspect the e-paper flat cable and panel
- Examine the **flat-flex cable connector** to ensure it's properly seated.
- Check the **edges of the e-paper panel** for any visible damage or cracks.

<CenteredImage src="/img/inkplate_6_motion/flat_cable.jpg" alt="Inkplate 6 e-Paper flat cable" caption="E-paper flat cable connector" width="500px"/>

#### 5. Still having issues?
If none of these steps resolve the issue, **contact our support team** [**here**](https://soldered.com/contact/) with details of your setup and the troubleshooting steps taken.
</ExpandableSection>

<ExpandableSection title="My display refreshes but has artifacts/streaks">
If you notice **artifacts, streaks, or ghosting** on your Inkplate 6 display, follow these steps to clean the screen and check for potential connection issues:

#### 1. Run a display cleaning cycle
Try running the following sketch, which performs **30** full refresh cycles to remove any persistent artifacts:

```cpp
#include <Inkplate.h>
Inkplate inkplate;
int cleanTimes = 30;

void setup()
{
    inkplate.begin();
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
If artifacts persist after cleaning or appear as long vertical lines or streaks, it may indicate a loose, improperly connected, or possibly **damaged** flat cable.

Try re-seating the e-paper flat cable by carefully disconnecting and reconnecting it.

<CenteredImage src="/img/inkplate_6_motion/flat_cable.jpg" alt="Inkplate e-Paper flat cable" caption="E-paper flat cable connector" width="500px"/>

#### 3. Still having issues?
If none of these steps resolve the issue, **contact our support team** [**here**](https://soldered.com/contact/) with details of your setup and the troubleshooting steps you've tried.
</ExpandableSection>

<ExpandableSection title="How to connect a battery to Inkplate?">
All Inkplate models have a 2-pin 2.0mm JST connector for connecting a 3.7V Li-ion battery. Inkplate 6 features an onboard MCP73831 charging IC, which automatically charges the battery when connected via USB and seamlessly switches to battery power when unplugged.

<CenteredImage src="/img/inkplate_6_motion/battery_jst_connector.jpg" alt="Inkplate 6 battery JST connector" caption="JST battery connector" width="500px"/>

<WarningBox>**Warning:** Battery polarity must be correct! Connecting a battery with reversed polarity may permanently damage your Inkplate. See [**this**](/inkplate/6/hardware/battery) page in the documentation for info regarding the battery.</WarningBox>
</ExpandableSection>

<ExpandableSection title="Where can I find hardware files and schematics for Inkplate 6?">
All hardware design files, including schematics, KiCad project files, gerber files, and more, are available in the [**Inkplate 6 hardware repository on GitHub**](https://github.com/SolderedElectronics/Soldered-Inkplate-6-hardware-design).

Additionally, this documentation contains detailed hardware design insights on the [**hardware design page**](/inkplate/6/hardware/design/).
</ExpandableSection>

<ExpandableSection title="Where can I download the 3D files for the enclosure for Inkplate 6?">
We are currently working on making 3D enclosure files available in the [**Inkplate 6 hardware repository**](https://github.com/SolderedElectronics/Soldered-Inkplate-6-hardware-design). Stay tuned for updates!
</ExpandableSection>

<ExpandableSection title="Can I use Inkplate 6 as an e-reader/monitor?">
Short answer: No.

Inkplate 6 is an e-paper development platform and functions similarly to an Arduino with an integrated e-paper display. While it is not designed to be a plug-and-play e-reader or monitor, you could write your own Arduino sketch to display data sent from a PC via USB.

However, if you're looking for a true e-ink monitor experience, Inkplate 6 is not the right choice.
</ExpandableSection>

<ExpandableSection title="Can I use Inkplate 6 with ESPHome/Home Assistant?">
At this time, Inkplate 6 is not officially supported by ESPHome.

There is currently no ESPHome display component for this model, but we are actively working on expanding ESPHome compatibility for all Inkplate devices. Stay tuned for future updates!
</ExpandableSection>

<InfoBox>In case you haven't found the answer to your question, please **Contact us** via [**this**](https://soldered.com/contact/) link.</InfoBox>