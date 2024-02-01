import os


name = "text1.txt"
file = open(name)
# with open(name) as file:
    # pass -> this will close the file after ending
# abs = os.path.join(os.path.abspath(__file__), "..")
path = os.path.join("..", "text2.txt")
file_two = open(path)
a = 5

# ABSOLUTE_DIR_PATH = (os.path.abspath(__file__))
# -> дефинира се във файл който е в working directory на проекта
# ABSOLUTE_DIR_PATH =  os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
ABSOLUTE_DIR_PATH = os.path.dirname(os.path.abspath(__file__))
# -> спира до името на директорията където е файла без името на файла който се рънва!!!
p = os.path.join(ABSOLUTE_DIR_PATH, "..", "text2.txt" )
# -> от file handling отиваме едно ниво нагоре " .. " и после името на файла
f = open(p)