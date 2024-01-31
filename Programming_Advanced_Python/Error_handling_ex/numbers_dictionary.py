numbers_dictionary = {}
first_line = input()

while first_line != "Search":
    number_as_string = first_line

    try:
        number = int(input())
        numbers_dictionary[number_as_string] = number
    except ValueError:
        print("The variable number must be an integer")

    first_line = input()

second_line = input()

while second_line != "Remove":
    searched = second_line
    try:
        print(numbers_dictionary[searched])
    except KeyError:
        print("Number does not exist in dictionary")

    second_line = input()

third_line = input()

while third_line != "End":
    searched = third_line
    try:
        del numbers_dictionary[searched]
    except KeyError:
        print("Number does not exist in dictionary")

    third_line = input()

print(numbers_dictionary)
