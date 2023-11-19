import re

string_line = input()
searched_word = input()
regex = fr'\b{searched_word}\b'
matches = re.findall(regex, string_line, re.IGNORECASE)
print(len(matches))