name = input()
count_poor_grades = 0
years = 0
total_grades = 0
while True:
    current_grade = float(input())

    if current_grade < 4:
        count_poor_grades += 1

        if count_poor_grades > 1:
            failed_year = years + 1
            print(f'{name} has been excluded at {failed_year} grade')
            break

        continue

    else:
        years += 1
        total_grades += current_grade

    if years == 12:
        avg = total_grades / years
        print(f'{name} graduated. Average grade: {avg:.2f}')
        break


