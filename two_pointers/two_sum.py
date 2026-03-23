nums = [11, -2, 7, 2, 15]
target = 9


def two_sum(nums, target):
    res = []
    visited = {}

    for idx, val in enumerate(nums):
        if target - val in visited:
            res.append((visited[target - val], idx))

        visited[val] = idx

    return res


print(two_sum(nums, target))
