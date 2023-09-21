string = input()
string = string.lower()
counter = 0
if string.count("sand") > 0:
    counter += string.count("sand")
if string.count("water") > 0:
    counter += string.count("water")
if string.count("fish") > 0:
    counter += string.count("fish")
if string.count("sun") > 0:
    counter += string.count("sun")
print(counter)