import re

names = input()
pattern = r"\b[A-Z][a-z]+ [A-Z]{1}[a-z]+\b"
result = re.findall(pattern, names)
print(' '.join(result))
