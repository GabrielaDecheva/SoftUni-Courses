import re

string_line = input()
while string_line:
    pattern = r'\d+'
    matches = re.findall(pattern, string_line)
    if matches:
        for match in matches:
            print(match, end=' ')
    string_line = input()