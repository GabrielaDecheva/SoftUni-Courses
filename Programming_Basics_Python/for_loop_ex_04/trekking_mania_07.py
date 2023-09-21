count_groups = int(input())

Musala = 0
Monblan = 0
Kilimandjaro = 0
K2 = 0
Everest = 0

for _ in range(count_groups):
    current_group = int(input())
    if current_group <= 5:
        Musala += current_group
    elif 6 <= current_group <= 12:
        Monblan += current_group
    elif 13 <= current_group <= 25:
        Kilimandjaro += current_group
    elif 26 <= current_group <= 40:
        K2 += current_group
    elif current_group > 40:
        Everest += current_group

total_count = Musala + Monblan + Kilimandjaro + K2 + Everest
Musala_percent = (Musala / total_count) * 100
Monblan_percent = (Monblan / total_count) * 100
Kilimandjaro_percent = (Kilimandjaro / total_count) * 100
K2_percent = (K2 / total_count) * 100
Everest_percent = (Everest / total_count) * 100

print(f'{Musala_percent:.2f}%')
print(f'{Monblan_percent:.2f}%')
print(f'{Kilimandjaro_percent:.2f}%')
print(f'{K2_percent:.2f}%')
print(f'{Everest_percent:.2f}%')