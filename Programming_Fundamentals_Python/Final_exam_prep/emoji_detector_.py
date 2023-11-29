import re

input_line = input()

cool_threshold = re.findall(r'\d', input_line)
count_cool_thresholds = 1
for digit in cool_threshold:
    count_cool_thresholds *= int(digit)
print(f"Cool threshold: {count_cool_thresholds}")

pattern = r'(:{2}|\*{2})([A-Z][a-z]{2,})\1'
match_emojis = re.findall(pattern, input_line)
found_emojis = len(match_emojis)
print(f"{found_emojis} emojis found in the text. The cool ones are:")
for element in match_emojis:
    is_cool = 0
    for letter in element[1]:
        is_cool += ord(letter)
    if is_cool >= count_cool_thresholds:
        print(f'{element[0]}{element[1]}{element[0]}')



