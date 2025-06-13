---
slug: /inkplate/6flick/basics/image-converter
title: Inkplate 6FLICK – Soldered Image Converter
id: 6flick-image-converter
hide_title: true
---

<SectionTitle title="Soldered Image Converter" backgroundImage="/img/inkplate_2/hardware.png" />

<CenteredImage src="/img/inkplate_6_motion/image_converter.png" alt="Soldered Image Converter" caption="Graphical user interface of the Soldered Image Converter" width="800px" />

Soldered Image Converter is an open-source Python program by Soldered. It is used to convert images for Inkplate boards into .h files, which can be included in Arduino sketches for Inkplate and then displayed.
<QuickLink 
  title="Soldered Image Converter Repository" 
  description="See the README in this repository for details on how to download and install the Soldered Image Converter."
  url="https://github.com/SolderedElectronics/Soldered-Image-Converter/" 
/>

After converting images, export the .h files and save them in your Inkplate sketch's project folder. To locate this folder, go to `Sketch -> Show Sketch Folder` in Arduino.

Once the exported .h files are in the folder, include them in the sketch and use the `drawImage` function.

---