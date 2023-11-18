import re

input_dates = input()
pattern = r'\b(\d{2})([-.\/])([A-Z][a-z]{2})\2(\d{4})\b'
# match_dates = re.findall(pattern, input_dates)
# for match in match_dates:
#     print(f"Day: {match[0]}, Month: {match[2]}, Year: {match[3]}")

match_dates = re.finditer(pattern, input_dates)
for match in match_dates:
    day = match.group(1)
    month = match.group(3)
    year = match.group(4)
    print(f"Day: {day}, Month: {month}, Year: {year}")

