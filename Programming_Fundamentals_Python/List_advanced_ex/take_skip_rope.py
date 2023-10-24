def filter_lists(string: str) -> None:
    sub_number_list = []
    for element in string:
        if element.isdigit():
            sub_number_list.append(int(element))
        else:
            letters.append(element)
    for index in range(len(sub_number_list)):
        if index % 2 == 0:
            take_list.append(sub_number_list[index])
        else:
            skip_list.append(sub_number_list[index])


def get_hidden_message(take: list, skip: list, string_list: list) -> str:
    index = 0
    result_string = ""
    while index < len(take):
        for _ in range(take[index]):
            if string_list:
                result_string += string_list.pop(0)
        for _ in range(skip[index]):
            if string_list:
                string_list.pop(0)
        index += 1
    return result_string


letters = []
take_list = []
skip_list = []
filter_lists(input())
print(get_hidden_message(take_list, skip_list, letters))