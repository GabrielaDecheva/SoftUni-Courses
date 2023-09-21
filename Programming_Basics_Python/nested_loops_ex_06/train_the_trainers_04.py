count_jury = int(input())
input_line = input()

count_grades = 0
sum_grades = 0

while input_line != 'Finish':
    presentation_name = input_line

    presentation_grade = 0
    for i in range(count_jury):
        grade = float(input())
        presentation_grade += grade
        count_grades += 1
        sum_grades += grade
    avg_current_grade = presentation_grade / count_jury
    print(f'{presentation_name} - {avg_current_grade:.2f}.')
    input_line = input()

avg_final_assessment = sum_grades / count_grades
print(f"Student's final assessment is {avg_final_assessment:.2f}.")




