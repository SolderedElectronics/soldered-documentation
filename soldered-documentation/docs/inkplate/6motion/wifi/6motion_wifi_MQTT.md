---
slug: /inkplate/6motion/wifi/MQTT
title: MQTT
id: 6motion-wifi-mqtt
---

Using **MQTT** on Inkplate 6 MOTION allows sending and receiving messages over the network using the lightweight MQTT protocol, commonly used for IoT applications. The following sections explain how to connect to an MQTT broker, subscribe to topics, and send or receive messages.

---

## Connecting and subscribing to a topic

To establish an MQTT connection, first initialize the MQTT library with `mqtt.begin()`, set the MQTT server using `mqtt.setServer()`, and attempt to connect with `mqtt.connect()`. Once connected, subscribe to a topic using `mqtt.subscribe()`.

<WarningBox>Make sure the Inkplate 6 MOTION is connected to a **Wi-Fi network** before attempting to use MQTT.</WarningBox>

```cpp
// Initialize the MQTT library and set the internal buffer for RX messages
mqtt.begin(48);

// Set the MQTT broker information
mqtt.setServer("test.mosquitto.org", 1883);

// Attempt to connect to the MQTT broker
inkplate.print("Connecting to the MQTT broker...");
inkplate.partialUpdate(true);
if (!mqtt.connect())
{
    inkplate.println("Connect failed!");
    inkplate.partialUpdate(false);

    // Stop execution if the connection fails
    while (1);
}
inkplate.println("Connected!");
inkplate.partialUpdate(true);

// Subscribe to a topic
inkplate.print("Subscribing to ");
inkplate.print("solderedTest/solderedDasduino");
inkplate.print(" topic...");
inkplate.partialUpdate(true);
if (!mqtt.subscribe((char *)"solderedTest/solderedDasduino"))
{
    inkplate.print("failed!");
    inkplate.partialUpdate(false);

    // Stop execution if subscription fails
    while (1);
}
inkplate.println("Subscribed!\r\n");
inkplate.partialUpdate(true);
```

<FunctionDocumentation functionName="mqtt.begin()" 
  description="Initializes the MQTT library and allocates memory for incoming messages." 
  returnDescription="Returns true if memory allocation was successful, false otherwise."
  parameters={[ 
    { type: 'uint16_t', name: 'bufferSize', description: "Size of the allocated buffer (in bytes) for storing incoming MQTT messages." } 
  ]} 
/>

<FunctionDocumentation functionName="mqtt.begin()" 
  description="Initializes the MQTT library using a user-defined buffer for incoming messages." 
  returnDescription="Returns true if the user-defined buffer was accepted, false otherwise."
  parameters={[ 
    { type: 'uint8_t*', name: 'buffer', description: "Pointer to a user-defined buffer for storing incoming messages." },
    { type: 'uint16_t', name: 'bufferSize', description: "Size of the user-defined buffer (in bytes)." }
  ]} 
/>

<FunctionDocumentation functionName="mqtt.setServer()" 
  description="Configures the MQTT broker's hostname/IP and port. This does not immediately establish a connection." 
  returnDescription="Returns true if the server details were set successfully, false otherwise."
  parameters={[ 
    { type: 'char*', name: 'server', description: "MQTT broker's domain name or IP address." }, 
    { type: 'uint16_t', name: 'port', description: "MQTT broker's port (typically 1883 for unencrypted communication)." } 
  ]} 
/>

<FunctionDocumentation functionName="mqtt.connect()" 
  description="Attempts to establish a connection to the MQTT broker with optional authentication." 
  returnDescription="Returns true if the connection was successful, false otherwise."
  parameters={[ 
    { type: 'char*', name: 'clientId', description: "Optional MQTT Client ID. Use NULL if not required." }, 
    { type: 'char*', name: 'username', description: "Optional username for authentication. Use NULL if not required." }, 
    { type: 'char*', name: 'password', description: "Optional password for authentication. Use NULL if not required." } 
  ]} 
/>

<FunctionDocumentation functionName="mqtt.subscribe()" 
  description="Subscribes to a specified MQTT topic to receive messages." 
  returnDescription="Returns true if subscription was successful, false otherwise."
  parameters={[ 
    { type: 'const char*', name: 'topic', description: "The name of the topic to subscribe to." } 
  ]} 
/>

<FunctionDocumentation functionName="mqtt.unsubscribe()" 
  description="Unsubscribes from a specified MQTT topic to stop receiving messages." 
  returnDescription="Returns true if unsubscription was successful, false otherwise."
  parameters={[ 
    { type: 'char*', name: 'topic', description: "The name of the topic to unsubscribe from." } 
  ]} 
