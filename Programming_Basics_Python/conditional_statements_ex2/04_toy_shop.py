trip = float(input())
puzzle_count = int(input())
dolls_count = int(input())
teddy_count = int(input())
minions_count = int(input())
truck_count = int(input())


price_for_all_toys = (puzzle_count * 2.60) + (dolls_count * 3) + (teddy_count * 4.10) + (minions_count * 8.20) + (truck_count * 2)

count_all_toys = puzzle_count + dolls_count + teddy_count + minions_count + truck_count

if count_all_toys >= 50:
    price_for_all_toys = price_for_all_toys - (price_for_all_toys * 0.25)

total_income = price_for_all_toys - (price_for_all_toys * 0.10)

amount = abs(total_income - trip)

if total_income >= trip:
    print(f'Yes! {amount:.2f} lv left.')
else:
    print(f'Not enough money! {amount:.2f} lv needed.')
