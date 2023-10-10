def min_number(some_numbers: list):
    return min(some_numbers)


def max_number(some_numbers: list):
    return max(some_numbers)


def sum_of_all_numbers(some_numbers: list):
    return sum(some_numbers)


input_numbers = input().split()
list_of_numbers = []
for num in input_numbers:
    list_of_numbers.append(int(num))


smallest = min_number(list_of_numbers)
biggest = max_number(list_of_numbers)
total_sum = sum_of_all_numbers(list_of_numbers)
print(f'The minimum number is {smallest}')
print(f'The maximum number is {biggest}')
print(f'The sum number is: {total_sum}')