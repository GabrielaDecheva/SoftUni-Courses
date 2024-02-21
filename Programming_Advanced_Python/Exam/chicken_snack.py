from collections import deque

money = [int(x) for x in input().split()]
prices = deque(int(x) for x in input().split())

eaten_foods_count = 0

while money and prices:
    current_money = money.pop()
    current_price = prices.popleft()

    if current_money == current_price:
        eaten_foods_count += 1
    elif current_money > current_price:
        eaten_foods_count += 1
        change = current_money - current_price
        if money:
            money[-1] += change
    # elif current_money < current_price:
    #     continue

if not eaten_foods_count:
    print("Henry remained hungry. He will try next weekend again.")
elif eaten_foods_count >= 4:
    print(f"Gluttony of the day! Henry ate {eaten_foods_count} foods.")
elif eaten_foods_count == 1:
    print(f"Henry ate: {eaten_foods_count} food.")
else:
    print(f"Henry ate: {eaten_foods_count} foods.")