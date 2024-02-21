def cookbook(*recipe_info):
    recipes = {}
    result = ""
    for recipe, cuisine, ingredients in recipe_info:
        if cuisine not in recipes.keys():
            recipes[cuisine] = {}
        recipes[cuisine][recipe] = ingredients

    sorted_recipes = sorted(recipes.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))
    for cuisine, recipes_info in sorted_recipes:
        result += f"{cuisine} cuisine contains {len(recipes_info)} recipes:\n"
        sorted_info = sorted(recipes_info.items(), key=lambda kvp: kvp[0])
        for recipe in sorted_info:
            result += f"  * {recipe[0]} -> Ingredients: {', '.join(recipe[1])}\n"
    return result.rstrip()


# print(cookbook(
#     ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
#     ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
#     ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
#     ("Croissant", "French", ["flour", "butter", "yeast"]),
#     ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"])
# ))
print(cookbook(
    ("Pad Thai", "Thai", ["rice noodles", "shrimp", "peanuts", "bean sprouts", "tamarind sauce"])
    ))
