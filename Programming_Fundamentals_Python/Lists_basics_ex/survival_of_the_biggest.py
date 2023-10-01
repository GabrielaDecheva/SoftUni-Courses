import sys

list_of_numbers = input().split()
numbers_to_remove = int(input())
list_of_integers = []
for current_number in list_of_numbers:
    list_of_integers.append(int(current_number))
for _ in range(numbers_to_remove):
    smallest_number = min(list_of_integers)
    list_of_integers.remove(smallest_number)

print(*list_of_integers, sep=', ')