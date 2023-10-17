def condition(numbers):
    return numbers % 2 == 0


number_list = [int(i) for i in input().split(", ")]
even_list = [i for i in range(len(number_list)) if condition(number_list[i])]
print(even_list)