input_gifts = input().split()
gifts_list = []
for gift in input_gifts:
    gifts_list.append(gift)
command = input()
while command != 'No Money':
    if 'OutOfStock ' in command:
        for element in command:
            type_of_command, type_of_gift = command.split()
            for i in range(len(gifts_list)):
                if gifts_list[i] == type_of_gift:
                    gifts_list[i] = 'None'
    elif 'Required ' in command:
        for element in command:
            element_items = command.split()
            type_of_command = element_items[0]
            type_of_gift = element_items[1]
            number_index = int(element_items[2])
            if number_index < len(gifts_list) - 1:
                gifts_list[number_index] = type_of_gift
    elif 'JustInCase ' in command:
        for element in command:
            type_of_command, type_of_gift = command.split()
            gifts_list[-1] = type_of_gift
    command = input()

while 'None' in gifts_list:
    gifts_list.remove('None')

print(*gifts_list)

