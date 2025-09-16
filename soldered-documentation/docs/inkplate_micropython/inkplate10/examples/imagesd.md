---
slug: /inkplate_micropython/inkplate10/examples/drawing-images-sdcard
title: Drawing images from a MicroSD Card
id: drawing-images-sdcard
---

For this example, you will need a MicroSD Card. It is recommended to format it to FAT32.

Inkplate 10 allows you to display an image from your MicroSD Card in just a few lines of code.

## Drawing images from a MicroSD Card
First we need to initialize the onboard SD Card module by calling `inkplate.initSDCard(fastBoot=True)`. Before we can access the 
