import math

count_ppl = int(input())
tax_entry = float(input())
price_one_sunbed = float(input())
price_one_umbrella = float(input())

all_tax_entry = count_ppl * tax_entry
count_all_sunbeds = math.ceil(count_ppl * 0.75)
all_price_sunbed = count_all_sunbeds * price_one_sunbed
count_all_umbrellas = math.ceil(count_ppl / 2)
all_price_umbrella = count_all_umbrellas * price_one_umbrella
total_cost = all_tax_entry + all_price_umbrella + all_price_sunbed

print(f'{total_cost:.2f} lv.')