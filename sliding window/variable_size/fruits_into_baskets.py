"""
Fruit Into Baskets (K=2 Distinct)
Input: Array fruits where fruits[i] is the type of fruit.

Goal: You have two baskets, and each basket can only hold a single type of fruit. What is the maximum number of fruits you can collect in a contiguous row?

Example: [1, 2, 3, 2, 2] → Output: 4 ([2, 3, 2, 2]).
"""

def max_fruits(ls, k):
    max_fruits = 0

    fruits_map = {}

    left = 0

    st, end = -1, -1

    for right, val in enumerate(ls):
        fruits_map[val] = fruits_map.get(val, 0) + 1

        while len(fruits_map) > k:
            if fruits_map[ls[left]] == 1:
                del fruits_map[ls[left]]
            else:
                fruits_map[ls[left]] -= 1
            left += 1

        if (right - left + 1) > max_fruits:
            max_fruits = right - left + 1
            st = left
            end = right

    return max_fruits, st, end


s = [1, 2, 3, 2, 2]
k = 2
m, st, e = max_fruits(s, k)

print(m, s[st:e+1])

