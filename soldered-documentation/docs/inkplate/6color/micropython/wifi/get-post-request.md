---
slug: /inkplate/6color/micropython/wifi/requests
title: Inkplate 6COLOR – GET & POST Request
sidebar_label: GET & POST Request
id: get-post-request
hide_title: false
---

Now that your Inkplate has internet access, you can use it to exchange information/data with sensors, custom services or your APIs. Below are examples showing how to receive and send data over the internet with Inkplate.

## GET request

Use `HTTP GET` request to easily download and handle data on your Inkplate. This example shows how to use GET for `.html` file and print it on Inkplate.

```python
# Include needed libraries
from inkplate6_color import Inkplate
import network
import socket
import time

# WiFi credentials
SSID = "YOUR_SSID_HERE"
PASSWORD = "YOU_PASSWORD_HERE"

# Connect to WiFi network
def do_connect():
    connected = False
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print("Connecting to network...")
        sta_if.active(True)
        try:
            sta_if.connect(SSID, PASSWORD)
        except Exception as e:
            print(f"Wi-Fi connect error: {e}\n")
            print("Check your credentials!")
        else:
            timeout = 30  # seconds
            start = time.ticks_ms()

            while not sta_if.isconnected():
                if time.ticks_diff(time.ticks_ms(), start) > timeout * 1000:
                    print("Failed to connect within timeout")
                    break
                time.sleep(0.5)
            else:
                connected = True
    else:
        connected = True

    if connected:
        print(f"CONNECTED: \n{sta_if.ifconfig()}")
        return True
    else:
        return False

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

# Connect to WiFi
if not do_connect():
    raise SystemExit("WiFi connection failed")

# Do a GET request to the webhook platform
# Replace this with your own webhook.site URL, or point it at any page you like
response = http_get("http://webhook.site/YOUR-UNIQUE-WEBHOOK-ID")

# Remove the header part from response so that we only print HTML part
parts = response.split("\r\n\r\n", 1)
if len(parts) > 1:
    html = parts[1]
else:
    html = response

# Create and initialize inkplate object
inkplate = Inkplate()
inkplate.begin()

# Keep the text at its original size so more of the page fits on screen
inkplate.set_text_size(1)

# Print response line by line
inkplate.print(html)

# Display content from buffer
inkplate.display()
```

<CenteredImage src="/img/6color/get-request.jpg" alt="GET Request example" caption="Expected HTML output on display"/> 

## POST request

To send data from Inkplate to a web server we'll use **[ThingSpeak.com](https://thingspeak.mathworks.com)**, which is a great free online IoT platform. To send data to ThingSpeak with a **POST request**, you need your channel's **Write API Key**. You can find this key under **Channels** tab in your account, opening the channel you created, and checking under the **API Keys** section. This key is used in your request when sending data.

```python
from inkplate6_color import Inkplate
import network
import socket
import time

# Replace with your credentials
SSID = ""
PASSWORD = ""

# ThingSpeak Write API key
API_KEY = ""

# Initialize Inkplate
inkplate = Inkplate()
inkplate.begin()

def do_connect():
    connected = False
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print("Connecting to network...")
        sta_if.active(True)
        try:
            sta_if.connect(SSID, PASSWORD)
        except Exception as e:
            print(f"Wi-Fi connect error: {e}\n")
            print("Check your credentials!")
        else:
            timeout = 30  # seconds
            start = time.ticks_ms()

            while not sta_if.isconnected():
                if time.ticks_diff(time.ticks_ms(), start) > timeout * 1000:
                    print("Failed to connect within timeout")
                    break
                time.sleep(0.5)
            else:
                connected = True
    else:
        connected = True

    if connected:
        print(f"CONNECTED: \n{sta_if.ifconfig()}")
        return True
    else:
        return False

# Function to sent HTTP Post request
def http_post(url, data, host):
    addr = socket.getaddrinfo(host, 80)[0][-1]
    s = socket.socket()                        # Create a TCP socket
    s.connect(addr)                            # Connect to server (ThingSpeak)

    # Build HTTP POST request
    request = (
        "POST /update HTTP/1.1\r\n"                            # Method (POST), path (/update), protocol (HTTP/1.1)
        "Host: " + host + "\r\n"                               # Specify host
        "Content-Type: application/x-www-form-urlencoded\r\n"  # Data format to send
        "Content-Length: " + str(len(data)) + "\r\n"           # Content length
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
if not do_connect():
    raise SystemExit("WiFi connection failed")

# Example: update field1 with value 125
payload = "api_key={}&field1={}".format(API_KEY, 125)

response = http_post("http://api.thingspeak.com/update", payload, "api.thingspeak.com")

# Display HTTP response data
inkplate.print(response)
inkplate.display()
```

<CenteredImage src="/img/6color/post-request.jpg" alt="POST example" caption="Expected HTTP response output on display" />

---

## Full examples

<QuickLink title="get_request.py" 
description="Connect to WiFi and perform an HTTP GET request over a socket." 
url="https://github.com/SolderedElectronics/Inkplate-micropython/blob/master/examples/inkplate6color/get_request.py" />

<QuickLink title="post_request.py" 
description="Connect to WiFi and POST a field value to ThingSpeak over a socket." 
url="https://github.com/SolderedElectronics/Inkplate-micropython/blob/master/examples/inkplate6color/post_request.py" />
