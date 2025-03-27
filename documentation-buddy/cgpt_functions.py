import os
import json
from openai import OpenAI


def load_api_key():
    """
    Load the OpenAI API key from the configured path.
    Returns the API key as a string or None if not found.
    """
    # Try to load the API key path from a configuration file
    # Assuming config is stored in a JSON file in the same directory
    config_path = os.path.join(os.path.dirname(
        os.path.abspath(__file__)), 'config.json')

    try:
        if os.path.exists(config_path):
            with open(config_path, 'r') as f:
                config = json.load(f)
                api_key_path = config.get('api_key_path', '')
        else:
            return None

        # Check if the API key file exists
        if not api_key_path or not os.path.exists(api_key_path):
            print(f"API key file not found at: {api_key_path}")
            return None

        # Read the API key from the file
        with open(api_key_path, 'r') as f:
            api_key = f.read().strip()

        if not api_key:
            print("API key file is empty")
            return None

        return api_key

    except Exception as e:
        print(f"Error loading API key: {str(e)}")
        return None


def save_api_key_path(api_key_path):
    """
    Save the API key path to a configuration file.
    Returns True if successful, False otherwise.
    """
    config_path = os.path.join(os.path.dirname(
        os.path.abspath(__file__)), 'config.json')

    try:
        # Load existing config if it exists
        if os.path.exists(config_path):
            with open(config_path, 'r') as f:
                config = json.load(f)
        else:
            config = {}

        # Update the API key path
        config['api_key_path'] = api_key_path

        # Save the updated config
        with open(config_path, 'w') as f:
            json.dump(config, f, indent=2)

        return True

    except Exception as e:
        print(f"Error saving API key path: {str(e)}")
        return False


def create_openai_client():
    """
    Create and return an OpenAI client with the configured API key.
    Returns None if the API key cannot be loaded.
    """
    api_key = load_api_key()
    if not api_key:
        return None

    return OpenAI(api_key=api_key)


def spell_check_text(text):
    """
    Use the OpenAI API to spell check the provided text.
    Returns a tuple of (corrected_text, changes_made, error_message)
    """
    client = create_openai_client()
    if not client:
        return None, None, "API key not configured or invalid"

    try:
        # Instruct the API to correct spelling and grammar and return JSON
        completion = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "system",
                    "content":
                    """
                    You are a helpful assistant that corrects spelling and grammar in markdown files. Only make necessary corrections while maintaining the original meaning. If you notice something can be said in better English, make the correction as well. Leave the header of the markdown as it is. It will be similar to this:
                    ---
                    slug: /shtc3/arduino/geting-started 
                    title: Getting started
                    id: shtc3-arduino-1 
                    hide_title: False
                    ---
                    * Here below is the markdown you need to spell check *
                    
                    Return the corrected text and a list of changes made in JSON format (IMPORTANT): {\"corrected_text\": \"...\", \"changes\": [\"Change 1\", \"Change 2\", ...]}.
                    """
                },
                {
                    "role": "user",
                    "content": f"Please check and correct this markdown file:\n\n{text}"
                }
            ],
            response_format={"type": "json_object"}
        )

        # Parse the response
        response_content = completion.choices[0].message.content

        try:
            # Remove any markdown code block formatting if present
            clean_content = response_content
            if clean_content.startswith("```"):
                clean_content = clean_content.split("```")[1]
                if clean_content.startswith("json"):
                    clean_content = clean_content[4:].strip()
            if clean_content.endswith("```"):
                clean_content = clean_content.rsplit("```", 1)[0].strip()

            # Try to parse as JSON
            result = json.loads(clean_content)
            corrected_text = result.get("corrected_text", text)
            changes = result.get("changes", [])

            # If no changes were made, provide feedback
            if not changes or (len(changes) == 1 and changes[0] == "No changes needed"):
                changes = ["No spelling or grammar errors found."]

            return corrected_text, changes, None

        except json.JSONDecodeError as e:
            # If not valid JSON, try to extract what we can
            print(f"JSON parse error: {e}")
            print(f"Response content: {response_content}")

            # Try to extract text between quotes after "corrected_text":
            import re
            text_match = re.search(
                r'"corrected_text"\s*:\s*"([^"]*)"', response_content)
            if text_match:
                corrected_text = text_match.group(1)
            else:
                corrected_text = text

            return corrected_text, ["Could not parse changes - API response format error"], None

    except Exception as e:
        return None, None, f"Error during spell check: {str(e)}"


def generate_documentation(keyword, category):
    """
    Use the OpenAI API to generate documentation for the given keyword and category.
    Returns generated content or None if there was an error.
    """
    client = create_openai_client()
    if not client:
        return None, "API key not configured or invalid"

    try:
        # Create a prompt based on the keyword and category
        prompt = f"""
        Generate comprehensive documentation for a {category} component with the keyword '{keyword}'.
        Include the following sections:
        1. Overview
        2. Technical specifications
        3. Installation instructions
        4. Usage examples
        5. Troubleshooting
        
        Format as markdown.
        """

        completion = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "system",
                    "content": "You are a technical documentation assistant specializing in electronics and microcontrollers."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return completion.choices[0].message.content, None

    except Exception as e:
        return None, f"Error generating documentation: {str(e)}"
