strawberry_price_per_kg = float(input())
banana_kg = float(input())
orange_kg = float(input())
raspberries_kg = float(input())
strawberry_kg = float(input())

raspberries_price_per_kg = strawberry_price_per_kg / 2
orange_price_per_kg = raspberries_price_per_kg * 0.6
banana_price_per_kg = raspberries_price_per_kg * 0.2

total_raspberries = raspberries_kg * raspberries_price_per_kg
total_orange = orange_kg * orange_price_per_kg
total_banana = banana_kg * banana_price_per_kg
total_strawberries = strawberry_kg * strawberry_price_per_kg

total_amount = total_banana + total_orange + total_strawberries + total_raspberries

print(f'{total_amount:.2f}')