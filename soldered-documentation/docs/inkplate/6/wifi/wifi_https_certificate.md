---  
slug: /inkplate/6/wifi/https_certificate  
title: HTTPS certificate  
id: wifi-https-certificate  
---

Now that Inkplate is connected to the internet, you will likely want to securely receive data from a website. This page provides an example of how to implement an HTTPS certificate for your connection.

## HTTPS example
This example shows how to securely download a .bmp file from the web by providing a certificate for the website that will be validated upon connection. Using `applyHttpsCertificate()`, you can store the certificate for your connection:

```cpp
Inkplate inkplate;
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
Check out all the functions mentioned above in this example:

<QuickLink 
  title="Inkplate6_HTTPS_With_Certificate.ino" 
  description="This example shows how you can securely download a .bmp file (image) from the web by providing a certificate for the website that will be validated upon connection and display that image on the e-paper display."
  url="https://github.com/SolderedElectronics/Inkplate-Arduino-library/blob/master/examples/Inkplate6/Advanced/WEB_WiFi/Inkplate6_HTTPS_With_Certificate/Inkplate6_HTTPS_With_Certificate.ino" 
/>