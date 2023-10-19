message = input().split()
new_message = ''

for element in message:
    element_list = list(element)
    digit = []
    for char in element_list:
        if char.isdigit():
            digit += char
    element_list = [element for element in element_list if element not in digit]
    full_number = int(''.join(digit))
    element_list[0], element_list[-1] = element_list[-1], element_list[0]
    element_list.insert(0, chr(full_number))
    new_message += f"{''.join(element_list)} "
print(new_message)