import re


def extract_info(input_information):
    pattern = r'[a-zA-Z0-9]'
    extracted_chars = re.findall(pattern, input_information)
    return extracted_chars


def is_racer(names_racers, extracted_chars, dict_racers):
    name = ''
    distance = 0
    for char in extracted_chars:
        if char.isdigit():
            distance += int(char)
        elif char.isalpha():
            name += char
    if name in names_racers:
        if name in dict_racers.keys():
            dict_racers[name] += distance
        else:
            dict_racers[name] = distance
    return dict_racers


names = input().split(', ')
input_line = input()
racer_results = {}
while input_line != 'end of race':
    extracted_chars = extract_info(input_line)
    racer_results = is_racer(names, extracted_chars, racer_results)
    input_line = input()

sorted_results = sorted(racer_results.items(), key=lambda x: x[1], reverse=True)
places = ['1st', '2nd', '3rd']
top_racers = [f'{place} place: {racer}' for place, (racer, _) in zip(places, sorted_results[:3])]
print('\n'.join(top_racers))