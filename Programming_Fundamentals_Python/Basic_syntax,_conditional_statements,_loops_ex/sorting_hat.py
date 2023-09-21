name= input()
house = ''
flag = False
while name != 'Welcome!':
    if name == 'Voldemort':
        flag = True
        break
    elif len(name) < 5:
        house = 'Gryffindor'
    elif len(name) == 5:
        house = 'Slytherin'
    elif len(name) == 6:
        house = 'Ravenclaw'
    elif len(name) > 6:
        house = 'Hufflepuff'
    print(f'{name} goes to {house}.')
    name = input()
if flag:
    print('You must not speak of that name!')
else:
    print('Welcome to Hogwarts.')