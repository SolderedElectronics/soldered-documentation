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
        # Use text format for the response
        completion = client.chat.completions.create(
            model="o3-mini",
            messages=[
                {
                    "role": "system",
                    "content":
                    """
                    You are a helpful assistant tasked with correcting spelling and grammar in markdown files. Follow these instructions carefully:
                    1. Correct spelling and grammar mistakes and improve sentence structure when necessary, but do NOT alter the original meaning.
                    2. The markdown text contains custom React components (such as <QuickLink>, <ExpandableSection>, <CenteredImage>, <InfoBox>, <WarningBox>) and standard markdown syntax (links, headers, bullet points, code blocks, bold, italic, etc.).
                    IMPORTANT: These custom React elements MUST NOT be removed, modified, or omitted under any circumstances. Preserve these EXACTLY as they appear.
                    3. Keep the front matter (header) of the markdown intact and unchanged. It typically looks like this:
                    ---
                    slug: /example/path
                    title: Example Title
                    id: example-id
                    hide_title: False
                    ---
                    4. Return your response in this exact format:
                       a. First, provide the complete corrected markdown text.
                       b. Then, add a line containing only "###CORRECTIONS###" as a separator.
                       c. After the separator, list all corrections made as bullet points.
                       
                    Example:
                    <corrected markdown text here>
                    
                    ###CORRECTIONS###
                    * Changed "recieve" to "receive"
                    * Fixed capitalization in heading
                    * Added missing period at end of paragraph
                    
                    NEVER omit or modify the React elements or markdown syntax.
                    """
                },
                {
                    "role": "user",
                    "content": f"Please check and correct this markdown file, preserving all markdown syntax and custom React elements exactly as they appear:\n\n{text}"
                }
            ]
        )
        
        # Get the response content
        response_content = completion.choices[0].message.content
        
        # Print the raw response for debugging
        print("Raw response from GPT-4o:")
        print(response_content)
        
        # Split the response at the separator
        if "###CORRECTIONS###" in response_content:
            parts = response_content.split("###CORRECTIONS###", 1)
            corrected_text = parts[0].strip()
            changes_text = parts[1].strip()
            
            # Parse changes into a list of bullet points
            changes = []
            for line in changes_text.split('\n'):
                line = line.strip()
                # Be more lenient with what we consider a bullet point
                if line and (line.startswith('*') or line.startswith('-') or line.startswith('•')):
                    # Remove the bullet character and any whitespace
                    change = line.lstrip('*-• \t').strip()
                    if change:  # Ensure we're not adding empty strings
                        changes.append(change)
            
            # If no changes were found in the expected format
            if not changes:
                # Try to just split the text into lines as a fallback
                changes = [line.strip() for line in changes_text.split('\n') if line.strip()]
                if not changes:
                    changes = ["No significant changes needed"]
        else:
            # Fallback if separator not found
            corrected_text = response_content
            changes = ["Response format error - separator not found"]
        
        return corrected_text, changes, None
        
    except Exception as e:
        import traceback
        print(f"Spell check error: {str(e)}")
        print(traceback.format_exc())
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
