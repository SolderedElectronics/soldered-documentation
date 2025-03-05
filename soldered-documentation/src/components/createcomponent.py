import os

# Ask for the component name
component_name = input("Enter the component name (e.g., ErrorBox): ")

# Generate the names for files and CSS class
js_filename = f"{component_name.lower()}.js"
css_filename = f"{component_name.lower()}.module.css"
css_class = component_name.lower()

# Content for the .js file
js_content = f"""import React from 'react';
import styles from './{css_class}.module.css';

const {component_name} = ({{ children }}) => (
  <div className={{styles.{css_class}}}>
    <span className={{styles.icon}}></span>
    <div>{{children}}</div>
  </div>
);

export default {component_name};
"""

# Content for the .module.css file
css_content = f""".{css_class} {{
    background-color: #ffe6e6;
    border-left: 5px solid #ff4d4d;
    padding: 1rem;
    display: flex;
    align-items: center;
    margin: 1rem 0;
    border-radius: 5px;
  }}

  .icon {{
    margin-right: 0.5rem;
  }}
"""

# Write the .js file
with open(js_filename, "w") as js_file:
    js_file.write(js_content)

# Write the .module.css file
with open(css_filename, "w") as css_file:
    css_file.write(css_content)

print(f"{js_filename} and {css_filename} created successfully!")
