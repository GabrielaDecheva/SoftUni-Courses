# characters = input().split(', ')
# dict_result = {}
#
# for char in characters:
#     key = char
#     value = int(ord(key))
#     dict_result[key] = value
#
# print(dict_result)

characters = input().split(', ')

dict_result = {char: ord(char) for char in characters}

print(dict_result)