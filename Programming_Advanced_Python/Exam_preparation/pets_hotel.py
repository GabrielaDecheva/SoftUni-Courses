def accommodate_new_pets(availability, pets_allowed_kg, *pets_info):
    accommodated_pets = {}
    overweight = 0
    first_print_line = ""
    second_print_line = "Accommodated pets:\n"
    for pet in pets_info:
        if availability > 0:
            if float(pet[1]) <= float(pets_allowed_kg):
                if pet[0] not in accommodated_pets.keys():
                    accommodated_pets[pet[0]] = 0
                accommodated_pets[pet[0]] += 1
                availability -= 1
            else:
                overweight += 1
        else:
            break

    if sum(accommodated_pets.values()) + overweight == len(pets_info):
        first_print_line += f"All pets are accommodated! Available capacity: {availability}."
    else:
        first_print_line += "You did not manage to accommodate all pets!"

    sorted_pets = sorted(accommodated_pets.items(), key=lambda kvp: kvp[0])
    for pet, count in sorted_pets:
        second_print_line += f"{pet}: {count}\n"
    return f"{first_print_line}\n{second_print_line}"


print(accommodate_new_pets(
    10,
    15.0,
    ("cat", 15.8),
    ("dog", 15.2),
))
# print(accommodate_new_pets(
#     2,
#     15.0,
#     ("dog", 10.0),
#     ("cat", 5.8),
#     ("cat", 2.7),
# ))

# print(accommodate_new_pets(
#     10,
#     15.0,
#     ("cat", 5.8),
#     ("dog", 10.0),
# ))