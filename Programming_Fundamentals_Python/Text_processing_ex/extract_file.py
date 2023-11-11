path = input().split('\\')
name_and_extension = path[-1].split('.')
name_of_file, extension = name_and_extension[0], name_and_extension[1]
print(f'File name: {name_of_file}')
print(f'File extension: {extension}')
