string = input()
digits = ''
letters = ''
other = ''
for char in string:
    if char.isalpha():
        letters += char
    elif char.isnumeric():
        digits += char
    else:
        other += char
print(digits)
print(letters)
print(other)