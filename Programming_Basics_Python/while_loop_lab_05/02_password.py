username = input()
password = input()

current_data = input()

while current_data != password:
    current_data = input()

print(f'Welcome {username}!')