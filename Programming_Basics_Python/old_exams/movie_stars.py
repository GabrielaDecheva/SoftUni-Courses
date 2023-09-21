budget = float(input())
total_salary = 0
percent_salary = 0
input_line = input()
while input_line != 'ACTION':
    name_of_actor = input_line
    if len(name_of_actor) <= 15:
        actor_salary = float(input())
        total_salary += actor_salary
    else:
        percent_salary = (budget - total_salary) * 0.2
        total_salary += percent_salary
    if total_salary >= budget:
        break

    input_line = input()

diff = abs(budget - total_salary)
if budget >= total_salary:
    print(f'We are left with {diff:.2f} leva.')
else:
    print(f'We need {diff:.2f} leva for our actors.')
