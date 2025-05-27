import os
import re
import yaml
import json
from openai import OpenAI

# --- CONFIGURATION ---

# Extend this mapping as needed for all your products.
PRODUCT_NAME_MAP = {
    'relay': 'Relay board',
    'led-matrix': 'LED matrix',
    'digipot': 'Digital potentiometer',
    'mcp23017': 'MCP23017 IO expander',
    'pcf85063a': 'PCF85063A RTC',
    'mcp47a1': 'MCP47A1 DAC',
    'stepper-motor-driver': 'Stepper motor driver',
    'ws2812b': 'WS2812B',
    'buzzer': 'Buzzer',
    'temperature-sensor': 'Temperature sensor',
    'humidity-sensor': 'Humidity sensor',
    'pressure-sensor': 'Pressure sensor',
    'distance-sensor': 'Distance sensor',
    'oled-display': 'OLED display',
    'rtc': 'RTC',
    'i2c-expander': 'I2C expander',
    'motor-driver': 'Motor driver',
    'servo-controller': 'Servo controller',
    'sound-sensor': 'Sound sensor',
    'light-sensor': 'Light sensor',
    'current-sensor': 'Current sensor',
    'voltage-sensor': 'Voltage sensor',
    'spi-flash': 'SPI Flash',
    'eeprom': 'EEPROM',
    'sd-card': 'SD card',
    'usb-uart': 'USB UART',
    'can-bus': 'CAN bus',
    'rs485': 'RS485',
    'gps': 'GPS',
    'gsm': 'GSM',
    'wifi': 'WiFi',
    'bluetooth': 'Bluetooth',
    'rfid': 'RFID',
    'nfc': 'NFC',
    'accelerometer': 'Accelerometer',
    'gyroscope': 'Gyroscope',
    'magnetometer': 'Magnetometer',
    'compass': 'Compass',
    'joystick': 'Joystick',
    'keypad': 'Keypad',
    'touch-sensor': 'Touch sensor',
    'infrared': 'Infrared',
    'fan': 'Fan',
    # Alternate/legacy slugs for compatibility:
    'relay-board': 'Relay board',
    'led-matrix-breakout': 'LED matrix',
    # Add more as you discover new official names.
}

# --- API KEY LOADING ---

def load_api_key():
    config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.json')
    try:
        if os.path.exists(config_path):
            with open(config_path, 'r') as f:
                config = json.load(f)
                api_key_path = config.get('api_key_path', '')
        else:
            return None
        if not api_key_path or not os.path.exists(api_key_path):
            print(f"API key file not found at: {api_key_path}")
            return None
        with open(api_key_path, 'r') as f:
            api_key = f.read().strip()
        if not api_key:
            print("API key file is empty")
            return None
        return api_key
    except Exception as e:
        print(f"Error loading API key: {str(e)}")
        return None

def create_openai_client():
    api_key = load_api_key()
    if not api_key:
        return None
    return OpenAI(api_key=api_key)

# --- FRONTMATTER PARSING ---

def parse_frontmatter(content):
    match = re.match(r'^---\s*\n(.*?)\n---\s*\n(.*)', content, re.DOTALL)
    if not match:
        return None, None
    frontmatter = yaml.safe_load(match.group(1))
    body = match.group(2)
    return frontmatter, body

# --- PRODUCT & PAGE NAME EXTRACTION ---

def extract_product_and_page(slug, filepath):
    """
    Extracts product key and page name from slug or filepath.
    """
    if slug and slug.startswith('/'):
        parts = slug.strip('/').split('/')
        if len(parts) >= 2:
            product_key = parts[0]
            page = ' '.join(parts[1:]).replace('-', ' ')
            return product_key, page
        elif len(parts) == 1:
            return parts[0], ''
    # Fallback: use folder and filename
    parts = filepath.split(os.sep)
    for i, part in enumerate(parts):
        if part in PRODUCT_NAME_MAP:
            product_key = part
            page = os.path.splitext(parts[-1])[0].replace('-', ' ')
            return product_key, page
    return None, None

def get_official_product_name(product_key):
    return PRODUCT_NAME_MAP.get(product_key, product_key.replace('-', ' ').title())

def prettify_page_name(page):
    # Lowercase, replace dashes/underscores with spaces, capitalize as needed
    page = page.replace('-', ' ').replace('_', ' ')
    # Special cases
    if page.lower() == 'overview':
        return 'Overview'
    if page.lower() == 'how it works':
        return 'How it works'
    if page.lower() == 'hardware':
        return 'Hardware details'
    return page.strip().capitalize()

# --- AI TITLE GENERATION ---

