import os
import re

def get_title_from_md(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    frontmatter_match = re.search(r'^---\s*\r?\n(.*?)(?:\r?\n)?---', content, re.DOTALL | re.MULTILINE)
    if not frontmatter_match:
        return None

    frontmatter = frontmatter_match.group(1)
    title_match = re.search(r'^title:\s*(.*)$', frontmatter, re.MULTILINE)
    return title_match.group(1).strip() if title_match else None

def update_title_in_md(file_path, user_input):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    frontmatter_match = re.search(r'^---\s*\r?\n(.*?)(?:\r?\n)?---', content, re.DOTALL | re.MULTILINE)
    if not frontmatter_match:
        print(f"⚠️ No frontmatter found in {file_path}")
        return

    frontmatter = frontmatter_match.group(1)
    title_match = re.search(r'^title:\s*(.*)$', frontmatter, re.MULTILINE)
    if not title_match:
        print(f"⚠️ No title field found in {file_path}")
        return

    old_title = title_match.group(1).strip()
    if '-' in old_title or '–' in old_title:
        print(f"⏭️ Skipping {file_path} — title already contains '-' or '–'")
        return

    new_title = f"{user_input} – {old_title}"
    new_frontmatter = re.sub(r'^(title:\s*).*$', f'title: {new_title}', frontmatter, flags=re.MULTILINE)
    new_content = content.replace(frontmatter, new_frontmatter, 1)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f"✅ Updated title in {file_path}: '{old_title}' -> '{new_title}'")

def process_folder(parent_folder):
    for folder_name in os.listdir(parent_folder):
        folder_path = os.path.join(parent_folder, folder_name)
        if not os.path.isdir(folder_path):
            continue

        print(f"\n📂 Folder: {folder_name}")
        user_input = input("Enter prefix for title update: ").strip()

        for subfolder in [folder_path, os.path.join(folder_path, 'arduino_library')]:
            if not os.path.exists(subfolder):
                continue

            for file in os.listdir(subfolder):
                if file.endswith('.md'):
                    file_path = os.path.join(subfolder, file)
                    update_title_in_md(file_path, user_input)

if __name__ == "__main__":
    parent_dir = input("Enter the path to the parent folder: ").strip()
    if not os.path.isdir(parent_dir):
        print("❌ Invalid folder path.")
    else:
        process_folder(parent_dir)
