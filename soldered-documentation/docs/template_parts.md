---
slug: /template-parts
title: Template parts
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

