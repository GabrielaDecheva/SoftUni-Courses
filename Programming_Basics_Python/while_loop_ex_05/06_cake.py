cake_length = int(input())
cake_width = int(input())
pieces_total = cake_width * cake_length
flag = False
current_input = input()

while current_input != 'STOP':
    current_piece = int(current_input)

    pieces_total -= current_piece

    if pieces_total <= 0:
        flag = True
        break

    current_input = input()

if flag:
    print(f'No more cake left! You need {abs(pieces_total)} pieces more.')
else:
    print(f'{pieces_total} pieces are left.')
