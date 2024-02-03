import os

directory = "text_files"

while True:
    command, *details = input().split("-")
    if command == "End":
        break

    file_name = details[0]
    file_path = os.path.join(directory, file_name)

    if command == "Create":
        if not os.path.exists(file_path):
            with open(file_path, "w") as file:
                print(f"File '{file_name}' created successfully!")
        else:
            print(f"File '{file_name}' already exists!")

    elif command == "Add":
        with open(file_path, "a") as file:
            file.write(f"{details[1]}\n")

    elif command == "Replace":
        try:
            with open(file_path, "r+") as file:
                text = file.read()
                text = text.replace(details[1], details[2])

                file.seek(0)
                file.write(text)
                file.truncate()
        except FileNotFoundError:
            print("An error occurred!")

    elif command == "Delete":
        try:
            os.remove(f"text_files/{details[0]}")
            print(f"File '{details[0]}' deleted successfully!")
        except FileNotFoundError:
            print("An error occurred!")
