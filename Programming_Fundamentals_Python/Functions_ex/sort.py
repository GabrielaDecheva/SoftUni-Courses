input_as_string = input().split()
input_as_digit = []
for element in input_as_string:
    input_as_digit.append(int(element))

sorted_list = sorted(input_as_digit)
print(sorted_list)