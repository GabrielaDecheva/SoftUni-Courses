string = input()
result = list()

for i, character in enumerate(string):
    if character.isupper():
        result.append(i)
print(result)