list_of_numbers = input().split()
numbers_to_remove = int(input())
list_of_integers = []
for current_number in list_of_numbers:
    list_of_integers.append(int(current_number))
list_of_integers.sort(reverse=True)
while len(list_of_numbers) > (len(list_of_numbers) - numbers_to_remove):
    list_of_integers.sort(reverse=True)
    list_of_integers.pop()
    numbers_to_remove -= 1

print(list_of_integers)