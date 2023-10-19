initial_schedule = input().split(', ')
command = input().split(':')
exercises = []

while command[0] != 'course start':
    if command[0] == 'Add':
        lesson = command[1]
        if lesson not in initial_schedule:
            initial_schedule.append(lesson)
    elif command[0] == 'Insert':
        lesson = command[1]
        index = int(command[2])
        if lesson not in initial_schedule:
            initial_schedule.insert(index, lesson)
    elif command[0] == 'Remove':
        lesson = command [1]
        if lesson in initial_schedule:
            initial_schedule.remove(lesson)
        if lesson in exercises:
            exercises.remove(lesson)
            initial_schedule.remove(f'{lesson}-Exercise')

    elif command[0] == 'Swap':
        first_lesson = command[1]
        second_lesson = command[2]
        if first_lesson in initial_schedule and second_lesson in initial_schedule:
            first_index = initial_schedule.index(first_lesson)
            second_index = initial_schedule.index(second_lesson)
            initial_schedule[first_index], initial_schedule[second_index] = initial_schedule[second_index], initial_schedule[first_index]
            if first_lesson in exercises:
                initial_schedule.pop(first_index + 1)
                initial_schedule.insert(second_index + 1, f'{first_lesson}-Exercise')
            if second_lesson in exercises:
                initial_schedule.pop(second_index + 1)
                initial_schedule.insert(first_index + 1, f'{second_lesson}-Exercise')
    elif command[0] == 'Exercise':
        lesson = command[1]
        if lesson in initial_schedule and lesson not in exercises:
            lesson_index = initial_schedule.index(lesson)
            initial_schedule.insert(lesson_index + 1, f'{lesson}-Exercise')
            exercises.append(lesson)
        elif lesson not in initial_schedule:
            initial_schedule.append(lesson)
            initial_schedule.append(f'{lesson}-Exercise')
            exercises.append(lesson)
    command = input().split(':')

for element in initial_schedule:
    print(f'{initial_schedule.index(element) + 1}.{element}')