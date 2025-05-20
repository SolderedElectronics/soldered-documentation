---
slug: /inkplate/6motion/wifi/image-from-web
title: 6Motion - Draw Image from Web
id: 6motion-wifi-image-from-web
---


Drawing an image from the web on Inkplate 6MOTION is simple using the `draw` function, which supports multiple image formats.

<InfoBox>Supported formats: JPG, BMP, and PNG.</InfoBox>

<WarningBox>JPG files **without** progressive encoding are supported.</WarningBox>

<InfoBox>If you experience issues displaying an image, try re-saving it with an image editing program. The issue is usually related to the image format.</InfoBox>

---

## Drawing an Image from a URL

Let's draw this image of the Eurodom building in Osijek, Croatia on Inkplate 6MOTION:
<CenteredImage src="/img/inkplate_6_motion/sample_image.jpg" alt="Example Image" caption="Example image by @filipbaotic on Pexels" />

```cpp
// Ensure Inkplate is connected to the internet
const char * imageUrl = "docs.inkplate.com/img/sample_image.jpg";
// Draw the image using Floyd-Steinberg dither kernel
if (!inkplate.image.draw(imageUrl, 0, 0, false, 1, FS_KERNEL, FS_KERNEL_SIZE))
{
    // Show error on the screen if decoding fails
    inkplate.println("Image download or decode failed!");
    inkplate.printf("Decode Err: %d\r\n", inkplate.image.getError());
}
// Show the result on the display
inkplate.partialUpdate();
```

<FunctionDocumentation
  functionName="inkplate.image.draw()"
  description="Loads an image from the microSD card or web, decodes it, and stores it in the ePaper framebuffer. Supports optional dithering, color inversion, and format/path specification."
  returnDescription="Returns true if the image was successfully loaded into the framebuffer, otherwise false. Use ImageDecoder::getError() for failure details."
  parameters={[ 
    { type: "const char*", name: "_path", description: "Path and filename of the image. Can be a URL (for web images) or a file path (on the microSD card)." },
    { type: "int", name: "_x", description: "X-coordinate of the image's upper-left corner in the framebuffer." },
    { type: "int", name: "_y", description: "Y-coordinate of the image's upper-left corner in the framebuffer." },
    { type: "bool", name: "_invert", description: "If true, inverts colors." },
    { type: "uint8_t", name: "_dither", description: "Dithering mode: 0 (disabled), 1 (enabled)." },
    { type: "const KernelElement*", name: "_ditherKernelParameters", description: "Dithering kernel to be used. Options: FS_KERNEL (Floyd-Steinberg), STUCKI_KERNEL, SIERRA_KERNEL, SIERRA_LITE_KERNEL, ATKINSON_KERNEL, BURKES_KERNEL." },
    { type: "size_t", name: "_ditherKernelParametersSize", description: "Size of the selected dithering kernel, e.g., FS_KERNEL_SIZE." },
    { type: "enum InkplateImageDecodeFormat", name: "_format", description: "Optional. Forces a specific image format if automatic detection fails." },
    { type: "enum InkplateImagePathType", name: "_pathType", description: "Optional. Forces a specific image source (web or microSD card)." }
  ]}
/>

In case of an error, you can use `getError()`:

<FunctionDocumentation
  functionName="inkplate.image.getError()"
  description="Retrieves the last error encountered while decoding an image using ImageDecoder::draw(). Errors are cleared before each decoding process."
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

## Full Example

<QuickLink 
  title="Inkplate_6_Motion_Image_From_Web.ino" 
  description="Connect to WiFi and draw an image from the web."
  url="https://github.com/SolderedElectronics/Inkplate_Motion_Arduino_Library/blob/main/examples/Inkplate6Motion/Advanced/Web_WiFi/Inkplate_6_Motion_Image_From_Web/Inkplate_6_Motion_Image_From_Web.ino" 
/>
