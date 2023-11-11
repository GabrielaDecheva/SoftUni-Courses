input_string = input()
string_to_print = ''
explosion_strength = 0
for index in range(len(input_string)):
    if explosion_strength > 0 and input_string[index] != '>':
        explosion_strength -= 1
    elif input_string[index] == '>':
        string_to_print += input_string[index]
        explosion_strength += int(input_string[index + 1])
    else:
        string_to_print += input_string[index]

print(string_to_print)

