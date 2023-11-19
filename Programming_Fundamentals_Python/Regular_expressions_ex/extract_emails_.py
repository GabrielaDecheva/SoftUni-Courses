import re

string_line = input()
pattern = r'\s(([a-z0-9]+[a-z0-9\.\-\_]*)@([a-z\-]+)(\.[a-z]+)+)\b'
matched_emails = re.findall(pattern, string_line)
for email in matched_emails:
    print(email[0])