import re

string_line = input()
pattern = r'(#|\|)([A-Za-z ]+\s?)\1(\d{2}\/\d{2}\/\d{2})\1(\d+)\1'
matches = re.findall(pattern, string_line)
total_calories = 0
calories_per_day = 2000
for food in matches:
    total_calories += int(food[3])
total_days = total_calories // calories_per_day
print(f'You have food to last you for: {total_days} days!')
for food in matches:
    print(f'Item: {food[1]}, Best before: {food[2]}, Nutrition: {food[3]}')