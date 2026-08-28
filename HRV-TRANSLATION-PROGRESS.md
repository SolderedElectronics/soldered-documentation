# Zero to Hero (HRV) translation progress

Croatian copy of the Embedded Journey Kit - Zero to Hero docs. Lands in the
sidebar inside **Beginner Kits**, directly below the English kit entry, as
**Embedded Journey Kit - Zero to Hero (HRV)**.

## Layout

- `docs/beginner kits/soldered-nula-beginner-kit-arduino-hrv/`
- `docs/beginner kits/soldered-nula-beginner-kit-micropython-hrv/`

Filenames are kept identical to the English originals. Frontmatter `id` is kept
identical too (the folder disambiguates it); `slug` gets the `-hrv` folder
prefix so the URLs do not collide.

## Rules

1. **Never translate** the 40 terms in `Soldered Glossary.xlsx`: Soldered,
   Soldered Electronics / Manufacturing / For Makers, Making for Makers,
   Inkplate (+ 4TEMPERA, 6MOTION, 6FLICK, 6COLOR, 13SPECTRA), NULA (+ Mini
   ESP32-C6, Max RP2350, Core, DeepSleep, Beginner Kit), Inputronic (+ BRIDGE,
   KEYBOARD), CONNECT programmer, Stop Me Game, Reaction Game, Simon Says,
   Dasduino Core, Dasduino Beginner Kit - Basic, all Solder Kits, Qwiic,
   Breakout, Protoboard, HAT, ESPFlash, USB-Cereal, STlink, TowerPro.
2. **Product and site names stay English:** Thonny, MicroPython, Arduino, VSCode,
   GitHub, webhook.site, and every hardware part name.
3. **Code blocks:** translate the comments, leave printed and serial strings in
   English so console output still matches the screenshots. This means the docs
   code intentionally diverges from the example repos.
4. **A whole page stored as a string literal stays English**, embedded comments
   included. In 6.2 the `HTML_PAGE` triple-quoted block is left untouched, because
   it is a string and the screenshots show the English page rendered from it.
5. Image and video `src` paths are unchanged, so both languages share the same
   assets. Screenshots keep their English UI.
6. Internal links are repointed at the `-hrv` slugs.
11. **Link text uses the Croatian page title**, even though sidebar labels stay
   English. Inline links are prose.
7. No em dashes, matching the English pages.
8. **Sidebar labels stay English** for now, so every page carries an explicit
   English `sidebar_label` in frontmatter while `title` is Croatian.
9. **In-page anchor links:** translate the heading but pin the original English
   anchor onto it with the Docusaurus `{#id}` syntax, so the link keeps working
   without depending on how diacritics get slugified. First case is 4.1, heading
   `Ako je pozadinsko svjetlo upaljeno a ekran prazan
   {#if-the-backlight-is-on-but-the-screen-is-empty}`.
10. Links to pages outside the kit (for example `/ch340-drivers`) keep pointing at
   the English pages, since no Croatian copy of those exists.

## Terms deliberately left in English - reviewed, decision: keep

These were translated first, then reverted on request. Reviewed on 2026-08-28 with
all 47 pages done: **both stay English**, uninflected, exactly as they are below.
This is settled, not pending.

- **active low** - not `aktivna u nizini`. Appears wherever a pull-up button is
  explained (2.1, 2.2 and the later button examples).
- **debounce** - not `debouncing tipke`, and never Croatian-inflected forms like
  `debounceanim` or `debouncinga`. Used uninflected: `softverski debounce`,
  `debounce tipke`, `debounce logika`, `pritiskom tipke uz debounce`. The noun
  `debouncer` is kept as-is since it is already English.

The image filename `button-debouncing-graph.webp` is an asset path and stays
untouched.

## Terminology

| EN | HR |
|---|---|
| board | pločica |
| console | konzola |
| serial | serijska komunikacija |
| jumper wire | jumper žica |
| breadboard | breadboard |
| example | primjer |
| sketch | skica |
| to print | ispisati |
| row / column | red / stupac |
| pin | pin |
| driver | driver |
| firmware | firmware |
| folder | folder |
| naredbeni redak | command line |
| resistor | otpornik |
| pushbutton | tipka |
| buzzer | buzzer |
| power rail | naponska tračnica |

## Status

Total: 47 pages, 136 395 words (24 Arduino / 23 MicroPython).

