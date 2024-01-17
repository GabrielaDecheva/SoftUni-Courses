from functools import reduce
from math import floor

expression = input().split() #["6", "3","+"...]

index = 0

functions = {
    "*": lambda i: reduce(lambda a, b: a * b, map(int, expression[:i])),
    "/": lambda i: reduce(lambda a, b: a / b, map(int, expression[:i])),
    "+": lambda i: reduce(lambda a, b: a + b, map(int, expression[:i])),
    "-": lambda i: reduce(lambda a, b: a - b, map(int, expression[:i])),
}
while index < len(expression): # while len(expression) > 1
    element = expression[index]

    if element in "*/+-":
        expression[0] = functions[element](index)
        [expression.pop(1) for _ in range(index)]
        index = 1
    index += 1

print(floor(int(expression[0])))