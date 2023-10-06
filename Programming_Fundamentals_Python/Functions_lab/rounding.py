input_numbers = input().split()
list_rounded_numbers = []

for number in input_numbers:
    list_rounded_numbers.append(round(float(number)))

print(list_rounded_numbers)

