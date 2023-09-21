poor_grades = int(input())

total_of_grades = 0
number_of_tasks = 0
count_poor_grades = 0
last_task = ''
flag = False

task = input()
while task != 'Enough':
    current_grade = int(input())
    number_of_tasks += 1
    total_of_grades += current_grade
    if current_grade <= 4:
        count_poor_grades += 1
        if count_poor_grades == poor_grades:
            flag = True
            break

    last_task = task
    task = input()

if flag:
    print(f'You need a break, {poor_grades} poor grades.')
else:
    average = total_of_grades / number_of_tasks
    print(f'Average score: {average:.2f}')
    print(f'Number of problems: {number_of_tasks}')
    print(f'Last problem: {last_task}')

