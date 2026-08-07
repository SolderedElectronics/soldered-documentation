---  
slug: /inkplate/5v2/faq-troubleshooting/  
title: Inkplate 5V2 - FAQ and troubleshooting  
sidebar_label: FAQ and troubleshooting
id: faq-troubleshooting  
hide_title: true  
pagination_next: null
---

<SectionTitle title="FAQ and troubleshooting" backgroundImage="/img/faq.webp" />

Here are the questions we get asked most often, with answers. Maker hardware and software can be tricky at times, so browse through the list below and see if your issue is covered.

<ExpandableSection title="I can't upload code to Inkplate 5V2">
If you're having trouble uploading code, try the following troubleshooting steps:

#### Restart device
- Disconnect the device and power it off completely.
- Reconnect via USB.  

#### Make sure that the device is turned ON
This step is easy to miss. Check that the **ON** LED is lit.

#### Verify Arduino IDE version
Inkplate 5V2 requires Arduino IDE 2.0+ for proper board and library support.  
If you're using an older version, update to Arduino IDE 2.0 or later to avoid compatibility issues.

#### Still having issues?
If none of these steps resolve the issue, contact our support team [**here**](https://soldered.com/contact/) with details of your setup and the troubleshooting steps you've tried.
</ExpandableSection>

<ExpandableSection title="Can I use partial update all the time on Inkplate 5V2?">
To preserve display quality and extend the lifespan of the panel, it's recommended to perform a full update (`inkplate.display()`) after a certain number of partial updates. 
</ExpandableSection>

<ExpandableSection title="My display won't refresh, what am I doing wrong?">
If your Inkplate 5V2 display is not refreshing, follow these steps to diagnose and resolve the issue:

#### 1. Verify that the code is uploading correctly
- Enable verbose output in Arduino under `File → Preferences`, then check the compile and upload logs.
- A successful upload should print:

```
Leaving... 
Hard resetting via RTS pin...
```

#### 2. Test with an official example
Test with an unmodified Arduino example from the Inkplate library. Custom code can look almost right and still keep the display from refreshing properly.

Try uploading these tested examples:

<QuickLink 
  title="Inkplate5V2_Hello_World.ino" 
  description="Writing 'Hello world' to the Inkplate 5V2." 
  url="https://github.com/SolderedElectronics/Inkplate-Arduino-library/blob/master/examples/Inkplate5V2/Basic/Inkplate5V2_Hello_World/Inkplate5V2_Hello_World.ino" 
/>

<QuickLink 
  title="Inkplate5V2_Grayscale.ino" 
  description="Example of showing all of the grayscale levels of the Inkplate 5V2." 
  url="https://github.com/SolderedElectronics/Inkplate-Arduino-library/blob/master/examples/Inkplate5V2/Basic/Inkplate5V2_Grayscale/Inkplate5V2_Grayscale.ino" 
/>

#### 3. Check your power source
- Some laptop and PC USB ports don't supply enough current, which can leave Inkplate stuck mid-refresh.
- Try a different USB port, power adapter, or USB cable so the board gets stable power.

#### 4. Inspect the e-paper flat cable and panel
- Check that the flat-flex cable connector is properly seated.
- Look along the edges of the e-paper panel for visible damage or cracks.
<CenteredImage src="/img/inkplate_6_motion/flat_cable.jpg" alt="Inkplate 5V2 e-Paper flat cable" caption="E-paper flat cable connector" width="500px"/>

#### 5. Still having issues?
If none of these steps resolve the issue, contact our support team [**here**](https://soldered.com/contact/) with details of your setup and the troubleshooting steps taken.
</ExpandableSection>

<ExpandableSection title="My display refreshes but has artifacts/streaks">
If you notice artifacts, streaks, or ghosting on your Inkplate 5V2 display, follow these steps to clean the screen and check for connection issues:

#### 1. Run a display cleaning cycle
Try running the sketch below. It performs 30 full refresh cycles to clear out any persistent artifacts:

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
        inkplate.fillRect(0, 0, 1280, 720, BLACK);
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
If artifacts persist after cleaning, or show up as long vertical lines or streaks, the flat cable may be loose, seated incorrectly, or damaged.

Try re-seating the e-paper flat cable by carefully disconnecting and reconnecting it.

<CenteredImage src="/img/inkplate_6_motion/flat_cable.jpg" alt="Inkplate e-Paper flat cable" caption="E-paper flat cable connector" width="500px"/>

#### 3. Still having issues?
If none of these steps resolve the issue, contact our support team [**here**](https://soldered.com/contact/) with details of your setup and the troubleshooting steps you've tried.
</ExpandableSection>

<ExpandableSection title="How to connect a battery to Inkplate?">
All Inkplate models have a 2-pin 2.0mm JST connector for a 3.7V Li-ion battery. Inkplate 5V2 has an onboard MCP73831 charging IC, which charges the battery whenever the board is connected via USB and switches over to battery power when you unplug it.

<CenteredImage src="/img/inkplate_6_motion/battery_jst_connector.jpg" alt="Inkplate 5V2 battery JST connector" caption="JST battery connector" width="500px"/>

<WarningBox>**Battery polarity must be correct!** Connecting a battery with reversed polarity may permanently damage your Inkplate. See [**this**](/inkplate/5v2/hardware/battery) page in the documentation for more about the battery.</WarningBox>
</ExpandableSection>

<ExpandableSection title="Where can I find hardware files and schematics for Inkplate 5V2?">
All hardware design files, including schematics, KiCad project files, gerber files, and more, are available in the [**Inkplate 5V2 hardware repository on GitHub**](https://github.com/SolderedElectronics/Soldered-Inkplate-5-Gen2-hardware-design).

This documentation also walks through the hardware in more detail on the [**hardware design page**](/inkplate/5v2/hardware/design/).
</ExpandableSection>

<ExpandableSection title="Where can I download the 3D files for the enclosure for Inkplate 5V2?">
We're working on making the 3D enclosure files available in the [**Inkplate 5V2 hardware repository**](https://github.com/SolderedElectronics/Soldered-Inkplate-5-Gen2-hardware-design).
</ExpandableSection>

<ExpandableSection title="Can I use Inkplate 5V2 as an e-reader/monitor?">
Short answer: No.  

Inkplate 5V2 is an e-paper development platform, and it works much like an Arduino with an e-paper display attached. It isn't designed as a plug-and-play e-reader or monitor, though you could write your own Arduino sketch to display data sent from a PC over USB.

If what you want is a proper e-ink monitor, Inkplate 5V2 isn't the right choice.
</ExpandableSection>

<ExpandableSection title="Can I use Inkplate 5V2 with ESPHome/Home Assistant?">
Inkplate 5V2 is not officially supported by ESPHome at the moment.  

There is no ESPHome display component for this model yet. We're working on expanding ESPHome compatibility across Inkplate devices.
</ExpandableSection>

<InfoBox>If you haven't found the answer to your question, contact us via [**this**](https://soldered.com/contact/) link, or ask on the [**Soldered community**](https://community.soldered.com), where you can browse existing questions or post your own.</InfoBox>