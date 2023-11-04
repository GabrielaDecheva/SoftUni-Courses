countries = input().split(', ')
capitals = input().split(', ')
final_dict = {countries[index]: capitals[index] for index in range(len(countries))}

# final_dict = dict(zip(countries,capitals))

for country, capital in final_dict.items():
    print(f'{country} -> {capital}')
