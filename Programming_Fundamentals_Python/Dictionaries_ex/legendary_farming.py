materials = {'shards': 0, 'fragments': 0, 'motes': 0}
obtained = False
while not obtained:
    input_materials = input().split()
    for index in range(0, len(input_materials), 2):
        key = input_materials[index + 1].lower()
        value = int(input_materials[index])
        if key not in materials.keys():
            materials[key] = 0
        materials[key] += value
        if materials['shards'] >= 250:
            print(f'Shadowmourne obtained!')
            materials['shards'] -= 250
            obtained = True
        elif materials["fragments"] >= 250:
            print(f"Valanyr obtained!")
            materials["fragments"] -= 250
            obtained = True
        elif materials["motes"] >= 250:
            print(f"Dragonwrath obtained!")
            materials["motes"] -= 250
            obtained = True
        if obtained:
            break
for material, quantity in materials.items():
    print(f"{material}: {quantity}")
