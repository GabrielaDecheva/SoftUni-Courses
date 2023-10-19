electrons_count = int(input())
shells = []

for shell in range(1, electrons_count + 1):
    max_electrons_for_shell = 2 * shell ** 2
    if electrons_count >= max_electrons_for_shell:
        shells.append(max_electrons_for_shell)
        electrons_count -= max_electrons_for_shell
        if electrons_count == 0:
            break
    else:
        shells.append(electrons_count)
        break

print(shells)
        