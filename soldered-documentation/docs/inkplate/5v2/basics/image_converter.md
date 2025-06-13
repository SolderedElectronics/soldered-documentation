---  
slug: /inkplate/5v2/image-converter  
title: Inkplate 5V2 – Soldered Image Converter
id: image-converter  
---  
<CenteredImage src="/img/inkplate_6_motion/image_converter.png" alt="Soldered Image Converter" caption="Graphical user interface of the Soldered Image Converter" width="800px" />

Soldered Image Converter is an open-source Python program created by Soldered. It converts images for Inkplate boards into .h files, which can be included in Arduino sketches for Inkplate and then displayed.  
<QuickLink 
  title="Soldered Image Converter Repository" 
  description="See the README in this repository for details on how to download and install the Soldered Image Converter."
  url="https://github.com/SolderedElectronics/Soldered-Image-Converter/" 
/>

After converting images, export the .h files and save them in your Inkplate sketch's project folder. To find this folder, go to `Sketch -> Show Sketch Folder` in Arduino.

Place the exported .h files in that folder, then include them in the sketch and use the `drawImage` function.