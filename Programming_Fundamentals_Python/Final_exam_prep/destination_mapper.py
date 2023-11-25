import re

input_string = input()
pattern = r'(=|\/)([A-Z][A-Za-z]{2,})\1'
matches = re.findall(pattern, input_string)
travel_points = 0
destinations = []
for match in matches:
    current_points = int(len(match[1]))
    travel_points += current_points
    destinations.append(match[1])
print(f"Destinations: {', '.join(destinations)}")
print(f'Travel Points: {travel_points}')
