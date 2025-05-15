---
slug: /inkplate/10/hardware/jumpers
title: Jumpers
id: 10-hardware-jumpers
---

Inkplate 10 features several **on-board jumpers**, which can be used to modify the behavior of certain components. Some jumpers are **connected by default**, while others need to be manually shorted.

See the table below for a detailed explanation of each jumper's function:

---

## Board jumpers

| Jumper  | Default State | Function |
|---------|--------------|----------|
| **JP1** | **Open** (not connected) | When shorted, it **keeps the microSD card powered at 3.3V** at all times. Useful for troubleshooting, but not ideal for low-power applications. |
| **JP2** | **Connected by default** | Bridges the **WAKE button** with **PC13**, allowing the board to wake from deep sleep via button press. |
| **JP3** | **Connected by default** | Bridges the **USER1 button** with **PG6**, enabling button input functionality. |
| **JP4** | **Connected by default** | Bridges the **USER2 button** with **PG0**, allowing interaction with USER2. |

<CenteredImage src="/img/inkplate10/jumpers.png" alt="Inkplate 10 on-board jumpers" caption="Inkplate 10 on-board jumpers" />  