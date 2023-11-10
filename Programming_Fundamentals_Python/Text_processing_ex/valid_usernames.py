strings = input().split(', ')
valid = False

for string in strings:
    if 3 <= len(string) <= 16:
        if all(char.isalnum() or char in ['_','-'] for char in string):
            print(string)

