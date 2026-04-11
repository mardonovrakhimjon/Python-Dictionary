
def filter_non_zero(d: dict[str, int]) -> dict[str, int]:
    return {k: v for k, v in d.items() if v != 0}

print(filter_non_zero) #({'a': 1, 'b': 0, 'c': 2, 'd': 0}))