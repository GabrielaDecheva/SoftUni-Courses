budget = float(input())
price_for_one_kg_flour = float(input())
number_of_loaves = 0
colored_eggs = 0
remaining_budget = budget


pack_of_eggs_price = price_for_one_kg_flour * 0.75
one_milk_price = price_for_one_kg_flour + (price_for_one_kg_flour * 0.25)
milk_needed_price = one_milk_price / 4
one_loaf_price = price_for_one_kg_flour + pack_of_eggs_price + milk_needed_price

while remaining_budget > 0:
    if remaining_budget < one_loaf_price:
        break
    else:
        number_of_loaves += 1
        colored_eggs += 3
        remaining_budget -= one_loaf_price
        if number_of_loaves % 3 == 0:
            colored_eggs -= number_of_loaves - 2


print(f'You made {number_of_loaves} loaves of Easter bread! Now you have {colored_eggs} eggs and {remaining_budget:.2f}BGN left.')

