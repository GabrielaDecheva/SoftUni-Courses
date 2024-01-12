numbers = tuple([float(num) for num in input().split()])

nums_and_occ = {}
for num in numbers:
    if num not in nums_and_occ:
        nums_and_occ[num] = numbers.count(num)

for number, occ in nums_and_occ.items():
    print(f'{number} - {occ} times')
