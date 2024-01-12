from collections import deque

current_food = int(input())

orders = deque([int(x) for x in input().split()])

print(max(orders))

for order in orders.copy():
    if current_food >= order:
        orders.popleft()
        current_food -= order
    else:
        print(f"Orders left:", *orders)
        break
else:
    print('Orders complete')

# solution 2
#
# while orders:
#     order = orders.popleft()
#
#     if food >= order:
#         food -= order
#     else:
#         print(f"Orders left:", order, *orders)  # " ".join([str(x) for x in orders])
#         break
# else:
#     print("Orders complete")
