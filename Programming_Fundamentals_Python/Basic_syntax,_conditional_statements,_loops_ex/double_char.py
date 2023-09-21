string = input()
while string != 'End':
    if string != 'SoftUni':
        double_character = ''
        for character in string:
            double_character += character * 2
        print(double_character)
    string = input()