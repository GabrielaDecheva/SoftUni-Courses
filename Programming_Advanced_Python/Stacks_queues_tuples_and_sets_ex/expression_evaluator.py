from collections import deque
from math import floor

expression = deque(input().split()) #["6", "3","+"...]

index = 0

while index < len(expression): # while len(expression) > 1
    element = expression[index]

    if element == "*":
        for _ in range(index - 1):
            expression.appendleft(int(expression.popleft()) * int(expression.popleft()))
    elif element == "/":
        for _ in range(index - 1):
            expression.appendleft(int(expression.popleft()) / int(expression.popleft()))
    elif element == "-":
        for _ in range(index - 1):
            expression.appendleft(int(expression.popleft()) - int(expression.popleft()))
    elif element == "+":
        for _ in range(index - 1):
            expression.appendleft(int(expression.popleft()) + int(expression.popleft()))

    if element in "*/+-":
        del expression[1]
        index = 1
    index += 1

print(floor(int(expression[0])))