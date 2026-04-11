from pprint import pprint


def group_indices(numbers: list[int]) -> dict[int, list[int]]:
    group = {}

    for index, number in enumerate(numbers):
        group.setdefault(number, []).append(index)

    return group


nums = [1, 3, 4, 5, 6, 5, 4, 3, 2, 1, 1, 5, 2, 7, 7, 6, 4]
result = group_indices(nums)
pprint(result)