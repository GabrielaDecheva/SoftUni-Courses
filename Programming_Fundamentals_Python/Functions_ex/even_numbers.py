numbers = input().split()
numbers_as_digits = []
for num in numbers:
    numbers_as_digits.append(int(num))

is_even = lambda x: x % 2 == 0
final_result = list(filter(is_even, numbers_as_digits))
print(final_result)
