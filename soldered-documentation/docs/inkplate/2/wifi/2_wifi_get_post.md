---  
slug: /inkplate/2/wifi/get-post  
title: Inkplate 2 – GET & POST requests
id: 2-wifi-get-post  
hide_title: true  
---  

<SectionTitle title="GET & POST Requests" backgroundImage="/img/inkplate_2/hardware.png" />

Now that Inkplate is connected to the internet, you will likely want to send and receive data on it from sensors, messages, or your custom APIs. This page contains examples of how to send and receive data on Inkplate via the internet:

---

## GET request

Using `client.GET()` will enable you to easily download and handle data on Inkplate however you want. Here is an example of how to GET a .html file and print it on Inkplate:

```cpp
/*
    Inkplate2_HTTP_Request example for Soldered Inkplate 2
    For this example you will need USB cable, Inkplate 2 and stable WiFi Internet connection
    Select "Soldered Inkplate2" from Tools -> Board menu.
    Don't have "Soldered Inkplate2" option? Follow our tutorial and add it:
    https://soldered.com/learn/add-inkplate-6-board-definition-to-arduino-ide/

    This example will show you how to connect to a WiFi network, get data from the Internet and display that data on the e-paper.
    This example is NOT about how to parse HTML data from the Internet - it will just print HTML on the screen.

    In quotation marks you will need to write your WiFi SSID and WiFi password in order to connect to your WiFi network.

    Want to learn more about Inkplate? Visit www.inkplate.io
    Looking to get support? Write on our forums: https://forum.soldered.com/
    30 March 2022 by Soldered
*/

// Next 3 lines are a precaution, you can ignore those, and the example would also work without them
#ifndef ARDUINO_INKPLATE2
#error "Wrong board selection for this example, please select Soldered Inkplate2 in the boards menu."
#endif

#include "Inkplate.h"   //Include Inkplate library to the sketch
#include <HTTPClient.h> //Include HTTP library to this sketch
#include <WiFi.h>       //Include ESP32 WiFi library to our sketch

const char ssid[] = ""; // Your WiFi SSID
const char pass[] = ""; // Your WiFi password

Inkplate display; // Create an object on Inkplate library

void setup()
{
    Serial.begin(115200);    // Initialize serial communication with PC
    display.begin();         // Init Inkplate library (you should call this function ONLY ONCE)
    display.clearDisplay();  // Clear frame buffer of display
    display.setCursor(0, 0); // Set print position
    display.setTextColor(INKPLATE2_BLACK, INKPLATE2_WHITE); // Set text color to black and background color to white
    display.println("Scanning for WiFi networks...");       // Write text
    display.display();                                      // Send everything to display (refresh display)

    int n =
        WiFi.scanNetworks(); // Start searching WiFi networks and put the number of found WiFi networks in variable n
    Serial.println("Scanning networks");
    display.setCursor(0, 0); // Set print position
    if (n == 0)
    {
        // If you did not find any network, show the message and stop the program.
        display.print("No WiFi networks found!");
        display.display();
        while (true)
            ;
    }
    else
    {
        if (n > 10)
            n = 10; // If you did find, print name (SSID), encryption and signal strength of first 10 networks
        for (int i = 0; i < n; i++)
        {
            display.setTextColor(INKPLATE2_BLACK,
                                 INKPLATE2_WHITE); // Set text color to black and background color to white
            display.print(WiFi.SSID(i));
            display.print((WiFi.encryptionType(i) == WIFI_AUTH_OPEN) ? 'O' : '*');
            display.print(' ');
            display.setTextColor(INKPLATE2_RED, INKPLATE2_WHITE); // Set text color to red and background color to white
            display.println(WiFi.RSSI(i), DEC);
        }
        display.display(); // Refresh screen
    }

    display.clearDisplay();          // Clear everything in frame buffer
    display.setCursor(0, 0);         // Set print cursor to new position
    display.print("Connecting to "); // Print the name of WiFi network
    display.print(ssid);
    WiFi.begin(ssid, pass); // Try to connect to WiFi network
    Serial.println("Connecting to WiFi");
    while (WiFi.status() != WL_CONNECTED)
    {
        Serial.print(".");
        delay(
            1000); // While it is connecting to network, display dot every second, just to know that Inkplate is alive.
    }
    Serial.println("Connected!");

    char *webData;
    webData = (char *)ps_malloc(100000); // Allocate array for the stream of data
    if (webData != NULL)
    {
        HTTPClient http;
        int m = 0;
        if (http.begin("http://example.com/index.html"))
        {
            // Now try to connect to some web page (in this example www.example.com. And yes, this is a valid Web page
            // :))
            if (http.GET() == 200)
            {
                // If connection was successful, try to read content of the Web page and display it on screen
                while (http.getStream().available()) // If data available store data in data variable
                {
                    webData[m++] = http.getStream().read();
                }
                display.clearDisplay();
                display.setCursor(0, 0);
                display.setTextColor(INKPLATE2_RED, INKPLATE2_WHITE);
                display.print(webData);
                Serial.print(webData);
                display.display();
            }
        }
        free(webData); // Free allocated memory
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

To send data from Inkplate to a web server, you can use the same built-in `WiFiClient` class. Let's use [**ThingSpeak.com**](https://thingspeak.mathworks.com/), which is a great resource for testing POST and GET requests. By visiting the site, you get a unique URL to which a POST request from Inkplate can be sent and that data will then be visible on the site:

```cpp
/*
   Inkplate2_HTTP_POST_Request example for Soldered Inkplate2
   For this example you will need USB cable, Inkplate2 and stable WiFi Internet connection.
   Select "Soldered Inkplate2" from Tools -> Board menu.
   Don't have "Soldered Inkplate2" option? Follow our tutorial and add it:
   https://soldered.com/learn/add-inkplate-6-board-definition-to-arduino-ide/

   This example will show you how to connect to a WiFi network and send a POST request via HTTP.
   We will use ThingSpeak API to see post requests. It's a free API that allows you to store and retrieve data using
   HTTP.
   1. Go to ThingSpeak.com and create a free account.
   2. Open the Channels tab.
   3. Create a new channel.
   4. Create fields you want to use.
   5. Open the channel, go to the API Keys tab and copy your Write API Key.
   6. Enter your API key in the code below.

   When you send a POST request, open your channel and you will see the graph with your sent data.

   Want to learn more about Inkplate? Visit www.inkplate.io
   Looking to get support? Write on our forums: https://forum.soldered.com/
   26 January 2023 by Soldered
*/

