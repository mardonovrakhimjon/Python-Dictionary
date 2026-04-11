# def merge_dicts(a: dict, b: dict) -> dict:
#     a.update(b)

#     return a
def merge_dicts(a: dict, b: dict) -> dict:

    merged = a.copy()
    merged.update(b)
    
    return merged
print(merge_dicts(dict1, dict2))