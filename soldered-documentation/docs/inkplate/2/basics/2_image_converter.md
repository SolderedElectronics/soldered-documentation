---
slug: /inkplate/2/basics/image-converter
title: Inkplate 2 – Soldered Image Converter
id: 2-image-converter
hide_title: true
---

<SectionTitle title="Soldered Image Converter" backgroundImage="/img/inkplate_2/hardware.png" />

<CenteredImage src="/img/inkplate_6_motion/image_converter.png" alt="Soldered Image Converter" caption="Graphical user interface of the Soldered Image Converter" width="800px" />

Soldered Image Converter is an open-source Python program developed by Soldered. It is used to convert images for Inkplate boards into .h files, which can then be included in Arduino sketches for Inkplate and displayed.
<QuickLink 
  title="Soldered Image Converter Repository" 
  description="See the README in this repository for details on how to download and install the Soldered Image Converter."
  url="https://github.com/SolderedElectronics/Soldered-Image-Converter/" 
/>

After converting the images, export the .h files and save them in your Inkplate sketch's project folder. To find this folder, go to `Sketch -> Show Sketch Folder` in Arduino.

Place the exported .h files in that folder, then include them in the sketch and use the `drawImage` function.