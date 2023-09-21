n = int(input())

for _ in range(n):
    current_num = int(input())
    if current_num == 88:
        print('Hello')
    elif current_num == 86:
        print('How are you?')
    elif current_num < 88:
        print('GREAT!')
    else:
        print('Bye.')