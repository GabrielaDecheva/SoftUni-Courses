import os
from string import punctuation

ABSOLUTE_DIR_PATH = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(ABSOLUTE_DIR_PATH, "text_files", "text_1.txt")

with open(path, "r") as line_numbers_file:
    text = line_numbers_file.readlines()

new_file = open("text_files/new_file.txt", "w")

for row in range(len(text)):
    count_letters = 0
    count_marks = 0

    for symbol in text[row]:
        if symbol.isalpha():
            count_letters += 1
        elif symbol in punctuation:
            count_marks += 1

    new_file.write(f"Line {row + 1}: {text[row][:-1]} ({count_letters}) ({count_marks})\n")

new_file.close()

