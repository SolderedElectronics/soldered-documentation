---
slug: /inkplate/6motion/microsd/sd-image
title: 6Motion - Image from microSD
id: 6motion-microsd-image
---


To draw images from the microSD card, use the `draw` function. 

<InfoBox>Supported formats are: JPG, BMP and BMP.</InfoBox>

<WarningBox>JPG files **without** progressive encoding are supported.</WarningBox>

---

## Drawing PNG, JPG and BMP files from the microSD card

Let's draw the example images of different formats on Inkplate, download them from the [**Inkplate library**](https://github.com/SolderedElectronics/Inkplate_Motion_Arduino_Library/tree/main/examples/Inkplate6Motion/Advanced/SD/Inkplate_6_Motion_Images_From_SD) and place them in the root folder of the microSD card:
<CenteredImage src="/img/inkplate_6_motion/6motion_images_on_sd.png" alt="Images on the microSD card" caption="Images on the microSD card" width="500px" />

Let's draw `image1.png` at coordinates 0, 0 and using the Floyd-Steinberg dither kernel:

```cpp
// Make sure Inkplate and then the microSD card are initialized before this
if (!inkplate.image.draw("image1.png", 0, 0, false, 1, FS_KERNEL, FS_KERNEL_SIZE))
{
    // Show error on the screen if decode failed
    inkplate.println("Image decode failed!");
    inkplate.printf("Decode Err: %d\r\n", inkplate.image.getError());
    inkplate.partialUpdate();
}
else
{
    // The image has been drawn!
    // Otherwise, refresh the screen with a partial update
    inkplate.partialUpdate();
}
```

Here are some more examples: drawing `image2.jpg` without dithering, and `image3.bmp` with Sierra Lite dithering:

```cpp
inkplate.image.draw("image2.jpg", 0, 0, false, 0, NULL, 0));
```

```cpp
inkplate.image.draw("image3.bmp", 0, 0, false, 1, SIERRA_LITE_KERNEL, SIERRA_LITE_KERNEL_SIZE);
```

<FunctionDocumentation
  functionName="inkplate.image.draw()"
  description="Part of the ImageDecoder class. Loads an image from the microSD card or the web, decodes it, and stores the decoded image in the main ePaper framebuffer. Supports optional dithering, color inversion, and format/path specification."
  returnDescription="Returns true if the image was successfully loaded into the framebuffer, otherwise returns false. Use ImageDecoder::getError() to check for failure reasons."
  parameters={[
    { type: "const char*", name: "_path", description: "Path and filename of the image. Can be a URL for a web image or a file path on the microSD card." },
    { type: "int", name: "_x", description: "X position of the image in the ePaper framebuffer (upper-left corner)." },
    { type: "int", name: "_y", description: "Y position of the image in the ePaper framebuffer (upper-left corner)." },
    { type: "bool", name: "_invert", description: "If true, colors are inverted." },
    { type: "uint8_t", name: "_dither", description: "Dithering mode: 0 (disabled), 1 (enabled)." },
    { type: "const KernelElement*", name: "_ditherKernelParameters", description: "Dithering kernel to be used. Options: FS_KERNEL (Floyd-Steinberg), STUCKI_KERNEL (Stucki), SIERRA_KERNEL (Sierra), SIERRA_LITE_KERNEL (Sierra Lite), ATKINSON_KERNEL (Atkinson), BURKES_KERNEL (Burke)." },
    { type: "size_t", name: "_ditherKernelParametersSize", description: "Size of the selected dithering kernel. Use the kernel name with the '_SIZE' suffix, e.g., FS_KERNEL_SIZE." },
    { type: "enum InkplateImageDecodeFormat", name: "_format", description: "Optional. Forces a specific image format if automatic detection fails." },
    { type: "enum InkplateImagePathType", name: "_pathType", description: "Optional. Forces a specific image source (web or microSD card)." }
  ]}
/>
In case there's an error, as mentioned, you can use `getError`:
<FunctionDocumentation
  functionName="inkplate.image.getError()"
  description="Retrieves the last error encountered while decoding an image using ImageDecoder::draw(). If no error occurred, it returns INKPLATE_IMAGE_DECODE_NO_ERR. Errors are cleared before each new decoding process."
  returnDescription="Returns an InkplateImageDecodeErrors enum value representing the last encountered error."
/>

| Enum Value                                 | Description                                  |
|--------------------------------------------|----------------------------------------------|
| INKPLATE_IMAGE_DECODE_NO_ERR               | No error                                    |
| INKPLATE_IMAGE_DECODE_ERR_BAD_PARAM        | Invalid parameter                           |
| INKPLATE_IMAGE_DECODE_ERR_UNKNOWN_FORMAT   | Unknown image format                        |
| INKPLATE_IMAGE_DECODE_ERR_FILE_OPEN_FAIL   | Failed to open image file                   |
| INKPLATE_IMAGE_DECODE_ERR_NO_MEMORY        | Not enough memory for decoding              |
| INKPLATE_IMAGE_DECODE_ERR_BMP_DECODER_FAULT| BMP decoder error                           |
| INKPLATE_IMAGE_DECODE_ERR_JPG_DECODER_FAULT| JPG decoder error                           |
| INKPLATE_IMAGE_DECODE_ERR_PNG_DECODER_FAULT| PNG decoder error                           |
| INKPLATE_IMAGE_DECODE_ERR_BMP_HARD_FAULT   | Critical BMP decoding fault                 |

---

## Full example

<QuickLink 
  title="Inkplate_6_Motion_Images_From_SD.ino" 
  description="Full example of opening and displaying images from the SD card."
  url="https://github.com/SolderedElectronics/Inkplate_Motion_Arduino_Library/blob/main/examples/Inkplate6Motion/Advanced/SD/Inkplate_6_Motion_Images_From_SD/Inkplate_6_Motion_Images_From_SD.ino" 
/>