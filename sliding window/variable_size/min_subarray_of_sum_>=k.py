"""
Input: Array nums and target K.
Goal: Find the minimal length of a contiguous subarray of which the sum is >= K. If there isn't one, return 0.
Example: target = 7, nums = [2, 3, 1, 2, 4, 3] → Output: 2 ([4, 3]).
"""


def min_subarray(nums, k):
    min_len = float("inf")
    left = 0
    st, end = -1, -1
    current_sum = 0
    for right, val in enumerate(nums):
        current_sum += val

        while current_sum >= k:
            if right - left + 1 < min_len:
                min_len = right - left + 1
                st = left
                end = right + 1

            current_sum -= nums[left]
            left += 1

    if min_len == float("inf"):
        return 0, []

    return min_len, nums[st: end]

nums = [2, 3, 1, 2, 4, 3]
k = 7

m_l, res = min_subarray(nums, k)

print(m_l, res)




