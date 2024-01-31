import os

name = "file_to_delete.txt"

os.remove(name)

if os.path.exists(name):
    os.remove(name)