---
slug: /inkplate/6/wifi/get-post
title: Inkplate 6 – GET & POST requests
sidebar_label: GET & POST requests
id: wifi-get-post
---

Now that Inkplate is connected to the internet, you will likely want to send and receive data from sensors, messages, and your custom APIs. This page contains examples of how to send and receive data using Inkplate over the internet:

---

## GET request

Using `http.GET()` enables you to easily download and handle data on Inkplate according to your needs. Here is an example of how to GET a .html file and print it on Inkplate:

```cpp
#include "Inkplate.h"   //Include Inkplate library to the sketch
#include <HTTPClient.h> //Include HTTP library to this sketch
#include <WiFi.h>       //Include ESP32 WiFi library to our sketch

#define ssid "" // Name of the WiFi network (SSID) that you want to connect Inkplate to
#define pass "" // Password of that WiFi network

Inkplate display(INKPLATE_1BIT); // Create an object on Inkplate library and also set library into 1 Bit mode (BW)

void setup()
{
    display.begin();                                  // Init Inkplate library (you should call this function ONLY ONCE)
    display.clearDisplay();                           // Clear frame buffer of display
    display.display();                                // Put clear image on display
    display.setTextSize(2);                           // Set text scaling to two (text will be two times bigger)
    display.setCursor(0, 0);                          // Set print position
    display.setTextColor(BLACK, WHITE);               // Set text color to black and background color to white
    display.println("Scanning for WiFi networks..."); // Write text
    display.display();                                // Send everything to display (refresh display)

    int n = WiFi.scanNetworks(); // Start searching WiFi networks and put the nubmer of found WiFi networks in variable
                                 // n
    if (n == 0)
    { // If you did not find any network, show the message and stop the program.
        display.print("No WiFi networks found!");
        display.partialUpdate();
        while (true)
            ;
    }
    else
    {
        if (n > 10)
            n = 10; // If you did find, print name (SSID), encryption and signal strength of first 10 networks
        for (int i = 0; i < n; i++)
        {
            display.print(WiFi.SSID(i));
            display.print((WiFi.encryptionType(i) == WIFI_AUTH_OPEN) ? 'O' : '*');
            display.print('\n');
            display.print(WiFi.RSSI(i), DEC);
        }
        display.partialUpdate(); //(Partial) refresh thescreen
    }

    display.clearDisplay();          // Clear everything in frame buffer
    display.setCursor(0, 0);         // Set print cursor to new position
    display.print("Connecting to "); // Print the name of WiFi network
    display.print(ssid);
    WiFi.begin(ssid, pass); // Try to connect to WiFi network
    while (WiFi.status() != WL_CONNECTED)
    {
        delay(1000); // While it is connecting to network, display dot every second, just to know that Inkplate is
                     // alive.
        display.print('.');
        display.partialUpdate();
    }
    display.print("connected"); // If it's connected, notify user
    display.partialUpdate();

    HTTPClient http;
    if (http.begin("http://example.com/index.html"))
    { // Now try to connect to some web page (in this example www.example.com. And yes, this is a valid Web page :))
        if (http.GET() > 0)
        { // If connection was successful, try to read content of the Web page and display it on screen
            String htmlText;
            htmlText = http.getString();
            display.setTextSize(1); // Set smaller text size, so everything can fit on screen
            display.clearDisplay();
            display.setCursor(0, 0);
            display.print(htmlText);
            display.display();
        }
    }
}

void loop()
{
    // Nothing
}
```

<CenteredImage src="/img/6/get.jpg" alt="GET request" width="500px" caption="GET request" />

<FunctionDocumentation
    functionName="WiFi.begin()"
    description="This function attempts to connect to WiFi"
    returnDescription="Returns wl_status_t enum value"
    returnType="wl_status_t"
    parameters={[  
        {type: 'const char*', name:'ssid', description:'Network SSID.' },
        {type: 'const char*', name:'passphrase', description:'Optional, depends on WiFi network security certificate' },
    ]}
/>

