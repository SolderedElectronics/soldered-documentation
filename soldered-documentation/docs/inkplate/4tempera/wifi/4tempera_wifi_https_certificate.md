---
slug: /inkplate/4tempera/wifi/https_certificate
title: Inkplate 4TEMPERA – HTTPS certificate
id: 4tempera-wifi-https-certificate
hide_title: true
---

<SectionTitle title="HTTPS Certificate" backgroundImage="/img/inkplate_2/hardware.png" />

Now that Inkplate is connected to the internet, you will likely want to securely receive data from a website. This page provides an example of how to implement an HTTPS certificate for your connection.

## HTTPS example
This example shows you how to download a .bmp file from the web securely by providing a certificate for the website that will be validated upon connection. Using `applyHttpsCertificate()`, you can store the certificate for your connection:

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
Check out all of the aforementioned functions in this example:

<QuickLink 
  title="Inkplate4TEMPERA_HTTPS_With_Certificate.ino" 
  description="This example will show you how you can download a .bmp file (picture) from the web securely by providing a certificate for the website that will be validated upon connection and display that image on the e-paper display."
  url="https://github.com/SolderedElectronics/Inkplate-Arduino-library/blob/master/examples/Inkplate4TEMPERA/Advanced/WEB_WiFi/Inkplate4TEMPERA_HTTPS_With_Certificate/Inkplate4TEMPERA_HTTPS_With_Certificate.ino" 
/>