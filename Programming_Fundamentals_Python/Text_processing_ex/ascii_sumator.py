first_character = input()
second_character = input()
string = input()
start_range = ord(first_character)
end_range = ord(second_character)
total_sum = 0
for char in string:
    if start_range < ord(char) < end_range:
        total_sum += ord(char)
print(total_sum)