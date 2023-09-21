import sys

number = input()

max_num = -sys.maxsize
while number != 'Stop':
    current_num = int(number)
    if current_num > max_num:
        max_num = current_num
    number = input()
print(max_num)
