input_line = input()

student_ticket = 0
standard_ticket = 0
kid_ticket = 0
all_tickets = 0

while input_line != 'Finish':
    name_of_movie = input_line
    capacity = int(input())

    current_ticket_count = 0
    command_line = input()
    while command_line != 'End':
        type_ticket = command_line
        current_ticket_count += 1

        if type_ticket == 'student':
            student_ticket += 1
        elif type_ticket == 'standard':
            standard_ticket += 1
        elif type_ticket == 'kid':
            kid_ticket += 1

        if current_ticket_count == capacity:
            break

        command_line = input()

    all_tickets += current_ticket_count

    percent_per_movie = current_ticket_count / capacity * 100
    print(f'{name_of_movie} - {percent_per_movie:.2f}% full.')

    input_line = input()

print(f'Total tickets: {all_tickets}')
percent_student = student_ticket / all_tickets * 100
print(f'{percent_student:.2f}% student tickets.')
percent_standard = standard_ticket / all_tickets * 100
print(f'{percent_standard:.2f}% standard tickets.')
percent_kid = kid_ticket / all_tickets * 100
print(f'{percent_kid:.2f}% kids tickets.')