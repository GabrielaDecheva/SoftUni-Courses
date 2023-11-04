string = [character for character in input() if character != ' ']
letters = {}
for char in string:
    if char not in letters.keys():
        letters[char] = 0
    letters[char] += 1

for char, occurrence in letters.items():
    print(f'{char} -> {occurrence}')
