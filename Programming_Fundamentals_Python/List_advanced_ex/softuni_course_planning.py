def add_func(current_lesson, schedule):
    if lesson not in initial_schedule:
        initial_schedule.append(lesson)


def insert_func(current_lesson, current_index, schedule):
    if lesson not in initial_schedule:
        initial_schedule.insert(index, lesson)


def remove_func(current_lesson, exercises, schedule):
    if lesson in initial_schedule:
        initial_schedule.remove(lesson)
    if lesson in exercises:
        exercises.remove(lesson)
        initial_schedule.remove(f'{lesson}-Exercise')


def swap_func(lesson1, lesson2, schedule, exercises):
    if lesson1 in schedule and lesson2 in schedule:
        first_index = schedule.index(lesson1)
        second_index = schedule.index(lesson2)
        schedule[first_index], schedule[second_index] = schedule[second_index], schedule[first_index]
        if lesson1 in exercises:
            schedule.pop(first_index + 1)
            schedule.insert(second_index + 1, f'{lesson1}-Exercise')
        if lesson2 in exercises:
            schedule.pop(second_index + 1)
            schedule.insert(first_index + 1, f'{lesson2}-Exercise')


def exercise_func(current_lesson, schedule, exercises):
    if current_lesson in schedule and current_lesson not in exercises:
        lesson_index = schedule.index(current_lesson)
        schedule.insert(lesson_index + 1, f'{current_lesson}-Exercise')
        exercises.append(current_lesson)
    elif current_lesson not in schedule:
        schedule.append(current_lesson)
        schedule.append(f'{current_lesson}-Exercise')
        exercises.append(current_lesson)


initial_schedule = input().split(', ')
command = input().split(':')
exercises = []

while command[0] != 'course start':
    if command[0] == 'Add':
        lesson = command[1]
        add_func(lesson, initial_schedule)
    elif command[0] == 'Insert':
        lesson = command[1]
        index = int(command[2])
        insert_func(lesson, index, initial_schedule)
    elif command[0] == 'Remove':
        lesson = command[1]
        remove_func(lesson, exercises, initial_schedule)
    elif command[0] == 'Swap':
        first_lesson = command[1]
        second_lesson = command[2]
        swap_func(first_lesson, second_lesson, initial_schedule, exercises)
    elif command[0] == 'Exercise':
        lesson = command[1]
        exercise_func(lesson, initial_schedule, exercises)

    command = input().split(':')

for element in initial_schedule:
    print(f'{initial_schedule.index(element) + 1}.{element}')
