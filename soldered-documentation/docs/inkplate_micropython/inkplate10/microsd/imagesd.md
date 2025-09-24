---
slug: /inkplate_micropython/inkplate10/microsd/drawing-images-sdcard
title: Inkplate 10 MicroPython - Drawing images from a MicroSD Card
id: drawing-images-sdcard
---

For this example, you will need a MicroSD Card. 
<WarningBox>**You need to format the MicroSD card to FAT32** to learn how to format the MicroSD card, check out: [PLACEHOLDER FOR FORMATING GUIDE]</WarningBox>

Inkplate 10 allows you to display an image from your MicroSD Card in just a few lines of code.

## Drawing images from a MicroSD Card
First we need to initialize the onboard SD Card module by calling `inkplate.initSDCard(fastBoot=True)`, before we can access the contents of the MicroSD card. By calling `inkplate.drawImage(path,x0,y0,invert,dither, kernel_type)` you can put the image in the buffer, and by calling `inkplate.display()` you actually display the image from buffer to the display.

<InfoBox>It is recommended to use grayscale mode for bigger color range</InfoBox>

<CenteredImage src="/img/inkplate10-micropython/imgweb.jpg" alt="Inkplate 10 running the example code" caption="Inkplate 10 running the example code" width="800px" />

```py
inkplate=Inkplate(Inkplate.INKPLATE_2BIT)
inkplate.begin()
inkplate.initSDCard(fastBoot=True)
inkplate.drawImage("sd/mountain.jpg",0,0,invert=False,dither=True, kernel_type=Inkplate.KERNEL_FLOYD_STEINBERG)
inkplate.display()
```

---

<FunctionDocumentation
  functionName="inkplate = Inkplate(Inkplate.INKPLATE_2BIT)"
  description="Create an Inkplate object in 2-bit grayscale mode."
  returnDescription="Nothing"
  parameters={[
    { type: 'Number', name: 'mode', description: 'Display mode: INKPLATE_1BIT (black & white) or INKPLATE_2BIT (2-bit grayscale).' }
  ]}
/>

<FunctionDocumentation
  functionName="inkplate.begin()"
  description="Initialize the Inkplate hardware and internal state. Must be called once after creating the object, before performing any drawing or display operations."
  returnDescription="Boolean — True if initialization succeeded, otherwise False."
  parameters={[]}
/>

<FunctionDocumentation
  functionName="inkplate.initSDCard(fastBoot=True)"
  description="Initialize the onboard microSD card interface, allowing images, fonts, and data files to be loaded from the SD card."
  returnDescription="Boolean — True if the SD card was successfully initialized, otherwise False."
  parameters={[
    { type: 'Boolean', name: 'fastBoot', description: 'Optional. If True (default), use faster initialization to reduce startup time.' }
  ]}
/>
<FunctionDocumentation
  functionName="inkplate.drawImage(path, x, y, invert=False, dither=True, kernel_type=Inkplate.KERNEL_FLOYD_STEINBERG)"
  description="Draw an image from the SD card or internal storage onto the screen buffer at the specified position."
  returnDescription="Boolean — True if the image was successfully loaded and drawn, otherwise False."
  parameters={[
    { type: 'String', name: 'path', description: 'Path to the image file (e.g. from SD card).' },
    { type: 'Number', name: 'x', description: 'X coordinate where the image’s top-left corner will be placed.' },
    { type: 'Number', name: 'y', description: 'Y coordinate where the image’s top-left corner will be placed.' },
    { type: 'Boolean', name: 'invert', description: 'Optional. If True, invert the image colors. Default is False.' },
    { type: 'Boolean', name: 'dither', description: 'Optional. Apply dithering to improve grayscale quality. Default is True.' },
    { type: 'Constant', name: 'kernel_type', description: 'Optional. Dithering algorithm to use (e.g. Inkplate.KERNEL_FLOYD_STEINBERG, Inkplate.KERNEL_SIMPLE). Default is Floyd-Steinberg.' }
  ]}
/>

<FunctionDocumentation
  functionName="inkplate.display()"
  description="Refresh the e-paper screen and display the current contents of the screen buffer."
  returnDescription="Nothing"
  parameters={[]}
/>

