---
slug: /inkplate/6flick/wifi/https_certificate
title: Inkplate 6FLICK – HTTPS certificate
id: 6flick-wifi-https-certificate
hide_title: true
---

<SectionTitle title="HTTPS Certificate" backgroundImage="/img/inkplate_2/hardware.png" />

Now that Inkplate is connected to the internet, you will likely want to securely receive data from a website. This page contains an example on how to implement an HTTPS certificate into your connection.

## HTTPS example
This example will show you how to download a .bmp file from the web securely by providing a certificate for the website that will be validated upon connection. Using `applyHttpsCertificate()` you can store the certificate for your connection:

```cpp
Inkplate inkplate(INKPLATE_1BIT);
const char* certificate = ""; //insert your certificate
//..
void setup(){
    inkplate.applyHttpsCertificate(certificate);
}
//...
```

<FunctionDocumentation
  functionName="inkplate.applyHttpsCertificate()"
  description="Applies a certificate that will be checked when communicating with a website."
  returnType="void"
  parameters={[ 
    { type: 'const char*', name: 'certificate', description: 'The certificate in a string format.' },
  ]}
/>

---

## Full example
Check out all the above-mentioned functions in this example:

<QuickLink 
  title="Inkplate6FLICK_HTTPS_With_Certificate.ino" 
  description="This example will show you how you can download a .bmp file (picture) from the web securely by providing a certificate for the website that will be validated upon connection and display that image on the e-paper display."
  url="https://github.com/SolderedElectronics/Inkplate-Arduino-library/blob/dev/examples/Inkplate6FLICK/Advanced/WEB_WiFi/Inkplate6FLICK_HTTPS_With_Certificate/Inkplate6FLICK_HTTPS_With_Certificate.ino" 
/>