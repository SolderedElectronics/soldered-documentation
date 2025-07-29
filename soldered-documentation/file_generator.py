import os
import re

def create_directory(path):
    """Create directory if it doesn't exist"""
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Created directory: {path}")
    else:
        print(f"Directory already exists: {path}")

def create_file(path, content):
    """Create file with specified content"""
    with open(path, 'w') as file:
        file.write(content)
    print(f"Created file: {path}")

def update_sidebar(keyword, category):
    """Update sidebars.js file with new component"""
    sidebar_path = "sidebars.js"
    
    # Format keyword for display (e.g., 'shtc3' -> 'SHTC3')
    display_keyword = keyword.upper()
    
    # Prepare component configuration
    component_config = f"""        {{
          type: 'category',
          label: '{display_keyword} Temperature and Humidity Sensor',
          items: [
            {{
              type: 'doc',
              id: '{category}/{keyword}/{keyword}-overview',
            }},
            {{
              type: 'doc',
              id: '{category}/{keyword}/{keyword}-hardware',
            }},
            {{
              type: 'doc',
              id: '{category}/{keyword}/{keyword}-how-it-works',
            }},
            {{
              type: 'category',
              label: 'Arduino library',
              items: [
                {{
                  type: 'doc',
                  id: '{category}/{keyword}/arduino_library/{keyword}-arduino-1',
                }},
                {{
                  type: 'doc',
                  id: '{category}/{keyword}/arduino_library/{keyword}-arduino-2',
                }},
                {{
                  type: 'doc',
                  id: '{category}/{keyword}/arduino_library/{keyword}-arduino-3',
                }},
              ],
            }},
          ],
        }},"""
    
    try:
        # Read the current sidebar file
        with open(sidebar_path, 'r') as file:
            content = file.read()
        
        # Find the appropriate category section to insert the new component
        if category == "sensors":
            pattern = r'(type: \'category\',\s+label: \'Sensors\',\s+items: \[)'
        elif category == "actuators":
            pattern = r'(type: \'category\',\s+label: \'Actuators\',\s+items: \[)'
        elif category == "communication":
            # If communication category doesn't exist, we'll add it
            if "label: 'Communication'," not in content:
                # Find the end of the last category to add a new one
                last_category_end = content.rfind('},')
                if last_category_end != -1:
                    # Create new communication category
                    comm_category = f"""    {{
      type: 'category',
      label: 'Communication',
      items: [
{component_config}
      ],
    }},"""
                    
                    # Split the content and insert the new category
                    first_part = content[:last_category_end+2]
                    second_part = content[last_category_end+2:]
                    updated_content = first_part + "\n" + comm_category + "\n" + second_part
                    
                    # Write the updated content back to the file
                    with open(sidebar_path, 'w') as file:
                        file.write(updated_content)
                    
                    print(f"Added new Communication category with {keyword} to {sidebar_path}")
                    return
            else:
                pattern = r'(type: \'category\',\s+label: \'Communication\',\s+items: \[)'
                
        # Find the match for the category pattern
        match = re.search(pattern, content)
        if match:
            insert_pos = match.end()
            updated_content = content[:insert_pos] + "\n" + component_config + content[insert_pos:]
            
            # Write the updated content back to the file
            with open(sidebar_path, 'w') as file:
                file.write(updated_content)
            
            print(f"Added {keyword} to {category} category in {sidebar_path}")
        else:
            print(f"Could not find {category} category in {sidebar_path}")
            print("Please add the component manually.")
    except Exception as e:
        print(f"Error updating sidebar: {e}")
        print("Please add the component manually.")

def main():
    # Prompt for keyword and category
    keyword = input("Enter keyword (e.g., shtc3): ").strip().lower()
    
    # Validate category selection
    valid_categories = ["sensors", "actuators", "communication"]
    print("\nSelect a category:")
    for i, category in enumerate(valid_categories, 1):
        print(f"{i}. {category}")
    
    while True:
        try:
            category_choice = int(input("\nEnter the number of your category choice: "))
            if 1 <= category_choice <= len(valid_categories):
                category = valid_categories[category_choice - 1]
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Please enter a number.")
    
    print(f"\nCreating files for {keyword} in category {category}...")
    
    # Create directory for images
    img_path = os.path.join("static", "img", keyword)
    create_directory(img_path)
    
    # Create main category directory
    docs_path = os.path.join("docs", category, keyword)
    create_directory(docs_path)
    
    # Create Arduino library directory
    arduino_path = os.path.join(docs_path, "arduino_library")
    create_directory(arduino_path)
    
    # Create main documentation files
    create_file(
        os.path.join(docs_path, f"{keyword}_overview.md"),
        f"""---
slug: /{keyword}/overview
title: Overview
id: {keyword}-overview 
hide_title: False
pagination_prev: null
---
"""
    )
    
    create_file(
        os.path.join(docs_path, f"{keyword}_hardware_details.md"),
        f"""---
slug: /{keyword}/hardware 
title: Hardware details
id: {keyword}-hardware 
hide_title: False
---
"""
    )
    
    create_file(
        os.path.join(docs_path, f"{keyword}_how_it_works.md"),
        f"""---
slug: /{keyword}/how-it-works 
title: How it works
id: {keyword}-how-it-works 
hide_title: False
---  
"""
    )
    
    # Create Arduino library files
    create_file(
        os.path.join(arduino_path, f"{keyword}_arduino_1.md"),
        f"""---
slug: /{keyword}/arduino/geting-started 
title: Getting started
id: {keyword}-arduino-1 
hide_title: False
---
"""
    )
    
    create_file(
        os.path.join(arduino_path, f"{keyword}_arduino_2.md"),
        f"""---
slug: /{keyword}/arduino/examples 
title: Measuring temperature and humidity (examples)
id: {keyword}-arduino-2 
hide_title: False
---
"""
    )
    
    create_file(
        os.path.join(arduino_path, f"{keyword}_arduino_3.md"),
        f"""---
slug: /{keyword}/arduino/troubleshooting 
title: Troubleshooting
id: {keyword}-arduino-3 
hide_title: False
pagination_next: null
---
"""
    )
    
    # Update sidebars.js
    update_sidebar(keyword, category)
    
    print("\nAll files created successfully!")
    print("The sidebar.js file has been updated automatically.")

if __name__ == "__main__":
    main()