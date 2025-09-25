---
slug: /inkplate/6color/micropython/wifi/requests
title: Inkplate 6COLOR – GET & POST requests
sidebar_label: GET & POST requests
id: get-post-request
hide_title: false
---

Now that your Inkplate has internet access, you can use it to exchange information/data with sensors, custom services or your APIs. Below are examples showing how to receive and send data over the internet with Inkplate.

## GET Request

Use `HTTP GET` request to easily download and handle data on your Inkplate. This example shows how to use GET for `.html` file and print it on Inkplate.

```python
# Include needed libraries
from inkplate6COLOR import Inkplate
import network
import socket
import time

# WiFi credentials
SSID = "YOUR_SSID_HERE"
PASSWORD = "YOU_PASSWORD_HERE"

# Connect to WiFi network
def do_connect():
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print("connecting to network...")
        sta_if.active(True)
        sta_if.connect(ssid, password)
        while not sta_if.isconnected():
            pass
    print("network config:", sta_if.ifconfig())

# This function does a HTTP GET request
# More info here: https://docs.micropython.org/en/latest/esp8266/tutorial/network_tcp.html
def http_get(url):
    res = ""
    _, _, host, path = url.split("/", 3)
    addr = socket.getaddrinfo(host, 80)[0][-1]
    s = socket.socket()
    s.connect(addr)
    s.send(bytes("GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n" % (path, host), "utf8"))
    while True:
        data = s.recv(100)
        if data:
            res += str(data, "utf8")
        else:
            break
    s.close()
    return res

# First, connect
do_connect()

# Do a GET request to the webhook platform
# Change the url to do GET request to a different page
response = http_get("http://webhook.site/c8c5e570-639e-47bd-860a-e4343b8e9d85")

# Remove the header part from response so that we only print HTML part
parts = response.split("\r\n\r\n", 1)
if len(parts) > 1:
    html = parts[1]
else:
    html = response

# Create and initialize inkplate object
inkplate = Inkplate()
inkplate.begin()

# Set text size to double from the original size, so we can see the text better
inkplate.setTextSize(1)

# Print response line by line
inkplate.print(html)

# Display content from buffer
inkplate.display()
```

<CenteredImage src="/img/6color/get-request.jpg" alt="GET Request example" caption="Expected HTML output on display"/> 

## POST Request

To send data from Inkplate to a web server we'll use **[ThingSpeak.com](https://thingspeak.mathworks.com)**, which is a great free online IoT platform. To send data to ThingSpeak with a **POST request**, you need your channel's **Write API Key**. You can find this key under **Channels** tab in your account, opening the channel you created, and checking under the **API Keys** section. This key is used in your request when sending data.

```python
from inkplate6COLOR import Inkplate
import network
import socket

# Replace with your credentials
ssid = ""
password = ""

# ThingSpeak Write API key
API_KEY = ""

# Initialize Inkplate
inkplate = Inkplate()
inkplate.begin()

# Connect to WiFi network
def do_connect():
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print("Connecting to network...")
        sta_if.active(True)
        sta_if.connect(ssid, password)
        while not sta_if.isconnected():
            pass
    print("Network config:", sta_if.ifconfig())

# Function to sent HTTP Post request
def http_post(url, data, host):
    addr = socket.getaddrinfo(host, 80)[0][-1] # 
    s = socket.socket()                        # Create a TCP socket
    s.connect(addr)                            # Connect to server (ThingSpeak)

    # Build HTTP POST request
    request = (
        "POST /update HTTP/1.1\r\n"                            # Method (POST), path (/update), protocol (HTTP/1.1)
        "Host: " + host + "\r\n"                               # Specify host
        "Content-Type: application/x-www-form-urlencoded\r\n"  # Data format to send
        "Content-Length: " + str(len(data)) + "\r\n"           # Content lenght
        "Connection: close\r\n\r\n" +                          # Close connection after response + end of header
        data                                                   # The actual data
    )

    s.send(bytes(request, "utf8")) # Send full HTTP request
    res = ""
    while True:
        buf = s.recv(100) # Read server response
        if not buf:
            break
        res += str(buf, "utf8")

    s.close() # Close the socket
    return res # Return server Response

# Connect to WiFi
do_connect()

# Example: update field1 with value 125
payload = "api_key={}&field1={}".format(API_KEY, 125)

response = http_post("http://api.thingspeak.com/update", payload, "api.thingspeak.com")

# Display HTTP response data
inkplate.print(response)
inkplate.display()
```

<CenteredImage src="/img/6color/post-request.jpg" alt="POST example" caption="Expected HTTP response output on display" />