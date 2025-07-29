---
slug: /inkplate/6motion/wifi/get-post
title: 6Motion - GET & POST requests
sidebar_label: GET & POST requests
id: 6motion-wifi-get-post
---


Now that Inkplate is connected to the internet, you will likely want to send and recieve data on it form sensors, messages, from your custom API's etc. This page contains examples on how to send and recieve data on Inkplate via the internet:

---

## GET request

Using `client.GET()` will enable you to easily download and handle data on Inkplate however you want. Here is an example on how to GET a .txt file and print it on Inkplate:

```cpp
// This is the file which will be downloaded:
char httpUrl[] = {"https://raw.githubusercontent.com/SolderedElectronics/Inkplate_Motion_Arduino_Library/refs/heads/main/examples/Inkplate6Motion/Advanced/Web_WiFi/Inkplate_6_Motion_WiFi_Simple/exampleFile.txt"};

// Make sure Inkplate is previously connected to WiFi

// Create the WiFi client object for HTTP request
WiFiClient client;
// Since the file will be received in chunks, keeps track of the byte received
uint32_t totalSize = 0;
// Try to open the page
if (client.begin(httpUrl))
{
    // Make GET request on that httpUrl
    if (client.GET())
    {
        // GET was successful! Let's print some info
        inkplate.print("Connected, file size: ");
        inkplate.print(client.size(), DEC);
        inkplate.println("bytes");
        inkplate.partialUpdate(true);
        inkplate.println("");
        inkplate.println("File contents:");

        // Read file contents:
        while (client.available())
        {
            // Use blocking method to get all chunks of the HTTP
            {
                if (client.available() > 0)
                {
                    char myBuffer[2000];
                    int n = client.read(myBuffer, sizeof(myBuffer));
                    totalSize += n;

                    // Print out the chunk.
                    for (int i = 0; i < n; i++)
                    {
                        inkplate.print(myBuffer[i]);
                    }
                }
            }
        }
    }
}
else
{
    inkplate.println("Failed to get the file!");
}
// Show updates on the display
inkplate.partialUpdate(true);

// Really important, end the WiFiClient connection!
// Otherwise any other AT command to the modem will fail!
client.end();
```
<WarningBox>It's important to end the client connection with `client.end()`, otherwise communicating with the ESP32 modem won't work and no further requests can be made.</WarningBox>

---

## POST request

To send data from Inkplate to a web server, you can use the same built-in `WiFiClient` class. Let's use [**webhook.site**](https://webhook.site/), which is a great resource for testing POST and GET requests. By visiting the site, you get a unique URL which can then be sent a POST request to from Inkplate which will then be visible on the site:
```cpp
// Add webhook.site URL here, something like
// https://webhook.site/0e92fcdc-test-1234-test-44e5ca8a0b47
char httpUrl[] = {""};

// This function sends a POST request to the set URL
void sendPost()
{
    // Before using this function, make sure Inkplate is connected to the internet

    // Create the WiFi client object for HTTP request
    WiFiClient client;

    // Since the file will be received in chunks, keeps track of the byte received
    uint32_t totalSize = 0;

    // Begin connection to URL
    if (client.begin(httpUrl))
    {
        // We're connected! 
        // Create request body, a simple request with one data field
        char bodyStr[256];
        // Here is where data is added
        // In this case, we will add a random number from -126 to 128
        sprintf(bodyStr, "data=%d", random(-127, 128));
        // See details of the sprintf c++ function to see how to add different types of data here
        // Do the actual POST request
        if (client.POST(bodyStr, strlen(bodyStr)))
        {
            // Read the response
            // This is optional
            while (client.available())
            {
                // Use blocking method to get all chunks of the HTTP reply
                {
                    if (client.available() > 0)
                    {
                        char myBuffer[2000];
                        int n = client.read(myBuffer, sizeof(myBuffer));
                        totalSize += n;

                        // Print out the response chunk on Inkplate
                        for (int i = 0; i < n; i++)
                        {
                            inkplate.print(myBuffer[i]);
                        }
                    }
                }
            }
        }
        // Add new line at the end
        inkplate.println();

        // Refresh the screen
        inkplate.partialUpdate();
    }
    else
    {
        // Error? inform the user
        inkplate.println("Failed to do POST request!");
        inkplate.partialUpdate();
    }
    
    // Really important, end the WiFiClient connection!
    // Otherwise any other AT command to the modem will fail!
    if (!client.end())
    {
        inkplate.println("Client end problem");
    }
}
```
The randomly generated number will then be visible on webhook.site.

