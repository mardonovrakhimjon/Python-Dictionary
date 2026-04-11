def count_names(names: list[str]) -> dict[str, int]:
    result = {}

    for name in names:
        #if name not in result.keys():
        count = names.count(name)

        result[name] = count

    return result

names = ["ali","vali","sami","gani","vali","ali","vali","sami"]
result = count_names(names=names)
print(result)