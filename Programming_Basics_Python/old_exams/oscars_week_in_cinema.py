name_of_movie = input()
type_hall = input()
count_tickets = int(input())

ticket_price = 0

if name_of_movie == 'A Star Is Born':
    if type_hall == 'normal':
        ticket_price = 7.50
    elif type_hall == 'luxury':
        ticket_price = 10.50
    elif type_hall == 'ultra luxury':
        ticket_price = 13.50
elif name_of_movie == 'Bohemian Rhapsody':
    if type_hall == 'normal':
        ticket_price = 7.35
    elif type_hall == 'luxury':
        ticket_price = 9.45
    elif type_hall == 'ultra luxury':
        ticket_price = 12.75
elif name_of_movie == 'Green Book':
    if type_hall == 'normal':
        ticket_price = 8.15
    elif type_hall == 'luxury':
        ticket_price = 10.25
    elif type_hall == 'ultra luxury':
        ticket_price = 13.25
elif name_of_movie == 'The Favourite':
    if type_hall == 'normal':
        ticket_price = 8.75
    elif type_hall == 'luxury':
        ticket_price = 11.55
    elif type_hall == 'ultra luxury':
        ticket_price = 13.95

profit = ticket_price * count_tickets

print(f'{name_of_movie} -> {profit:.2f} lv.')