<WarningBox>It's important to end the client connection with `client.end()`, otherwise communicating with the ESP32 modem won't work and no further requests can be made.</WarningBox>

---

## POST request with JSON

It's possible not only to send data the old-school HTTP way, using the `ArduinoJSON` library it's possible to send data from Inkplate in this powerful and versatile format:
```cpp
// Include ArduinoJSON library. Get it from here: https://github.com/bblanchon/ArduinoJson
#include <ArduinoJson.h>

// Add webhook.site URL here, something like
// https://webhook.site/0e92fcdc-test-1234-test-44e5ca8a0b47
char httpUrl[] = {""};

// This function sends the POST request but with a JSON body
void sendPostWithJson()
{
    // Create the WiFi client object for HTTP request
    WiFiClient client;

    // Since the file will be received in chunks, keeps track of the byte received
    uint32_t totalSize = 0;

    // Connect to the URL
    if (client.begin(httpUrl))
    {
        // Add a HTTP header (must be added for JSON in this case)
        client.addHeader("Content-Type: application/json");

        // Create body with JSON
        char jsonData[256];
        StaticJsonDocument<200> webhookSiteJSON;
        // Add number data to field1
        webhookSiteJSON["dataField"] = random(-127, 128);
        // Serialize it so that it can be added to the POST request
        serializeJson(webhookSiteJSON, jsonData);

        // Do POST
        if (client.POST(jsonData, strlen(jsonData)))
        {
            while (client.available())
            {
                // Use blocking method to get all chunks of the HTTP reply
                {
                    if (client.available() > 0)
                    {
                        char myBuffer[2000];
                        int n = client.read(myBuffer, sizeof(myBuffer));
                        totalSize += n;

                        // Print out the chunk
                        for (int i = 0; i < n; i++)
                        {
                            inkplate.print(myBuffer[i]);
                        }
                    }
                }
            }
        }
        // Update the display
        inkplate.partialUpdate(true);
    }
    else
    {
        // Error? Inform the user
        inkplate.println("Failed to POST");
        inkplate.partialUpdate(true);
    }

    // Really important, end the WiFiClient connection!
    // Otherwise any other AT command to the modem will fail!
    if (!client.end())
    {
        inkplate.println("Client end problem");
    }
}
```

---

## Full examples

<QuickLink 
  title="Inkplate_6_Motion_WiFi_Simple.ino" 
  description="Full example on how to connect to WiFi, GET a .txt file and print it out to Inkplate"
  url="https://github.com/SolderedElectronics/Inkplate_Motion_Arduino_Library/blob/main/examples/Inkplate6Motion/Advanced/Web_WiFi/Inkplate_6_Motion_WiFi_Simple/Inkplate_6_Motion_WiFi_Simple.ino" 
/>

<QuickLink 
  title="Inkplate_6_Motion_HTTP_POST.ino" 
  description="Full example on how to send data to a webserver via HTTP and POST request on Inkplate 6 MOTION"
  url="https://github.com/SolderedElectronics/Inkplate_Motion_Arduino_Library/blob/main/examples/Inkplate6Motion/Advanced/Web_WiFi/Inkplate_6_Motion_HTTP_POST/Inkplate_6_Motion_HTTP_POST.ino" 
/>