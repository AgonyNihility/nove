import re

# Read the file content
with open('天降女友.txt', 'r', encoding='utf-8') as file:
    content = file.read()

# Add a newline before each "第n章"
updated_content = re.sub(r'(第\d+章)', r'\n\1', content)

# Save the updated content to a new file
with open('天降女友_更新版.txt', 'w', encoding='utf-8') as file:
    file.write(updated_content)
