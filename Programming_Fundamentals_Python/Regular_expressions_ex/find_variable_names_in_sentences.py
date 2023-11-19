import re

string = input()
pattern = r'\b\_([A-Za-z0-9]+)\b'
variable_names = re.findall(pattern, string)
print(','.join(variable_names))