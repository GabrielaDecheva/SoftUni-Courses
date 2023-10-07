def odd_and_even_sum(number: str):
    odd_sum = 0
    even_sum = 0
    for num in number:
        if int(num) % 2 == 0:
            even_sum += int(num)
        else:
            odd_sum += int(num)
    return odd_sum, even_sum


input_num = input()
sum_of_odd_nums, sum_of_even_nums = odd_and_even_sum(input_num)
print(f'Odd sum = {sum_of_odd_nums}, Even sum = {sum_of_even_nums}')