input_version = list(map(int, input().split('.')))
input_version[-1] += 1
for i in range(len(input_version) - 1, 0, -1):
    if input_version[i] > 9:
        input_version[i] = 0
        input_version[i - 1] += 1

print('.'.join(str(number) for number in input_version))

