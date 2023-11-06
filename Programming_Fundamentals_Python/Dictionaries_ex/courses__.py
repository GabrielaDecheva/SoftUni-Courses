courses = {}
while True:
    command = input()
    if ':' not in command:
        break
    course_info, name = command.split(' : ')
    if course_info not in courses.keys():
        courses[course_info] = []
    courses[course_info].append(name)

for course, name in courses.items():
    print(f'{course}: {len(name)}')
    for student in name:
        print(f'-- {student}')