string = input()
last_string_found = ''
string_to_print = ''
for letter in string:
    if letter != last_string_found:
        last_string_found = letter
        string_to_print += letter
print(string_to_print)
