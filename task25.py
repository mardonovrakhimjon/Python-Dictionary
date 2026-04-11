def group_by_age(people: list[dict[str, int | str]]) -> dict[int, list[str]]:
    result = {}

    for person in people:
        age = person['age']
        name = person['name']

        if age not in result:
            result[age] = []

        result[age].append(name)

    return result

people = [
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 25},
    {'name': 'Charlie', 'age': 30},
    {'name': 'David', 'age': 25}
]

print(group_by_age(people))