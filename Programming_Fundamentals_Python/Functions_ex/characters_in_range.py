def characters(char_one, char_two):
    my_list = []
    for char in range(ord(char_one) + 1, ord(char_two)):
        my_list.append(chr(char))
    return my_list


first_input = input()
second_input = input()
result = characters(first_input, second_input)
print(*result)
