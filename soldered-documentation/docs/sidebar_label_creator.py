import os
import re

def check_title_format(title):
    match = re.match(r'^(.*?) [–-] (.+)$', title)
    if match:
        prefix, name = match.groups()
        return prefix.strip(), name.strip()
    return None

def process_md_file(file_path, issues):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    frontmatter_match = re.search(r'^---\s*\r?\n(.*?)(?:\r?\n)?---', content, re.DOTALL | re.MULTILINE)
    if not frontmatter_match:
        return

    frontmatter = frontmatter_match.group(1)
    title_match = re.search(r'^title:\s*(.+)$', frontmatter, re.MULTILINE)
    if not title_match:
        return

    full_title = title_match.group(1).strip()
    result = check_title_format(full_title)

    if not result:
        issues.append(f"⚠️ Invalid title format in: {file_path}")
        return

    prefix, name = result

    # Check if sidebar_label already exists
    if re.search(r'^sidebar_label:\s*.+$', frontmatter, re.MULTILINE):
        return  # Already has sidebar_label

    # Insert sidebar_label below title line
    lines = content.splitlines()
    for i, line in enumerate(lines):
        if line.strip().startswith('title:'):
            lines.insert(i + 1, f'sidebar_label: {name}')
            break

    new_content = '\n'.join(lines)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f"✅ Added sidebar_label to {file_path}: '{name}'")

def scan_folder_for_titles(root_folder):
    issues = []

    for dirpath, _, filenames in os.walk(root_folder):
        for file in filenames:
            if file.endswith('.md'):
                file_path = os.path.join(dirpath, file)
                process_md_file(file_path, issues)

    if issues:
        print("\n⚠️ Files with invalid title format:")
        for issue in issues:
            print(issue)
    else:
        print("\n✅ All titles were valid and updated where needed.")

if __name__ == "__main__":
    folder = input("Enter the path to the root folder: ").strip()
    if not os.path.isdir(folder):
        print("❌ Invalid folder path.")
    else:
        scan_folder_for_titles(folder)
