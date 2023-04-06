import re

def read_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content

def write_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)

def modify_image_urls(content, modify_function):
    img_url_pattern = re.compile(r'!\[(.*?)\]\((.*?)\)')
    modified_content = img_url_pattern.sub(modify_function, content)
    return modified_content

def my_modify_function(match):
    alt_text = match.group(1)
    img_url = match.group(2)
    new_img_url = "My New Scaler URL" # Modify the image URL as needed
    return f'![{alt_text}]({new_img_url})'

file_path = 'markdown.md'

content = read_file(file_path)
modified_content = modify_image_urls(content, my_modify_function)
write_file(file_path, modified_content)


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