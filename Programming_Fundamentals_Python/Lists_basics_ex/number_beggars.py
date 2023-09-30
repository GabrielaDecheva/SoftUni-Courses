offers_as_string = input().split(", ")
count_beggars = int(input())
offers_as_integers = []
for current_offer in offers_as_string:
    offers_as_integers.append(int(current_offer))
final_sums_offers = []
start_index = 0
while start_index < count_beggars:
    current_beggar_final_sum = 0
    for current_index in range(start_index, len(offers_as_integers), count_beggars):
        current_beggar_final_sum += offers_as_integers[current_index]
    final_sums_offers.append(current_beggar_final_sum)
    start_index += 1
print(final_sums_offers)

