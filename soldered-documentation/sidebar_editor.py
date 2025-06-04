from flask import Flask, render_template_string, request, jsonify
import os
import re
import json
import ast # For safely evaluating string to Python literal

app = Flask(__name__)
SIDEBARS_FILE = 'sidebars.js' # Assumes sidebars.js is in the same folder

def extract_sidebar_object_string(content):
    """
    Extracts the JavaScript object string assigned to 'const sidebars'.
    It expects a structure like: const sidebars = { ... }; export default sidebars;
    """
    # Regex to capture the object literal (including its braces)
    match = re.search(
        r"const\s+sidebars\s*=\s*(\{[\s\S]*?\})\s*;?\s*export\s+default\s+sidebars;",
        content,
        re.DOTALL
    )
    if match:
        return match.group(1)  # The "{...}" part

    # Fallback for a slightly different common pattern that might include comments after the object
    match_fallback = re.search(
        r"const\s+sidebars\s*=\s*(\{[\s\S]*?\})\s*;?\s*\n\s*// @ts-ignore\s*\n\s*export\s+default\s+sidebars;",
        content,
        re.DOTALL
    )
    if match_fallback: # pragma: no cover
        return match_fallback.group(1)

    app.logger.warning("Could not find 'const sidebars = { ... }; export default sidebars;' pattern.")
    return None

def js_object_to_python(js_obj_str):
    """
    Converts the extracted JavaScript object string to a Python dictionary.
    This involves:
    1. Removing comments.
    2. Quoting unquoted keys (e.g., `label:` to `"label":`).
    3. Removing trailing commas (which ast.literal_eval doesn't like).
    4. Using ast.literal_eval to parse.
    """
    if not js_obj_str:
        return None

    # 1. Remove JavaScript comments
    s = re.sub(r"//.*", "", js_obj_str)  # Remove single-line comments
    s = re.sub(r"/\*[\s\S]*?\*/", "", s, flags=re.MULTILINE)  # Remove multi-line comments
    s = s.strip()

    # 2. Ensure keys are quoted (e.g., { key: value } to { "key": value })
    s = re.sub(r'([\{\s,])\s*([a-zA-Z_\$][\w\$]*)\s*:', r'\1"\2":', s)

    # 3. Remove trailing commas before '}' or ']' as ast.literal_eval is strict
    s = re.sub(r",\s*(?=[}\]])", "", s)

    try:
        return ast.literal_eval(s)
    except Exception as e:
        app.logger.error(f"Failed to parse JS object string with ast.literal_eval: {e}")
        app.logger.error(f"Problematic string content after transformation:\n{s[:500]}...")
        return None