/>

---

## Sending and receiving messages

Once connected and subscribed, messages can be published using mqtt.publish(), and received by checking mqtt.available().

```cpp
// Check if a new message is available on the subscribed topic
int mqttData = mqtt.available();
if (mqttData)
{
    inkplate.print("Topic: ");
    inkplate.print(mqtt.topic());
    inkplate.print(", Payload: ");
    
    // Read and print the received message
    for (int i = 0; i < mqttData; i++)
    {
        inkplate.print(mqtt.read());
    }
    inkplate.println();
    inkplate.partialUpdate(false);
}

// Publish a message when the WAKE button is pressed
if (checkButton(PC13, &publishBtnOldState, LOW))
{
    char message[40];
    sprintf(message, "inkplate_%lu", millis());

    inkplate.print("Publish \"");
    inkplate.print(message);
    inkplate.print("\" ");
    
    if (mqtt.publish((char *)mqttTopicTx, message, 0, true))
    {
        inkplate.println("ok");
    }
    else
    {
        inkplate.println("failed");
    }
    inkplate.partialUpdate(false);
}
```

<FunctionDocumentation functionName="mqtt.available()" 
  description="Checks if a new MQTT message is available on the subscribed topic." 
  returnDescription="Returns the length of the available message in bytes, or 0 if no message is available."
/>

<FunctionDocumentation functionName="mqtt.publish()" 
  description="Publishes a message to a specified MQTT topic." 
  returnDescription="Returns true if the message was published successfully, false otherwise."
  parameters={[ 
    { type: 'char*', name: 'topic', description: "The topic to publish the message to." }, 
    { type: 'char*', name: 'payload', description: "The message content to be sent." }, 
    { type: 'uint16_t', name: 'length', description: "Length of the message. If the message is a null-terminated string, set this to 0." }, 
    { type: 'bool', name: 'retain', description: "If true, the broker retains the message for future subscribers." } 
  ]} 
/>

<FunctionDocumentation functionName="mqtt.read()" 
  description="Reads the next byte from the received MQTT message." 
  returnDescription="Returns the next byte of the message as an integer, or 0 if no data is available."
/>

<FunctionDocumentation functionName="mqtt.read()" 
  description="Reads a specified number of bytes from an incoming MQTT message into a user-defined buffer." 
  returnDescription="Returns the number of bytes actually stored in the buffer."
  parameters={[ 
    { type: 'uint8_t*', name: 'buffer', description: "Pointer to the buffer where the received message will be stored." }, 
    { type: 'uint16_t', name: 'length', description: "Maximum number of bytes to store in the buffer." } 
  ]} 
/>

<FunctionDocumentation functionName="mqtt.disconnect()" 
  description="Disconnects from the MQTT broker and cleans up resources." 
  returnDescription="Returns true if disconnection was successful, false otherwise."
/>

<FunctionDocumentation functionName="mqtt.connected()" 
  description="Checks if the Inkplate is currently connected to an MQTT broker." 
  returnDescription="Returns true if connected, false otherwise."
/>

<FunctionDocumentation functionName="mqtt.reconnect()" 
  description="Enables or disables automatic reconnection in case of a dropped connection." 
  parameters={[ 
    { type: 'uint8_t', name: 'mode', description: "Set to 1 to enable automatic reconnect, 0 to disable it." } 
  ]} 
/>

<FunctionDocumentation functionName="mqtt.topic()" 
  description="Retrieves the topic of the most recently received MQTT message." 
  returnDescription="Returns a pointer to the string containing the topic name."
/>


<FunctionDocumentation functionName="mqtt.setQoS()" 
  description="Sets the Quality of Service (QoS) level for MQTT message delivery." 
  parameters={[ 
    { type: 'int', name: 'qos', description: "QoS level: 0 (at most once), 1 (at least once), or 2 (exactly once)." } 
  ]} 
/>

<FunctionDocumentation functionName="mqtt.loop()" 
  description="Checks for new incoming MQTT messages and processes them. This function should be called frequently." 
/>

---

## Full example

For a complete MQTT implementation, including connecting, subscribing, publishing, and receiving messages, see the full example:

<QuickLink 
  title="Inkplate_6_Motion_WiFi_MQTT.ino" 
  description="Full example on how to init, subscribe, unsubscribe, transmit and recieve data via MQTT"
  url="https://github.com/SolderedElectronics/Inkplate_Motion_Arduino_Library/blob/main/examples/Inkplate6Motion/Advanced/Web_WiFi/Inkplate_6_Motion_WiFi_MQTT/Inkplate_6_Motion_WiFi_MQTT.ino" 
/>
