---
slug: /inkplate/2/faq-troubleshooting
title: Inkplate 2 - FAQ and troubleshooting
sidebar_label: FAQ and troubleshooting
id: 2-faq-troubleshooting
hide_title: true
pagination_next: null
---


<SectionTitle title="FAQ and troubleshooting" backgroundImage="/img/faq.webp" />

We've gathered the most common questions about Inkplate 2 here, along with detailed answers to help you get the most out of your device. Maker hardware and software can be tricky at times, so browse through the questions below. You might find the solution you're looking for.

<ExpandableSection title="I can't upload code to Inkplate 2">
If you're having trouble uploading code, try the following troubleshooting steps.

#### Restart device
- Disconnect the device and power it off completely.
- Reconnect via USB.  

#### Make sure that the device is turned ON
This step often gets overlooked. Make sure that the **ON** LED is turned on.

#### Verify Arduino IDE version
Inkplate 2 requires Arduino IDE 2.0+ for proper board and library support.  
If you're using an older version, update to Arduino 2.0 or later to avoid compatibility issues.

#### Still having issues?
If none of these steps resolve the issue, contact our support team [**here**](https://soldered.com/contact/) with details of your setup and the troubleshooting steps you've tried.
</ExpandableSection>

<ExpandableSection title="My display won't refresh, what am I doing wrong?">
If your Inkplate 2 display is not refreshing, follow these steps to diagnose and resolve the issue.

#### 1. Verify that the code is uploading correctly
- **Enable verbose output** in Arduino under **File → Preferences**, then check the **compile and upload logs**.
- When uploading, a successful upload should print:

```
Leaving... 
Hard resetting via RTS pin...
```

#### 2. Test with an official example
Make sure you're testing with an **unmodified Arduino example** from the Inkplate library. Custom code that looks correct can still prevent the display from refreshing properly.

Try uploading this tested example:

<QuickLink 
  title="Inkplate2_Black_White_Red.ino" 
  description="Full example using the 3-color black, white, and red display mode on Inkplate 2." 
  url="https://github.com/SolderedElectronics/Inkplate-Arduino-library/blob/master/examples/Inkplate2/Basic/Inkplate2_Black_White_Red/Inkplate2_Black_White_Red.ino" 
/>

#### 3. Check your power source
- Some laptop or PC USB ports don't provide enough current, which can cause Inkplate to get stuck while refreshing.
- Try a **different USB port, power adapter, or USB cable** to ensure the board is receiving stable power.

#### 4. Inspect the e-paper flat cable and panel
- Examine the **flat-flex cable connector** to ensure it's properly seated.
- Check the **edges of the e-paper panel** for any visible damage or cracks.

#### 5. Still having issues?
If none of these steps resolve the issue, **contact our support team** [**here**](https://soldered.com/contact/) with details of your setup and troubleshooting steps taken.
</ExpandableSection>

<ExpandableSection title="My display refreshes but has artifacts/streaks">
If you notice **artifacts, streaks, or ghosting** on your Inkplate 2 display, follow these steps to clean the screen and check for potential connection issues.

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
        inkplate.fillRect(0, 0, 212, 104, INKPLATE2_BLACK);
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
If artifacts persist after cleaning or appear as long vertical lines or streaks, it may indicate a loose, improperly connected, or possibly damaged flat cable.

Try re-seating the e-paper flat cable by carefully disconnecting and reconnecting it.


#### 3. Still having issues?
If none of these steps resolve the issue, **contact our support team** [**here**](https://soldered.com/contact/) with details of your setup and the troubleshooting steps you've tried.
</ExpandableSection>

<ExpandableSection title="Can I use partial update all the time on Inkplate 2?">
Tri-color e-paper displays, like the one on Inkplate 2, are more sensitive to ghosting. It's recommended to perform a full update (`inkplate.display()`) after every few partial updates to maintain clarity and avoid burn-in.
</ExpandableSection>

<ExpandableSection title="Where can I find hardware files and schematics for Inkplate 2?">
All hardware design files, including schematics, KiCad project files, gerber files, and more, are available in the [**Inkplate 2 hardware repository on GitHub**](https://github.com/SolderedElectronics/Soldered-Inkplate-2-hardware-design).

Additionally, this documentation contains detailed hardware design insights on the [**hardware design page**](/inkplate/2/hardware/design/).
</ExpandableSection>

<ExpandableSection title="Where can I download the 3D files for the enclosure for Inkplate 2?">
We're currently working on making 3D enclosure files available in the [**Inkplate 2 hardware repository**](https://github.com/SolderedElectronics/Soldered-Inkplate-2-hardware-design). Stay tuned for updates!
</ExpandableSection>

<ExpandableSection title="Can I use Inkplate 2 as an e-reader/monitor?">
Short answer: no.  

Inkplate 2 is an e-paper development platform, similar to an Arduino with a built-in e-paper display. It's not a plug-and-play e-reader or monitor, though you can write your own Arduino sketch to display data sent from a PC over USB. If you're looking for a true e-ink monitor, this isn't the board for that.
</ExpandableSection>

<ExpandableSection title="Can I use Inkplate 2 with ESPHome/Home Assistant?">
Right now, Inkplate 2 isn't officially supported by ESPHome.  

There's currently no ESPHome display component for this model, but we're actively working on expanding ESPHome compatibility for all Inkplate devices. Stay tuned for future updates!
</ExpandableSection>

<InfoBox>In case you haven't found the answer to your question, please **Contact us** via [**this**](https://soldered.com/contact/) link, or ask on the [**Soldered community**](https://community.soldered.com), where you can browse existing questions or post your own.</InfoBox>