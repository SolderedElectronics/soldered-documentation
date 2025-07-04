---
slug: /template-parts
title: Template Parts - Template parts
id: template-parts
hide_title: false
---

Hi! You've found the secret **template parts** page! This page contains code snippets of React elements specifically made for this documentation! Let's get started:

---

## Code block

```cpp
// include the library code:
#include <LiquidCrystal.h>

// initialize the library by associating any needed LCD interface pin
// with the arduino pin number it is connected to
const int rs = 12, en = 11, d4 = 5, d5 = 4, d6 = 3, d7 = 2;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);

void setup() {
  // set up the LCD's number of columns and rows:
  lcd.begin(16, 2);
  // Print a message to the LCD.
  lcd.print("hello, world!");
}

void loop() {
  // set the cursor to column 0, line 1
  // (note: line 1 is the second row, since counting begins with 0):
  lcd.setCursor(0, 1);
  // print the number of seconds since reset:
  lcd.print(millis() / 1000);
}
```

---

## Error box

<ErrorBox>This is some sort of error message to inform the user they are doing something wrong if xyz</ErrorBox>

---

## Info box

<InfoBox>This is some general information for the user</InfoBox>

---

## Warning box

<WarningBox>A note to the user to be careful about something</WarningBox>

---

## Success box

<SuccessBox>Used to highlight if some step was successful</SuccessBox>

---

## Product Table

<ProductTable 
  products={[
    {
      sku: "333134",
      name: "Basic stepper driver",
      storeLink: "https://soldered.com/product/basic-stepper-driver/",
      soldeRedLink: "https://solde.red/333134"
    },
    {
      sku: "333250",
      name: "Stepper motor with driver",
      storeLink: "https://soldered.com/product/stepper-motor-with-driver/",
      soldeRedLink: "https://solde.red/333250"
    }
  ]}
/>

---

## Expandable Section

<ExpandableSection title="Click on this, and it will expand!">

You can write markdown here!

```cpp
// include the library code:
#include <LiquidCrystal.h>

// initialize the library by associating any needed LCD interface pin
// with the arduino pin number it is connected to
const int rs = 12, en = 11, d4 = 5, d5 = 4, d6 = 3, d7 = 2;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);

void setup() {
  // set up the LCD's number of columns and rows:
  lcd.begin(16, 2);
  // Print a message to the LCD.
  lcd.print("hello, world!");
}

void loop() {
  // set the cursor to column 0, line 1
  // (note: line 1 is the second row, since counting begins with 0):
  lcd.setCursor(0, 1);
  // print the number of seconds since reset:
  lcd.print(millis() / 1000);
}
```

</ExpandableSection>

---

## Centered Image

<CenteredImage src="/img/soldered_docs_social_card.jpg" alt="Soldered Docs Social Card" caption="This is an example caption." />

---

## Centered Image with Set Width

<CenteredImage src="/img/soldered_docs_social_card.jpg" alt="Soldered Docs Social Card" caption="This is an example caption." width="300px" />

---

## Centered Image with attribution

<CenteredImage
  src="/img/soldered_docs_social_card.jpg"
  alt="Descriptive alt text"
  caption="This is a cool image"
  attribution_name="Unsplash Author"
  attribution_link="https://unsplash.com/@author"
/>


---

## QuickLink

<QuickLink 
  title="Soldered Electronics GitHub" 
  description="Find libraries, hardware files and more"
  url="https://github.com/SolderedElectronics" 
/>

---

## QuickLink with image

<QuickLink 
  title="1-channel relay board with easyC" 
  description="Soldered webstore page for 1-channel relay board with easyC"
  url="https://soldered.com/product/1-channel-relay-board-with-easyc/"
  image="img/small_product_images/333021.jpg" 
/>

---

## Youtube Embed

<YouTubeEmbed videoId="7zRY-R7_--E" />

---

## Section title

<SectionTitle title="Troubleshooting" backgroundImage="/img/faq.webp" />

---

## Function documentation

<FunctionDocumentation
  functionName="inkplate.connectWiFi()"
  description="This function attempts to connect to WiFi."
  returnDescription="Number"
  returnType="int"
  parameters={[
    { type: 'Number', name: 'a', description: 'The first number to add.' },
    { type: 'Number', name: 'b', description: 'The second number to add.' },
  ]}
/>

---

import WebmPlayer from '@site/src/components/WebmPlayer';

# My Page with a WebM Video

Here's a cool WebM video:

<WebmPlayer src="/videos/test2.webm" width={600} />

Another video, full width:

<WebmPlayer src="/videos/test2.webm" />