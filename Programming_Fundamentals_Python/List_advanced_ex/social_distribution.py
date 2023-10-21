def distribute_wealth(min_wealth: int, list_population: list):
    if sum(list_population) // len(list_population) < min_wealth:
        return "No equal distribution possible"
    for index in range(len(list_population)):
        if list_population[index] < min_wealth:
            take_from_index = list_population.index(max(list_population))
            add_value = min_wealth - list_population[index]
            list_population[index] += add_value
            list_population[take_from_index] -= add_value
    return list_population


population = [int(i) for i in input().split(", ")]
minimum_wealth = int(input())
print(distribute_wealth(minimum_wealth, population))