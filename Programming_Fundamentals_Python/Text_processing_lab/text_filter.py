banned_list = input().split(', ')
text = input()

for string in banned_list:
    while string in text:
        text = text.replace(string, '*'*len(string))
print(text)