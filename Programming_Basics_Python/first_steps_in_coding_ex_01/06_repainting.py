sq_meters_nylon = int(input())
litres_paint = int(input())
litres_razr = int(input())
hours_for_work = int(input())
bags = 0.4

nylon_price = (sq_meters_nylon + 2) * 1.5
paint_price = (litres_paint + (litres_paint/100 * 10)) * 14.5
razr_price = litres_razr * 5
price_for_all_materials = nylon_price + paint_price + razr_price + bags
price_for_workers = (price_for_all_materials * 30/100) * hours_for_work
total_price = price_for_all_materials + price_for_workers
print(total_price)