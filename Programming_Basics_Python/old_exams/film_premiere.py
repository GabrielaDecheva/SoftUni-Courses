name_of_movie = input()
package = input()
count_tickets = int(input())

ticket_price = 0

if name_of_movie == 'John Wick':
    if package == 'Drink':
        ticket_price = 12
    elif package == 'Popcorn':
        ticket_price = 15
    elif package == 'Menu':
        ticket_price = 19
elif name_of_movie == 'Star Wars':
    if package == 'Drink':
        ticket_price = 18
    elif package == 'Popcorn':
        ticket_price = 25
    elif package == 'Menu':
        ticket_price = 30
elif name_of_movie == 'Jumanji':
    if package == 'Drink':
        ticket_price = 9
    elif package == 'Popcorn':
        ticket_price = 11
    elif package == 'Menu':
        ticket_price = 14

if name_of_movie == 'Star Wars' and count_tickets >= 4:
    ticket_price = ticket_price * 0.7
if name_of_movie == 'Jumanji' and count_tickets == 2:
    ticket_price = ticket_price * 0.85

bill = count_tickets * ticket_price

print(f'Your bill is {bill:.2f} leva.')
