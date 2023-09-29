factor = int(input())
count = int(input())
my_list = []
for num in range(1, (factor * count) + 1):
    if num % factor == 0:
        my_list.append(num)
print(my_list)

