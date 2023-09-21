name_of_movie = input()
count_days = int(input())
count_tickets_sold_per_day = int(input())
ticket_price = float(input())
percent_for_the_cinema = int(input())

profit_tickets_per_day = count_tickets_sold_per_day * ticket_price
total_profit = profit_tickets_per_day * count_days

amount_for_the_cinema = total_profit * (percent_for_the_cinema / 100)
final_profit = total_profit - amount_for_the_cinema

print(f'The profit from the movie {name_of_movie} is {final_profit:.2f} lv.')