---
slug: /breadboard-power-supply-board/how-it-works
title: How it works
id: breadboard-power-supply-board-how-it-works
hide_title: false
---  

## How it supplies power

The board accepts two power inputs: a 12V DC jack and a 5V USB-C connector. If both are connected at the same time, an automatic input selection circuit ensures the DC jack takes priority, protecting the USB-C source from back-feeding.

When powered via the DC jack, the onboard **7805 voltage regulator** converts the input down to 5V. It accepts inputs from 7V to 35V. The **SE5218 LDO regulator** takes that 5V and steps it further down to 3.3V.

<InfoBox>Image coming soon.</InfoBox>

---

## Output voltage selection

The board has two independently controlled output rails:

| Rail | Switch | Options |
|------|--------|---------|
| **VOUT1** | S2 | 12V or 3.3V |
| **VOUT2** | S3 | 5V or 3.3V |

The **S1** switch turns the entire board on or off.

Find more detail about each switch [**here**](/breadboard-power-supply-board/hardware#switch-details).
