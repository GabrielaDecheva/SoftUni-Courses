def merge_function(start_i, end_i, input_message):
    if start_i < 0:
        start_i = 0
    if end_i > len(input_message) - 1:
        end_i = len(input_message) - 1
    merged_element = ''.join(input_message[start_i:end_i + 1])
    input_message[start_i:end_i + 1] = [merged_element]


def divide_function(current_index, parts, input_message):
    element = input_message[current_index]
    divided_partition = []
    length_of_partition = len(element) // parts
    for current_element_index in range(parts):
        if current_element_index != parts - 1:
            divided_partition.append(element[current_element_index * length_of_partition: (current_element_index + 1) * length_of_partition])
        else:
            divided_partition.append(element[current_element_index * length_of_partition:])
    input_message[current_index:current_index + 1] = divided_partition


input_line = input().split()
command_line = input().split()
while command_line[0] != '3:1':
    if command_line[0] == 'merge':
        start_index = int(command_line[1])
        end_index = int(command_line[2])
        merge_function(start_index, end_index, input_line)
    elif command_line[0] == 'divide':
        index = int(command_line[1])
        partitions = int(command_line[2])
        divide_function(index, partitions, input_line)

    command_line = input().split()

print(*input_line)