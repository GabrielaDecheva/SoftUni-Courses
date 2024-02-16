from collections import deque

time_needed_for_one_task = deque([int(x) for x in input().split()])
number_of_tasks = [int(x) for x in input().split()]

ducks = {
    "Darth Vader Ducky": 0,
    "Thor Ducky": 0,
    "Big Blue Rubber Ducky": 0,
    "Small Yellow Rubber Ducky": 0
}

while time_needed_for_one_task and number_of_tasks:
    current_time = time_needed_for_one_task.popleft()
    current_task = number_of_tasks.pop()

    result = current_task * current_time

    if result > 240:
        number_of_tasks.append(current_task - 2)
        time_needed_for_one_task.append(current_time)
        continue

    duck_type = ""
    if 0 <= result <= 60:
        duck_type = "Darth Vader Ducky"
    elif 61 <= result <= 120:
        duck_type = "Thor Ducky"
    elif 121 <= result <= 180:
        duck_type = "Big Blue Rubber Ducky"
    elif 181 <= result <= 240:
        duck_type = "Small Yellow Rubber Ducky"

    ducks[duck_type] += 1


print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")
print(f"Darth Vader Ducky: {ducks['Darth Vader Ducky']}\n"
      f"Thor Ducky: {ducks['Thor Ducky']}\n"
      f"Big Blue Rubber Ducky: {ducks['Big Blue Rubber Ducky']}\n"
      f"Small Yellow Rubber Ducky: {ducks['Small Yellow Rubber Ducky']}")
