count_chicken_menu = int(input())
count_fish_menu = int(input())
count_vegi_menu = int(input())
delivery = 2.5

price_chicken_menu = count_chicken_menu * 10.35
price_fish_menu = count_fish_menu * 12.40
price_vegi_menu = count_vegi_menu * 8.15
total_all_menus = price_chicken_menu + price_fish_menu + price_vegi_menu
dessert_price = total_all_menus/100 * 20

total_price = total_all_menus + dessert_price + delivery

print(total_price)