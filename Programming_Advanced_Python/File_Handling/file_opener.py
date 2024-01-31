import os


name = "text1.txt"
file = open(name)
# with open(name) as file:
    # pass -> this will close the file after ending
# abs = os.path.join(os.path.abspath(__file__), "..")
path = os.path.join("..", "text2.txt")
file_two = open(path)