// Next 3 lines are a precaution, you can ignore those, and the example would also work without them
#ifndef ARDUINO_INKPLATE2
#error "Wrong board selection for this example, please select Soldered Inkplate2 in the boards menu."
#endif

// Include needed libraries
#include "Inkplate.h"
#include "WiFi.h"

// Create objects from included libraries
Inkplate display;
WiFiClient client;

// Here you can change the interval of sending POST requests
#define POSTING_INTERVAL_IN_SECS 10

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
    // Init serial communication
    Serial.begin(115200);

    // Init Inkplate library (you should call this function ONLY ONCE)
    display.begin();

    // Clear frame buffer of display
    display.clearDisplay();

    // Set text color and size
    display.setTextColor(BLACK, WHITE);
    display.setTextSize(1);

    // Display a message
    display.printf("HTTP POST request example\n\n");
    display.printf("Open Serial Monitor at \n115200 baud rate to see \nwhat's happening");
    display.display();

    // Connect to the WiFi network
    WiFi.mode(WIFI_MODE_STA);
    WiFi.begin(ssid, pass);
    Serial.print("Connecting to Wifi ");
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
    if (millis() - lastConnectionTime > POSTING_INTERVAL_IN_SECS * 1000LL)
    {
        // Clear frame buffer of display
        display.clearDisplay();

        // Connect the WiFi client to the server via port 80
        if (!client.connect(server, 80))
        {
            // If it fails, print a message, remember time, stop the client and reset the loop
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
            String data = "field1=" + String(field1Data); // shows how to include additional field data in http post

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

                Serial.println("The POST request is done.");
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