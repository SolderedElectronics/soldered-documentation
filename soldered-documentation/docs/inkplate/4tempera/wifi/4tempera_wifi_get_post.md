---
slug: /inkplate/4tempera/wifi/get-post
title: Inkplate 4TEMPERA – GET & POST requests
sidebar_label: GET & POST requests
id: 4tempera-wifi-get-post
hide_title: true
---

<SectionTitle title="GET & POST Requests" backgroundImage="/img/inkplate_2/hardware.png" />

Now that Inkplate is connected to the internet, you will likely want to send and receive data from sensors, messages, and your custom APIs. This page contains examples of how to send and receive data on Inkplate via the internet:

---

## GET request

Using `client.GET()` enables you to easily download and handle data on Inkplate as you wish. Here is an example of how to GET an HTML file and print it on Inkplate:

```cpp
#include "Inkplate.h"   // Include Inkplate library to the sketch
#include <HTTPClient.h> // Include HTTP library to this sketch
#include <WiFi.h>       // Include ESP32 WiFi library to our sketch

#define ssid "yourssid" // Name of the WiFi network (SSID) that you want to connect Inkplate to
#define pass "yourpassword" // Password of that WiFi network

Inkplate inkplate(INKPLATE_1BIT); // Create an object from the Inkplate library and also set the library into 1 Bit mode (BW)

void setup()
{
    inkplate.begin();                                  // Initialize Inkplate library (you should call this function ONLY ONCE)
    inkplate.clearDisplay();                           // Clear frame buffer of display
    inkplate.display();                                // Put clear image on Inkplate
    inkplate.setTextSize(2);                           // Set text scaling to two (text will be two times bigger)
    inkplate.setCursor(0, 0);                          // Set print position
    inkplate.setTextColor(BLACK, WHITE);               // Set text color to black and background color to white
    inkplate.println("Scanning for WiFi networks..."); // Write text
    inkplate.display();                                // Send everything to Inkplate (refresh Inkplate)

    int n = WiFi.scanNetworks(); // Start searching for WiFi networks and store the number of found networks in variable n
    if (n == 0)
    { // If you did not find any network, show the message and stop the program.
        inkplate.print("No WiFi networks found!");
        inkplate.partialUpdate();
        while (true)
            ;
    }
    else
    {
        if (n > 10)
            n = 10; // If networks are found, print name (SSID), encryption, and signal strength of the first 10 networks
        for (int i = 0; i < n; i++)
        {
            inkplate.print(WiFi.SSID(i));
            inkplate.print((WiFi.encryptionType(i) == WIFI_AUTH_OPEN) ? 'O' : '*');
            inkplate.print('\n');
            inkplate.print(WiFi.RSSI(i), DEC);
        }
        inkplate.partialUpdate(); // (Partial) refresh the screen
    }

    inkplate.clearDisplay();          // Clear everything in the frame buffer
    inkplate.setCursor(0, 0);         // Set print cursor to new position
    inkplate.print("Connecting to "); // Print the name of the WiFi network
    inkplate.print(ssid);
    WiFi.begin(ssid, pass); // Try to connect to the WiFi network
    while (WiFi.status() != WL_CONNECTED)
    {
        delay(1000); // While connecting to the network, Inkplate prints a dot every second to show that it is active.
        inkplate.print('.');
        inkplate.partialUpdate();
    }
    inkplate.print("connected"); // If it's connected, notify the user
    inkplate.partialUpdate();

    HTTPClient http;
    if (http.begin("http://example.com/index.html"))
    { // Now try to connect to some web page (in this example www.example.com. And yes, this is a valid web page.)
        if (http.GET() > 0)
        { // If connection was successful, try to read the content of the web page and print it on the screen
            String htmlText;
            htmlText = http.getString();
            inkplate.setTextSize(1); // Set smaller text size, so everything can fit on the screen
            inkplate.clearDisplay();
            inkplate.setCursor(0, 0);
            inkplate.print(htmlText);
            inkplate.display();
        }
    }
    else{
        
    }
}

void loop()
{
    // Nothing
}
```

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
  description="This function attempts to open an HTTP communication to a given URL"
  returnDescription="Returns true if communication is successful, otherwise returns false."
  returnType="bool"
  parameters={[ 
    { type: 'String', name: 'url', description: 'URL of the specified website' },
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

To send data from Inkplate to a web server, you can use the same built-in `WiFiClient` class. Let's use [**ThingSpeak.com**](https://thingspeak.mathworks.com/), which is a great resource for testing POST and GET requests. By visiting the site, you get a unique URL to which you can send a POST request from Inkplate, and the data will then be visible on the site:

```cpp
/*
   This example will show you how to connect to a WiFi network and send a POST request via HTTP.
   We will use the ThingSpeak API to view POST requests. It's a free API that allows you to store and retrieve data using HTTP.
   1. Go to ThingSpeak.com and create a free account.
   2. Open the Channels tab.
   3. Create a new channel.
   4. Create the fields you want to use (this example uses one field called field1, and this name must be used when sending data).
   5. Open the channel, go to the API Keys tab, and copy your Write API Key.
   6. Enter your API key in the code below.

   When you send a POST request, open your channel and you will see the graph displaying your sent data.
*/

// Include needed libraries
#include "Inkplate.h"
#include "WiFi.h"

// Create objects from included libraries
Inkplate display(INKPLATE_1BIT);
WiFiClient client;

// Here you can change the interval for sending POST requests (minimum 15 seconds with a free license)
#define POSTING_INTERVAL_IN_SECS 20

// Enter your WiFi credentials
const char *ssid = "";
const char *pass = "";

// ThingSpeak settings
char *server = "api.thingspeak.com";
String writeAPIKey = ""; // Enter your Write API Key

// Variable that holds last connection time
unsigned long lastConnectionTime = 0;


void setup()
{
    // Initialize serial communication
    Serial.begin(115200);

    // Initialize Inkplate library (you should call this function ONLY ONCE)
    display.begin();

    // Clear frame buffer of display
    display.clearDisplay();

    // Set text color and size
    display.setTextColor(BLACK, WHITE);
    display.setTextSize(6);

    // Display a message
    display.printf("HTTP POST request example\n\n");
    display.printf("Open Serial Monitor at \n115200 baud rate to see \nwhat's happening");
    display.display();

    // Connect to the WiFi network
    WiFi.mode(WIFI_MODE_STA);
    WiFi.begin(ssid, pass);
    Serial.print("Connecting to WiFi ");
    while (WiFi.status() != WL_CONNECTED)
    {
        delay(500);
        Serial.print(".");
    }
    Serial.println();
    Serial.print("Connected to WiFi network with IP Address: ");
    Serial.println(WiFi.localIP());
}


void loop()
{
    // Every POSTING_INTERVAL_IN_SECS seconds make the POST request
    if ((unsigned long)(millis() - lastConnectionTime) > POSTING_INTERVAL_IN_SECS * 1000LL)
    {
        // Clear frame buffer of display
        display.clearDisplay();

        // Connect the WiFi client to the server via port 80
        if (!client.connect(server, 80))
        {
            // If it fails, print a message, record the time, stop the client, and reset the loop
            Serial.println("Connection failed");
            lastConnectionTime = millis();
            client.stop();
            return;
        }
        else
        {
            // If you have any sensor or something else, here you have to put data to send instead of a random number
            int field1Data = random(40);

            // Create data string to send to ThingSpeak
            String data = "field1=" + String(field1Data); // shows how to include additional field data in an HTTP POST

            // POST data to ThingSpeak
            if (client.connect(server, 80))
            {
                client.println("POST /update HTTP/1.1");
                client.println("Host: api.thingspeak.com");
                client.println("Connection: close");
                client.println("User-Agent: ESP32WiFi/1.1");
                client.println("X-THINGSPEAKAPIKEY: " + writeAPIKey);
                client.println("Content-Type: application/x-www-form-urlencoded");
                client.print("Content-Length: ");
                client.print(data.length());
                client.print("\n\n");
                client.print(data);

                Serial.print("The POST request is done: ");
                Serial.println(data);
                lastConnectionTime = millis();
                delay(250);
            }
        }
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
  description="This function attempts to open an HTTP communication to a given URL"
  returnDescription="Returns true if communication is successful, otherwise returns false."
  returnType="bool"
  parameters={[ 
    { type: 'String', name: 'url', description: 'URL of the specified website' },
  ]}
/>

## Full example

To see more details, check out our full examples:
<QuickLink 
  title="Inkplate4TEMPERA_HTTP_GET_Request.ino" 
  description="Inkplate 4TEMPERA WiFi GET request example from the Inkplate library"
  url="https://github.com/SolderedElectronics/Inkplate-Arduino-library/blob/master/examples/Inkplate4TEMPERA/Advanced/WEB_WiFi/Inkplate4TEMPERA_HTTP_Request/Inkplate4TEMPERA_HTTP_Request.ino" 
/>

<QuickLink 
  title="Inkplate4TEMPERA_HTTP_POST_Request.ino" 
  description="Inkplate 4TEMPERA WiFi POST request example from the Inkplate library"
  url="https://github.com/SolderedElectronics/Inkplate-Arduino-library/blob/master/examples/Inkplate4TEMPERA/Advanced/WEB_WiFi/Inkplate4TEMPERA_HTTP_POST_Request/Inkplate4TEMPERA_HTTP_POST_Request.ino" 
/>