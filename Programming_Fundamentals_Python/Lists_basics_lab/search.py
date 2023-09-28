n = int(input())
word = input()
strings = []

for _ in range(n):
    current_string = input()
    strings.append(current_string)
print(strings)

filtered_strings = []

for string in strings:
    if word in string:
        filtered_strings.append(string)
print(filtered_strings)
