def softuni_students(*id_and_name, **id_and_course):
    valid_students = {}
    invalid_students = []
    for info in id_and_name:
        id, user = info
        if id not in id_and_course:
            invalid_students.append(user)
        else:
            course = id_and_course[id]
            valid_students[user] = course

    sorted_result = sorted(valid_students.items())

    string_to_print = []

    for username, course_name in sorted_result:
        string_to_print.append(f"*** A student with the username {username} "
                               f"has successfully finished the course {course_name}!")

    if invalid_students:
        message = f"!!! Invalid course students: {', '.join(sorted(invalid_students))}"
        string_to_print.append(message)

    return '\n'.join(string_to_print)


# print(softuni_students(
#     ('id_1', 'Kaloyan9905'),
#     id_1='Python Web Framework',
# ))

print(softuni_students(
    ('id_7', 'Silvester1'),
    ('id_32', 'Katq21'),
    ('id_7', 'The programmer'),
    id_76='Spring Fundamentals',
    id_7='Spring Advanced',
))