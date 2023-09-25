number_of_snowballs = int(input())
highest_snowball_value = 0
max_weight = 0
max_time = 0
max_quality = 0
for _ in range(number_of_snowballs):
    current_weight = int(input())
    current_time = int(input())
    current_quality = int(input())
    current_value = (current_weight / current_time) ** current_quality
    if current_value > highest_snowball_value:
        highest_snowball_value = current_value
        max_weight = current_weight
        max_time = current_time
        max_quality = current_quality
print(f'{max_weight} : {max_time} = {int(highest_snowball_value)} ({max_quality})')