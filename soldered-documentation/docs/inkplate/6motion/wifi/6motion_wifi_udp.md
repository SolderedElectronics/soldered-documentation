---
slug: /inkplate/6motion/wifi/udp
title: 6Motion - UDP
sidebar_label: UDP
id: 6motion-wifi-udp
---

It's possible to use UDP servers to easily retrieve the current time, which is useful for displaying timestamps, scheduling requests, or enabling/disabling display updates during certain hours.

<InfoBox>If you prefer, you can also use regular APIs like [**timeapi**](https://timeapi.io/).</InfoBox>

---

## Getting Time via a UDP Server

Here's how to get time data via UDP:

```cpp
// Use Google's public NTP server
// You can change this to another NTP server (time.windows.com, time.apple.com, etc.)
const char ntpServerName[] = {"time.google.com"};

// Ensure Inkplate is connected to the internet
// This function returns a standard C++ time_t value of the current time

time_t getUDPClock()
{
    time_t _epoch = 0; // Return value (epoch time)
    
    WiFiUDP udp; // Create an object for the UDP protocol

    // Set connection timeout to 10 seconds
    udp.setConnectionTimeout(10000ULL);

    // Initialize UDP, using port 8888 for the NTP local port
    if (udp.begin(8888))
    {
        // Try to connect to the host; NTP uses port 123
        if (udp.setHost(ntpServerName, 123))
        {
            udp.beginPacket(); // Initialize UDP for packet sending

            // Create the byte array for the NTP request
            uint8_t ntpPacket[48] = {0};
            ntpPacket[0] = B11100011; // Clock is unsynced, NTP version 4, Symmetric passive
            ntpPacket[12] = 49;
            ntpPacket[13] = 0x4E;
            ntpPacket[14] = 49;
            ntpPacket[15] = 52;

            // Send the packet (NTP packet is 48 bytes long)
            if (udp.write(ntpPacket, 48))
            {
                // Wait for the response
                if (udp.available())
                {
                    // Read the response
                    udp.read(ntpPacket, 48);

                    // Extract NTP epoch from received data
                    int32_t epochRaw = ntpPacket[40] << 24 | ntpPacket[41] << 16 | ntpPacket[42] << 8 | ntpPacket[43];
                    _epoch = epochRaw - 2208988800UL;
                }
            }
        }
    }

    udp.end(); // Must be called, or further commands to the ESP32 may fail
    return _epoch; // Return the epoch time (zero indicates failure)
}
```

Now, this can be used to retrieve and display the time on Inkplate:

```cpp
// Example loop that periodically synchronizes time on Inkplate
void loop()
{
    time_t epoch = getUDPClock(); // Try to get the NTP time

    if (epoch)
    {
        epoch += (timezone * 3600); // Apply timezone offset

        struct tm ntpTime;
        memcpy(&ntpTime, localtime((const time_t *)(&epoch)), sizeof(ntpTime));

        // Format and print the time
        char timeAndDateStr[40];
        sprintf(timeAndDateStr, "NTP: %02d:%02d:%02d %d.%02d.%04d. %+dGMT",
                ntpTime.tm_hour, ntpTime.tm_min, ntpTime.tm_sec,
                ntpTime.tm_mday, ntpTime.tm_mon + 1, ntpTime.tm_year + 1900, timezone);
        
        inkplate.println(timeAndDateStr);
        inkplate.partialUpdate(false);
    }
    else
    {
        // Print error if NTP retrieval failed
        inkplate.println("NTP clock retrieval failed!");
        inkplate.partialUpdate(false);
    }

    delay(30000ULL); // Wait 30 seconds before the next sync (not needed frequently)
}
```

---

## Full Example

<QuickLink 
  title="Inkplate_6_Motion_WiFi_UDP.ino" 
  description="Complete example on how to connect to WiFi and retrieve time data via a UDP server."
  url="https://github.com/SolderedElectronics/Inkplate_Motion_Arduino_Library/blob/main/examples/Inkplate6Motion/Advanced/Web_WiFi/Inkplate_6_Motion_WiFi_UDP/Inkplate_6_Motion_WiFi_UDP.ino" 
/>