def get_sidebar_data():
    """Reads and parses the sidebars.js file."""
    if not os.path.exists(SIDEBARS_FILE):
        app.logger.error(f"{SIDEBARS_FILE} not found.")
        return None
    try:
        with open(SIDEBARS_FILE, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e: # pragma: no cover
        app.logger.error(f"Error reading {SIDEBARS_FILE}: {e}")
        return None

    obj_str = extract_sidebar_object_string(content)
    if not obj_str:
        app.logger.error("Could not extract sidebar object string from file content.")
        return None

    data = js_object_to_python(obj_str)
    if data is None:
        app.logger.error("Failed to convert sidebar object string to Python data.")
    return data


def save_sidebar_data(py_data):
    """Saves the Python data back to the sidebars.js file."""
    new_sidebar_json_content = json.dumps(py_data, indent=2)

    try:
        with open(SIDEBARS_FILE, 'r', encoding='utf-8') as f:
            original_content = f.read()
    except Exception as e: # pragma: no cover
        app.logger.error(f"Error reading {SIDEBARS_FILE} for saving: {e}")
        return False

    pattern = r"(const\s+sidebars\s*=\s*)(\{[\s\S]*?\})(\s*;?\s*export\s+default\s+sidebars;)"
    fallback_pattern = r"(const\s+sidebars\s*=\s*)(\{[\s\S]*?\})(\s*;?\s*\n\s*// @ts-ignore\s*\n\s*export\s+default\s+sidebars;)"

    match = re.search(pattern, original_content, re.DOTALL)
    if not match: # pragma: no cover
        match = re.search(fallback_pattern, original_content, re.DOTALL)

    if not match:
        app.logger.error("Could not find the sidebar object block for replacement in save operation.")
        return False

    prefix = match.group(1)
    suffix = match.group(3)
    updated_content = prefix + new_sidebar_json_content + suffix

    try:
        with open(SIDEBARS_FILE, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        return True
    except Exception as e: # pragma: no cover
        app.logger.error(f"Error writing to {SIDEBARS_FILE}: {e}")
        return False

# --- Flask Routes ---
@app.route('/')
def index():
    if not os.path.exists(SIDEBARS_FILE):
        return f"Error: {SIDEBARS_FILE} not found in the current directory. Please ensure it exists.", 404

    sidebar_py_data = get_sidebar_data()
    if sidebar_py_data is None:
        return "Error loading or parsing sidebar data from sidebars.js. Check server console for details. The `sidebars.js` might be malformed or the script couldn't parse it.", 500

    html_template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Sidebars.js Editor</title>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/Sortable/1.15.2/Sortable.min.js"></script>
        <style>
            body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; margin: 0; background-color: #f0f2f5; color: #1c1e21; line-height: 1.5; }
            .container { max-width: 900px; margin: 20px auto; padding: 20px; background-color: #fff; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
            h1 { color: #1c1e21; border-bottom: 1px solid #ddd; padding-bottom: 10px; margin-top:0; }
            ul.sortable-list { list-style-type: none; padding-left: 0; margin-top: 10px; }
            li.sidebar-item.collapsible > ul.sortable-list { display: none; } /* Collapsed by default */
            li.sidebar-item.collapsible.expanded > ul.sortable-list { display: block; } /* Shown when expanded */
            ul.sortable-list ul.sortable-list { padding-left: 25px; }
            li.sidebar-item {
                background-color: #f7f7f7; margin: 8px 0; padding: 12px; border: 1px solid #ccd0d5;
                border-radius: 6px; cursor: grab; display: flex; flex-direction: column;
            }
            li.sidebar-item:hover { border-color: #8a8d91; }
            .item-header { font-weight: bold; color: #333; margin-bottom: 5px; display: flex; align-items: center; }
            .item-id, .item-label { font-size: 0.9em; color: #555; word-break: break-all; }
            .item-label { color: #0056b3; }
            li.type-category > .item-header { color: #006827; }
            .toggle-btn {
                cursor: pointer;
                margin-right: 8px;
                font-size: 1.1em;
                width: 20px; /* Ensure consistent width */
                display: inline-block;
                user-select: none; /* Prevent text selection on click */
            }
            .toggle-btn.no-items { color: #aaa; cursor: default; }
            .controls { margin-top: 25px; text-align: right; }
            button {
                background-color: #1877f2; color: white; padding: 10px 20px; border: none;
                border-radius: 6px; cursor: pointer; font-size: 16px; transition: background-color 0.2s;
            }
            button:hover { background-color: #166fe5; }
            #status { margin-top: 15px; font-weight: 500; padding: 10px; border-radius: 4px; text-align: center;}
            .status-success { background-color: #e9f5e9; color: #006827; }
            .status-error { background-color: #fdecea; color: #c91c1c; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Edit Docusaurus Sidebar: <code>solderedDocsSidebar</code></h1>
            <div id="sidebar-editor-container">
                </div>
            <div class="controls">
                <button onclick="saveChanges()">Save Changes</button>
                <div id="status"></div>
            </div>
        </div>

        <script>
            let currentSidebarData = {{ sidebar_json_data | tojson }};

            function createSidebarElement(itemData) {
                const li = document.createElement('li');
                li.classList.add('sidebar-item');

                const header = document.createElement('div');
                header.classList.add('item-header');
                li.appendChild(header);

                if (typeof itemData === 'string') {
                    li.dataset.type = 'doc';
                    li.dataset.id = itemData;
                    header.textContent = 'Document';
                    const idSpan = document.createElement('span');
                    idSpan.classList.add('item-id');
                    idSpan.textContent = `ID: ${itemData}`;
                    li.appendChild(idSpan);
                } else if (itemData && typeof itemData === 'object') {
                    li.dataset.type = itemData.type;
                    let headerText = `Type: ${itemData.type}`;

                    const hasItems = itemData.items && Array.isArray(itemData.items) && itemData.items.length > 0;

                    if (itemData.type === 'category') {
                        li.classList.add('type-category');
                        li.classList.add('collapsible'); // All categories are collapsible
                        // Initially collapsed by CSS (`li.sidebar-item.collapsible > ul.sortable-list { display: none; }`)

                        const toggle = document.createElement('span');
                        toggle.classList.add('toggle-btn');
                        if (hasItems) {
                            toggle.textContent = '►'; // Collapsed indicator
                            toggle.addEventListener('click', function(event) {
                                event.stopPropagation(); // Prevent SortableJS drag start
                                const parentLi = this.closest('li.sidebar-item');
                                parentLi.classList.toggle('expanded');
                                this.textContent = parentLi.classList.contains('expanded') ? '▼' : '►';
                            });
                        } else {
                            toggle.textContent = '•'; // Indicate no items, or make it empty
                            toggle.classList.add('no-items');
                        }
                        header.appendChild(toggle);
                    }


                    if (itemData.label) {
                        li.dataset.label = itemData.label;
                        const labelSpan = document.createElement('span');
                        labelSpan.classList.add('item-label');
                        labelSpan.textContent = `Label: ${itemData.label}`;
                        const headerLabel = document.createTextNode(itemData.label); // Text node for label
                        header.appendChild(headerLabel); // Append text after toggle
                        if(itemData.type === 'category') headerText = itemData.label; // Use label for category header text
                    } else {
                         const headerType = document.createTextNode(headerText);
                         header.appendChild(headerType);
                    }


                    if (itemData.id) {
                        li.dataset.id = itemData.id;
                        const idSpan = document.createElement('span');
                        idSpan.classList.add('item-id');
                        idSpan.textContent = `ID: ${itemData.id}`;
                        li.appendChild(idSpan);
                    }
                    if (itemData.dirName) {
                        li.dataset.dirName = itemData.dirName;
                        const dirNameSpan = document.createElement('span');
                        dirNameSpan.classList.add('item-id');
                        dirNameSpan.textContent = `dirName: ${itemData.dirName}`;
                        li.appendChild(dirNameSpan);
                    }

                    if (itemData.items && Array.isArray(itemData.items)) {
                        const nestedUl = document.createElement('ul');
                        nestedUl.classList.add('sortable-list');
                        li.appendChild(nestedUl); // Append even if initially hidden
                        itemData.items.forEach(subItem => {
                            nestedUl.appendChild(createSidebarElement(subItem));
                        });
                        new Sortable(nestedUl, { group: 'nested', animation: 150 });
                    }
                }
                return li;
            }

            function renderSidebar(sidebarName, sidebarItems, containerElement) {
                containerElement.innerHTML = '';
                const rootUl = document.createElement('ul');
                rootUl.classList.add('sortable-list');
                rootUl.dataset.sidebarName = sidebarName;

                sidebarItems.forEach(item => {
                    rootUl.appendChild(createSidebarElement(item));
                });
                containerElement.appendChild(rootUl);
                new Sortable(rootUl, { group: 'nested', animation: 150 });
            }

            function buildDataFromDOM(ulElement) {
                const items = [];
                ulElement.childNodes.forEach(liNode => {
                    if (liNode.nodeType !== Node.ELEMENT_NODE || liNode.tagName !== 'LI') return;

                    const type = liNode.dataset.type;
                    let itemData;

                    if (type === 'doc' && liNode.dataset.id && !liNode.dataset.label && Object.keys(liNode.dataset).length === 2) { // Simple string doc
                        itemData = liNode.dataset.id;
                    } else {
                        itemData = { type: type };
                        if (liNode.dataset.id) itemData.id = liNode.dataset.id;
                        if (liNode.dataset.label) itemData.label = liNode.dataset.label;
                        if (liNode.dataset.dirName) itemData.dirName = liNode.dataset.dirName;

                        const nestedUl = liNode.querySelector('ul.sortable-list');
                        if (nestedUl) {
                            itemData.items = buildDataFromDOM(nestedUl);
                        } else if (type === 'category') { // Ensure categories always have an items array
                            itemData.items = [];
                        }
                    }
                    items.push(itemData);
                });
                return items;
            }

            document.addEventListener('DOMContentLoaded', () => {
                const editorContainer = document.getElementById('sidebar-editor-container');
                if (currentSidebarData && currentSidebarData.solderedDocsSidebar) {
                    renderSidebar('solderedDocsSidebar', currentSidebarData.solderedDocsSidebar, editorContainer);
                } else { // pragma: no cover
                    editorContainer.innerHTML = '<p>Could not load <code>solderedDocsSidebar</code> data or it is empty.</p>';
                }
            });

            async function saveChanges() {
                const statusDiv = document.getElementById('status');
                statusDiv.textContent = 'Saving...';
                statusDiv.className = '';

                const mainUl = document.querySelector('#sidebar-editor-container > ul.sortable-list');
                if (!mainUl || mainUl.dataset.sidebarName !== 'solderedDocsSidebar') { // pragma: no cover
                    statusDiv.textContent = 'Error: Could not find the sidebar content to save.';
                    statusDiv.classList.add('status-error');
                    return;
                }

                const newSolderedDocsSidebar = buildDataFromDOM(mainUl);
                const dataToSave = { ...currentSidebarData, solderedDocsSidebar: newSolderedDocsSidebar };

                try {
                    const response = await fetch('/save_sidebars', {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify(dataToSave)
                    });
                    const result = await response.json();
                    if (response.ok) {
                        statusDiv.textContent = result.message;
                        statusDiv.classList.add('status-success');
                        currentSidebarData = dataToSave;
                    } else { // pragma: no cover
                        statusDiv.textContent = `Error: ${result.message || response.statusText}`;
                        statusDiv.classList.add('status-error');
                    }
                } catch (error) { // pragma: no cover
                    console.error('Save error:', error);
                    statusDiv.textContent = `Network error: ${error.message}`;
                    statusDiv.classList.add('status-error');
                }
            }
        </script>
    </body>
    </html>
    """
    return render_template_string(html_template, sidebar_json_data=sidebar_py_data)


@app.route('/save_sidebars', methods=['POST'])
def save_sidebars_route():
    try:
        new_data = request.get_json()
        if not new_data: # pragma: no cover
            return jsonify({"message": "No data received"}), 400

        if save_sidebar_data(new_data):
            return jsonify({"message": "Sidebars.js saved successfully!"}), 200
        else: # pragma: no cover
            return jsonify({"message": "Failed to save sidebars.js. Check server logs."}), 500
    except Exception as e: # pragma: no cover
        app.logger.error(f"Exception in /save_sidebars: {e}", exc_info=True)
        return jsonify({"message": f"An internal server error occurred: {e}"}), 500

if __name__ == '__main__': # pragma: no cover
    print("Starting Flask Sidebar Editor...")
    print(f"Ensure '{SIDEBARS_FILE}' is in the same directory as this script.")
    print("Open http://127.0.0.1:5000 in your browser.")
    app.run(debug=True)