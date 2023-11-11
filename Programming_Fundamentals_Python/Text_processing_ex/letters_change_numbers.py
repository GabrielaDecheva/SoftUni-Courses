input_string = [string.strip() for string in input().split()]
alphabet = '.abcdefghijklmnopqrstuvwxyz'
number = ''
total_sum = 0
current_sum = 0
for string in input_string:
    first_position = alphabet.index(string[0].lower())
    second_position = alphabet.index(string[-1].lower())
    for char in string:
        if char.isdigit():
            number += char
    if string[0].isupper() and string[-1].isupper():
        current_sum += int(number) / int(first_position)
        current_sum -= int(second_position)
    elif string[0].isupper() and string[-1].islower():
        current_sum += int(number) / int(first_position)
        current_sum += int(second_position)
    elif string[0].islower() and string[-1].isupper():
        current_sum += int(number) * int(first_position)
        current_sum -= int(second_position)
    elif string[0].islower() and string[-1].islower():
        current_sum += int(number) * int(first_position)
        current_sum += int(second_position)
    total_sum += current_sum
    current_sum = 0
    number = ''
print(f'{total_sum:.2f}')