def grocery_store(**products):
    products = sorted(products.items(), key=lambda kvp: (-kvp[1], -len(kvp[0]), kvp[0]))
    # sorted returns list
    result = []
    for product, quantity in products:
        result.append(f"{product}: {quantity}")

    return "\n".join(result)

    # "\n".join(f"{p}: {q}" for p,q in products)


print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))



