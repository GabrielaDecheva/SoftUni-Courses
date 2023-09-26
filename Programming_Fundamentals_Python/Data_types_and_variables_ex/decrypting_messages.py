key = int(input())
n = int(input())
message = ''
for char in range(n):
    current_char = input()
    message += chr(key + ord(current_char))

print(message)
