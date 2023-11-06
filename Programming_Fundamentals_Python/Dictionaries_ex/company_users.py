companies = {}
while True:
    command = input()
    if '->' not in command:
        break
    company, employee_id = command.split(' -> ')
    if company not in companies.keys():
        companies[company] = []
    if employee_id not in companies[company]:
        companies[company].append(employee_id)
for company, id_list in companies.items():
    print(company)
    for id in id_list:
        print(f'-- {id}')
