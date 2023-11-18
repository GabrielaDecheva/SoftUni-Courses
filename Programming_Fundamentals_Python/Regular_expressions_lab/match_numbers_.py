import re

numbers = input()
pattern = r'(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))'
match_numbers = re.finditer(pattern, numbers)
for match in match_numbers:
    print(match.group(), end=' ')