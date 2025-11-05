---
slug: /i2s-audio-amplifier/arduino/troubleshooting
title: Stereo I2S Audio Amplifier - Troubleshooting
sidebar_label: Troubleshooting
id: i2s-audio-amplifier-arduino-5
hide_title: False
pagination_next: null
---

<ExpandableSection title="My sensor doesn't work! (Regular breakout board)">

#### Check wiring
Ensure that your cables are properly connected and in good condition. Try using the same cable with another device to verify that it works. If the issue persists, swap them out for  different cables to rule out any possible damage or defects.

</ExpandableSection>

<ExpandableSection title="Sketch too big">

#### Enable Huge APP (NO OTA)
Use the partition scheme **Huge App (NO OTA)** under **Tools -> Board** after selecting **ESP32 Dev Module** so that there is enough memory for the program to upload along with you other extensions.

#### Upgrade to latest ESP32 board package
Make sure to update your board definitions to latest version, as new versions introduce new changes.

</ExpandableSection>

<InfoBox>In case you haven't found the answer to your question, please **contact us** via [**this**](https://soldered.com/contact/) link.</InfoBox>