### MicroPython (23 / 23) - COMPLETE
- [x] 1.1 Hello World
- [x] 0.1 Setting up MicroPython
- [x] 1.2 LED Blinking
- [x] 2.1 Button Counter
- [x] 2.2 Button Debounce
- [x] 2.3 Photoresistor Analog Read
- [x] 2.4 Buzzer Beep
- [x] 3.1 Measuring distance
- [x] 3.2 Distance Fade LED
- [x] 4.1 LCD Message Display
- [x] 4.2 Autoscroll text
- [x] 5.1 Temperature and Humidity
- [x] 6.1 Connecting and getting data
- [x] 6.2 WiFi LED control
- [x] 6.3 Sending data
- [x] 7.1 Smart Weather Station
- [x] 7.2 Mini Piano
- [x] 7.3 Parking Sensor
- [x] 7.4 RGB LED Controller
- [x] 7.5 Shift Register
- [x] 7.6 Morse Code
- [x] 7.7 Alarm Clock
- [x] 7.8 LED Traffic Light

### Arduino (24 / 24) - COMPLETE
- [x] 0.1 Breadboard fundamentals
- [x] 0.2 Setting up the Arduino environment
- [x] 1.1 Hello World
- [ ] 1.1 LED Blink
- [x] 2.1 Button Counter
- [x] 2.2 Button Debounce
- [x] 2.3 Photoresistor Analog Read
- [x] 2.4 Buzzer Beep
- [x] 3.1 Measuring Distance
- [x] 3.2 Distance Fade LED
- [x] 4.1 Print Message
- [x] 4.2 Auto Scroll Text
- [x] 5.1 Reading Temperature and Humidity
- [x] 6.1 Connecting and Getting Data
- [x] 6.2 Wi-Fi LED Control
- [x] 6.3 Sending Data
- [x] 7.1 Smart Weather Station
- [x] 7.2 Mini Piano
- [x] 7.3 Parking Sensor
- [x] 7.4 RGB LED Controller
- [ ] 7.5 Shift Register
- [ ] 7.6 Morse Code
- [x] 7.7 Alarm Clock
- [x] 7.8 LED Traffic Light

## Proofreading pass, 2026-08-28

A full grammar and usage pass over all 47 pages. Two stages: a scripted lint for the
mechanically detectable error classes, then a read-through of every page (the
MicroPython tree was reviewed against the lines that differ from the Arduino tree,
since the two share most of their prose).

Systematic errors found and fixed corpus-wide:

- **`bez da` + verb, 33 uses.** A Germanism; standard Croatian is `a da ne` +
  present. Each one was rewritten in context, not blind-replaced.
- **`protivn-` where `suprotn-` belongs, 30 uses.** "protivan" means opposed;
  "suprotan" means opposite. Every "protivni rub / protivna strana / protivni
  krajevi" was wrong.
- **`kabl-` declension, 13 uses.** Serbian; Croatian is kabel → kabela → kabeli.
  "dva kabla", "dvaju kablova", "Qwiic kablovi", "USB-C kablovi".
- **`startati`, 24 uses.** Colloquial, and one was the Serbian form `startuje`.
  Now "pokrenuti" throughout.
- **`meni` → `izbornik`, 10 uses.** "izbornik" is the standard term for a UI menu.
- **`najvanjskiji`, 8 uses.** Not a Croatian superlative; now "krajnji".
- **`Thonny-ju` / `Thonny-ja`, 9 uses.** Croatian attaches case endings to foreign
  names directly: "Thonnyju".
