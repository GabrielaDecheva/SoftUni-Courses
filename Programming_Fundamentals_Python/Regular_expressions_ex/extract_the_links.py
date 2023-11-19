import re

input_line = input()
pattern = r'(w{3}\.[A-Za-z0-9\-\.]+\.[a-z]+)'
while input_line:
    matched_links = re.search(pattern, input_line)
    if matched_links:
        valid_url = matched_links.group(1)
        print(valid_url)
    input_line = input()
