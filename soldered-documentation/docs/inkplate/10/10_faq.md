---
slug: /inkplate/10/faq-troubleshooting
title: Inkplate 10 - FAQ and troubleshooting
sidebar_label: FAQ and troubleshooting
id: 10-faq-troubleshooting
hide_title: true
pagination_next: null
---


<SectionTitle title="FAQ and troubleshooting" backgroundImage="/img/faq.webp" />

Here, we've gathered the most frequently asked questions and answers to help you get the most out of your Inkplate 10. Whether you're new to e-paper development or troubleshooting an issue, this page is here to guide you through common problems and solutions.

<ExpandableSection title="I can't upload code to Inkplate 10">
If you're having trouble uploading code, try the following troubleshooting steps.

#### Restart device
- Disconnect the device and power it off completely.
- Reconnect via USB.  

#### Make sure that the device is turned ON
This one is easy to forget. Make sure the **ON** LED is lit.

#### Verify Arduino IDE version
Inkplate 10 requires Arduino IDE 2.0+ for proper board and library support.  
If you're using an older version, update to Arduino 2.0 or later to avoid compatibility issues.

#### Still having issues?
If none of these steps resolve the issue, contact our support team [**here**](https://soldered.com/contact/) with details of your setup and the troubleshooting steps you've tried.
</ExpandableSection>



<ExpandableSection title="My display won't refresh, what am I doing wrong?">
If your Inkplate 10 display is not refreshing, follow these steps to diagnose and resolve the issue.

#### 1. Verify that the code is uploading correctly
- **Enable verbose output** in Arduino under **File → Preferences**, then check the **compile and upload logs**.
- A successful upload ends with:

```
Leaving... 
Hard resetting via RTS pin...
```

#### 2. Test with an official example
Make sure you're testing with an **unmodified Arduino example** from the Inkplate library. Running custom code might be **almost correct** but could still prevent the display from refreshing properly.

Try uploading these tested examples:

<QuickLink 
  title="Inkplate10_Black_And_White.ino" 
  description="Full example using black and white display mode on Inkplate 10." 
  url="https://github.com/SolderedElectronics/Inkplate-Arduino-library/blob/master/examples/Inkplate10/Basic/Inkplate10_Black_And_White/Inkplate10_Black_And_White.ino" 
/>

<QuickLink 
  title="Inkplate10_Grayscale.ino" 
  description="Full example using grayscale display mode on Inkplate 10." 
  url="https://github.com/SolderedElectronics/Inkplate-Arduino-library/blob/master/examples/Inkplate10/Basic/Inkplate10_Grayscale/Inkplate10_Grayscale.ino" 
/>

#### 3. Check your power source
- Some **laptop or PC USB ports provide insufficient current**, which may cause Inkplate to get stuck while refreshing.
- Try a **different USB port, power adapter, or USB cable** to ensure the board is receiving stable power.

#### 4. Inspect the e-paper flat cable and panel
- Examine the **flat-flex cable connector** to ensure it's properly seated.
- Check the **edges of the e-paper panel** for any visible damage or cracks.
<CenteredImage src="/img/inkplate_6_motion/flat_cable.jpg" alt="Inkplate 10 e-Paper flat cable" caption="E-paper flat cable connector" width="500px"/>

#### 5. Still having issues?
If none of these steps resolve the issue, **contact our support team** [**here**](https://soldered.com/contact/) with details of your setup and troubleshooting steps taken.
</ExpandableSection>

<ExpandableSection title="My display refreshes but has artifacts/streaks">
If you notice **artifacts, streaks, or ghosting** on your Inkplate 10 display, follow these steps to clean the screen and check for potential connection issues.

#### 1. Run a display cleaning cycle
Try running the following sketch, which performs **30** full refresh cycles to remove any persistent artifacts:

```cpp
#include <Inkplate.h>
Inkplate display(INKPLATE_1BIT);
int cleanTimes = 30;

void setup()
{
    display.begin();
    for(int i = 0; i < cleanTimes; i++)
    {
        display.clearDisplay();
        display.display();
        delay(500);
        display.fillRect(0, 0, 1200, 825, BLACK);
        display.display();
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

<CenteredImage src="/img/inkplate_6_motion/flat_cable.jpg" alt="Inkplate 10 e-Paper flat cable" caption="E-paper flat cable connector" width="500px"/>

#### 3. Still having issues?
If none of these steps resolve the issue, **contact our support team** [**here**](https://soldered.com/contact/) with details of your setup and the troubleshooting steps you've tried.
</ExpandableSection>

<ExpandableSection title="Can I use partial update all the time on Inkplate 10?">
To preserve display quality and extend the lifespan of the panel, it's recommended to perform a full update (`display.display()`) after a certain number of partial updates. 
</ExpandableSection>

<ExpandableSection title="How to connect a battery to Inkplate?">
All Inkplate models have a 2-pin 2.0mm JST connector for connecting a 3.7V Li-ion battery. Inkplate 10 features an onboard MCP73831 charging IC, which automatically charges the battery when connected via USB and switches over to battery power on its own when you unplug it.

<CenteredImage src="/img/inkplate_6_motion/battery_jst_connector.jpg" alt="Inkplate 10 battery JST connector" caption="JST battery connector" width="500px"/>

<WarningBox>**Warning:** Battery polarity must be correct! Connecting a battery with reversed polarity may permanently damage your Inkplate. See [**this**](/inkplate/10/hardware/battery) page in the documentation for info regarding the battery.</WarningBox>
</ExpandableSection>

<ExpandableSection title="Where can I find hardware files and schematics for Inkplate 10?">
All hardware design files, including schematics, KiCad project files, gerber files, and more, are available in the [**Inkplate 10 hardware repository on GitHub**](https://github.com/SolderedElectronics/Soldered-Inkplate-10-hardware-design).

Additionally, this documentation contains detailed hardware design insights on the [**hardware design page**](/inkplate/10/hardware/design/).
</ExpandableSection>

<ExpandableSection title="Where can I download the 3D files for the enclosure for Inkplate 10?">
They're in the [**Inkplate 10 hardware repository**](https://github.com/SolderedElectronics/Soldered-Inkplate-10-hardware-design/tree/main/OUTPUTS/V1.3.1/3D%20printable%20files). The `OUTPUTS/V1.3.1/3D printable files` folder has print-ready `.stl` files for the top and bottom of the case, along with a description text file covering the settings we use.

If you'd rather modify the case than print it as is, the editable sources are under `CAD/V1.3.1/Source 3D files` as `.step`, and the V1.3.0 folder also includes Fusion 360 `.f3d` and `.f3z` files.
</ExpandableSection>

<ExpandableSection title="Can I use Inkplate 10 as an e-reader/monitor?">
Short answer: No.  

Inkplate 10 is an e-paper development platform and functions similarly to an Arduino with an integrated e-paper display. While it is not designed to be a plug-and-play e-reader or monitor, you could write your own Arduino sketch to display data sent from a PC via USB.

However, if you're looking for a true e-ink monitor experience, Inkplate 10 is not the right choice.
</ExpandableSection>

<ExpandableSection title="Can I use Inkplate 10 with ESPHome/Home Assistant?">
Yes. ESPHome ships an Inkplate display platform that covers Inkplate 10. Set the `model` key to `inkplate_10`:

```yaml
display:
  - platform: inkplate6
    model: inkplate_10
    greyscale: false
    partial_updating: false
    update_interval: 60s
```

The platform is named `inkplate6` for all Inkplate models, so don't be thrown by the name. See the [**ESPHome Inkplate documentation**](https://esphome.io/components/display/inkplate6.html) for the full list of configuration options and the GPIO pin assignments the platform expects.
</ExpandableSection>

<InfoBox>In case you haven't found the answer to your question, please **Contact us** via [**this**](https://soldered.com/contact/) link, or ask on the [**Soldered community**](https://community.soldered.com), where you can browse existing questions or post your own.</InfoBox>