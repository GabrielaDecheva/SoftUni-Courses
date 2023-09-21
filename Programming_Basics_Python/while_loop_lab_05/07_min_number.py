import sys

number = input()

min_num = sys.maxsize
while number != 'Stop':
    current_num = int(number)
    if current_num < min_num:
        min_num = current_num
    number = input()
print(min_num)
