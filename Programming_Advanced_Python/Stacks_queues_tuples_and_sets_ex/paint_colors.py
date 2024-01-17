from collections import deque

string = deque(input().split())

colors = {"red", "yellow", "blue", "purple", "orange", "green"}
req_colors = {
    "orange": {"red", "yellow"},
    "purple": {"blue", "red"},
    "green": {"yellow", "blue"},
}

result = []

while string:
    first_str = string.popleft()
    second_str = string.pop() if string else ""

    for color in (first_str + second_str, second_str + first_str):
        if color in colors:
            result.append(color)
            break
    else:
        for el in (first_str[:-1], second_str[:-1]):
            if el:
                string.insert(len(string) // 2 , el)

for color in set(req_colors.keys()).intersection(result):
    if not req_colors[color].issubset(result):
        result.remove(color)
print(result)