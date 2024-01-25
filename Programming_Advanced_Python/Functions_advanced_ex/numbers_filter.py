def even_odd_filter(**kwargs):
    for key, value in kwargs.items():
        if key == "even":
            kwargs["even"] = [num for num in value if num % 2 == 0]
        elif key == "odd":
            kwargs["odd"] = [num for num in value if num % 2 != 0]

    return dict(sorted(kwargs.items(), key=lambda kvp: len(kvp[1]), reverse=True))


print(even_odd_filter(
    odd=[2, 2, 30, 44, 10, 5],
))