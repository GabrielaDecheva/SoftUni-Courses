import os

symbols = ("-", ",", ".", "!", "?")

ABSOLUTE_DIR_PATH = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(ABSOLUTE_DIR_PATH, "text_files", "text_1.txt")

with open(path, "r") as even_lines_file:
    text = even_lines_file.readlines()

for row in range(0, len(text), 2):
    for symbol in symbols:
        text[row] = text[row].replace(symbol, "@")

    print(*text[row].split()[::-1])
