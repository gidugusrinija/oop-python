nums = [-7, -3, 2, 3, 11]


def sorted_squares(nums):
    n = len(nums)
    i = 0
    j = n - 1
    res = [0] * n
    res_p = n - 1
    while i <= j:
        if abs(nums[i]) > abs(nums[j]):
            res[res_p] = nums[i] ** 2
            i += 1
        else:
            res[res_p] = nums[j] ** 2
            j -= 1

        res_p -= 1

    return res


print(sorted_squares(nums))
