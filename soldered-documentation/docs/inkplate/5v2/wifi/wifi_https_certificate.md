---
slug: /inkplate/5v2/wifi/https_certificate
title: Inkplate 5V2 – HTTPS certificate
sidebar_label: HTTPS certificate
id: wifi-https-certificate
---

Now that Inkplate is online, you'll probably want to receive data from a website securely. Here's an example of using an HTTPS certificate for your connection.

## HTTPS example
This example downloads a .bmp file from the web securely. You provide a certificate for the website, which is validated when the connection is made. Use `applyHttpsCertificate()` to store the certificate for your connection:

```cpp
Inkplate inkplate(INKPLATE_1BIT);
const char* certificate = ""; // Insert your certificate
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
See these functions at work in a complete sketch:

<QuickLink 
  title="Inkplate5V2_HTTPS_With_Certificate.ino" 
  description="This example shows how you can download a .bmp file (picture) from the web securely by providing a certificate for the website that will be validated upon connection and display that image on the e-paper display."
  url="https://github.com/SolderedElectronics/Inkplate-Arduino-library/blob/master/examples/Inkplate5V2/Advanced/WEB_WiFi/Inkplate5V2_HTTPS_With_Certificate/Inkplate5V2_HTTPS_With_Certificate.ino" 
/>