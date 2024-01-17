# first_set = set(int(x) for x in input().split())
# second_set = set(int(x) for x in input().split())
#
# for _ in range(int(input())):
#     first_comm, second_comm, *data = input().split()
#     #add, first, list of some numbers(different count each time)
#
#     command = first_comm + " " + second_comm
#
#     if command == "Add First":
#         [first_set.add(int(el)) for el in data]
#     elif command == "Add Second":
#         [second_set.add(int(el)) for el in data]
#     elif command == "Remove First":
#         [first_set.discard(int(el)) for el in data] # if el does not exist , no error will be raised
#     elif command == "Remove Second":
#         [second_set.discard(int(el)) for el in data]
#     elif command == "Check Subset":
#         print(first_set.issubset(second_set) or second_set.issubset(first_set)) # True/False
#
#
# print(*sorted(first_set), sep=", ")
# print(*sorted(second_set), sep=", ")

first_set = set(int(x) for x in input().split())
second_set = set(int(x) for x in input().split())

functions = {
    "Add First": lambda x: [first_set.add(int(el)) for el in x],
    "Add Second": lambda x: [second_set.add(int(el)) for el in x],
    "Remove First": lambda x: [first_set.discard(int(el)) for el in x],
    "Remove Second": lambda x: [second_set.discard(int(el)) for el in x],
    "Check Subset": print(first_set.issubset(second_set) or second_set.issubset(first_set)) # True/False
}
for _ in range(int(input())):
    first_comm, second_comm, *data = input().split()
    #add, first, list of some numbers(different count each time)

    command = first_comm + " " + second_comm

    functions[command](data)

print(*sorted(first_set), sep=", ")
print(*sorted(second_set), sep=", ")
