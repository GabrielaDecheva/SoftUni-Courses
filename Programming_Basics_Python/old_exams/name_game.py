w_points = 0
w_name = ''
input_line = input()
while input_line != 'Stop':
    name = input_line
    points = 0
    for i in range(len(name)):
        number = int(input())
        if ord(name[i]) == number:
            points += 10
        else:
            points += 2
    if points == w_points:
        w_points = points
        w_name = name
    if points > w_points:
        w_points = points
        w_name = name
    input_line = input()
print(f'The winner is {w_name} with {w_points} points!')
