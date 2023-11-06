all_students = {}
highest_grades = {}
number_of_students = int(input())
for _ in range(number_of_students):
    name = input()
    grade = float(input())
    if name not in all_students.keys():
        all_students[name] = []
    all_students[name].append(grade)

for student, grades in all_students.items():
    average_grade = sum(grades) / len(grades)
    if average_grade >= 4.50:
        highest_grades[student] = average_grade

for student, average_grade in highest_grades.items():
    print(f'{student} -> {average_grade:.2f}')


