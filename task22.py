from pprint import pprint


def group_students(students: list[dict[str, str]]) -> dict[str, list[str]]:
    groups = {}

    for student in students:   
            groups.setdefault(student['group'], []).append(student['name'])
            
    return groups


students = [
    {
        "name": "Ali",
        "group": "A",
    },
    {
        "name": "Vali",
        "group": "B",
    },
    {
        "name": "Ade",
        "group": "B",
    },
    {
        "name": "Sami",
        "group": "A",
    },
    {
        "name": "G\'ani",
        "group": "B",
    },
    {
        "name": "Alim",
        "group": "B",
    },
]

result = group_students(students)
pprint(result)