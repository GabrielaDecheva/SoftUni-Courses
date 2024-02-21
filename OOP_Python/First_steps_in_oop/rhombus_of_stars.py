size = int(input())


def bottom_part(size):
    for row in range(size - 1, 0, -1):
        print(f"{' '*(size - row)}{'* ' * row}")


def upper_part(size):
    for row in range(1, size + 1):
        print(f"{' '*(size - row)}{'* ' * row}")


def print_rhombus(size):
    upper_part(size)
    bottom_part(size)


print_rhombus(size)