<FunctionDocumentation
  functionName="http.begin()"
  description="This function attempts to open a HTTP communication to given url"
  returnDescription="Returns true if communication is successful, otherwise returns false."
  returnType="bool"
  parameters={[  
    { type: 'String', name: 'url', description: 'Url of the specified website' },
  ]}
/>

<FunctionDocumentation
  functionName="http.GET()"
  description="This function handles GET requests."
  returnDescription="Returns the size of available data"
  returnType="int"
/>
---

## POST request

To send data from Inkplate to a web server, you can use the built-in `WiFiClient` class. Let's use [**webhook.site**](https://webhook.site), which is an excellent resource for testing POST and GET requests. Visiting the site gives you a unique URL to send POST requests to, and the requests then show up live on the page:

```cpp
// Include needed libraries
#include "Inkplate.h"
#include "WiFi.h"

// Create objects
Inkplate display(INKPLATE_1BIT);
WiFiClient client;

// Interval between POST requests (seconds)
#define POSTING_INTERVAL_IN_SECS 20

// WiFi credentials
const char *ssid = "";
const char *pass = "";

// Webhook.site settings
const char *server = "webhook.site";
const char *WEBHOOK_PATH = "/YOUR-UNIQUE-WEBHOOK-ID"; // e.g. "/abcd-1234-efgh"

// Last connection time
unsigned long lastConnectionTime = 0;

void setup()
{
    Serial.begin(115200);

    // Init Inkplate
    display.begin();
    display.clearDisplay();
    display.setTextColor(BLACK, WHITE);
    display.setTextSize(6);

    display.printf("HTTP POST example\n\n");
    display.printf("Using webhook.site\n\n");
    display.printf("Open Serial Monitor\nat 115200 baud");
    display.display();

    // Connect to WiFi
    WiFi.mode(WIFI_MODE_STA);
    WiFi.begin(ssid, pass);

    Serial.print("Connecting to WiFi");
    while (WiFi.status() != WL_CONNECTED)
    {
        delay(500);
        Serial.print(".");
    }

    Serial.println();
    Serial.print("Connected, IP address: ");
    Serial.println(WiFi.localIP());
}

void loop()
{
    if ((unsigned long)(millis() - lastConnectionTime) > POSTING_INTERVAL_IN_SECS * 1000UL)
    {
        display.clearDisplay();

        if (!client.connect(server, 80))
        {
            Serial.println("Connection failed");
            lastConnectionTime = millis();
            client.stop();
            return;
        }

        // Example data (replace with sensor readings if needed)
        int value = random(40);

        // URL-encoded POST body
        String data = "value=" + String(value);

        // Send HTTP POST request
        client.print(String("POST ") + WEBHOOK_PATH + " HTTP/1.1\r\n");
        client.print(String("Host: ") + server + "\r\n");
        client.println("Connection: close");
        client.println("User-Agent: Inkplate-ESP32");
        client.println("Content-Type: application/x-www-form-urlencoded");
        client.print("Content-Length: ");
        client.println(data.length());
        client.println();
        client.print(data);

        Serial.print("POST sent: ");
        Serial.println(data);

        lastConnectionTime = millis();
        delay(250);

        client.stop();
    }
}
```

<FunctionDocumentation
  functionName="WiFi.mode()"
  description="This function sets the MCU WiFi chip as STA or AP."
  returnType="bool"
  parameters={[  
    { type: 'wifi_mode_t', name: 'mode', description: 'WiFi mode value, can be either WIFI_MODE_STA or WIFI_MODE_AP' },
  ]}
/>

<FunctionDocumentation
    functionName="WiFi.begin()"
    description="This function attempts to connect to WiFi"
    returnDescription="Returns wl_status_t enum value"
    returnType="wl_status_t"
    parameters={[  
        {type: 'const char*', name:'ssid', description:'Network SSID.' },
        {type: 'const char*', name:'passphrase', description:'Optional, depends on WiFi network security certificate' },
    ]}
/>

<FunctionDocumentation
  functionName="http.begin()"
  description="This function attempts to open a HTTP communication to given url"
  returnDescription="Returns true if communication is successful, otherwise returns false."
  returnType="bool"
  parameters={[  
    { type: 'String', name: 'url', description: 'Url of the specified website' },
  ]}
/>