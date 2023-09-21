total_steps = 0
init_input = input()

while init_input != 'Going home':
    current_steps = int(init_input)
    total_steps += current_steps

    if total_steps >= 10000:
        break

    init_input = input()

if init_input == 'Going home':
    steps_home = int(input())
    total_steps += steps_home


diff = abs(10000 - total_steps)
if total_steps < 10000:
    print(f'{diff} more steps to reach goal.')
else:
    print(f'Goal reached! Good job!')
    print(f'{diff} steps over the goal!')
