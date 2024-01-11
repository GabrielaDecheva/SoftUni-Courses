from collections import deque
customers = deque()
command = input()
while command != 'End':
    if command != 'Paid':
        customers.append(command)
    else:
        while customers:
            print(customers.popleft())
    command = input()

print(f'{len(customers)} people remaining.')