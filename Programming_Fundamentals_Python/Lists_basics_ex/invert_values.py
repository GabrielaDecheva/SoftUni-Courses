input_string = input()
numbers = input_string.split()
opposite_list = []

for number in numbers:
    num = int(number)
    opposite = -num
    opposite_list.append(opposite)

print(opposite_list)