def build_ai_prompt(product_name, page_name, old_title, slug):
    # Add your detailed examples and instructions
    return f"""
You are a documentation assistant specializing in generating clear, human-friendly page titles for technical documentation.

Task:
- Generate a concise, well-formatted title for a documentation page, following the format: [Official Product Name] – [Page Name].

Role:
- Your role is to act as a technical editor, ensuring each title is accurate, professional, and easy to understand.

Context:
- Product slug: {slug}
- Official product name: {product_name}
- Page name: {page_name}
- Old title: {old_title}

Guidelines:
1. The title must strictly follow this format: [Official Product Name] – [Page Name].
2. Use the full, official product name (not the folder name or abbreviation). If unsure, infer the most standard and professional name possible.
3. Capitalize the title appropriately for a documentation page.
4. Do not include the word 'documentation', file extensions, or unnecessary descriptors.
5. If the page is an overview, simply use 'Overview' as the page name (e.g., 'Relay Board – Overview').
6. Only generate the new title—do not include any explanations or additional text.

Examples:
Input slug: /relay/arduino/geting-started
Official product name: Relay Board
Output: Relay Board – Arduino getting started

Input slug: /led-matrix/arduino/examples
Official product name: LED Matrix breakout
Output: LED Matrix breakout – Arduino examples (displaying text)

Input slug: /digipot/arduino/troubleshooting
Official product name: Digital potentiometer breakout
Output: Digital potentiometer breakout – Arduino troubleshooting

Input slug: /mcp23017/how-it-works
Official product name: MCP23017 IO expander breakout
Output: MCP23017 IO expander breakout – How it works

Input slug: /pcf85063a/hardware
Official product name: PCF85063A RTC breakout
Output: PCF85063A RTC breakout – Hardware details

Input slug: /mcp47a1/arduino/examples
Official product name: MCP47A1 DAC breakout
Output: MCP47A1 DAC breakout – Arduino examples (setting specific voltages)

Input slug: /relay/arduino/regular-example
Official product name: Relay Board
Output: Relay Board – Arduino switching the relay (regular example)

Input slug: /mcp47a1/arduino/generating-a-waveform
Official product name: MCP47A1 DAC breakout
Output: MCP47A1 DAC breakout – Arduino generating a waveform

Input slug: /mcp23017/arduino/button-input-example
Official product name: MCP23017 IO expander breakout
Output: MCP23017 IO expander breakout – Arduino button input example

Input slug: /pcf85063a/arduino/setting-up-an-alarm
Official product name: PCF85063A RTC breakout
Output: PCF85063A RTC breakout – Arduino setting up an alarm

Output Format:
- Return ONLY the new title as a single line of text, with no extra commentary or formatting.
"""

def ai_generate_title(client, product_name, page_name, old_title, slug):
    prompt = build_ai_prompt(product_name, page_name, old_title, slug)
    completion = client.chat.completions.create(
        model="o3-mini",
        messages=[
            {"role": "system", "content": "You are a technical documentation assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return completion.choices[0].message.content.strip()

# --- FILE PROCESSING ---

def process_file(filepath, client):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    frontmatter, body = parse_frontmatter(content)
    if not frontmatter or 'slug' not in frontmatter or 'title' not in frontmatter:
        print(f"Skipping {filepath}: no valid frontmatter.")
        return False
    slug = frontmatter['slug']
    old_title = frontmatter['title']
    product_key, page_raw = extract_product_and_page(slug, filepath)
    if not product_key:
        print(f"Could not determine product key for {filepath}. Skipping.")
        return False
    product_name = get_official_product_name(product_key)
    page_name = prettify_page_name(page_raw)
    new_title = ai_generate_title(client, product_name, page_name, old_title, slug)
    if new_title == old_title:
        print(f"No change for {filepath}")
        return False
    frontmatter['title'] = new_title
    new_frontmatter = '---\n' + yaml.dump(frontmatter, sort_keys=False).strip() + '\n---\n'
    new_content = new_frontmatter + body
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Updated title in {filepath} to: {new_title}")
    return True

def walk_and_process(root_dir, max_files=400):
    client = create_openai_client()
    if not client:
        print("OpenAI client could not be created. Check your API key.")
        return
    files_edited = 0
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith('.md'):
                filepath = os.path.join(dirpath, filename)
                changed = process_file(filepath, client)
                if changed:
                    files_edited += 1
                    if files_edited >= max_files:
                        print(f"\nReached the maximum of {max_files} files edited. Stopping early for testing.")
                        return

if __name__ == "__main__":
    walk_and_process(os.getcwd())