- **`odčekati`, 4 uses.** Not a word; now "pričekati" / "počekati".
- Plus ~70 one-off fixes: agreement errors ("nijedna dva otpornika", "dva pina
  koje"), double negatives ("bio bi spojen ni na što"), calques ("vrijedi
  trenutak", "isplata od zaglavlja", "zapečati dlan", "što ti kupuje sat"),
  garbled word order, "Pogrešiti" → "Pogriješiti", `sa` before a consonant that
  is not s/š/z/ž, and `rikverc`.

One content fix: Arduino 6.2 linked to the LED blink page as "1.1 LED Blink" -
English text and the wrong number. The English source has the same mistake there;
the page is 1.2. The Croatian now reads "1.2 Blinkanje LED-ice".

The lint is clean on all of the above, the Cyrillic sweep is clean, and
`npm run build` still passes.

### Terminology decisions

- **`blinkanje` (59 uses)** is an anglicism where "treptanje" or "bljeskanje"
  would be standard. **Decided 2026-08-28: keep `blinkanje`.** It is used
  consistently and appears in the locked title **1.2 Blinkanje LED-ice**. Arduino
  7.8 was the one file that used "treptanje"; it was aligned to "blinkanje" to
  match the rest. Do not "fix" this later - it is the chosen term.
- ~~**`browser`**~~ **Decided 2026-08-28: now `preglednik`.** All 99 prose and
  comment occurrences were replaced with the correctly declined form
  (preglednik / preglednika / pregledniku / preglednike / preglednici - note the
  k → c palatalisation in the nominative plural). Three occurrences stay English:
  the `Access the board in your browser at:` string that 6.2 prints, and the same
  line in its console output, because sketch and script strings stay English.
  The first prose mention on each of the eight pages that use the word (6.1, 6.2,
  6.3 and 7.1 in both trees) is glossed once as `preglednik (engl. browser)`, so a
  reader who only knows the English term is not left guessing. One gloss per page,
  never repeated.
- **`USB-c` (11 uses)** with a lowercase c, against 140 correct `USB-C`. Inherited
  from the English pages verbatim, so it was left as-is in both trees.

## Content issues inherited from the English pages

Translated faithfully, not silently fixed. They need fixing in the English pages
first, then the Croatian ones follow.

- **7.3 states the ultrasonic sensor reports millimetres** and divides by ten to
  get centimetres, with a warning that getting the unit wrong changes the project
  completely. 3.1 and 3.2 describe the same sensor as reporting centimetres and do
  no conversion. Two pages, one sensor, contradictory units. 7.3 is the one whose
  code proves its claim.

## Where to pick up

All 47 pages are translated. Nothing is left to translate.

### Before calling the whole thing done

1. [x] Sidebar wired. `sidebars.js` now carries a second category,
   `Embedded Journey Kit - Zero to Hero (HRV)`, directly below the English kit
   inside `Beginner Kits` and above `Solder Kits`. It mirrors the English
   structure exactly: the breadboard doc, then `Arduino`, then `MicroPython`,
   same order, same English labels, with every doc id pointing at the `-hrv`
   folder. Verified 1:1 against the English block: 47 ids, 47 counterparts, no
   extras on either side.
2. [x] Build run and clean. `npm run build` succeeds. `onBrokenLinks` is
   `'throw'`, so every `-hrv` link resolves, and all pinned anchors resolve too.
   All 47 HRV pages appear under `build/`. The one broken anchor the build
   reports, `/rotary-encoder/how-it-works/#address-selection-for-qwiic-version`,
   is pre-existing on an unrelated page and has nothing to do with this work.
3. [x] Cyrillic sweep clean across both HRV folders, 0 hits.
4. [x] Reviewed 2026-08-28. `active low` and `debounce` **stay English**, as they
   are. The locked title list stands.
5. [x] Sidebar labels are **Croatian** as of 2026-08-28. Every `sidebar_label` in
   both HRV folders now carries the same string as that page's `title`, and the one
   explicit label in `sidebars.js` (the breadboard doc) reads `Osnove breadboarda`.
   The two `1.1 Hello World` rows were already identical in both languages. The
   inner `Arduino` and `MicroPython` category labels are product names and stay.

- **7.5 disagrees with itself across the two tracks about a reversed 74HC595.**
  Arduino 7.5 says a chip seated backwards "gets no power at all in that position".
  MicroPython 7.5 says the supply lands **backwards** rather than absent, which
  forward-biases the diode inside the package, can make the chip noticeably warm and
  can destroy it, so it must not be left powered. Rotating a DIP end for end swaps
  pin 8 (GND) and pin 16 (VCC) across the channel, so the MicroPython version is the
  physically correct one and the Arduino page understates a way to kill the part.

## Sidebar

Wired. The HRV category was generated from the English block by rewriting the two
folder segments in each doc id and appending ` (HRV)` to the category label, so
ordering and labels match the English side line for line. If a page is ever added
to the English kit, add it to both blocks or the two trees drift apart.

### Morse code: `Morseov kod`, on both 7.6 pages

Settled 2026-08-28. Arduino 7.6 was titled `7.6 Morseov predajnik`, which was
rejected; both pages are now `7.6 Morseov kod`, matching the MicroPython page.

For the record, the reference works lean the other way. **Hrvatski jezicni portal**
lists `Morseovi znakovi`, `Morseova svjetiljka` and `Morseova abeceda` under the
adjective *Morseov* and does not list `Morseov kod` at all, and **Hrvatska
enciklopedija** glosses the code as *(Morseova abeceda)*. `Morseov kod` is closer
to the English, it is what Croatian Wikipedia titles its article, and it is common
in the press. It was tried as `Morseova abeceda` and changed back on request, so
this is a deliberate choice - do not "correct" it later.

The Arduino page title drops the "Transmitter" of the English title. The alt text
on step 6 carries it instead, as `predajnik Morseovog koda`.

## Locked Croatian titles

Fixed up front so forward references stay consistent. `sidebar_label` keeps the
English title from the same row.

### MicroPython
| EN | HR |
|---|---|
| 0.1. Setting up MicroPython | 0.1. Postavljanje MicroPythona |
| 1.1 Hello World | 1.1 Hello World |
| 1.2 LED Blinking | 1.2 Blinkanje LED-ice |
| 2.1 Button Counter | 2.1 Brojac pritisaka tipke |
| 2.2 Button Debounce | 2.2 Debounce tipke |
| 2.3 Photoresistor Analog Read | 2.3 Analogno citanje fotootpornika |
| 2.4 Buzzer Beep | 2.4 Piskanje buzzera |
| 3.1 Measuring distance | 3.1 Mjerenje udaljenosti |
| 3.2 Distance Fade LED | 3.2 Udaljenost i zatamnjivanje LED-ice |
| 4.1 LCD Message Display | 4.1 Prikaz poruke na LCD-u |
| 4.2 Autoscroll text | 4.2 Automatsko pomicanje teksta |
| 5.1 Temperature and Humidity | 5.1 Temperatura i vlaga |
| 6.1 Connecting and getting data | 6.1 Povezivanje i dohvat podataka |
| 6.2 WiFi LED control | 6.2 Upravljanje LED-icom preko WiFija |
| 6.3 Sending data | 6.3 Slanje podataka |
| 7.1 Smart Weather Station | 7.1 Pametna meteo stanica |
| 7.2 Mini Piano | 7.2 Mini piano |
| 7.3 Parking Sensor | 7.3 Senzor za parkiranje |
| 7.4 RGB LED Controller | 7.4 RGB LED kontroler |
| 7.5 Shift Register | 7.5 Shift registar |
| 7.6 Morse Code | 7.6 Morseov kod |
| 7.7 Alarm Clock | 7.7 Budilica |
| 7.8 LED Traffic Light | 7.8 LED semafor |

### Arduino
| EN | HR |
|---|---|
| 0.1 Breadboard Fundamentals | 0.1 Osnove breadboarda |
| 0.2 Setting up the Arduino environment | 0.2 Postavljanje Arduino okruzenja |
| 1.1 Hello World | 1.1 Hello World |
| 1.2 LED Blink | 1.2 Blinkanje LED-ice |
| 2.1 Button Counter | 2.1 Brojac pritisaka tipke |
| 2.2 Button Debounce | 2.2 Debounce tipke |
| 2.3 Photoresistor Analog Read | 2.3 Analogno citanje fotootpornika |
| 2.4 Buzzer Beep | 2.4 Piskanje buzzera |
| 3.1 Measuring Distance | 3.1 Mjerenje udaljenosti |
| 3.2 Distance Fade LED | 3.2 Udaljenost i zatamnjivanje LED-ice |
| 4.1 Print Message | 4.1 Ispis poruke |
| 4.2 Auto Scroll Text | 4.2 Automatsko pomicanje teksta |
| 5.1 Reading Temperature and Humidity | 5.1 Citanje temperature i vlage |
| 6.1 Connecting and Getting Data | 6.1 Povezivanje i dohvat podataka |
| 6.2 Wi-Fi LED Control | 6.2 Upravljanje LED-icom preko Wi-Fija |
| 6.3 Sending Data | 6.3 Slanje podataka |
| 7.1 Smart Weather Station | 7.1 Pametna meteo stanica |
| 7.2 Mini Piano | 7.2 Mini piano |
| 7.3 Parking Sensor | 7.3 Senzor za parkiranje |
| 7.4 RGB LED Controller | 7.4 RGB LED kontroler |
| 7.5 Shift Register Binary Counter | 7.5 Binarni brojac sa shift registrom |
| 7.6 Morse Code Transmitter | 7.6 Morseov kod |
| 7.7 Alarm Clock | 7.7 Budilica |
| 7.8 LED Traffic Light | 7.8 LED semafor |

Note: the Arduino filename `1.1-led-blink.md` carries the title `1.2 LED Blink`,
so the numbering is right and only the filename is misleading.
