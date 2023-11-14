def find_name(current_element):
    name = ''
    for word in current_element:
        if '@' in word and '|' in word:
            start = word.index('@') + 1
            end = word.index('|')
            for letter_index in range(start, end):
                name += word[letter_index]
    return name


def find_age(current_element):
    age = ''
    for word in current_element:
        if '#' in word and '*' in word:
            for character in word:
                if character.isdigit():
                    age += character
    return age


count_strings = int(input())
for string in range(count_strings):
    current_string = input()
    element = current_string.split()
    current_name = find_name(element)
    current_age = find_age(element)
    print(f'{current_name} is {current_age} years old.')

