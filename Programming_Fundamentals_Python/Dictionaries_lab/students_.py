students = []
course_to_search = None

while True:
    info = input()

    if ':' not in info:
        course_to_search = info
        break

    name, id, course = info.split(':')
    students.append({'name': name, 'ID': id, 'Course': course})

for student in students:
    if course_to_search.startswith(student['Course'][0:3]):
        print(f'{student["name"]} - {student["ID"]}')
