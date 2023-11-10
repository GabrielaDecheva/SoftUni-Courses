string = input().split()
new_string = ''
for element in string:
    new_string += element * len(element)
print(new_string)